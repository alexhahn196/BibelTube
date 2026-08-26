#!/usr/bin/env python3
"""
Schritt 5 - Videospur und Montage.

Formel §5 fuehrt "Standmotiv mit **sanfter Bewegung**" als PFLICHT
(11 von 11 Stichproben). Ein voellig statisches Bild waere ein Verstoss
gegen das Dokument - deshalb ein sehr langsamer Zoom.

Der Zoom laeuft als **Atemzyklus**, nicht monoton: er beginnt und endet bei
Faktor 1,0 und hat an beiden Enden die Steigung null. Dadurch ist ein
einzelner Zyklus exakt schleifenfaehig, und die vollen 3,5 Stunden entstehen
durch Kopieren des Bitstroms statt durch Kodieren. Monoton gerechnet
braeuchte dieselbe Laufzeit rund zwei Stunden Encoder-Zeit (gemessen:
zoompan schafft 1,8-fache Echtzeit); so sind es wenige Minuten - bei
identischem Ergebnis.

Aufruf:
    python3 produktion/pipeline/schritt5_video.py V1
"""
import argparse
import json
import math
import os
import subprocess
import sys
import time

import numpy as np
import soundfile as sf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gemeinsam import SR, arbeit, config, dauer_s, ffprobe, hms, ordner  # noqa: E402

NAME_BILD = "PLATZHALTER_standbild.png"


def pixelformat(cfg):
    """Pixelformat der Videospur.

    Seit 2026-08-23 konfigurierbar, Vorgabe unveraendert yuv420p. Anlass ist
    ein gemessener Banding-Befund: bei CRF 28 verliert der Nachthimmel in
    8 Bit sieben der 48 Luma-Stufen im dunklen Bereich, und die groesste
    einfarbige Flaeche waechst gegenueber dem Quellbild um Faktor 90. In
    yuv420p10le bleiben alle 48 Stufen, der Faktor faellt auf 15 - und die
    Datei wird KLEINER (4,92 statt 6,62 MB je 300-s-Zyklus), weil 10 Bit die
    Praediktion verbessert. Messung: siehe produktion/motive/bandingtest/.

    Die Umstellung ist nicht entschieden: yuv420p10le ist H.264 High 10, und
    ob YouTubes Ingest das annimmt, ist ungeprueft.
    """
    return str(cfg["video_pixelformat"])


def zyklus_bauen(bild, ziel, cfg):
    fps = int(cfg["fps"])
    T = int(cfg.get("zoom_zyklus_s", 300))
    A = float(cfg["zoom_faktor"]) - 1.0
    n = fps * T
    if cfg.get("zoom", True) and A > 0:
        # Kosinus: z(0)=1, z(n)=1, Steigung an beiden Enden 0 -> nahtlos
        z = f"1+{A/2:.6f}*(1-cos(2*PI*on/{n}))"
        vf = (f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
              f":d=1:s={cfg['breite']}x{cfg['hoehe']}:fps={fps},"
              f"format={pixelformat(cfg)}")
    else:
        vf = f"scale={cfg['breite']}:{cfg['hoehe']},format={pixelformat(cfg)}"
    cmd = ["ffmpeg", "-y", "-loglevel", "error",
           "-loop", "1", "-framerate", str(fps), "-t", str(T), "-i", bild,
           "-vf", vf, "-c:v", "libx264", "-preset", str(cfg["video_preset"]),
           "-crf", str(int(cfg["video_crf"])), "-g", str(fps * 10),
           "-pix_fmt", pixelformat(cfg), "-an", ziel]
    subprocess.run(cmd, check=True)
    return T


def montieren(zyklus, audio, ziel, cfg, gesamt_s):
    """Geloopte Bildspur mit der Tonspur zusammenfuehren.

    Die Laenge wird mit **-t** gesetzt, nicht mit -shortest. Bei einer
    Bildspur aus -stream_loop und -c:v copy greift -shortest unzuverlaessig:
    die Kopie schreibt ganze Pakete weiter, und das Video laeuft dann ueber
    das Tonende hinaus (gemessen: 293 s stumm am Ende). -t schneidet hart
    an der Tondauer.
    """
    wdh = math.ceil(gesamt_s / dauer_s(zyklus)) + 1
    cmd = ["ffmpeg", "-y", "-loglevel", "error",
           "-stream_loop", str(wdh), "-i", zyklus,
           "-i", audio,
           "-map", "0:v:0", "-map", "1:a:0",
           "-c:v", "copy",
           "-c:a", "aac", "-b:a", str(cfg["audio_bitrate"]),
           "-t", f"{gesamt_s:.3f}", "-movflags", "+faststart", ziel]
    subprocess.run(cmd, check=True)
    return wdh


def sync_pruefen(mp4, mix, bei_s=3600.0, fenster_s=8.0):
    """Versatz zwischen der Tonspur im MP4 und der Mischung messen.

    Kreuzkorrelation eines Ausschnitts aus der Mitte - eine Laengenangabe
    aus ffprobe wuerde einen konstanten Versatz nicht auffallen lassen.
    """
    def hole(quelle):
        r = subprocess.run(
            ["ffmpeg", "-v", "error", "-ss", str(bei_s), "-t", str(fenster_s),
             "-i", quelle, "-ac", "1", "-ar", "8000", "-f", "f32le", "-"],
            capture_output=True, check=True)
        return np.frombuffer(r.stdout, np.float32)
    a, b = hole(mp4), hole(mix)
    n = min(len(a), len(b))
    if n < 8000:
        return None
    a, b = a[:n] - a[:n].mean(), b[:n] - b[:n].mean()
    k = np.fft.irfft(np.fft.rfft(a, 2 * n) * np.conj(np.fft.rfft(b, 2 * n)), 2 * n)
    lag = int(np.argmax(np.abs(k)))
    if lag > n:
        lag -= 2 * n
    return lag / 8000.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("--neu-zyklus", action="store_true", dest="neu_zyklus",
                    help="Zoom-Zyklus neu kodieren statt wiederverwenden")
    a = ap.parse_args()
    cfg = config()
    t0 = time.time()

    bild = os.path.join(ordner(a.video), NAME_BILD)
    if not os.path.exists(bild):
        raise SystemExit(f"Standbild fehlt: {bild} — erst Schritt 4 laufen lassen.")
    mix = arbeit(a.video, "mix.wav")
    if not os.path.exists(mix):
        raise SystemExit(f"Mischung fehlt: {mix} — erst Schritt 3 laufen lassen.")

    zyklus = arbeit(a.video, "zyklus.mp4")
    if cfg["videoquelle"] == "ki_clips":
        # Echte Bild-zu-Video-Clips als Zyklus, per Bitstrom-Kopie gefuegt.
        # Kein Zoom obendrauf: die Clips bewegen sich selbst (Formel §5
        # ist damit erfuellt), und ein Zoom wuerde den kompletten
        # Re-Encode der Montage erzwingen.
        from gemeinsam import pfad as _pfad
        import glob as _glob
        # Jedes Video hat eigene Clips: sie gehoeren zu seinem Standbild und
        # sind mit keinem anderen Motiv verwendbar. Ein Eintrag
        # ki_clip_ordner_V2 schlaegt deshalb den allgemeinen Wert.
        # Der allgemeine Wert ki_clip_ordner ist KEIN brauchbarer Rueckfall:
        # er zeigt auf die Clips von V1. Ein Video ohne eigenen Eintrag wuerde
        # damit still mit fremdem Motiv rendern - 35 Minuten Rechenzeit fuer
        # ein Ergebnis, das die Serienbindung (Formel §5, Gate 1.7) bricht,
        # ohne dass irgendetwas warnt. Beim Anlegen von V05 ist genau das
        # aufgefallen (2026-08-23). Deshalb: harter Abbruch statt Rueckfall.
        schluessel = f"ki_clip_ordner_{a.video}"
        if schluessel not in cfg:
            raise SystemExit(
                f"videoquelle=ki_clips, aber {schluessel} fehlt in config.md.\n"
                f"Ohne eigenen Eintrag wuerde {a.video} mit den Clips von "
                f"{cfg['ki_clip_ordner']} rendern - also mit fremdem Motiv.\n"
                f"Entweder {schluessel} eintragen oder videoquelle=standbild setzen.")
        ordner_clips = cfg[schluessel]
        clips = sorted(_glob.glob(os.path.join(_pfad(ordner_clips),
                                               "clip-*.mp4")))
        if not clips:
            raise SystemExit(f"videoquelle=ki_clips, aber keine clip-*.mp4 in "
                             f"{ordner_clips}")
        lst = arbeit(a.video, "zyklus_liste.txt")
        open(lst, "w").write("".join(f"file '{c}'\n" for c in clips))
        # EINMAL neu kodieren, nicht kopieren: die Generator-Clips kommen
        # mit ~10 Mbit/s - per Bitstrom-Kopie geloopt waeren das ~16,6 GB
        # fuer 3,5 h (gemessen, Lauf abgebrochen). Ein Encode des kurzen
        # Zyklus drueckt das auf ~1,3-1,8 Mbit/s; die Montage loopt danach
        # wieder kostenlos per Kopie.
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat",
                        "-safe", "0", "-i", lst,
                        "-c:v", "libx264", "-preset",
                        str(cfg["video_preset"]),
                        "-crf", str(int(cfg["video_crf"])),
                        "-pix_fmt", pixelformat(cfg),
                        "-x264-params", "keyint=240:min-keyint=240:scenecut=0",
                        "-an", zyklus], check=True)
        T = int(round(dauer_s(zyklus)))
        print(f"  KI-Clip-Zyklus: {len(clips)} Clips → {T} s, einmal neu "
              f"kodiert (CRF {cfg['video_crf']}, "
              f"{os.path.getsize(zyklus)/1e6:.1f} MB → "
              f"{os.path.getsize(zyklus)*8/T/1e6:.2f} Mbit/s), kein Zoom",
              flush=True)
    elif (os.path.exists(zyklus) and not a.neu_zyklus
            and os.path.getmtime(zyklus) > os.path.getmtime(bild)):
        T = int(round(dauer_s(zyklus)))
        print(f"  Zoom-Zyklus übernommen ({T} s, "
              f"{os.path.getsize(zyklus)/1e6:.1f} MB)", flush=True)
    else:
        T = zyklus_bauen(bild, zyklus, cfg)
        print(f"  Zoom-Zyklus {T} s gebaut ({os.path.getsize(zyklus)/1e6:.1f} MB), "
              f"{time.time()-t0:.0f}s", flush=True)

    ziel = os.path.join(ordner(a.video), f"video-{int(a.video[1:]):02d}.mp4")
    gesamt = dauer_s(mix)
    wdh = montieren(zyklus, mix, ziel, cfg, gesamt)
    versatz = sync_pruefen(ziel, mix, bei_s=min(3600.0, gesamt / 2))

    d = dauer_s(ziel)
    zeilen = ffprobe(ziel, "stream=duration").splitlines()
    vd, ad = float(zeilen[0]), float(zeilen[1])
    b = {
        "datei": os.path.relpath(ziel, os.path.dirname(arbeit(a.video))),
        "dauer_s": round(d, 2), "dauer_hms": hms(d), "dauer_h": round(d / 3600, 3),
        "dauer_audio_quelle_s": round(gesamt, 2),
        "video_stream_s": round(vd, 2), "audio_stream_s": round(ad, 2),
        "differenz_streams_s": round(abs(vd - ad), 2),
        "sync_versatz_s": versatz,
        "groesse_mb": round(os.path.getsize(ziel) / 1e6, 1),
        "bitrate_gesamt_kbps": round(os.path.getsize(ziel) * 8 / d / 1000, 1),
        "zyklus_s": T, "zyklus_wiederholungen": wdh,
        "zoom": bool(cfg.get("zoom", True)), "zoom_faktor": float(cfg["zoom_faktor"]),
        "fps": int(cfg["fps"]), "aufloesung": f"{cfg['breite']}x{cfg['hoehe']}",
        "renderzeit_s": round(time.time() - t0, 1),
    }
    b["im_zielband"] = float(cfg["laufzeit_ziel_von_h"]) <= b["dauer_h"] <= float(cfg["laufzeit_ziel_bis_h"])
    b["ueber_untergrenze"] = b["dauer_h"] >= float(cfg["laufzeit_min_h"])
    json.dump(b, open(arbeit(a.video, "qa_video.json"), "w"), ensure_ascii=False, indent=1)

    print(f"\nVIDEO {a.video}")
    print(f"  Datei                 {os.path.basename(ziel)}  {b['groesse_mb']} MB")
    print(f"  Laufzeit              {b['dauer_hms']}  ({b['dauer_h']:.2f} h)")
    print(f"  Zielband {cfg['laufzeit_ziel_von_h']}–{cfg['laufzeit_ziel_bis_h']} h  "
          f"→ {'im Band' if b['im_zielband'] else 'AUSSERHALB'} · "
          f"Untergrenze {cfg['laufzeit_min_h']} h "
          f"{'eingehalten' if b['ueber_untergrenze'] else 'VERLETZT'}")
    print(f"  Bild                  {b['aufloesung']} @ {b['fps']} fps, "
          f"Zoom {'an' if b['zoom'] else 'aus'} bis {b['zoom_faktor']}×, "
          f"Zyklus {T} s × {wdh}")
    print(f"  Gesamtbitrate         {b['bitrate_gesamt_kbps']} kbit/s")
    print(f"  Streamlängen          Video {b['video_stream_s']} s, "
          f"Audio {b['audio_stream_s']} s, Differenz {b['differenz_streams_s']} s")
    print(f"  Ton-Versatz gemessen  {b['sync_versatz_s']} s")
    print(f"  Renderzeit            {b['renderzeit_s']} s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
