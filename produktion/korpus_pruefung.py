#!/usr/bin/env python3
"""
korpus_pruefung.py - prueft einen Textkorpus gegen M8, Formel Paragraph 2 und
die Doppelvergabe.

Gate 1 fuehrt seit 2026-08-23 zwei Pruefungen, die vorher nicht existierten:
  1.13 Korpusart  - Hauptkorpus muss durchlaufender Erzaehlstoff sein
  1.1  Korpuslaenge - 29.000-31.500 Woerter = 3,4-3,8 h bei 140 WPM
Beide standen dort als "von Hand". Dieses Skript macht sie nachrechenbar.

GATTUNGSTABELLE: Die Zuordnung Erzaehlung/Nicht-Erzaehlung steht unten im
Klartext, kapitelweise, und ist das einzige Urteil in diesem Skript - alles
andere ist Arithmetik auf produktion/korpus/kapitel.json. Sie folgt der
Standardgliederung und ist bewusst konservativ: im Zweifel NICHT Erzaehlung.
Wer sie fuer falsch haelt, aendert sie hier und sieht sofort, was das an den
Prozentsaetzen bewegt.

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
BAND = (29000, 31500)
WPM = 140

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


def bewerte(specs, kap):
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
    w = sum(t["woerter"] for t in teile)
    erz = sum(t["erzaehlung"] for t in teile)
    doppelt = len(kapitel) - len(set(kapitel))
    groesster = max(teile, key=lambda t: t["woerter"]) if teile else None
    return {"teile": teile, "kapitel": set(kapitel), "woerter": w, "erzaehlung": erz,
            "erz_pct": 100 * erz / w if w else 0, "stunden": w / WPM / 60,
            "doppelt": doppelt, "groesster": groesster,
            "groesster_ist_erzaehlung": bool(groesster and
                                             groesster["erzaehlung"] / groesster["woerter"] >= 0.8)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("bausteine", nargs="*")
    ap.add_argument("--plan", help="Video aus korpus/plan.json statt Bausteinen")
    ap.add_argument("--gegen", action="append", default=[],
                    help="Video aus plan.json, gegen das auf Doppelvergabe geprueft wird")
    a = ap.parse_args()
    kap = json.load(open(KAPITEL, encoding="utf-8"))

    if a.plan:
        plan = json.load(open(PLAN, encoding="utf-8"))
        refs = plan[a.plan]["refs"]
        kapitel = [(k.rsplit(" ", 1)[0], int(k.rsplit(" ", 1)[1])) for k in refs]
        w = sum(kap[k]["w"] for k in refs)
        erz = sum(kap[f"{b} {i}"]["w"] for b, i in kapitel if ERZAEHLUNG.get(b, lambda _: False)(i))
        r = {"teile": [], "kapitel": set(kapitel), "woerter": w, "erzaehlung": erz,
             "erz_pct": 100 * erz / w, "stunden": w / WPM / 60, "doppelt": 0,
             "groesster": None, "groesster_ist_erzaehlung": True}
        print(f"Plan {a.plan}: {plan[a.plan]['name']}")
    else:
        if not a.bausteine:
            ap.error("Bausteine oder --plan angeben")
        r = bewerte(a.bausteine, kap)

    print(f"\n{'Baustein':34s} {'Woerter':>8s} {'Erzaehlung':>11s} {'ganzes Buch':>12s}")
    for t in r["teile"]:
        q = 100 * t["erzaehlung"] / t["woerter"] if t["woerter"] else 0
        print(f"{t['spec']:34s} {t['woerter']:8,d} {q:10.1f} % {'ja' if t['ganzes_buch'] else 'NEIN':>12s}")

    print(f"\n{'SUMME':34s} {r['woerter']:8,d} {r['erz_pct']:10.1f} %")
    print(f"{'Laufzeit bei ' + str(WPM) + ' WPM':34s} {r['stunden']:8.2f} h")

    fehler = []
    print("\nPruefungen:")
    band = BAND[0] <= r["woerter"] <= BAND[1]
    print(f"  1.1  Korpuslaenge {BAND[0]:,}-{BAND[1]:,} W   "
          f"{'OK' if band else 'REISST — ' + ('zu kurz' if r['woerter'] < BAND[0] else 'zu lang')}")
    if not band:
        fehler.append("1.1")
    erz_ok = r["erz_pct"] >= 80
    print(f"  1.13 Erzaehlanteil >= 80 %            "
          f"{'OK' if erz_ok else 'REISST'}  ({r['erz_pct']:.1f} %)")
    if not erz_ok:
        fehler.append("1.13")
    if r["groesster"]:
        g = r["groesster"]
        gk = r["groesster_ist_erzaehlung"]
        print(f"  1.13 groesster Block ist Erzaehlung   {'OK' if gk else 'REISST'}  "
              f"({g['spec']}, {g['woerter']:,} W = {100*g['woerter']/r['woerter']:.1f} % des Korpus)")
        if not gk:
            fehler.append("1.13-Hauptkorpus")
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
