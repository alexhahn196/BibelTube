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

## Grenze der Messgröße (Sanity-Check 2026-08-23)

Die Metrik misst **Flachheit**, nicht Banding — und Rauschen macht flach unflach.
Gegenprobe am **unencodierten** Standbild, nur der Filter `noise=alls=4`, kein
Encode dazwischen:

| | Luma-Stufen | größte einfarbige Fläche |
|---|---|---|
| Quellbild | 48 | 0,0124 % |
| Quellbild + `noise=alls=4` | 48 | **0,0025 %** (Faktor 0,20) |

**Was das für die Ergebnisse oben heißt — je nach Vergleich unterschiedlich:**

- **i gegen ii (8 Bit gegen 10 Bit) bleibt gültig.** Keine der beiden Varianten
  ist gedithert, beide laufen durch dieselbe Filterkette und unterscheiden sich
  nur in der Bittiefe. Der Vergleich ist sauber.
- **Der Stufenwert ist von diesem Effekt gar nicht betroffen.** Dither ändert die
  Anzahl der Luma-Stufen nicht (48 bleibt 48). Der Verlust auf 41 ist reine
  Wertebereichs-Arithmetik und unabhängig von der Metrik nachgerechnet.
- **iii und iv (die Dither-Varianten) sind konfundiert** — aber der Fehler geht
  **zu ihren Gunsten**: hätte das Rauschen den Encode überlebt, wäre ihr Messwert
  *gesunken*. Er ist stattdessen gestiegen (1,345 % und 1,397 % gegen 1,114 %).
  Das Rauschen hat den Encode also nicht überlebt und zusätzlich Bitrate gekostet.
  Die Aussage „Dither hilft nicht" wird durch den Konfundierungsfehler nicht
  geschwächt, sondern gestützt.

Wer die Dither-Frage sauber entscheiden wollte, bräuchte eine Metrik, die
Stufenkanten misst statt Flächengleichheit. Da die Frage entschieden ist
(nicht weiterverfolgen), ist das nicht gebaut.

## Der wichtigste Vorbehalt: der Zuschauer sieht diesen Strom nie

**YouTube encodiert alles neu**, meist VP9 oder AV1 und meist in 8 Bit. Jede
Zahl in der Tabelle oben ist am **lokalen** Strom gemessen und damit **nicht**
das, was beim Zuschauer ankommt.

10 Bit hilft trotzdem, aber **indirekt**: ein bandingfreier Quellstrom gibt dem
YouTube-Encoder nichts zum Verstärken. Banding im Zulieferstrom ist ein Signal
wie jedes andere — der nachgelagerte Encoder reproduziert es, oft verstärkt,
weil harte Kanten zwischen flachen Flächen billig zu kodieren sind. Umgekehrt
kann er aus einem sauberen Verlauf zwar eigenes Banding erzeugen, hat dafür aber
keine Vorlage.

**Nachweisbar ist das erst nach dem Upload.** Die Tabelle oben belegt, dass der
Quellstrom besser wird; sie belegt **nicht**, dass das Ergebnis beim Zuschauer
besser wird. Wer es wissen will, lädt dasselbe Material zweimal unlisted hoch
und vergleicht auf einem großen Schirm.

## Offen

`yuv420p10le` ist **H.264 High 10**. Ob YouTubes Ingest das annimmt, ist
**nicht geprüft** — hier gibt es keinen Netzzugang dorthin. Die Datei selbst ist
gültig und dekodiert fehlerfrei (`ffmpeg -f null -`).

`produktion/config.md` steht seit 2026-08-23 auf `video_pixelformat = yuv420p10le`.
**Getesteter Rückfallweg**, falls der Upload durchfällt: `yuv420p` bei
`video_crf = 22` — 0,99 GB statt 0,55 GB, Fleckenfaktor 28 statt 90. Dither ist
**kein** Rückfallweg, siehe oben.

## Bilder

`vergleich_gespreizt.png` — derselbe Himmelsausschnitt 640×360 dreimal
übereinander: Quelle / 8 Bit / 10 Bit, Kontrast gespreizt, damit der
Unterschied auf einem Handydisplay überhaupt sichtbar wird.
`vergleich_echt.png` — dieselben drei bei echtem Pegel.
