#!/usr/bin/env python3
"""Rechnet durch, welche Korpora fuer V07 und V08 aus dem freien Bestand
moeglich sind - mit den am 2026-09-02 geaenderten Schwellen.

Das ist eine MESSUNG, kein Vorschlag. Es steht hier keine Empfehlung, keine
Reihenfolge und keine Bewertung der Nachttauglichkeit; das Skript sagt nur, was
die drei Gates durchlassen und was nicht.

Erzeugt produktion/korpus/v07_v08_moeglichkeiten.json.

Alle Schwellen kommen aus produktion/config.md, gelesen ueber
produktion/erzaehlanteil.py - hier steht keine Zahl doppelt. Die Wort- und
Erzaehlwerte kommen aus produktion/korpus/erzaehlanteil.json, erzeugt vom selben
Skript, also mit derselben Zaehlmethode wie V01-V06.

Aufruf:  python3 produktion/v07_v08_moeglichkeiten.py
"""
import importlib.util
import itertools
import json
import os
import re
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("erzaehlanteil", os.path.join(HIER, "erzaehlanteil.py"))
ea = importlib.util.module_from_spec(_spec)
sys.modules["erzaehlanteil"] = ea
_spec.loader.exec_module(ea)

PLAN = "produktion/korpus/plan.json"
AUS = "produktion/korpus/v07_v08_moeglichkeiten.json"

#: Bloecke, aus denen ein Korpus gebaut werden darf. Ganze Buecher zuerst;
#: Teilungen nur an einer Naht, die begruendet ist. "urteil" markiert, dass die
#: Naht Ermessen ist und keine Messung - es gibt im Repo keine Nahtliste.
BLOECKE = [
    ("genesis",     1, 50, "ganzes Buch", None),
    ("genesis",     1, 11, "Teilung",
     "Ende der Urgeschichte. Gen 11 schliesst mit Terachs Tod in Haran, Gen 12 setzt mit "
     "Abrams Ruf neu an - die klassischste Naht des Buches. URTEIL, keine Messung."),
    ("genesis",    12, 50, "Teilung",
     "Gegenstueck zu Gen 1-11: die Vaetergeschichte am Stueck, von Abrams Ruf bis zu "
     "Josephs Tod. URTEIL, keine Messung."),
    ("genesis",     1, 36, "Teilung",
     "Vor der Josephsnovelle. Gen 36 ist die Toledot Esaus und damit ein Listenabschluss, "
     "Gen 37 beginnt 'Jakob wohnte...' und laeuft ohne Unterbrechung bis Gen 50. URTEIL."),
    ("genesis",    37, 50, "Teilung",
     "Die Josephsnovelle am Stueck - der geschlossenste Erzaehlbogen des Buches. URTEIL."),
    ("genesis",    12, 36, "Teilung",
     "Vaetergeschichte ohne Josephsnovelle: Abraham, Isaak, Jakob. URTEIL."),
    ("genesis",     1, 42, "Teilung",
     "Die Naht der Planfassung V08. Sie liegt mitten in der Hungersnot-Sequenz - die "
     "Brueder sind einmal in Aegypten gewesen und muessen wieder hin. Als Naht schwach; "
     "hier nur mitgerechnet, weil sie im Bestand steht. URTEIL."),
    ("genesis",    43, 50, "Teilung",
     "Rest der Planfassung V08 (zweite Reise bis Josephs Tod). URTEIL."),
    ("exodus",      1, 40, "ganzes Buch", None),
    ("exodus",      1, 18, "Teilung",
     "Vor dem Sinai. Ex 18 endet mit Jitros Rat und der Einsetzung der Richter, Ex 19 "
     "beginnt die Gesetzgebung am Berg - die Naht zwischen Erzaehlung und Gesetzbuch. URTEIL."),
    ("joshua",      1, 24, "ganzes Buch", None),
    ("joshua",      1, 12, "Teilung",
     "Ende des Eroberungsberichts. Jos 12 ist die Koenigsliste als Abschluss, ab Jos 13 "
     "folgen die Landverteilungslisten. URTEIL."),
    ("judges",      1, 21, "ganzes Buch", None),
    ("judges",      1, 16, "Teilung",
     "Ende der Richtergestalten mit Simsons Tod; Ri 17-21 ist der Anhang. URTEIL."),
    ("judges",     17, 21, "Teilung",
     "Der Anhang des Richterbuchs (Micha, Dan, das Weib von Gibea, der Krieg gegen "
     "Benjamin) - eigener Erzaehlbogen. URTEIL."),
    ("1 samuel",    1, 31, "ganzes Buch", None),
    ("2 samuel",    1, 24, "ganzes Buch", None),
    ("1 kings",     1, 22, "ganzes Buch", None),
    ("1 kings",    12, 22, "Teilung",
     "Ab der Reichsteilung; 1 Koen 1-11 ist zur Haelfte Tempelbau und Weihgebet. URTEIL."),
    ("2 kings",     1, 25, "ganzes Buch", None),
    ("2 kings",     1, 17, "Teilung",
     "Bis zum Fall Samarias. URTEIL."),
    ("2 kings",    18, 25, "Teilung",
     "Von Hiskija bis zum Exil. URTEIL."),
    ("esther",      1, 10, "ganzes Buch", None),
    ("ruth",        1,  4, "ganzes Buch", None),
    ("jonah",       1,  4, "ganzes Buch", None),
    ("daniel",      4, 12, "Rest", None),
    ("isaiah",      1, 66, "ganzes Buch", None),
    ("mark",        1, 16, "ganzes Buch", None),
    ("acts",        1, 28, "ganzes Buch", None),
    ("acts",        1, 12, "Teilung",
     "Bis zum Ende der Petrus-Erzaehlungen; ab Apg 13 die Paulusreisen. URTEIL."),
    ("acts",       13, 28, "Teilung",
     "Die Paulusreisen am Stueck. URTEIL."),
    ("romans",      1, 16, "ganzes Buch", None),
    ("revelation",  1, 22, "ganzes Buch", None),
]

MAX_TEILE = 3


def frei_ermitteln():
    """Was V01-V06 verbraucht haben, ist weg. Rest ist frei."""
    plan = json.load(open(PLAN))
    verbraucht = set()
    for v in ("V1", "V2", "V3", "V4", "V5", "V6"):
        verbraucht |= set(plan[v]["refs"])
    return verbraucht, plan


def block_refs(b):
    buch, von, bis = b[0], b[1], b[2]
    return ["%s %d" % (buch, i) for i in range(von, bis + 1)]


def korpus_rechnen(tabelle, bloecke):
    teile = []
    for b in bloecke:
        refs = block_refs(b)
        teile.append({"buch": b[0], "von": b[1], "bis": b[2],
                      "kapitel": b[2] - b[1] + 1,
                      "woerter": sum(tabelle[r]["woerter"] for r in refs),
                      "erzaehlend_woerter": sum(tabelle[r]["erzaehlend_woerter"] for r in refs)})
    woerter = sum(t["woerter"] for t in teile)
    erz = sum(t["erzaehlend_woerter"] for t in teile)
    pro_buch = {}
    for t in teile:
        pro_buch[t["buch"]] = pro_buch.get(t["buch"], 0) + t["woerter"]
    dominant, dom_w = max(pro_buch.items(), key=lambda x: x[1])
    vw = ea.vollwerk_pruefen(tabelle, dominant, teile)
    grenzen = ea.band(vw["erfuellt"])
    d = {
        "teile": teile,
        "woerter": woerter,
        "erzaehlend_woerter": erz,
        "erzaehlanteil": round(erz / woerter, 4),
        "laufzeit_h": round(woerter / ea.WPM / 60, 3),
        "dominantes_buch": dominant,
        "dominanz": round(dom_w / woerter, 4),
        "vollwerk": vw,
        "zielband_woerter": list(grenzen),
        "zielband_h": [round(grenzen[0] / ea.WPM / 60, 2), round(grenzen[1] / ea.WPM / 60, 2)],
    }
    d["pruefungen"] = {
        "band": grenzen[0] <= woerter <= grenzen[1],
        "erzaehlanteil": d["erzaehlanteil"] >= ea.GATE_ERZAEHLEND,
        "dominanz": d["dominanz"] >= ea.GATE_DOMINANZ,
    }
    d["bestanden"] = all(d["pruefungen"].values())
    return d


def name(bloecke):
    def eins(b):
        buch, von, bis = b[0], b[1], b[2]
        ganz = ea.buchlaenge(buch)
        return buch if (von, bis) == (1, ganz) else "%s %d-%d" % (buch, von, bis)
    return " + ".join(eins(b) for b in bloecke)


def ueberlappt(bloecke):
    gesehen = set()
    for b in bloecke:
        r = set(block_refs(b))
        if r & gesehen:
            return True
        gesehen |= r
    return False


def main():
    tabelle, verworfen = ea.einstufung_rechnen()
    if verworfen:
        print("Verworfene Teilungen:", verworfen)
    verbraucht, plan = frei_ermitteln()

    bloecke = [b for b in BLOECKE if not (set(block_refs(b)) & verbraucht)]
    raus = [name([b]) for b in BLOECKE if b not in bloecke]
    if raus:
        print("Nicht frei (in V01-V06 verbraucht): %s\n" % ", ".join(raus))

    treffer = []
    for n in range(1, MAX_TEILE + 1):
        for komb in itertools.combinations(bloecke, n):
            if ueberlappt(komb):
                continue
            d = korpus_rechnen(tabelle, komb)
            if not d["bestanden"]:
                continue
            d["name"] = name(komb)
            d["bloecke"] = [{"buch": b[0], "von": b[1], "bis": b[2], "art": b[3],
                             "naht": b[4]} for b in komb]
            d["refs"] = sorted({r for b in komb for r in block_refs(b)})
            treffer.append(d)

    # Nur die knappste Bauform je Materialmenge behalten: identische Kapitelmenge
    # aus mehreren Bloecken zusammengesetzt ist derselbe Korpus.
    einmalig = {}
    for d in treffer:
        schluessel = tuple(d["refs"])
        if schluessel not in einmalig or len(d["bloecke"]) < len(einmalig[schluessel]["bloecke"]):
            einmalig[schluessel] = d
    treffer = sorted(einmalig.values(), key=lambda d: (-d["erzaehlanteil"], d["woerter"]))

    # Planfassungen zur Gegenprobe
    planfassungen = {}
    for v in ("V7", "V8"):
        refs = plan[v]["refs"]
        gruppen = {}
        for r in refs:
            m = re.match(r"^(.*?)\s+(\d+)$", r)
            gruppen.setdefault(m.group(1), []).append(int(m.group(2)))
        komb = [(b, min(ks), max(ks), "Planfassung", None) for b, ks in gruppen.items()]
        d = korpus_rechnen(tabelle, komb)
        d["name"] = plan[v]["name"]
        planfassungen[v] = d

    # Paare: zwei Korpora, die einander nicht ins Material greifen
    paare = []
    for a, b in itertools.combinations(treffer, 2):
        if set(a["refs"]) & set(b["refs"]):
            continue
        paare.append({"v07": a["name"], "v08": b["name"],
                      "woerter": [a["woerter"], b["woerter"]],
                      "erzaehlanteil": [a["erzaehlanteil"], b["erzaehlanteil"]],
                      "dominanz": [a["dominanz"], b["dominanz"]]})

    json.dump({
        "stand": "2026-09-02",
        "was_das_ist": ("Messung, kein Vorschlag. Enthaelt jede Blockkombination aus dem "
                        "freien Bestand, die alle drei Gates haelt - ohne Bewertung."),
        "schwellen": {
            "quelle": "produktion/config.md",
            "wpm": ea.WPM,
            "erzaehlanteil_min": ea.GATE_ERZAEHLEND,
            "dominanz_min": ea.GATE_DOMINANZ,
            "zielband_woerter": list(ea.BAND),
            "zielband_woerter_vollwerk": list(ea.BAND_VOLLWERK),
            "vollwerk_bedingung": ("dominantes Buch in voller Laenge im Korpus UND selbst "
                                   ">= erzaehlanteil_min, kapitelweise gemessen"),
        },
        "freier_bestand": sorted({b[0] for b in bloecke}),
        "planfassungen": planfassungen,
        "moeglich": treffer,
        "paare_v07_v08": paare,
    }, open(AUS, "w"), ensure_ascii=False, indent=1)

    print("Schwellen aus produktion/config.md: Erzaehlanteil >= %g %%, Dominanz >= %g %%"
          % (ea.GATE_ERZAEHLEND * 100, ea.GATE_DOMINANZ * 100))
    print("Zielband %d-%d W (%.2f-%.2f h); dominantes Buch ganz und Erzaehlwerk: %d-%d W (%.2f-%.2f h)\n"
          % (ea.BAND[0], ea.BAND[1], ea.ZIEL_VON_H, ea.ZIEL_BIS_H,
             ea.BAND_VOLLWERK[0], ea.BAND_VOLLWERK[1], ea.ZIEL_VON_H_VOLLWERK, ea.ZIEL_BIS_H))

    kopf = "%-46s %8s %7s %7s %-12s %5s" % ("Korpus", "Woerter", "Erzaehl", "Domin.", "dominant", "Lauf")
    print("PLANFASSUNGEN AUS plan.json")
    print(kopf)
    for v, d in planfassungen.items():
        print("%-46s %8s %6.1f%% %6.1f%% %-12s %4.2fh  %s"
              % (v + " " + d["name"], "{:,}".format(d["woerter"]), d["erzaehlanteil"] * 100,
                 d["dominanz"] * 100, d["dominantes_buch"], d["laufzeit_h"],
                 "BESTANDEN" if d["bestanden"] else "gerissen: " + ", ".join(
                     k for k, ok in d["pruefungen"].items() if not ok)))

    print("\nMOEGLICH (%d Korpora)" % len(treffer))
    print(kopf + "  Band")
    for d in treffer:
        print("%-46s %8s %6.1f%% %6.1f%% %-12s %4.2fh  %s"
              % (d["name"], "{:,}".format(d["woerter"]), d["erzaehlanteil"] * 100,
                 d["dominanz"] * 100, d["dominantes_buch"], d["laufzeit_h"],
                 "3,0-3,8" if d["vollwerk"]["erfuellt"] else "3,4-3,8"))
    print("\nPaare V07/V08 ohne gemeinsames Material: %d" % len(paare))
    print("geschrieben: %s" % AUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
