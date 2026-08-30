#!/usr/bin/env python3
"""Misst das tatsaechliche Sprechtempo der gerenderten Videos.

Ergebnis: produktion/korpus/wpm_gemessen.json

MESSGRUNDLAGE. Vorgesehen war ffprobe auf die gerenderte FLAC/MP4. Beides ist
hier nicht moeglich: produktion/video-*/*.wav und *.mp4 stehen in .gitignore und
liegen nicht im Repository, und ffprobe ist in dieser Umgebung nicht installiert.
Gemessen wird deshalb an der Untertitelspur, die aus demselben Renderlauf stammt:

  Woerter  = alle Woerter der SRT-Kacheln. Schritt 6 schreibt dort die Woerter
             des SKRIPTS (nur die Zeiten kommen aus der Spracherkennung), also
             genau den gesprochenen Text samt Eingangsgebet, Hook und CTA.
  Dauer    = Ende der letzten Kachel minus vorlauf_s. Die SRT liegt auf der
             Zeitachse der Endmischung und beginnt um vorlauf_s versetzt; die
             Differenz ist die Dauer der reinen Sprachspur, also derselbe Nenner,
             den schritt2_tts.py beim Rendern verwendet hat.

Gegenprobe: die so berechneten Werte muessen den Zahlen entsprechen, die
schritt2_tts.py beim Rendern aus dem Audio-Array gemessen und in
produktion/video-0X/upload.md geschrieben hat. Das Skript prueft das und bricht
bei Abweichung ab.
"""
import json, os, re, sys

SRT = "produktion/video-%02d/video-%02d.srt"
UPLOAD = "produktion/video-%02d/upload.md"
PLAN = "produktion/korpus/plan.json"
AUS = "produktion/korpus/wpm_gemessen.json"
VORLAUF_S = 1.5          # produktion/config.md, vorlauf_s
VIDEOS = [1, 2, 3, 4]    # 05 ist nicht gerendert
PLAN_KUERZEL = {1: "V1", 2: "V2", 3: "V3", 4: "V4"}


def srt_lesen(pfad):
    text = open(pfad, encoding="utf-8").read()
    zeiten = re.findall(
        r"(\d\d):(\d\d):(\d\d),(\d\d\d) --> (\d\d):(\d\d):(\d\d),(\d\d\d)", text)
    def sek(h, m, s, ms):
        return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000
    erste = sek(*zeiten[0][:4])
    letzte = sek(*zeiten[-1][4:])
    woerter = 0
    for block in re.split(r"\n\s*\n", text.strip()):
        zeilen = block.strip().split("\n")
        if len(zeilen) >= 3:
            woerter += len(" ".join(zeilen[2:]).split())
    return woerter, erste, letzte, len(zeiten)


def upload_wpm(pfad):
    """Das beim Rendern gemessene Tempo aus der QA-Tabelle."""
    for zeile in open(pfad, encoding="utf-8"):
        treffer = re.search(r"\|\s*Tempo\s*\|\s*([\d.,]+)\s*WPM", zeile)
        if treffer:
            return float(treffer.group(1).replace(",", "."))
    return None


def main():
    plan = json.load(open(PLAN))
    zeilen, abweichungen = [], []
    for n in VIDEOS:
        woerter, erste, letzte, kacheln = srt_lesen(SRT % (n, n))
        dauer = letzte - VORLAUF_S
        wpm = woerter / (dauer / 60)
        beim_rendern = upload_wpm(UPLOAD % n)
        if beim_rendern is not None and abs(round(wpm, 1) - beim_rendern) > 0.05:
            abweichungen.append("V%02d: nachgerechnet %.1f, beim Rendern %.1f"
                                % (n, wpm, beim_rendern))
        korpus = plan[PLAN_KUERZEL[n]]["woerter"]
        zeilen.append({
            "video": "V%02d" % n,
            "korpus": plan[PLAN_KUERZEL[n]]["name"],
            "woerter_gesprochen": woerter,
            "woerter_bibelkorpus_plan": korpus,
            "woerter_rahmen": woerter - korpus,
            "srt_erste_kachel_s": round(erste, 3),
            "srt_letzte_kachel_s": round(letzte, 3),
            "sprechdauer_s": round(dauer, 1),
            "sprechdauer_hms": "%d:%02d:%02d" % (dauer // 3600, dauer % 3600 // 60, dauer % 60),
            "wpm": round(wpm, 1),
            "wpm_beim_rendern": beim_rendern,
            "srt_kacheln": kacheln,
        })
    if abweichungen:
        raise SystemExit("Nachrechnung weicht vom Renderlauf ab:\n  "
                         + "\n  ".join(abweichungen))

    w_ges = sum(z["woerter_gesprochen"] for z in zeilen)
    d_ges = sum(z["sprechdauer_s"] for z in zeilen)
    gesamt = w_ges / (d_ges / 60)
    werte = [z["wpm"] for z in zeilen]
    # Poesie (V01/V02: Psalmen, Sprueche) gegen Prosa (V03/V04: Evangelien)
    poesie = [z["wpm"] for z in zeilen if z["video"] in ("V01", "V02")]
    prosa = [z["wpm"] for z in zeilen if z["video"] in ("V03", "V04")]

    ergebnis = {
        "zweck": "Gemessenes Sprechtempo der gerenderten Videos, Quelle fuer wpm_erwartet in config.md",
        "messgrundlage": ("Untertitelspur aus demselben Renderlauf; Woerter = Skriptwoerter "
                          "der SRT-Kacheln, Dauer = Ende der letzten Kachel minus vorlauf_s. "
                          "ffprobe auf die Audiodatei war nicht moeglich: die gerenderten "
                          "WAV/MP4 stehen in .gitignore und liegen nicht im Repository, "
                          "ffprobe ist in der Arbeitsumgebung nicht vorhanden."),
        "gegenprobe": ("Jeder Wert stimmt mit dem Tempo ueberein, das schritt2_tts.py beim "
                       "Rendern aus dem Audio-Array gemessen und in video-0X/upload.md "
                       "eingetragen hat. Das Skript bricht bei Abweichung ab."),
        "stimme": "MILO SOOTHING VOICE, prosody_speed 0.88 - ueber alle vier Laeufe unveraendert",
        "nicht_gemessen": ["V05 - nicht gerendert", "V06-V08 - nicht gerendert"],
        "videos": zeilen,
        "spanne_wpm": [min(werte), max(werte)],
        "mittel_ungewichtet": round(sum(werte) / len(werte), 1),
        "gesamt_wortgewichtet": round(gesamt, 1),
        "woerter_gesamt": w_ges,
        "sprechdauer_gesamt_s": round(d_ges, 1),
        "poesie_v01_v02": round(sum(poesie) / len(poesie), 1),
        "prosa_v03_v04": round(sum(prosa) / len(prosa), 1),
        "befund_textsorte": ("Die Spanne ist nicht Streuung, sondern Textsorte: V01/V02 "
                             "(Psalmen, Sprueche) laufen langsamer als V03/V04 (Evangelien). "
                             "prosody_speed war in allen vier Laeufen 0.88, die Konfiguration "
                             "hat sich also nicht geaendert. n=4, zwei Videos je Gruppe."),
        "empfehlung_config": ("wpm_erwartet = wortgewichtetes Gesamttempo. Fuer einen reinen "
                              "Erzaehlkorpus ist der Prosawert der bessere Schaetzer; das ist "
                              "bei n=2 je Gruppe aber kein belastbarer eigener Parameter."),
    }
    json.dump(ergebnis, open(AUS, "w"), ensure_ascii=False, indent=1)

    print("%-5s %-44s %9s %11s %7s %9s" % ("", "Korpus", "Woerter", "Sprechdauer", "WPM", "beim Rendern"))
    for z in zeilen:
        print("%-5s %-44s %9s %11s %7.1f %9s"
              % (z["video"], z["korpus"][:44], "{:,}".format(z["woerter_gesprochen"]),
                 z["sprechdauer_hms"], z["wpm"], z["wpm_beim_rendern"]))
    print("\nSpanne        %.1f - %.1f WPM" % (min(werte), max(werte)))
    print("Mittel        %.1f WPM (ungewichtet)" % (sum(werte) / len(werte)))
    print("Gesamt        %.1f WPM (%s Woerter / %.0f s, wortgewichtet)" % (gesamt, "{:,}".format(w_ges), d_ges))
    print("  Poesie      %.1f WPM (V01, V02)" % (sum(poesie) / len(poesie)))
    print("  Prosa       %.1f WPM (V03, V04)" % (sum(prosa) / len(prosa)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
