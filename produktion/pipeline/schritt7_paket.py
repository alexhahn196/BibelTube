#!/usr/bin/env python3
"""
Schritt 7 - Upload-Paket.

Legt neben MP4, SRT und Platzhalterbild eine `upload.md` mit allem, was
beim Hochladen von Hand einzutragen ist. Der Upload laeuft bewusst nicht
automatisch: die **KI-Kennzeichnung** muss dabei gesetzt werden
(Formel §7/§8, Compliance-Entscheidung), und das Thumbnail ist zu dem
Zeitpunkt noch nicht final.

Aufruf:
    python3 produktion/pipeline/schritt7_paket.py V1
"""
import argparse
import datetime
import hashlib
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gemeinsam import CONFIG, arbeit, config, hms, ordner, pfad  # noqa: E402
import vorlage                                     # noqa: E402


def mmss(s):
    s = int(round(s))
    return (f"{s//3600}:{(s%3600)//60:02d}:{s%60:02d}" if s >= 3600
            else f"{s//60}:{s%60:02d}")


def lade(video, name):
    p = arbeit(video, name)
    return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else None


def beschreibung_bauen(roh, kap_block):
    """Beschreibung fuer den Upload fertigstellen.

    Zwei Dinge, die vorher von Hand nachgezogen werden mussten:

    1. **Spendenlink raus.** Die Vorlagen in `videos-01-08.md` tragen die Zeile
       „Support the channel: [Spendenlink]" als Platzhalter fuer einen Link,
       den es nicht gibt. Ein Platzhalter in der veroeffentlichten
       Beschreibung ist schlimmer als keine Zeile.
    2. **Hashtags bleiben die letzte Zeile.** Der Kapitelblock gehoert davor,
       nicht dahinter - so sieht das V01-Paket aus, und YouTube zeigt die
       ersten drei Hashtags ueber dem Titel nur, wenn sie am Ende stehen.
    """
    zeilen = [z for z in roh.rstrip().split("\n")
              if not z.strip().lower().startswith("support the channel")]
    # nachlaufende Leerzeilen entfernen, die der entfernte Link hinterlaesst
    while zeilen and not zeilen[-1].strip():
        zeilen.pop()

    hashtags = []
    if zeilen and zeilen[-1].lstrip().startswith("#"):
        hashtags = [zeilen.pop()]
        while zeilen and not zeilen[-1].strip():
            zeilen.pop()

    if kap_block:
        zeilen += ["", "Kapitel:", kap_block]
    if hashtags:
        zeilen += [""] + hashtags
    return "\n".join(zeilen)


def _git(*args):
    """Git-Auskunft, oder None wenn hier kein Repository liegt."""
    try:
        r = subprocess.run(["git", "-C", pfad(), *args],
                           capture_output=True, text=True, timeout=10)
        return r.stdout.strip() if r.returncode == 0 else None
    except Exception:
        return None


def _auszug(quelle, felder):
    """Die genannten Felder aus einer QA-Datei, fehlende stillschweigend aus.

    Fehlt die Quelle ganz (abgebrochener Lauf), kommt ein leeres Dict zurueck -
    eine halbe Messung ist besser als keine, solange sichtbar bleibt, welche
    Felder fehlen.
    """
    if not quelle:
        return {}
    return {k: quelle[k] for k in felder if k in quelle}


def qa_bauen(video, cfg, skript, qs, qm, qv, qsrt, qb, qnamen):
    """Die Messwerte EINES Renderlaufs, so klein wie moeglich, eingecheckt.

    Warum es diese Datei gibt: die QA-Dateien der Schritte 1-6 liegen in
    `produktion/arbeit/`, und das steht in `.gitignore`. Bis 2026-08-26 hatte
    damit **jeder** Messwert in `upload.md` keine im Repository nachpruefbare
    Quelle - er war maschinell erzeugt, aber nicht belegbar. Genau die
    Fehlerklasse, die der Prozessbefund in `produktion/workflow-gates.md`
    beschreibt.

    Aufgenommen wird nur, was in Berichten oder Gate-Pruefungen auftaucht:
    rund 40 Felder, ein bis zwei Kilobyte je Video. Draussen bleiben die
    grossen Zwischenstaende - die Chunk-Listen, die ASR-Wortzeiten, der
    Volltext des Skripts (der steht in `videos-01-08.md` und im SRT) und die
    Kapitelmarken (die stehen in `beschreibung.txt`).

    Der Kopf ist der eigentliche Punkt: `commit`, `arbeitsbaum_sauber` und
    `config_sha256` binden jeden Wert an einen **Stand**, nicht an eine
    Sitzung. Ohne sie waere die Datei nur eine weitere Zahl ohne Herkunft.
    """
    roh = open(CONFIG, "rb").read()
    kopf = {
        "video": video,
        "erzeugt": datetime.datetime.now().replace(microsecond=0).isoformat(),
        "commit": _git("rev-parse", "HEAD"),
        "arbeitsbaum_sauber": (_git("status", "--porcelain") == ""),
        "config_sha256": hashlib.sha256(roh).hexdigest()[:16],
        "bett_datei": cfg.get("bett_datei"),
        "videoquelle": cfg.get("videoquelle"),
        "stimme_id": cfg.get("stimme_id"),
        "tts_modell": cfg.get("tts_modell"),
        "prosody_speed": cfg.get("prosody_speed"),
    }
    b = (skript or {}).get("bericht") or {}
    return {
        **kopf,
        "schritt1_text": _auszug(b, (
            "titel", "hook_variante", "kapitel_anzahl", "woerter_gesamt",
            "woerter_korpus", "woerter_rahmen", "zeichen_tts",
            "laufzeit_erwartet_h", "cta_anzahl", "versalien_uebrig",
            "ziffern_im_text")),
        "schritt2_tts": _auszug(qs, (
            "dauer_h", "woerter", "wpm", "zeichen_tts", "chunks",
            "sprachanteil_pct", "sprachanteil_vergleichbar_pct",
            "laengste_pause_s", "sprach_rms_db", "peak_dbfs",
            "naht_sprung_max_db", "chunk_pegel_sprung_max_db")),
        "schritt3_bett": _auszug(qm, (
            "gain_stimme_db", "gain_bett_db", "gemessen_stimme_dbfs",
            "gemessen_bett_allein_dbfs", "gemessen_bett_je_kanal_dbfs",
            "gemessener_abstand_db", "gemessener_abstand_je_kanal_db",
            "bett_dekorreliert_db", "soll_abstand_db",
            "abstand_eingehalten_mono", "abstand_eingehalten_je_kanal",
            "peak_dbfs", "stichprobe_schreibweg_db", "ducking")),
        "schritt4_bild": _auszug(qb, ("dunkelanteil_pct", "warmpunkte",
                                      "breite", "hoehe")),
        "schritt5_video": _auszug(qv, (
            "dauer_hms", "dauer_h", "groesse_mb", "bitrate_gesamt_kbps",
            "aufloesung", "fps", "sync_versatz_s", "differenz_streams_s",
            "zyklus_s", "zoom", "zoom_faktor")),
        "schritt6_srt": _auszug(qsrt, (
            "kacheln", "erste_kachel_s", "abdeckung_pct", "modell",
            "zuordnungsquote_median", "ueberlappungen")),
        "qa_namen": _auszug(qnamen, ("eigennamen_gesamt", "vorkommen_gesamt",
                                     "beanstandet")),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    a = ap.parse_args()
    cfg = config()
    nr = int(a.video[1:])
    v = vorlage.lies(a.video)
    ord_ = ordner(a.video)

    skript = lade(a.video, "skript.json")
    qs = lade(a.video, "qa_stimme.json")
    qm = lade(a.video, "qa_mix.json")
    qv = lade(a.video, "qa_video.json")
    qsrt = lade(a.video, "qa_srt.json")
    qb = lade(a.video, "qa_bild.json")
    qnamen = lade(a.video, "qa_namen.json")
    marken = lade(a.video, "kapitelmarken.json") or []

    dateien = {n: os.path.exists(os.path.join(ord_, n)) for n in (
        f"video-{nr:02d}.mp4", f"video-{nr:02d}.srt", "PLATZHALTER_standbild.png")}

    # Kapitelmarken sind eine Entscheidung je Video, keine Eigenschaft der
    # Pipeline: videos-01-08.md empfiehlt ja bei 01/02/06/08, nein bei
    # 03/04/05/07 (Formel §7 fuehrt sie als optional). Schritt 6 erzeugt sie
    # immer; hier entscheidet sich, ob sie ins Paket kommen.
    erlaubt = [s.strip() for s in
               str(cfg.get("kapitelmarken_videos", "")).split(",") if s.strip()]
    if erlaubt and a.video not in erlaubt:
        marken = []

    kap_block = "\n".join(f"{mmss(m['zeit_s'])} {m['titel']}" for m in marken)
    beschreibung = beschreibung_bauen(v["beschreibung"], kap_block if marken else "")

    z = []
    z.append(f"# Upload — Video {nr:02d}\n")
    z.append("> Automatisch aus der Pipeline erzeugt. Alles unten wird beim Upload\n"
             "> **von Hand** eingetragen.\n")

    z.append("## Vor dem Upload zu erledigen\n")
    z.append('- [ ] **KI-Kennzeichnung setzen** („Altered or synthetic content" /')
    z.append('      „Realistic audio"). Die Stimme ist synthetisch. Formel §7 und §8')
    z.append('      führen das als Compliance-Entscheidung ohne Datenbeleg in beide')
    z.append('      Richtungen.')
    z.append('- [ ] **Thumbnail ersetzen.** Im Paket liegt nur')
    z.append('      `PLATZHALTER_standbild.png` — das ist das Standbild der Videospur,')
    z.append('      **nicht** das Thumbnail.')
    z.append(f"      Motivvorgabe: {v['thumb_motiv']}")
    z.append(f"      Thumbnail-Text: `{v['thumb_text']}` — Versalhöhe ≥ 11,5 % der")
    z.append('      Bildhöhe, Kontrast ≥ 10:1, höchstens 4 Wörter')
    z.append('      (`formel/thumbnail-checkliste.md`).')
    z.append("- [ ] Untertiteldatei hochladen (Sprache: Englisch).")
    z.append("- [ ] Sichtbarkeit/Zeitplan nach `produktion/videos-01-08.md` (5 Tage Abstand).\n")

    z.append("## Titel\n")
    z.append(f"```\n{v['titel']}\n```\n")

    z.append("## Beschreibung\n")
    z.append(f"```\n{beschreibung}\n```\n")

    z.append("## Tags\n")
    z.append("Formel §7: A hat auf **allen 8** Videos 0 Tags, B's drei gemessene Treffer\n"
             "ebenfalls 0. Sie kosten nichts — erwarte aber nichts von ihnen.\n")
    z.append("```\n" + ", ".join(v["tags"]) + "\n```\n")

    if marken:
        z.append(f"## Kapitelmarken ({len(marken)})\n")
        z.append("Formel §7: **optional, nicht Pflicht.** A's drei größte Treffer haben\n"
                 "null Kapitelmarken, B setzt sie durchgehend. Beide Muster gewinnen —\n"
                 "hier für die Nutzbarkeit gesetzt, nicht für die Reichweite.\n")
        z.append("Sie stehen bereits in der Beschreibung oben.\n")

    z.append("## Dateien im Paket\n")
    for n, da in dateien.items():
        z.append(f"- `{n}` {'✓' if da else '**FEHLT**'}")
    z.append("")

    z.append("## Messwerte dieses Renderlaufs\n")
    z.append("> Alle Werte dieser Tabelle stammen aus `qa.json` in diesem Ordner —\n"
             "> eingecheckt, mit Commit und Config-Pruefsumme. Kein Wert hier ist\n"
             "> von Hand eingetragen.\n")
    z.append("| Größe | Wert | Vorgabe |")
    z.append("|---|---|---|")
    if qv:
        z.append(f"| Laufzeit | {qv['dauer_hms']} ({qv['dauer_h']:.2f} h) | "
                 f"≥{cfg['laufzeit_min_h']} h, Ziel {cfg['laufzeit_ziel_von_h']}–"
                 f"{cfg['laufzeit_ziel_bis_h']} h |")
        z.append(f"| Dateigröße | {qv['groesse_mb']} MB | — |")
        z.append(f"| Bild | {qv['aufloesung']} @ {qv['fps']} fps | 1920×1080, 24–30 fps (§5) |")
        z.append(f"| Ton-Versatz | {qv['sync_versatz_s']} s | 0 |")
    if qs:
        z.append(f"| Tempo | {qs['wpm']} WPM | 120–160 WPM (§5b) |")
        z.append(f"| Sprachanteil (Lücken <1 s zugerechnet) | "
                 f"{qs['sprachanteil_vergleichbar_pct']} % | "
                 f"≥{cfg['sprachanteil_min_pct']} % (§3) |")
        z.append(f"| längste Pause | {qs['laengste_pause_s']} s | "
                 f"<{cfg['laengste_pause_max_s']} s (§3) |")
    if qm:
        z.append(f"| Abstand Stimme zu Bett | {qm['gemessener_abstand_db']} dB | "
                 f"{qm['soll_abstand_db']} dB (§5b) |")
        z.append(f"| Peak | {qm['peak_dbfs']} dBFS | <{cfg['peak_max_dbfs']} dBFS |")
    if qsrt:
        z.append(f"| Untertitelkacheln | {qsrt['kacheln']} | — |")
        z.append(f"| erste Kachel | {qsrt['erste_kachel_s']} s | "
                 f"Sprache in Sekunde 0–{cfg['sprachstart_max_s']} (§3) |")
    if skript:
        z.append(f"| CTA | {skript['bericht']['cta_anzahl']} | höchstens "
                 f"{cfg['cta_max']} (§3) |")
        z.append(f"| TTS-Zeichen | {skript['bericht']['zeichen_tts']:,} | — |"
                 .replace(",", "."))
    if qb:
        z.append(f"| Standbild dunkel | {qb['dunkelanteil_pct']} % der Fläche | "
                 f"dunkles Gesamtbild (§5) |")
    z.append("")

    z.append("## Stimme\n")
    z.append(f"`{cfg['stimme_name']}` — Fish Audio `{cfg['stimme_id']}`, "
             f"Modell {cfg['tts_modell']}, Tempo {cfg['prosody_speed']}.\n"
             f"Feste Kanalstimme, siehe `produktion/config.md`.\n")

    ziel = os.path.join(ord_, "upload.md")
    open(ziel, "w", encoding="utf-8").write("\n".join(z) + "\n")

    # Die Messwerte als eingecheckte Quelle neben den Bericht legen. Muss NACH
    # upload.md geschrieben werden: die Tabelle oben verweist darauf.
    qa_ziel = os.path.join(ord_, "qa.json")
    json.dump(qa_bauen(a.video, cfg, skript, qs, qm, qv, qsrt, qb, qnamen),
              open(qa_ziel, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    # Titel, Beschreibung und Tags zusaetzlich als nackte Textdateien: beim
    # Upload werden sie einzeln in die YouTube-Felder kopiert, und aus einer
    # Markdown-Datei mit Codebloecken herauszuschneiden ist fehleranfaellig.
    for name, inhalt in (("titel.txt", v["titel"]),
                         ("beschreibung.txt", beschreibung),
                         ("tags.txt", ", ".join(v["tags"]))):
        open(os.path.join(ord_, name), "w", encoding="utf-8").write(inhalt + "\n")

    print(f"\nPAKET {a.video}   {ord_}")
    for n, da in dateien.items():
        gr = (f"{os.path.getsize(os.path.join(ord_, n))/1e6:.1f} MB" if da else "FEHLT")
        print(f"  {'✓' if da else '✗'} {n:32s} {gr}")
    print(f"  ✓ upload.md                      "
          f"{os.path.getsize(ziel)/1000:.1f} kB, {len(marken)} Kapitelmarken")
    print(f"  ✓ qa.json                        "
          f"{os.path.getsize(qa_ziel)/1000:.1f} kB — eingecheckte Quelle der Messwerte")
    fehlend = [n for n, da in dateien.items() if not da]
    if fehlend:
        print(f"  ACHTUNG: {fehlend} fehlen")
    return 1 if fehlend else 0


if __name__ == "__main__":
    sys.exit(main())
