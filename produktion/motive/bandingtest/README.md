# Banding-Test der Videospur

**Stand 2026-08-23.** Erzeugt mit `produktion/motive/banding_test.py`.
Die sechs `.mp4`-Testdateien liegen **nicht** im Repo (63 MB, reproduzierbar):
`python3 produktion/motive/banding_test.py --encode` baut sie neu, danach
misst ein Lauf ohne `--encode` sie aus.

## Anlass

Der Fernseher liefert 12 % der Aufrufe, aber **30 % der Wiedergabezeit**
(70,4 min gegen 23,0 min am Handy). Auf einem großen Schirm im dunklen Zimmer
sind Streifen im Nachthimmel sichtbar, die am Handy niemand bemerkt — und
**Gate 1 prüft die encodierte Videospur überhaupt nicht** (Audit in
`produktion/workflow-gates.md`).

## Ergebnis

| Variante | Datei 3,5 h | Luma-Stufen | größte einfarbige Fläche | gegen Quelle |
|---|---|---|---|---|
| Quellbild (PNG, full range) | — | **48** | 0,012 % | 1× |
| **i** 8 Bit CRF 28 *(Ist-Zustand)* | 0,55 GB | 41 | 1,114 % | **90×** |
| **ii** 10 Bit CRF 28 | **0,48 GB** | **48** | 0,185 % | **15×** |
| iii 8 Bit CRF 28 + `noise=alls=4` | 0,45 GB | 41 | 1,345 % | 109× |
| iv 8 Bit CRF 28 `-tune grain` | 0,47 GB | 41 | 1,397 % | 113× |
| v 8 Bit CRF 22 | 0,99 GB | 41 | 0,352 % | 28× |
| vi 8 Bit CRF 20 | 1,29 GB | 41 | 0,142 % | 11× |

## Zwei Effekte, die nicht verwechselt werden dürfen

**1. Der Stufenverlust ist strukturell.** Der dunkle Bereich des Quellbilds
nutzt 48 Luma-Werte. Videofarbraum ist *limited range* (16–235), also bleiben
48 × 219/255 = **41,2** übrig. Gemessen: 41 — in **jeder** 8-Bit-Variante,
auch bei CRF 20. Keine Bitrate der Welt bringt sie zurück. In 10 Bit
(limited range 64–940) bleiben alle 48 erhalten.

**2. Die Fleckengröße hängt an der Bitrate.** CRF 28 → 90×, CRF 22 → 28×,
CRF 20 → 11×. **10 Bit bei CRF 28 liegt bei 15× — besser als 8 Bit bei CRF 22,
bei knapp der halben Dateigröße.**

## Was nicht funktioniert hat

Dither vor dem Encode — beide getesteten Wege haben das Banding **verschlechtert**
(109× bzw. 113× gegen 90× im Ist-Zustand). Der Grund ist Effekt 1: beide
arbeiten in 8 Bit, wo die Stufen bereits fehlen. Dither kann nur verteilen, was
da ist.

## Offen

`yuv420p10le` ist **H.264 High 10**. Ob YouTubes Ingest das annimmt, ist
**nicht geprüft** — hier gibt es keinen Netzzugang dorthin. Die Datei selbst ist
gültig und dekodiert fehlerfrei (`ffmpeg -f null -`). Da YouTube ohnehin alles
neu encodiert, betrifft die Frage nur die Annahme beim Upload, nicht die
Wiedergabe.

`produktion/config.md` trägt seit 2026-08-23 den Schlüssel `video_pixelformat`
mit unverändertem Vorgabewert `yuv420p`. Die Umstellung ist damit eine Zeile —
**entschieden ist sie nicht.**

## Bilder

`vergleich_gespreizt.png` — derselbe Himmelsausschnitt 640×360 dreimal
übereinander: Quelle / 8 Bit / 10 Bit, Kontrast gespreizt, damit der
Unterschied auf einem Handydisplay überhaupt sichtbar wird.
`vergleich_echt.png` — dieselben drei bei echtem Pegel.
