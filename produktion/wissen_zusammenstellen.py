#!/usr/bin/env python3
"""
wissen_zusammenstellen.py - baut bibeltube-wissen.md aus den vier
Arbeitsdokumenten neu.

Warum es dieses Skript gibt: bibeltube-wissen.md wurde am 04.08.2026 von Hand
zusammengestellt und enthielt schon zwei Tage spaeter (Kalibrierung vom 06.08.)
nicht mehr den Stand der Originale. Ein Einstiegsdokument, das veraltete Regeln
ausliefert, ist schlimmer als keines. Seit 2026-08-23 wird es erzeugt, nicht
gepflegt.

Einzige Abweichung vom Original: relative Links werden auf die Repo-Wurzel
umgeschrieben, damit sie aus der zusammengesetzten Datei heraus funktionieren.

Aufruf: python3 produktion/wissen_zusammenstellen.py
"""
import io
import os
import re
import subprocess
import sys

ZIEL = "bibeltube-wissen.md"
DOKUMENTE = [
    "regeln/erfolgsregeln.md",
    "formel/video-formel.md",
    "formel/thumbnail-checkliste.md",
    "produktion/videos-01-08.md",
]


def links_umschreiben(text, quelle):
    basis = os.path.dirname(quelle)

    def ersetze(m):
        label, ziel = m.group(1), m.group(2)
        if ziel.startswith(("http://", "https://", "#", "mailto:")):
            return m.group(0)
        pfad, _, anker = ziel.partition("#")
        if not pfad:
            return m.group(0)
        aufgeloest = os.path.normpath(os.path.join(basis, pfad))
        if not os.path.exists(aufgeloest):
            return m.group(0)
        return f"[{label}]({aufgeloest}{'#' + anker if anker else ''})"

    return re.sub(r"\[([^\]]*)\]\(([^)]+)\)", ersetze, text)


def kopf(datum):
    liste = "\n".join(f"{i}. `{d}`" for i, d in enumerate(DOKUMENTE, 1))
    return f"""# BibelTube — Wissensstand

Die vier Arbeitsdokumente, ungekürzt aneinandergehängt.
**Erzeugt am {datum} von `produktion/wissen_zusammenstellen.py`** — nicht von Hand
pflegen, sondern neu bauen.

{liste}

> **Momentaufnahme, keine Quelle.** Verbindlich sind immer die vier Originaldateien.
> Wer hier liest und etwas ändern will, ändert das Original und lässt diese Datei
> danach neu erzeugen.
>
> Der Text ist wörtlich übernommen. Einzige Abweichung: **relative Links sind auf die
> Repo-Wurzel umgeschrieben**, damit sie aus dieser Datei heraus funktionieren; in den
> Originalen stehen sie relativ zum jeweiligen Ordner.
"""


def main():
    datum = subprocess.run(["date", "+%d.%m.%Y"], capture_output=True,
                           text=True).stdout.strip()
    teile = [kopf(datum)]
    for d in DOKUMENTE:
        teile.append(f"\n---\n\n# {d}\n\n---\n\n")
        teile.append(links_umschreiben(io.open(d, encoding="utf-8").read(), d))
    text = "".join(teile)
    io.open(ZIEL, "w", encoding="utf-8").write(text)

    defekt = [m.group(1) for m in re.finditer(r"\]\(([^)]+)\)", text)
              if not m.group(1).startswith(("http", "#", "mailto:"))
              and not os.path.exists(m.group(1).split("#")[0])]
    print(f"{ZIEL}: {len(text):,} Zeichen, {text.count(chr(10))+1:,} Zeilen, "
          f"{len(DOKUMENTE)} Dokumente")
    if defekt:
        print("  WARNUNG, defekte relative Links:", sorted(set(defekt)))
        return 1
    print("  alle relativen Links loesen auf")
    return 0


if __name__ == "__main__":
    sys.exit(main())
