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

AUFLOESUNG - beim Vergleich zweier Kandidaten beachten: der Nenner ist die
eigene Wortzahl und liegt bei 3 bis 11 (Median 6). Ein einzelnes Wort wiegt
damit 9 bis 33 Prozentpunkte. Unterschiede unter rund 10 Punkten sind KEIN
Signal, und ein inhaltsleeres Fuellwort verbessert den Wert allein dadurch,
dass es den Nenner verduennt. Deshalb gibt dieses Skript die geteilten
Woerter mit aus - die sind die Aussage, nicht der Prozentwert.
Siehe formel/video-formel.md Paragraph 10, "Aufloesungsgrenze".

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

KOPISTEN = "produktion/kopisten_titel.json"


def _ausgeliefert(nr):
    """V5 -> True, wenn produktion/video-05/ existiert."""
    return os.path.isdir(os.path.join("produktion", f"video-{int(nr[1:]):02d}"))


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

    # Bis 2026-08-31 standen hier ZWEI Kopisten-Titel fest im Code, waehrend
    # produktion/kopisten_titel.json 45 fuehrt. Ein Kandidat konnte damit
    # dicht neben einem Kopisten-Titel liegen, ohne dass etwas gemeldet wurde -
    # und Naehe zu den Kopisten ist die einzige belegte Todesursache im
    # Datensatz (Kanal F: 18 Aufrufe).
    kopisten = json.load(open(KOPISTEN, encoding="utf-8"))["titel"]

    # Veroeffentlicht ist, wofuer ein Paketordner existiert. Frueher stand hier
    # ("V1","V2","V3","V4") fest verdrahtet - V05 war ausgeliefert und wurde
    # trotzdem nicht verglichen. Eine Liste, die von Hand nachgezogen werden
    # muss, wird irgendwann nicht nachgezogen.
    eigene_alle = json.load(open("produktion/eigene_titel.json", encoding="utf-8"))
    eigene = [d["titel"] for d in eigene_alle if _ausgeliefert(d["nr"])]
    geplant = [d["titel"] for d in eigene_alle if not _ausgeliefert(d["nr"])]

    print(f"Grenze {a.grenze*100:.0f} %  |  {len(gewinner)} Gewinner-Titel, "
          f"{len(eigene)} eigene veroeffentlichte, {len(kopisten)} Kopisten-Titel "
          f"({len(gewinner)+len(eigene)+len(kopisten)} Vergleichstitel gesamt)")
    if geplant:
        print(f"           dazu {len(geplant)} geplante eigene Titel - sie werden "
              f"mitgemessen, damit\n           nicht zwei Videos denselben Auftakt "
              f"bekommen.")
    print()

    verstoesse = 0      # Gate 1.2 - MUSS, bestimmt den Rueckgabewert
    soll_maengel = 0    # Gate 1.15 - SOLL, wird getrennt ausgewiesen
    ergebnis = []
    for t in kandidaten:
        (ag, qg, gg), n = naechster(t, gewinner)
        (ae, qe, ge), _ = naechster(t, eigene)
        (ak, qk, gk), _ = naechster(t, kopisten)
        (ap_, qp, gp), _ = naechster(t, geplant) if geplant else ((0.0, "", set()), n)
        # Gate 1.2 hat ZWEI Bedingungen. Die zweite - "nicht naeher an einem
        # Kopisten-Titel als am naechsten Gewinner" - stand hier bisher nur als
        # Warnung. Sie ist die Bedingung aus dem einzigen dokumentierten
        # Todesfall (Kanal F, 18 Aufrufe) und zaehlt ab 2026-08-31 als Verstoss.
        naeher_am_kopisten = ak > ag
        ok = ag <= a.grenze and not naeher_am_kopisten
        verstoesse += 0 if ok else 1
        print(f"{'OK    ' if ok else 'ZU NAH'}  {ag*100:5.1f} % gegen Gewinner   {t}")
        print(f"          {n} inhaltstragende Woerter: {sorted(inhalt(t))}")
        print(f"          geteilt mit Gewinner: {sorted(gg) if gg else '-'}")
        print(f"          naechster Gewinner-Titel: {qg}")
        print(f"          {ae*100:5.1f} % gegen den eigenen Katalog "
              f"(geteilt: {sorted(ge) if ge else '-'})")
        print(f"          naechster eigener Titel:  {qe}")
        warn = ("  <- VERSTOSS: naeher an einem Kopisten als am naechsten Gewinner"
                if naeher_am_kopisten else "")
        print(f"          {ak*100:5.1f} % gegen die Kopisten-Titel (V3){warn}")
        print(f"          naechster Kopisten-Titel: {qk}")
        if geplant:
            print(f"          {ap_*100:5.1f} % gegen die geplanten eigenen Titel "
                  f"(geteilt: {sorted(gp) if gp else '-'})")
            print(f"          naechster geplanter Titel: {qp if gp else '-'}")

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
                         "naeher_am_kopisten_als_am_gewinner": naeher_am_kopisten,
                         "gegen_geplante_pct": round(ap_ * 100, 1) if geplant else None,
                         "naechster_geplanter": qp if geplant else None,
                         "inhaltswoerter": n, "ok": ok,
                         "zeichen": lang, "laenge_ok": laenge_ok,
                         "eigenname_ab_zeichen": pos, "eigenname_ok": name_ok})
    # 1.15 ist SOLL, nicht MUSS - deshalb ein eigenes Zaehlwerk und kein
    # Einfluss auf den Rueckgabewert. Bis 2026-08-31 wurde es ueberhaupt nicht
    # gezaehlt: Laenge und Eigennamenposition standen gedruckt da, ein
    # 90-Zeichen-Titel ohne Eigennamen gab trotzdem 0 zurueck.
    for e in ergebnis:
        if e["laenge_ok"] is False or e["eigenname_ok"] is False:
            soll_maengel += 1
    print(f"Gate 1.2 (MUSS) - Verstoesse: {verstoesse}   "
          f"[Grenze {a.grenze*100:.0f} % oder naeher am Kopisten als am Gewinner]")
    print(f"Gate 1.15 (SOLL) - Maengel:   {soll_maengel}   "
          f"[unter {a.max_zeichen} Zeichen, Eigenname vor Zeichen {a.name_vor}]")
    if soll_maengel:
        print("  1.15 ist eine gesetzte Grenze, kein Messwert - sie geht NICHT in "
              "den\n  Rueckgabewert ein. Ein Verstoss gehoert gemeldet und "
              "begruendet, nicht\n  stillschweigend hingenommen (siehe V05, 73 statt 70 Zeichen).")
    print(json.dumps(ergebnis, ensure_ascii=False))
    return 1 if verstoesse else 0


if __name__ == "__main__":
    sys.exit(main())
