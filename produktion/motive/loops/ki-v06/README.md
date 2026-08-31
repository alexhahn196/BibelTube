# KI-Clips Video 06

Vier Bild-zu-Video-Clips aus `produktion/motive/motiv-V6.png`, erzeugt am
2026-08-31 mit `flux_3_video` (1080p, 12 s), **start_image = end_image = das
Standbild**, `generate_audio: false`. Bewegungsvorgabe je Clip verschieden
(Feuerflackern · Rauch und Sterne · Grasbewegung und Funke · hohe Wolken),
Kamera in allen vier ausdrücklich unbewegt.

## Zwei Nachbearbeitungen, beide gemessen

**1. Zuschnitt 1088 → 1080.** Der Generator lieferte 1920×1088 (kein
Letterbox-Balken, echter Inhalt). Mittig beschnitten, je vier Zeilen oben und
unten, ohne Skalierung.

**2. Schleife geschlossen.** Trotz identischem Start- und Endbild kam das
Modell nicht exakt auf den Anfangsframe zurück — `ki_clip_pruefung.py` maß
einen Nahtsprung von 3,37–5,18 (Median 4,06) bei einem normalen Frameschritt
von nur 0,07–0,12, also Faktor **40,8**. Jeder Clip wurde deshalb in sich
geschlossen: die letzte Sekunde wird über die erste geblendet
(`xfade`, 1 s), Länge dadurch 12,04 s → 11,0 s.

Ergebnis danach, mit demselben Werkzeug gemessen:

| | Nahtsprung Median | Naht / normaler Schritt |
|---|---:|---:|
| vorher | 4,06 | 40,8 |
| **nachher** | **2,49** | **9,5** |
| zum Vergleich V02 | 2,5 | 1,8 |
| zum Vergleich V03 | 2,7 | 2,7 |
| zum Vergleich V04 | 3,0 | 5,4 |

Der **absolute** Sprung liegt damit unter allen drei ausgelieferten Videos.
Der Faktor bleibt höher, weil diese Clips deutlich statischer sind
(Frameschritt 0,21–0,30 gegen 0,37–0,54 bei V04) — bei ruhigerem Bild fällt
derselbe Sprung relativ stärker auf. Kameradrift nach der Bearbeitung
0,007–0,021 px, also praktisch null.

Die Rohclips vor der Bearbeitung sind bewusst **nicht** im Repository (4×7 MB
ohne eigenen Nutzen); die Messwerte oben und `qa-ki-clips.json` halten fest,
was die Bearbeitung bewirkt hat.
