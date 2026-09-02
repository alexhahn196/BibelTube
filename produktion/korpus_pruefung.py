#!/usr/bin/env python3
"""
korpus_pruefung.py - prueft einen Textkorpus gegen M8, Formel Paragraph 2 und
die Doppelvergabe.

Gate 1 fuehrt seit 2026-08-23 zwei Pruefungen, die vorher nicht existierten:
  1.13 Korpusart  - Hauptkorpus muss durchlaufender Erzaehlstoff sein
  1.1  Korpuslaenge - Wortfenster, hergeleitet aus config.md (Zielband und
       wpm_erwartet). Kein fester Wert mehr: die Sprechgeschwindigkeit haengt
       am Korpus, und ein Fenster aus 140 WPM liess bei 148,1 zu kurze
       Korpora durch - genau so landete V05 bei 3,40 h statt 3,6 h.
Beide standen dort als "von Hand". Dieses Skript macht sie nachrechenbar.

=============================================================================
DIE 80-PROZENT-SCHWELLE IST AM 2026-08-31 GEFALLEN. WARUM.
=============================================================================
Bis dahin pruefte 1.13 hier "Erzaehlanteil >= 80 %" gegen die Gattungstabelle
weiter unten. Diese Tabelle stuft BUCHWEISE ein - Lukas ist darin komplett
Erzaehlung. Es gab aber eine zweite, eingecheckte Messung derselben Groesse:
produktion/korpus/erzaehlanteil.json stuft KAPITELWEISE ein und zaehlt
Lehrreden, Gleichniszyklen und eingelegte Gebete heraus.

Beide sind echte Messdateien. Sie widersprechen sich:

    Video          buchweise (hier)   kapitelweise
    V03 Johannes        62,3 %                38,2 %
    V04 Matthaeus       83,0 %                45,8 %
    V05 Lukas           81,7 %                47,6 %

(Die kapitelweisen Werte dieser drei Videos stehen in
produktion/korpus/eigene_videos_erzaehlanteil.json, nicht in erzaehlanteil.json -
letztere fuehrt die freien Buecher, nicht die verbrauchten.)

Dasselbe Gate gab damit je nach Koernung das Gegenteil aus: V05 bestand hier
mit 81,7 % und fiel dort mit 47,6 % durch. Zwei Wahrheiten sind schlimmer als
eine falsche - man kann sich die passende aussuchen.

Aufgeloest: die kapitelweise Messung ist die feinere und ist ab jetzt die
gueltige. Sie wird unten GEMELDET. Sie GATET nicht, und die buchweise erst
recht nicht:

  - Die 80 % sind von keiner eigenen Messung beruehrt. V01-V05 liegen
    kapitelweise bei 0,0 bis 47,6 % - kein einziges produziertes Video
    erreicht sie.
  - V03, das einzige Video des Kanals, das funktioniert hat (14,4 %
    Endretention, 80 % der Kanal-Wiedergabezeit), faellt in BEIDEN Messungen
    durch (62,3 / 38,2 %). Die 80 koennen also nicht die Groesse sein, an der
    V03 gegen V02 gewonnen hat.
  - Was M8 belegt, ist die STRUKTUR: Evangelium gegen Spruchsammlung, nicht
    80 gegen 79. Genau die prueft 1.13 jetzt:
        dominantes Buch >= gate_dominanz_min der Woerter
        UND dieses Buch ist selbst durchlaufendes Erzaehlwerk
            (>= gate_erzaehlanteil_min, KAPITELWEISE gemessen aus
             produktion/korpus/erzaehlanteil.json - nicht aus der
             Gattungstabelle weiter unten)
        UND es wird in voller Laenge gelesen ODER an einer Erzaehlnaht
            geteilt, die mit Begruendung in erzaehlnaehte_datei steht, und der
            gelesene Teil haelt fuer sich gate_erzaehlanteil_min
            (gelockert 2026-09-02)
        UND es liegt >= gate_abstand_min vor dem zweitgroessten Buch
            (neu am 2026-09-02)
    Nebenstoff ist frei.

=============================================================================
SCHWELLEN GEAENDERT AM 2026-09-02 - UND WO SIE JETZT STEHEN
=============================================================================
Keine Schwelle steht mehr als Literal in dieser Datei. DOMINANZ_MIN,
ERZAEHLWERK_MIN und beide Bandgrenzen kommen aus produktion/config.md.

  Dominanz            60 % -> 50 %. Die 60 waren selbstgesetzt und durch nichts
                      belegt. Sie sollen sichern, dass ein Eigenname aus dem
                      dominanten Buch Titel und Thumbnail traegt - das tut er
                      bei der Haelfte der Laufzeit genauso.
  untere Bandgrenze   3,4 h -> 3,0 h, aber NUR wenn der groesste Block ein
                      ganzes Buch ist und selbst Erzaehlwerk
                      (groesster_ist_vollwerk). Sonst unveraendert 3,4 h.
                      laufzeit_min_h (3,0 h) ist davon unberuehrt.

Grund: die beiden Regeln klemmten sich gegenseitig ein. Ein ganzes Erzaehlbuch
von 14.000-18.000 W kam bei 3,4 h Bandbeginn nie auf 60 % Dominanz und fiel an
der GROESSE aus, nicht an seiner Struktur - Markus (14.261 W) ist der Fall.

GATTUNGSTABELLE: Die Zuordnung Erzaehlung/Nicht-Erzaehlung steht unten im
Klartext und folgt der Standardgliederung. Sie ist nach dem Obigen NICHT mehr
die Quelle des Erzaehlanteils - sie beantwortet nur noch die Ja/Nein-Frage
"ist das dominante Buch ueberhaupt Erzaehlwerk". In dieser Rolle ist sie
belastbar: dass Lukas Erzaehlung ist und Jesaja nicht, haengt nicht an der
Koernung.

WICHTIG, NICHT LOESCHEN: Die buchweisen Prozentsaetze bleiben stehen und
werden weiter gedruckt - als "Gattungsanteil", nicht als Erzaehlanteil. Die
WPM-Regression in config.md (WPM = 141,15 + 0,0769 x Erzaehlanteil%) ist auf
GENAU DIESE Werte gefittet (0,0 / 0,0 / 62,3 / 83,0 / 81,7). Wer sie durch die
kapitelweisen ersetzt, muss die Regression neu fitten - sonst rechnet das
halbe Projekt mit einem falschen Tempo.

Aufruf:
    python3 produktion/korpus_pruefung.py "Apostelgeschichte" "Rut" "Ester"
    python3 produktion/korpus_pruefung.py --plan V5
    python3 produktion/korpus_pruefung.py --gegen V8 "Markus" "Exodus 1-20"
"""
import argparse
import json
import os
import re
import sys

KAPITEL = os.path.join("produktion", "korpus", "kapitel.json")
PLAN = os.path.join("produktion", "korpus", "plan.json")
#: Die feine, kapitelweise Einstufung. Sie ist die gueltige Messung des
#: Erzaehlanteils (siehe Kopfkommentar). Liegt sie nicht vor, wird der Wert
#: als NICHT GEMESSEN gemeldet - nicht durch den groben Wert ersetzt.
FEIN = os.path.join("produktion", "korpus", "erzaehlanteil.json")
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "pipeline"))
from gemeinsam import config as _config  # noqa: E402

_CFG = _config()
#: Aus config.md, damit jede Zahl nur EINMAL im Repo steht. Herleitung und
#: Korpusabhaengigkeit stehen dort im Kommentar bei wpm_erwartet.
WPM = float(_CFG["wpm_erwartet"])
ZIEL_H = (float(_CFG["laufzeit_ziel_von_h"]), float(_CFG["laufzeit_ziel_bis_h"]))
#: Untere Bandgrenze, wenn das dominante Buch selbst Erzaehlwerk ist UND in
#: voller Laenge im Korpus steht (2026-09-02). Sonst gilt ZIEL_H[0].
ZIEL_VON_H_VOLLWERK = float(_CFG["laufzeit_ziel_von_h_vollwerk"])
#: 2026-09-02 von 0,60 gesenkt. Stand vorher hier als Literal.
DOMINANZ_MIN = float(_CFG["gate_dominanz_min"])
#: Schwelle der Frage "ist der groesste Block ueberhaupt Erzaehlwerk"
#: (groesster_ist_erzaehlung). Stand vorher als 0.8 im Code.
ERZAEHLWERK_MIN = float(_CFG["gate_erzaehlanteil_min"])
#: Die Erzaehlnaht-Pruefung kommt aus produktion/erzaehlanteil.py - eine
#: Implementierung, nicht zwei. Der Pfad der Nahtdatei steht in config.md.
def _naht_werkzeug():
    import importlib.util
    pfad = os.path.join(os.path.dirname(os.path.abspath(__file__)), "erzaehlanteil.py")
    spec = importlib.util.spec_from_file_location("_ea_naht", pfad)
    modul = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modul)
    return modul


#: Mindestabstand des dominanten Buchs zum zweitgroessten, in Anteilspunkten.
#: NEU 2026-09-02: die Dominanzschwelle allein laesst 50,1 gegen 45,0 durch,
#: und dann verkauft der Eigenname im Titel ein Buch, das knapp die Haelfte
#: traegt. Herleitung und Messung in config.md bei gate_abstand_min.
ABSTAND_MIN = float(_CFG["gate_abstand_min"])
#: Wo die Erzaehlnaehte stehen - der Pfad kommt aus config.md, nicht von hier.
NAEHTE_DATEI = _CFG["erzaehlnaehte_datei"]
#: Vor- und Nachlauf des Klangbetts liegen vor bzw. hinter der Sprache und
#: verlaengern das fertige Video, ohne ein Wort zu kosten.
_RAND_S = float(_CFG["vorlauf_s"]) + float(_CFG["nachlauf_s"])
#: Der Rahmen (Hook, 2 CTA, Eingangsgebet). Gemessen an V05:
#: produktion/video-05/qa.json fuehrt woerter_rahmen 232.
RAHMEN_W = 232
#: Jede Kapitelansage ("Luke, chapter one") sind drei gesprochene Woerter.
#: An V05 exakt nachgerechnet: 29.880 + 3x36 + 232 = 30.220 = woerter_gesamt.
ANSAGE_W = 3


def _video_h(korpus_w: int, kapitel_n: int) -> float:
    """Laufzeit des fertigen Videos aus der reinen Korpus-Wortzahl."""
    gesamt = korpus_w + ANSAGE_W * kapitel_n + RAHMEN_W
    return gesamt / WPM / 60 + _RAND_S / 3600


def band_fuer(kapitel_n: int, vollwerk: bool = False) -> tuple[int, int]:
    """Das Korpus-Wortfenster des Zielbands. EINE Definition, geteilt mit
    produktion/erzaehlanteil.py (band()): round(h x 60 x WPM), reine
    Korpuswoerter.

    2026-09-02 vereinheitlicht. Bis dahin zog diese Funktion die Kapitelansagen
    (3 W je Kapitel), den Rahmen (232 W) und den Vor-/Nachlauf des Betts ab,
    erzaehlanteil.py nicht - dieselbe Pruefung 1.1 gab damit zwei Fenster aus,
    fuer V06 29.036-32.379 hier gegen 29.315-32.764 dort. Ein Korpus dazwischen
    bestand beim einen und riss beim anderen. Das ist genau der Fehler, den der
    Kopfkommentar oben beim Erzaehlanteil anprangert.

    Der Rahmen faellt damit aus dem GATE heraus, nicht aus der Rechnung: die
    erwartete Videolaufzeit steht weiter in _video_h() und wird gedruckt, und
    schritt1_text.py prueft die echte Laufzeit nach dem Textbau ein zweites Mal.
    Das Fenster hier ist die Planungsgroesse am Reissbrett.

    kapitel_n wird nicht mehr gebraucht und bleibt nur, damit bestehende Aufrufe
    weiterlaufen.

    vollwerk=True senkt die untere Grenze auf laufzeit_ziel_von_h_vollwerk.
    Erlaubt ist das nur, wenn das dominante Buch selbst Erzaehlwerk ist UND in
    voller Laenge im Korpus steht - beides misst zusammenfassen() mit.
    Die harte Untergrenze laufzeit_min_h ist davon unberuehrt."""
    def w(h: float) -> int:
        return round(h * 60 * WPM)
    return w(ZIEL_VON_H_VOLLWERK if vollwerk else ZIEL_H[0]), w(ZIEL_H[1])

DEUTSCH = {
    "apostelgeschichte": "acts", "markus": "mark", "matthaeus": "matthew",
    "matthäus": "matthew", "lukas": "luke", "johannes": "john",
    "rut": "ruth", "ester": "esther", "jona": "jonah", "exodus": "exodus",
    "josua": "joshua", "richter": "judges", "genesis": "genesis",
    "1. samuel": "1 samuel", "2. samuel": "2 samuel",
    "1. koenige": "1 kings", "1. könige": "1 kings",
    "2. koenige": "2 kings", "2. könige": "2 kings",
    "daniel": "daniel", "jesaja": "isaiah", "psalmen": "psalms",
    "sprueche": "proverbs", "sprüche": "proverbs", "prediger": "ecclesiastes",
    "offenbarung": "revelation", "roemer": "romans", "römer": "romans",
    "hebraeer": "hebrews", "hebräer": "hebrews", "epheser": "ephesians",
    "philipper": "philippians", "kolosser": "colossians", "jakobus": "james",
    "1. petrus": "1 peter", "1. johannes": "1 john",
}

# --- Gattung je Kapitel: True = durchlaufende Erzaehlung -------------------
# Begruendung der Nicht-Erzaehl-Abschnitte steht als Kommentar dahinter.
ERZAEHLUNG = {
    "acts": lambda i: True,
    "mark": lambda i: True,
    "matthew": lambda i: True,
    "luke": lambda i: True,
    "john": lambda i: True,
    "genesis": lambda i: True,
    "ruth": lambda i: True,
    "esther": lambda i: True,
    "jonah": lambda i: i != 2,                       # 2 = Gebet in Psalmenform
    "1 samuel": lambda i: True,
    "2 samuel": lambda i: i != 22,                   # 22 = Danklied (Ps 18)
    "1 kings": lambda i: True,
    "2 kings": lambda i: True,
    "judges": lambda i: True,
    "joshua": lambda i: i < 13 or i > 21,            # 13-21 = Gebietslisten
    # Exodus: 21-23 Bundesbuch, 25-31 Stiftshuetten-Anweisung,
    #         35-40 deren Ausfuehrung. 24 und 32-34 sind wieder Erzaehlung.
    "exodus": lambda i: i <= 20 or i in (24, 32, 33, 34),
    "daniel": lambda i: i <= 6,                      # 7-12 = Visionen
    "psalms": lambda i: False,
    "proverbs": lambda i: False,
    "ecclesiastes": lambda i: False,
    "isaiah": lambda i: False,                       # prophetische Rede
    "revelation": lambda i: False,                   # Apokalyptik
    "romans": lambda i: False, "hebrews": lambda i: False,
    "ephesians": lambda i: False, "philippians": lambda i: False,
    "colossians": lambda i: False, "james": lambda i: False,
    "1 peter": lambda i: False, "1 john": lambda i: False,
}


def fein_lesen():
    """Kapitelweise Erzaehleinstufung, falls eingecheckt. Sonst None."""
    if not os.path.exists(FEIN):
        return None
    try:
        return json.load(open(FEIN, encoding="utf-8"))["kapitel"]
    except (KeyError, ValueError):
        return None


def fein_anteil(kapitel, kap, fein):
    """Erzaehlanteil aus der kapitelweisen Einstufung.

    Gibt (anteil, abgedeckt_pct) zurueck. Kapitel, die die Einstufung nicht
    kennt, gehen NICHT als 0 ein - sie senken die Abdeckung. Ein Anteil ueber
    einer lueckenhaften Grundlage waere eine erfundene Zahl.

    Gezaehlt wird "erzaehlend_woerter", NICHT die Ja/Nein-Flagge "erzaehlend".
    Bei geteilten Kapiteln ist die Flagge nur ein Etikett nach der gemessenen
    Wortmehrheit - erzaehlanteil.json sagt das im Feld "hinweis_flagge" selbst.
    Bis zur Zusammenfuehrung am 2026-09-02 las diese Funktion die Flagge und kam
    damit auf andere Werte als produktion/erzaehlanteil.py, das dieselbe Datei
    schreibt: fuer V06 94,0 % hier gegen 89,0 % dort. Zwei Zahlen fuer dieselbe
    Groesse aus derselben Datei - genau der Fehler, den dieses Skript im
    Kopfkommentar anprangert.
    """
    w_ges = w_bekannt = w_erz = 0
    for b, i in kapitel:
        w = kap[f"{b} {i}"]["w"]
        w_ges += w
        e = fein.get(f"{b} {i}")
        if e is None:
            continue
        w_bekannt += w
        if "erzaehlend_woerter" in e:
            w_erz += e["erzaehlend_woerter"]
        elif e.get("erzaehlend"):
            w_erz += w
    if not w_bekannt:
        return None, 0.0
    return 100 * w_erz / w_bekannt, 100 * w_bekannt / w_ges


def buchlaenge(kap, buch):
    n = 0
    while f"{buch} {n+1}" in kap:
        n += 1
    return n


def aufloesen(spec, kap):
    """'Ester 1-8' oder 'Apostelgeschichte' -> (buch, von, bis)."""
    s = spec.strip()
    m = re.match(r"^(.*?)\s*(\d+)\s*[-–]\s*(\d+)$", s)
    if m:
        name, a, e = m.group(1), int(m.group(2)), int(m.group(3))
    else:
        m2 = re.match(r"^(.*?)\s+(\d+)$", s)
        name, a, e = (m2.group(1), int(m2.group(2)), int(m2.group(2))) if m2 else (s, None, None)
    buch = DEUTSCH.get(name.strip().lower(), name.strip().lower())
    if f"{buch} 1" not in kap:
        raise SystemExit(f"Unbekanntes Buch: {spec!r} (aufgeloest zu {buch!r})")
    if buch not in ERZAEHLUNG:
        raise SystemExit(f"Keine Gattungszuordnung fuer {buch!r} - bitte oben ergaenzen")
    if a is None:
        a, e = 1, buchlaenge(kap, buch)
    return buch, a, e


def kapitel_text(ii):
    """Kapitelliste als Text, zusammenhaengende Laeufe zusammengezogen:
    [1..25, 40..66] -> "1-25+40-66". Bis 2026-09-02 stand hier nur
    f"{ii[0]}-{ii[-1]}"; bei einem Korpus MIT LUECKE - genau der Fall des
    gestrichenen Jesaja-Plans - las sich das als "1-66" und die Meldung
    "gelesen 1-66 von 1-66 REISST" widersprach sich selbst."""
    laeufe, start, vorher = [], ii[0], ii[0]
    for i in ii[1:]:
        if i != vorher + 1:
            laeufe.append((start, vorher))
            start = i
        vorher = i
    laeufe.append((start, vorher))
    return "+".join(str(v) if v == b else f"{v}-{b}" for v, b in laeufe)


def zusammenfassen(teile, kapitel, kap=None, fein=None):
    """Baut das Ergebnis aus den Bloecken. EINE Stelle - der --plan-Weg und der
    Bausteinweg liefen hier frueher durch zwei getrennte, fast gleiche Dicts.

    Gate 1.13 rechnet auf dem BUCH, nicht auf dem Block, und misst KAPITELWEISE.
    Beides ist am 2026-09-02 berichtigt worden:

      - Vorher war "das dominante Buch" der groesste BLOCK (max ueber teile),
        der Mindestabstand aggregierte aber schon pro Buch. Stand ein Buch in
        mehreren Bloecken, war dasselbe Buch gleichzeitig "dominant" und
        "zweiter", und die Dominanz wurde zu klein gerechnet.
      - Vorher kam "ist das dominante Buch Erzaehlwerk" aus der buchweisen
        Gattungstabelle ERZAEHLUNG, die dieses Skript selbst als UEBERHOLT
        ausdruckt. Markus zaehlte dort 100 % und kapitelweise 79,4 % - dasselbe
        Gate gab je nach Werkzeug das Gegenteil aus. Gemessen wird jetzt aus
        produktion/korpus/erzaehlanteil.json, wie in erzaehlanteil.py.

    Liegt die kapitelweise Einstufung nicht vor, ist die Frage NICHT beantwortbar
    (None) - sie wird dann gemeldet und nicht durch den buchweisen Gattungswert
    ersetzt.
    """
    w = sum(t["woerter"] for t in teile)
    erz = sum(t["erzaehlung"] for t in teile)

    # Pro BUCH aggregieren: Woerter, gelesene Kapitel, ob das Buch ganz drinsteht.
    je_buch = {}
    for t in teile:
        b = je_buch.setdefault(t["buch"], {"buch": t["buch"], "woerter": 0, "kapitel": set()})
        b["woerter"] += t["woerter"]
        b["kapitel"] |= set(t.get("kapitel_gelesen") or range(t["von"], t["bis"] + 1))
    for b in je_buch.values():
        b["kapitel"] = sorted(b["kapitel"])
        b["spec"] = b["buch"]
        if kap is not None:
            voll = buchlaenge(kap, b["buch"])
            b["ganzes_buch"] = b["kapitel"] == list(range(1, voll + 1))
            if not b["ganzes_buch"]:
                b["spec"] = f"{b['buch']} {kapitel_text(b['kapitel'])}"
        else:
            b["ganzes_buch"] = any(t["buch"] == b["buch"] and t.get("ganzes_buch")
                                   for t in teile)

    rang = sorted(je_buch.values(), key=lambda x: -x["woerter"])
    dominant = rang[0] if rang else None
    zweiter = rang[1] if len(rang) > 1 else None

    erz_anteil_dominant = None
    if dominant and fein:
        bekannt = [k for k in dominant["kapitel"] if f"{dominant['buch']} {k}" in fein]
        if len(bekannt) == len(dominant["kapitel"]) and bekannt:
            ew = sum(fein[f"{dominant['buch']} {k}"].get("erzaehlend_woerter", 0) for k in bekannt)
            gw = sum(fein[f"{dominant['buch']} {k}"]["woerter"] for k in bekannt)
            erz_anteil_dominant = ew / gw if gw else 0.0

    ist_erzaehlwerk = (None if erz_anteil_dominant is None
                       else erz_anteil_dominant >= ERZAEHLWERK_MIN)
    naht_ok, fehlende_naehte = (True, [])
    if dominant and not dominant["ganzes_buch"] and kap is not None:
        naht_ok, fehlende_naehte = _naht_werkzeug().naht_gedeckt(
            dominant["buch"], dominant["kapitel"], buchlaenge(kap, dominant["buch"]))
    return {"teile": teile, "kapitel": set(kapitel), "woerter": w, "erzaehlung": erz,
            "erz_pct": 100 * erz / w if w else 0,
            "stunden": _video_h(w, len(set(kapitel))),
            "doppelt": len(kapitel) - len(set(kapitel)),
            "je_buch": rang,
            "groesster": dominant,
            "zweiter": zweiter,
            "erz_anteil_dominant": erz_anteil_dominant,
            "groesster_ist_erzaehlung": ist_erzaehlwerk,
            "groesster_an_naht": naht_ok and dominant is not None and not dominant["ganzes_buch"],
            "fehlende_naehte": fehlende_naehte,
            # Erzaehlwerk UND (ungekuerzt ODER an einer eingetragenen Naht
            # geteilt) - nur dann gilt das tiefere Band.
            "groesster_ist_vollwerk": bool(dominant
                                           and (dominant["ganzes_buch"] or naht_ok)
                                           and ist_erzaehlwerk)}


def bewerte(specs, kap, fein=None):
    teile, kapitel = [], []
    for s in specs:
        b, a, e = aufloesen(s, kap)
        fehlend = [i for i in range(a, e + 1) if f"{b} {i}" not in kap]
        if fehlend:
            raise SystemExit(f"Nicht gemessen: {b} {fehlend} - erst wortzahlen.py laufen lassen")
        voll = buchlaenge(kap, b)
        teile.append({"spec": s, "buch": b, "von": a, "bis": e,
                      "ganzes_buch": (a == 1 and e == voll),
                      "woerter": sum(kap[f"{b} {i}"]["w"] for i in range(a, e + 1)),
                      "erzaehlung": sum(kap[f"{b} {i}"]["w"] for i in range(a, e + 1)
                                        if ERZAEHLUNG[b](i))})
        kapitel += [(b, i) for i in range(a, e + 1)]
    return zusammenfassen(teile, kapitel, kap, fein)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("bausteine", nargs="*")
    ap.add_argument("--plan", help="Video aus korpus/plan.json statt Bausteinen")
    ap.add_argument("--gegen", action="append", default=[],
                    help="Video aus plan.json, gegen das auf Doppelvergabe geprueft wird")
    a = ap.parse_args()
    kap = json.load(open(KAPITEL, encoding="utf-8"))
    # Die kapitelweise Einstufung wird VOR der Bewertung geladen: Gate 1.13
    # misst mit ihr, nicht mit der buchweisen Gattungstabelle.
    fein = fein_lesen()

    if a.plan:
        plan = json.load(open(PLAN, encoding="utf-8"))
        refs = plan[a.plan]["refs"]
        kapitel = [(k.rsplit(" ", 1)[0], int(k.rsplit(" ", 1)[1])) for k in refs]
        w = sum(kap[k]["w"] for k in refs)
        erz = sum(kap[f"{b} {i}"]["w"] for b, i in kapitel if ERZAEHLUNG.get(b, lambda _: False)(i))
        # Bis 2026-08-31 blieb "teile" hier leer und 1.13 wurde beim Plan-Pfad
        # STILL uebersprungen - dieselbe Pruefung, die bei Bausteinen greift.
        # Die Bloecke werden jetzt aus den refs zurueckgebaut, damit --plan und
        # Bausteinaufruf dieselben Pruefungen fahren.
        teile = []
        for b in dict.fromkeys(b for b, _ in kapitel):
            ii = sorted(i for x, i in kapitel if x == b)
            bw = sum(kap[f"{b} {i}"]["w"] for i in ii)
            be = sum(kap[f"{b} {i}"]["w"] for i in ii
                     if ERZAEHLUNG.get(b, lambda _: False)(i))
            voll = buchlaenge(kap, b)
            ganz = ii == list(range(1, voll + 1))
            spec = b if ganz else f"{b} {kapitel_text(ii)}"
            teile.append({"spec": spec, "buch": b, "von": ii[0], "bis": ii[-1],
                          "kapitel_gelesen": ii, "ganzes_buch": ganz,
                          "woerter": bw, "erzaehlung": be})
        r = zusammenfassen(teile, kapitel, kap, fein)
        print(f"Plan {a.plan}: {plan[a.plan]['name']}")
    else:
        if not a.bausteine:
            ap.error("Bausteine oder --plan angeben")
        r = bewerte(a.bausteine, kap, fein)

    print(f"\n{'Baustein':34s} {'Woerter':>8s} {'Gattung*':>11s} {'ganzes Buch':>12s}")
    for t in r["teile"]:
        q = 100 * t["erzaehlung"] / t["woerter"] if t["woerter"] else 0
        print(f"{t['spec']:34s} {t['woerter']:8,d} {q:10.1f} % {'ja' if t['ganzes_buch'] else 'NEIN':>12s}")

    print(f"\n{'SUMME':34s} {r['woerter']:8,d} {r['erz_pct']:10.1f} %")
    print(f"{'Videolaufzeit bei ' + str(WPM) + ' WPM':34s} {r['stunden']:8.2f} h"
          f"   (Ziel {ZIEL_H[0]}-{ZIEL_H[1]} h)")
    print("\n* Gattungsanteil, buchweise gerechnet — UEBERHOLT, kein Erzaehlanteil.")
    print("  Der gueltige Erzaehlanteil steht unten. Siehe Kopfkommentar.")

    # --- Erzaehlanteil: gemessen und gemeldet, aber kein Gate ---
    if fein:
        anteil, abdeckung = fein_anteil(sorted(r["kapitel"]), kap, fein)
    else:
        anteil, abdeckung = None, 0.0
    print("\nErzaehlanteil (kapitelweise, die gueltige Messung):")
    if anteil is None:
        print(f"  NICHT GEMESSEN — {FEIN} fehlt oder kennt keines dieser Kapitel.")
        print("  Erzeugen mit: python3 produktion/erzaehlanteil.py")
        print("  Der Wert wird NICHT durch den buchweisen Gattungsanteil ersetzt.")
    else:
        print(f"  {anteil:.1f} %   (Grundlage: {abdeckung:.0f} % der Korpuswoerter "
              f"kapitelweise eingestuft)")
        if abdeckung < 99.5:
            print(f"  Die restlichen {100-abdeckung:.0f} % sind nicht eingestuft und "
                  f"gehen nicht in den Wert ein.")
    print("  Das ist eine Meldung, kein Gate. Begruendung im Kopfkommentar.")

    fehler = []
    print("\nPruefungen:")
    BAND = band_fuer(len(r["kapitel"]), r["groesster_ist_vollwerk"])
    band = BAND[0] <= r["woerter"] <= BAND[1]
    print(f"  1.1  Korpuslaenge {BAND[0]:,}-{BAND[1]:,} W   "
          f"{'OK' if band else 'REISST — ' + ('zu kurz' if r['woerter'] < BAND[0] else 'zu lang')}")
    if not band:
        fehler.append("1.1")
    if r["groesster"]:
        g = r["groesster"]
        anteil_dom = g["woerter"] / r["woerter"]
        dom_ok = anteil_dom >= DOMINANZ_MIN
        print(f"  1.13 dominantes Buch >= {DOMINANZ_MIN*100:.0f} %          "
              f"{'OK' if dom_ok else 'REISST'}  "
              f"({g['spec']}, {g['woerter']:,} W = {100*anteil_dom:.1f} %)")
        if not dom_ok:
            fehler.append("1.13-Dominanz")
        gk = r["groesster_ist_erzaehlung"]
        anteil_dom_erz = r["erz_anteil_dominant"]
        if gk is None:
            print("  1.13 dominantes Buch ist Erzaehlwerk  NICHT MESSBAR  "
                  "(kapitelweise Einstufung fehlt fuer dieses Buch; "
                  "python3 produktion/erzaehlanteil.py erzeugt sie)")
            fehler.append("1.13-Erzaehlwerk-nicht-messbar")
        else:
            print(f"  1.13 dominantes Buch ist Erzaehlwerk  {'OK' if gk else 'REISST'}  "
                  f"({100*anteil_dom_erz:.1f} % kapitelweise, Grenze {ERZAEHLWERK_MIN*100:.0f} %)")
            if not gk:
                fehler.append("1.13-Erzaehlwerk")
        voll_n = buchlaenge(kap, g["buch"])
        gelesen = g["kapitel"]
        ganz_oder_naht = g["ganzes_buch"] or r["groesster_an_naht"]
        if g["ganzes_buch"]:
            zusatz = ""
        elif r["groesster_an_naht"]:
            zusatz = (f"  (an Erzaehlnaht geteilt: {kapitel_text(gelesen)} = "
                      f"{len(gelesen)} von {voll_n} Kapiteln, Naht eingetragen in "
                      f"{NAEHTE_DATEI})")
        else:
            zusatz = (f"  (gelesen {kapitel_text(gelesen)} = {len(gelesen)} von "
                      f"{voll_n} Kapiteln; ohne Eintrag in {NAEHTE_DATEI}: "
                      f"{', '.join(r['fehlende_naehte'])})")
        print(f"  1.13 ganzes Buch oder Erzaehlnaht     "
              f"{'OK' if ganz_oder_naht else 'REISST'}" + zusatz)
        if not ganz_oder_naht:
            fehler.append("1.13-Vollstaendigkeit")
        # Mindestabstand zum zweitgroessten Buch (config.md, gate_abstand_min).
        # Dieselbe Buch-Aggregation wie oben - nicht noch einmal selbst gerechnet.
        zweiter = r["zweiter"]
        abstand = (g["woerter"] - (zweiter["woerter"] if zweiter else 0)) / r["woerter"]
        abstand_ok = abstand >= ABSTAND_MIN
        print(f"  1.13 Abstand zum zweiten >= {ABSTAND_MIN*100:.0f} Pkt   "
              f"{'OK' if abstand_ok else 'REISST'}  "
              f"({100*abstand:.1f} Punkte"
              + (f", zweiter: {zweiter['spec']} "
                 f"{100*zweiter['woerter']/r['woerter']:.1f} %)" if zweiter
                 else ", kein zweites Buch)"))
        if not abstand_ok:
            fehler.append("1.13-Abstand")
    doppelt_text = "OK" if not r["doppelt"] else f"{r['doppelt']} KAPITEL DOPPELT"
    print(f"  Doppelte Kapitel im Korpus            {doppelt_text}")
    if r["doppelt"]:
        fehler.append("doppelt")

    if a.gegen:
        plan = json.load(open(PLAN, encoding="utf-8"))
        for v in a.gegen:
            fremd = {(k.rsplit(" ", 1)[0], int(k.rsplit(" ", 1)[1])) for k in plan[v]["refs"]}
            ueb = r["kapitel"] & fremd
            print(f"  Ueberschneidung mit {v:19s} "
                  f"{'OK' if not ueb else f'{len(ueb)} KAPITEL DOPPELT VERGEBEN'}")
            if ueb:
                fehler.append(f"gegen {v}")
                for b in sorted({b for b, _ in ueb}):
                    n = sorted(i for x, i in ueb if x == b)
                    print(f"        {b} {n[0]}-{n[-1]}")

    print(f"\n{'BESTANDEN' if not fehler else 'DURCHGEFALLEN: ' + ', '.join(fehler)}")
    return 1 if fehler else 0


if __name__ == "__main__":
    sys.exit(main())
