#!/usr/bin/env python3
"""
titel_pruefung.py - prueft die eigenen Titel gegen alle Gewinner-Titel.

Kriterium: kein eigener Titel darf mehr als die Haelfte seiner inhaltstragenden
Woerter mit einem einzelnen Konkurrenztitel teilen.

"Inhaltstragend" = ohne Funktionswoerter. Pronomen der zweiten Person werden
BEWUSST mitgezaehlt statt weggefiltert: die Du-Ansprache ist in dieser Nische
inhaltlich, nicht grammatisch - "you" wegzulassen wuerde die Aehnlichkeit
kuenstlich kleinrechnen.

Vergleich mit einfachem Stemming (Plural-s, -ing, -ed), damit
"know"/"knows" und "psalm"/"psalms" als Treffer zaehlen. Das ist die
konservative Richtung: lieber ein Titel zu viel beanstandet als zu wenig.

Aufruf: python3 produktion/titel_pruefung.py
"""
import json, re, sys

STOPP = {
    "a", "an", "the", "to", "of", "in", "on", "and", "or", "but", "for", "with",
    "is", "are", "was", "be", "am", "at", "by", "from", "as", "so", "that",
    "this", "these", "those", "it", "its", "will", "shall", "can", "do", "does",
    "did", "have", "has", "had", "there", "here", "then", "than", "into", "over",
    "under", "up", "down", "out", "all", "any", "some", "more", "just", "very",
}


def stamm(w):
    for endung in ("ing", "ed", "es", "s"):
        if len(w) > 4 and w.endswith(endung):
            return w[: -len(endung)]
    return w


def inhalt(titel):
    t = titel.lower().replace("’", "'")
    t = re.sub(r"[^a-z' ]", " ", t)
    t = t.replace("you're", "you are").replace("don't", "do not")
    # Genitiv-s allgemein abtrennen, damit "Luke's" und "Luke" derselbe
    # Inhaltstraeger sind. Vorher standen hier nur die beiden Einzelfaelle
    # "god's" und "isaiah's"; die Verallgemeinerung aendert an keinem der
    # acht dokumentierten Werte etwas (nachgerechnet 2026-08-23).
    t = re.sub(r"(\w)'s\b", r"\1", t)
    woerter = [w.strip("'") for w in t.split()]
    return {stamm(w) for w in woerter if w and w not in STOPP and len(w) > 1}


def pruefe(eigene, fremde, grenze=0.5):
    zeilen = []
    verstoesse = 0
    for nr, mein in eigene:
        m = inhalt(mein)
        schlimmster = (0.0, None, set())
        for f in fremde:
            g = inhalt(f)
            if not m:
                continue
            anteil = len(m & g) / len(m)
            if anteil > schlimmster[0]:
                schlimmster = (anteil, f, m & g)
        anteil, quelle, gemeinsam = schlimmster
        ok = anteil <= grenze
        verstoesse += 0 if ok else 1
        zeilen.append((nr, mein, anteil, quelle, gemeinsam, ok, len(m)))
    return zeilen, verstoesse


def main():
    eigene = json.load(open("produktion/eigene_titel.json"))
    fremde = json.load(open("produktion/gewinner_titel.json"))
    zeilen, v = pruefe([(d["nr"], d["titel"]) for d in eigene], fremde)
    print(f"Vergleich gegen {len(fremde)} Gewinner-Titel, Grenze 50 %\n")
    for nr, mein, anteil, quelle, gem, ok, n in zeilen:
        print(f"{nr}  {anteil*100:5.1f} %  {'OK  ' if ok else 'ZU NAH'}  {mein}")
        print(f"        {n} inhaltstragende Woerter, davon geteilt: {sorted(gem) if gem else '-'}")
        print(f"        naechster Konkurrenztitel: {quelle}\n")
    print(f"Verstoesse: {v}")
    return 1 if v else 0


if __name__ == "__main__":
    sys.exit(main())
