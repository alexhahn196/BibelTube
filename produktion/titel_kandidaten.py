#!/usr/bin/env python3
"""
titel_kandidaten.py - prueft Titelkandidaten, bevor sie in eigene_titel.json
wandern.

Verwendet dieselbe Messung wie produktion/titel_pruefung.py (Gate 1, Pruefung
1.2) - importiert sie sogar, damit die Zahlen deckungsgleich sind. Zwei
Unterschiede:

  1. Es wird gegen DREI Mengen geprueft: die 21 Gewinner-Titel (Regel V3,
     "keinen fremden Titel kopieren") UND die eigenen, bereits
     veroeffentlichten Titel. Die zweite Menge ist keine Verbotsregel -
     ein bewaehrter Anker DARF wiederholt werden (Formel Paragraph 1, die
     Wiederholung war B's Durchbruch) - aber man sollte wissen, wie nah man
     am eigenen Katalog liegt.
  2. Die Grenze ist als Parameter frei setzbar. Gate 1 verlangt < 50 %;
     fuer V05 wurde vom Kanalinhaber < 45 % vorgegeben.

Aufruf:
    python3 produktion/titel_kandidaten.py --grenze 0.45 "Titel A" "Titel B"
    python3 produktion/titel_kandidaten.py --datei kandidaten.json
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from titel_pruefung import inhalt  # noqa: E402


def naechster(mein, menge):
    m = inhalt(mein)
    best = (0.0, None, set())
    for f in menge:
        g = inhalt(f)
        if not m:
            continue
        a = len(m & g) / len(m)
        if a > best[0]:
            best = (a, f, m & g)
    return best, len(m)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("titel", nargs="*")
    ap.add_argument("--datei", help="JSON-Liste von Titeln")
    ap.add_argument("--grenze", type=float, default=0.45)
    ap.add_argument("--eigenname", help="Buchname fuer Pruefung 1.15, z.B. "
                                        "'Gospel of Luke'")
    ap.add_argument("--max-zeichen", type=int, default=70,
                    help="Gate 1.15, gesetzte Grenze (SOLL)")
    ap.add_argument("--name-vor", type=int, default=60,
                    help="Gate 1.15: Eigenname beginnt vor diesem Zeichen")
    a = ap.parse_args()

    kandidaten = list(a.titel)
    if a.datei:
        kandidaten += json.load(open(a.datei, encoding="utf-8"))
    if not kandidaten:
        ap.error("keine Titel angegeben")

    gewinner = json.load(open("produktion/gewinner_titel.json", encoding="utf-8"))
    # Woertlich aus regeln/erfolgsregeln.md V3 bzw. formel/video-formel.md Paragraph 1.
    kopisten = [
        # Kanal C, Mashup aus A-Titeln, 17 Views
        "You're tired, I know... Rest to the Gospel of John",
        # Kanal F, woertliche Kopie von A's 233K-Titel inklusive Tippfehler, 18 Views
        "I Know You're Tried... Jesus Watches Over you Tonight",
    ]
    eigene_alle = json.load(open("produktion/eigene_titel.json", encoding="utf-8"))
    # veroeffentlicht sind V1-V4
    eigene = [d["titel"] for d in eigene_alle if d["nr"] in ("V1", "V2", "V3", "V4")]

    print(f"Grenze {a.grenze*100:.0f} %  |  {len(gewinner)} Gewinner-Titel, "
          f"{len(eigene)} eigene veroeffentlichte, {len(kopisten)} Kopisten-Titel "
          f"({len(gewinner)+len(eigene)+len(kopisten)} Vergleichstitel gesamt)\n")

    verstoesse = 0
    ergebnis = []
    for t in kandidaten:
        (ag, qg, gg), n = naechster(t, gewinner)
        (ae, qe, ge), _ = naechster(t, eigene)
        (ak, qk, gk), _ = naechster(t, kopisten)
        ok = ag <= a.grenze
        verstoesse += 0 if ok else 1
        print(f"{'OK    ' if ok else 'ZU NAH'}  {ag*100:5.1f} % gegen Gewinner   {t}")
        print(f"          {n} inhaltstragende Woerter: {sorted(inhalt(t))}")
        print(f"          geteilt mit Gewinner: {sorted(gg) if gg else '-'}")
        print(f"          naechster Gewinner-Titel: {qg}")
        print(f"          {ae*100:5.1f} % gegen den eigenen Katalog "
              f"(geteilt: {sorted(ge) if ge else '-'})")
        print(f"          naechster eigener Titel:  {qe}")
        warn = "  <- naeher an einem Kopisten als an jedem Gewinner" if ak > ag else ""
        print(f"          {ak*100:5.1f} % gegen die Kopisten-Titel (V3){warn}")
        print(f"          naechster Kopisten-Titel: {qk}")

        # Pruefung 1.15 - gesetzte Grenze, kein Messwert. Belegt ist nur der
        # Anlass: Gate 2 hat 68 % der Aufrufe am Handy gemessen, und in der
        # Vorschlagsleiste bricht der Titel dort ab. WO genau, ist nicht
        # gemessen und haengt an Geraet und Schriftgroesse - deshalb SOLL.
        lang = len(t)
        laenge_ok = lang < a.max_zeichen
        print(f"          {lang:5d} Zeichen             "
              f"{'OK' if laenge_ok else 'ZU LANG'} (SOLL < {a.max_zeichen}, gesetzt)")
        pos, name_ok = None, None
        if a.eigenname:
            i = t.find(a.eigenname)
            if i < 0:
                name_ok = False
                print(f"          Eigenname fehlt im Titel        "
                      f"REISST 1.14: {a.eigenname!r}")
            else:
                pos = i + 1
                name_ok = pos < a.name_vor
                print(f"          Eigenname ab Zeichen {pos:<3d}        "
                      f"{'OK' if name_ok else 'ZU SPAET'} "
                      f"(SOLL < {a.name_vor}, gesetzt)")
        print()
        ergebnis.append({"titel": t, "gegen_gewinner_pct": round(ag * 100, 1),
                         "naechster_gewinner": qg,
                         "gegen_eigene_pct": round(ae * 100, 1),
                         "naechster_eigener": qe,
                         "gegen_kopisten_pct": round(ak * 100, 1),
                         "naechster_kopist": qk,
                         "inhaltswoerter": n, "ok": ok,
                         "zeichen": lang, "laenge_ok": laenge_ok,
                         "eigenname_ab_zeichen": pos, "eigenname_ok": name_ok})
    print(f"Verstoesse gegen die {a.grenze*100:.0f}-%-Grenze: {verstoesse}")
    print(json.dumps(ergebnis, ensure_ascii=False))
    return 1 if verstoesse else 0


if __name__ == "__main__":
    sys.exit(main())
