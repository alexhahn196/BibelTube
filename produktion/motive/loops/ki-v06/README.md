# KI-Clips Video 06

**Neu erzeugt am 2026-09-02.** Der erste Satz (2026-08-31, `flux_3_video`) hat
das Video praktisch zum Standbild gemacht: im ausgelieferten MP4 lag der
Frameschritt bei **0,058** — gegen 0,518 bei V07. Die Clips selbst trugen
keine Bewegung; die Pipeline hat sie korrekt verarbeitet.

## Der jetzige Satz

Vier Bild-zu-Video-Clips aus `produktion/motive/motiv-V6.png`, Modell
`seedance1_5`, **1920×1080, 24 fps, 12,042 s, `resolution: 1080p`,
`generate_audio: false`**, `start_image = end_image = motiv-V6.png`.

Ausdrücklich animiert: Feuerflackern, Rauchfäden, Funkenflug, Sternenfunkeln,
leichte Stoffbewegung am Gewand. Ausdrücklich unverändert: Kamera, Bildaufbau,
Landschaft, Figur, **Größe und Helligkeit des Feuers**.

| | Frameschritt Median | Urteil |
|---|---:|---|
| alter Satz (flux_3_video) | 0,058 | Standbild mit Flackern |
| erster Neuversuch, zu starker Prompt | 2,495 | Feuer wuchs zur Lohe, Rauchwolke über dem halben Himmel — verworfen |
| **jetziger Satz** | **0,650** | bewegt sich sichtbar, Bildaufbau unverändert |

> **Der Prompt entscheidet, nicht das Modell.** „Kamera unbewegt" heißt nicht
> „Bild unbewegt" — die Bewegung muss ausdrücklich verlangt werden. Umgekehrt
> reißt ein zu starker Prompt das Motiv auseinander: „thick smoke", „showers of
> embers", „surge" ließen das Lagerfeuer zum Scheiterhaufen werden. Der
> gültige Prompt nennt beides: welche Elemente sich bewegen **und** dass Größe
> und Helligkeit des Feuers gleich bleiben.

## Zyklus

Vier Clips aneinander, CRF 28, 1156 Frames, 48,17 s. Nahtfaktoren
**2,19 / 2,73 / 2,29**.

Blende geprüft (`xfade` 0,5 s an den drei inneren Schnitten): Faktoren
**3,04 / 2,82 / 2,49** — zwei schlechter, einer praktisch gleich, dazu 1,5 s
Verlust. **Verworfen**, wie bei V07. Die Rundnaht clip‑4 → clip‑1 bleibt
unbehandelt; dafür gibt es im Repo kein Verfahren.
