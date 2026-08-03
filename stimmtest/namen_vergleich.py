#!/usr/bin/env python3
"""
namen_vergleich.py - Aussprache-Pruefung der Eigennamen ueber alle drei Stimmen.

Warum ein Kreuzvergleich: Die Spracherkennung schreibt seltene biblische Namen
oft anders, als sie im Bibeltext stehen ("Nathanael" -> "Nathaniel"), OHNE dass
die Aussprache falsch waere. Ein einzelner Nichttreffer beweist also nichts.
Aussagekraeftig ist erst:
  - Was hat der Erkenner an der Stelle tatsaechlich verstanden?
  - Weicht EINE Stimme von den beiden anderen ab? Dann liegt es an der Stimme.
  - Stimmen alle drei ueberein? Dann ist es eine Eigenheit des Erkenners.
"""
import json, re, difflib

NAMEN = {
    "Bethany":   ["bethany", "bethney", "bethani"],
    "Cephas":    ["cephas", "sephas", "seefas", "kephas"],
    "Nathanael": ["nathanael", "nathaniel", "nathanel"],
    "Isaiah":    ["isaiah", "isaias", "esaias"],
    "Capernaum": ["capernaum", "capernium", "capharnaum", "cafarnaum"],
    "Nicodemus": ["nicodemus", "nikodemus", "nicodimus"],
}
# Ankertexte, an denen der Name im Bibeltext steht - zum Auffinden im ASR
ANKER = {
    "Bethany":   "beyond the Jordan",
    "Cephas":    "which is by interpretation",
    "Nathanael": "Philip found",
    "Isaiah":    "said the prophet",
    "Capernaum": "went down to",
    "Nicodemus": "a ruler of the Jews",
}
STIMMEN = ["milo", "medit", "calm"]


def wortfenster(asr, anker, breite=140):
    i = asr.lower().find(anker.lower())
    if i < 0:
        return ""
    return re.sub(r"\s+", " ", asr[max(0, i - breite):i + breite])


def main():
    asr = {k: open(f"out/_{k}_asr.txt").read() for k in STIMMEN}
    print(f"{'Name':11s} " + " ".join(f"{k:>26s}" for k in STIMMEN) + "   Urteil")
    print("-" * 100)
    zeilen = []
    for name, varianten in NAMEN.items():
        gefunden = {}
        for k in STIMMEN:
            t = asr[k].lower()
            tr = None
            for v in varianten:
                if re.search(r"\b" + v + r"\b", t):
                    tr = v
                    break
            if tr is None:
                # Nichts Bekanntes gefunden: was steht im Kontextfenster?
                f = wortfenster(asr[k], ANKER[name])
                kand = difflib.get_close_matches(name.lower(), f.lower().split(), n=1, cutoff=0.6)
                tr = ("?" + kand[0]) if kand else "NICHT AUFFINDBAR"
            gefunden[k] = tr
        werte = [gefunden[k].lstrip("?") for k in STIMMEN]
        alle_gleich = len(set(werte)) == 1
        plausibel = all(w in varianten for w in werte)
        if plausibel and alle_gleich:
            urteil = "OK (alle gleich, korrektes Lautbild)"
        elif plausibel:
            urteil = "OK (Schreibvarianten des Erkenners)"
        elif alle_gleich:
            urteil = "ERKENNER-EIGENHEIT (alle drei identisch abweichend)"
        else:
            abw = [k for k in STIMMEN if gefunden[k].lstrip("?") not in varianten]
            urteil = f"PRUEFEN: abweichend nur bei {', '.join(abw)}"
        print(f"{name:11s} " + " ".join(f"{gefunden[k]:>26s}" for k in STIMMEN) + f"   {urteil}")
        zeilen.append({"name": name, "erkannt": gefunden, "urteil": urteil})
    json.dump(zeilen, open("namen_urteil.json", "w"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
