#!/usr/bin/env python3
"""
titel_pruefung.py - prueft eigene Titel gegen alle drei Vergleichslisten.

Kriterium: kein eigener Titel darf mehr als die erlaubte Quote seiner
inhaltstragenden Woerter mit einem EINZELNEN fremden Titel teilen.

Drei Listen, drei verschiedene Gruende:
  1. produktion/gewinner_titel.json (21)  - die belegten Treffer. Naehe dazu ist
     der dokumentierte Todesfall: Kanal F kopierte A's 233K-Titel und bekam
     18 Aufrufe (video-formel.md Paragraph 1).
  2. produktion/eigene_titel.json          - der eigene Katalog. Zwei eigene
     Videos duerfen einander im Vorschlagsband nicht doppeln.
  3. produktion/kopisten_titel.json (45)   - die Titel der beiden dokumentierten
     Kopisten C und F. Naehe dazu laeuft belegt ins Leere.

"Inhaltstragend" = ohne Funktionswoerter. Pronomen der zweiten Person werden
BEWUSST mitgezaehlt statt weggefiltert: die Du-Ansprache ist in dieser Nische
inhaltlich, nicht grammatisch - "you" wegzulassen wuerde die Aehnlichkeit
kuenstlich kleinrechnen.

Vergleich mit einfachem Stemming (Plural-s, -ing, -ed), damit
"know"/"knows" und "psalm"/"psalms" als Treffer zaehlen. Das ist die
konservative Richtung: lieber ein Titel zu viel beanstandet als zu wenig.

Zwei Grenzen, weil zwei Bestaende:
  Kandidaten (produktion/v06_titel_kandidaten.json): 45 %.
  Bestand (produktion/eigene_titel.json):            50 %, die Grenze, unter der
     diese Titel seinerzeit freigegeben wurden. Wer den Bestand an den 45 % der
     Kandidaten misst, sieht das unten als Warnung - der Rueckgabewert haengt
     nicht daran, denn diese Titel neu zu schneiden ist ein eigener Auftrag.

Der Rueckgabewert richtet sich nach den KANDIDATEN: 0 = alle halten alle drei
Listen.

Aufruf: python3 produktion/titel_pruefung.py
"""
import json, os, re, sys

GRENZE_KANDIDATEN = 0.45
GRENZE_BESTAND = 0.50

GEWINNER = "produktion/gewinner_titel.json"
EIGENE = "produktion/eigene_titel.json"
KOPISTEN = "produktion/kopisten_titel.json"
KANDIDATEN = "produktion/v06_titel_kandidaten.json"

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
    t = t.replace("you're", "you are").replace("don't", "do not")
    # Genitiv-s allgemein abtrennen, damit "Luke's" und "Luke" derselbe
    # Inhaltstraeger sind. Vorher standen hier die beiden Einzelfaelle
    # "god's" und "isaiah's"; die Verallgemeinerung aendert an keinem der
    # dokumentierten Werte etwas (nachgerechnet 2026-08-23 und erneut bei der
    # Zusammenfuehrung 2026-09-02 ueber alle 80 Titel der vier Listen -
    # 21 Gewinner, 8 eigene, 45 Kopisten, 6 Kandidaten: 0 Abweichungen).
    t = re.sub(r"(\w)'s\b", r"\1", t)
    # Satzzeichen abraeumen, sonst bleibt "tired," ein eigener Inhaltstraeger.
    t = re.sub(r"[^a-z' ]", " ", t)
    woerter = [w.strip("'") for w in t.split()]
    return {stamm(w) for w in woerter if w and w not in STOPP and len(w) > 1}


def schlimmster(mein, fremde):
    """Hoechste Einzelaehnlichkeit gegen eine Liste."""
    m = inhalt(mein)
    treffer = (0.0, None, set())
    if not m:
        return treffer
    for f in fremde:
        if f.strip() == mein.strip():
            continue                    # sich selbst nicht vergleichen
        g = inhalt(f)
        anteil = len(m & g) / len(m)
        if anteil > treffer[0]:
            treffer = (anteil, f, m & g)
    return treffer


def listen():
    fehlt = [p for p in (GEWINNER, EIGENE, KOPISTEN) if not os.path.exists(p)]
    if fehlt:
        raise SystemExit("fehlende Vergleichsliste(n): %s" % ", ".join(fehlt))
    gewinner = json.load(open(GEWINNER))
    eigene = json.load(open(EIGENE))
    kopisten = json.load(open(KOPISTEN))["titel"]
    if len(gewinner) != 21:
        print("WARNUNG: gewinner_titel.json hat %d statt 21 Titel" % len(gewinner))
    return [
        ("Gewinner", gewinner),
        ("eigener Katalog", [d["titel"] for d in eigene if d["nr"] in
                             ("V1", "V2", "V3", "V4", "V5")]),
        ("Kopisten C/F", kopisten),
    ]


def bericht(nr, titel, vergleiche, grenze):
    m = inhalt(titel)
    schlecht = max(vergleiche, key=lambda x: x[1][0])
    ok = schlecht[1][0] <= grenze
    print("%-6s %5.1f %%  %s  %s" % (nr, schlecht[1][0] * 100,
                                     "OK    " if ok else "ZU NAH", titel))
    print("        %d Zeichen, %d inhaltstragende Woerter" % (len(titel), len(m)))
    for name, (anteil, quelle, gem) in vergleiche:
        print("        gegen %-16s %5.1f %%  geteilt: %s"
              % (name + ":", anteil * 100, sorted(gem) if gem else "-"))
        if quelle:
            print("        %-22s %s" % ("", quelle))
    print()
    return ok


def main():
    refs = listen()
    print("Vergleichslisten: " + " | ".join("%s (%d)" % (n, len(l)) for n, l in refs))
    print()

    verstoesse = 0
    if os.path.exists(KANDIDATEN):
        kandidaten = json.load(open(KANDIDATEN))
        print("=" * 78)
        print("KANDIDATEN V06 - Grenze %d %%" % (GRENZE_KANDIDATEN * 100))
        print("=" * 78 + "\n")
        for d in kandidaten:
            v = [(n, schlimmster(d["titel"], l)) for n, l in refs]
            if not bericht(d["nr"], d["titel"], v, GRENZE_KANDIDATEN):
                verstoesse += 1
    else:
        print("(%s fehlt - keine Kandidaten geprueft)\n" % KANDIDATEN)
        kandidaten = []

    print("=" * 78)
    print("BESTAND - Grenze %d %% (historisch), zur Information" % (GRENZE_BESTAND * 100))
    print("=" * 78 + "\n")
    warnungen = []
    for d in json.load(open(EIGENE)):
        v = [(n, schlimmster(d["titel"], l)) for n, l in refs]
        hoechste = max(x[1][0] for x in v)
        marke = "OK    " if hoechste <= GRENZE_BESTAND else "ZU NAH"
        print("%-6s %5.1f %%  %s  %s" % (d["nr"], hoechste * 100, marke, d["titel"]))
        if GRENZE_KANDIDATEN < hoechste <= GRENZE_BESTAND:
            warnungen.append((d["nr"], hoechste, d["titel"]))
    if warnungen:
        print("\nHielten die 50 %, wuerden aber die 45 % der Kandidaten reissen:")
        for nr, a, t in warnungen:
            print("  %-4s %.1f %%  %s" % (nr, a * 100, t))
        print("  Nicht geaendert - Neuschnitt des Bestands ist ein eigener Auftrag.")

    print("\nKandidaten geprueft: %d, davon ueber der Grenze: %d" % (len(kandidaten), verstoesse))
    return 1 if verstoesse else 0


if __name__ == "__main__":
    sys.exit(main())
