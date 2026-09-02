#!/usr/bin/env python3
"""Misst den fertigen Renderlauf von Video 06 und schreibt
produktion/korpus/v06_render.json.

Das ist die Bestaetigung, die den rekonstruierten Werten aus V01-V05 fehlt:
dort war die Audiodauer aus der Untertitelspur zurueckgerechnet, weil die
gerenderten Dateien nicht im Repository liegen und ffprobe nicht vorhanden war.
Hier liegt die Datei lokal vor und wird direkt vermessen.

  Dauer   = ffprobe auf die lokale Tonspur des fertigen MP4 (format=duration),
            gegengeprueft gegen die Videospur und gegen die WAV-Mischung.
  Woerter = gesprochene Woerter aus dem gebauten Skript (Verse plus
            Kapitelueberschriften plus Rahmen), also derselbe Zaehler, den
            schritt1_text.py und schritt2_tts.py verwenden.
  WPM     = Woerter / (Sprechdauer / 60), wobei die Sprechdauer die Gesamtdauer
            abzueglich Vorlauf und Nachlauf ist - derselbe Nenner wie in
            produktion/korpus/wpm_gemessen.json, damit die Zahlen vergleichbar
            bleiben.

Aufruf: python3 produktion/render_messung.py
"""
import json, os, re, subprocess, sys

MP4 = "produktion/video-06/video-06.mp4"
MIX = "produktion/arbeit/video-06/mix.wav"
STIMME = "produktion/arbeit/video-06/stimme.wav"
SKRIPT = "produktion/arbeit/video-06/skript.json"
SRT = "produktion/video-06/video-06.srt"
AUS = "produktion/korpus/v06_render.json"


def ffprobe(datei, eintrag, stream=None):
    cmd = ["ffprobe", "-v", "error"]
    if stream:
        cmd += ["-select_streams", stream]
    cmd += ["-show_entries", eintrag, "-of", "default=nw=1:nk=1", datei]
    return subprocess.run(cmd, capture_output=True, text=True, check=True).stdout.strip()


def config_wpm():
    text = open("produktion/config.md", encoding="utf-8").read()
    werte = {}
    for zeile in "\n".join(re.findall(r"```ini\n(.*?)```", text, re.S)).splitlines():
        zeile = zeile.split("#", 1)[0].strip()
        if "=" in zeile:
            k, v = zeile.split("=", 1)
            werte[k.strip()] = v.strip()
    return (float(werte["wpm_erwartet"]), float(werte["vorlauf_s"]),
            float(werte["nachlauf_s"]), float(werte["laufzeit_ziel_von_h"]),
            float(werte["laufzeit_ziel_von_h_vollwerk"]), float(werte["laufzeit_ziel_bis_h"]))


def main():
    fehlt = [p for p in (MP4, MIX, STIMME, SKRIPT) if not os.path.exists(p)]
    if fehlt:
        raise SystemExit("fehlt: %s" % ", ".join(fehlt))
    wpm_soll, vorlauf, nachlauf, ziel_von, ziel_von_vollwerk, ziel_bis = config_wpm()
    b = json.load(open(SKRIPT))["bericht"]

    mp4_gesamt = float(ffprobe(MP4, "format=duration"))
    mp4_audio = float(ffprobe(MP4, "stream=duration", "a:0"))
    mp4_video = float(ffprobe(MP4, "stream=duration", "v:0"))
    mix_dauer = float(ffprobe(MIX, "format=duration"))
    stimme_dauer = float(ffprobe(STIMME, "format=duration"))

    woerter = b["woerter_gesamt"]
    sprechdauer = mp4_audio - vorlauf - nachlauf
    wpm = woerter / (sprechdauer / 60)

    d = {
        "was": ("Messung des fertigen V06-Renderlaufs. Erste Messung des Projekts "
                "direkt an der gerenderten Datei statt an der Untertitelspur."),
        "datum": "2026-08-31",
        "herkunft": "gemessen",
        "werkzeug": "ffprobe " + subprocess.run(
            ["ffprobe", "-version"], capture_output=True, text=True).stdout.split()[2],
        "datei": {
            "pfad": MP4,
            "groesse_mb": round(os.path.getsize(MP4) / 1e6, 1),
            "video_codec": ffprobe(MP4, "stream=codec_name", "v:0"),
            "aufloesung": "%sx%s" % (ffprobe(MP4, "stream=width", "v:0"),
                                     ffprobe(MP4, "stream=height", "v:0")),
            "pixelformat": ffprobe(MP4, "stream=pix_fmt", "v:0"),
            "fps": ffprobe(MP4, "stream=r_frame_rate", "v:0"),
            "audio_codec": ffprobe(MP4, "stream=codec_name", "a:0"),
            "audio_kanaele": int(ffprobe(MP4, "stream=channels", "a:0")),
        },
        "dauer": {
            "mp4_gesamt_s": round(mp4_gesamt, 3),
            "mp4_tonspur_s": round(mp4_audio, 3),
            "mp4_bildspur_s": round(mp4_video, 3),
            "mix_wav_s": round(mix_dauer, 3),
            "stimme_wav_s": round(stimme_dauer, 3),
            "hms": "%d:%02d:%02d" % (mp4_audio // 3600, mp4_audio % 3600 // 60, mp4_audio % 60),
            "stunden": round(mp4_audio / 3600, 3),
            "bild_ton_versatz_s": round(mp4_video - mp4_audio, 3),
        },
        "woerter": {
            "gesprochen_gesamt": woerter,
            "bibelverse": b["woerter_korpus"] - 166,
            "kapitelueberschriften": 166,
            "rahmen_gebet_hook_cta": b["woerter_rahmen"],
            "quelle": "produktion/arbeit/video-06/skript.json",
        },
        "wpm": {
            "gemessen": round(wpm, 1),
            "herkunft": "gemessen",
            "nenner": ("mp4_tonspur_s minus vorlauf_s (%.1f) und nachlauf_s (%.1f) "
                       "= reine Sprechdauer, gleicher Nenner wie wpm_gemessen.json"
                       % (vorlauf, nachlauf)),
            "sprechdauer_s": round(sprechdauer, 1),
            "config_wpm_erwartet": wpm_soll,
            "abweichung_wpm": round(wpm - wpm_soll, 1),
            "abweichung_pct": round((wpm / wpm_soll - 1) * 100, 1),
        },
        # Bandgrenzen aus config.md, nicht als Literal. Die untere Grenze haengt
        # daran, ob das dominante Buch Erzaehlwerk in voller Laenge ist - das
        # weiss dieses Skript nicht, es misst nur die fertige Datei. Deshalb
        # werden BEIDE Grenzen ausgewiesen und das engere Band als Urteil
        # genommen; korpus_pruefung.py hat den Fall am Reissbrett entschieden.
        "zielband": {
            "von_h": ziel_von, "von_h_vollwerk": ziel_von_vollwerk, "bis_h": ziel_bis,
            "laufzeit_h": round(mp4_audio / 3600, 3),
            "im_band": ziel_von <= mp4_audio / 3600 <= ziel_bis,
            "im_band_vollwerk": ziel_von_vollwerk <= mp4_audio / 3600 <= ziel_bis,
        },
    }
    if os.path.exists(SRT):
        d["untertitel"] = {"datei": SRT,
                           "kacheln": open(SRT, encoding="utf-8").read().count(" --> ")}
    json.dump(d, open(AUS, "w"), ensure_ascii=False, indent=1)

    print("V06 RENDERMESSUNG")
    print("  Datei                 %s, %.1f MB" % (MP4, d["datei"]["groesse_mb"]))
    print("  Bild                  %s %s %s fps, %s" % (d["datei"]["aufloesung"],
          d["datei"]["pixelformat"], d["datei"]["fps"], d["datei"]["video_codec"]))
    print("  Ton                   %s, %d Kanaele" % (d["datei"]["audio_codec"],
                                                     d["datei"]["audio_kanaele"]))
    print("  Dauer (ffprobe)       %s  (%.3f h)" % (d["dauer"]["hms"], d["dauer"]["stunden"]))
    print("  Bild gegen Ton        %+.3f s" % d["dauer"]["bild_ton_versatz_s"])
    print("  Gesprochene Woerter   %s" % "{:,}".format(woerter))
    print("  Sprechdauer           %.1f s" % sprechdauer)
    print("  GEMESSENES TEMPO      %.1f WPM" % d["wpm"]["gemessen"])
    print("  config.md erwartet    %.1f WPM  -> Abweichung %+.1f WPM (%+.1f %%)"
          % (wpm_soll, d["wpm"]["abweichung_wpm"], d["wpm"]["abweichung_pct"]))
    z = d["zielband"]
    print("  Zielband %.1f-%.1f h    %s%s" % (
        z["von_h"], z["bis_h"], "im Band" if z["im_band"] else "AUSSERHALB",
        "" if z["im_band"] or not z["im_band_vollwerk"] else
        " (im tieferen Band ab %.1f h - gilt nur, wenn Gate 1.13 haelt)" % z["von_h_vollwerk"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
