# Auslieferung — fertige Videos in Teilen im Repo

Fertige MP4s gehören **hierher**, zerlegt in Teile unter 100 MiB, und
**nicht** zu einem Filehoster. GoFile-Links verfallen; die Links zu den
Videos 01–03 waren bereits tot, und die Dateien waren damit weg.

## Wiederherstellen

```bash
produktion/auslieferung/zusammensetzen.sh video-04
# oder mit eigenem Ziel:
produktion/auslieferung/zusammensetzen.sh video-04 /pfad/video-04.mp4
```

Das Skript prüft dreistufig und bricht bei jedem Fehlschlag ab, ohne eine
halbfertige Datei liegen zu lassen:

1. sind alle im `manifest.txt` gemeldeten Teile da,
2. stimmt jeder Teil gegen `pruefsummen.sha256`,
3. stimmen Größe, SHA-256 und MD5 der gefügten Datei gegen `manifest.txt`.

## Einliefern

```bash
produktion/auslieferung/zerlegen.sh produktion/video-04/video-04.mp4
git add produktion/auslieferung/video-04
git commit -m "Video 04 in Teilen gesichert"
git push -u origin <branch>
```

## Teilegröße: nach Bytes, nicht nach fester Teilezahl

`zerlegen.sh` schneidet mit `split -b 90M`, nicht mit `split -n 20`. Eine
feste Teilezahl hält die Grenze nur zufällig ein — sie hängt an der
Dateigröße:

| Video | Größe | bei `-n 20` | | bei `-b 90M` | |
|---|---:|---:|---|---:|---|
| video-01 |  666,7 MB |  31,8 MiB × 20 | ok | 90 MiB × 8 | ok |
| video-02 | 2415,3 MB | **115,2 MiB × 20** | **über der Grenze** | 90 MiB × 26 | ok |
| video-03 | 1926,4 MB |  91,9 MiB × 20 | knapp ok | 90 MiB × 21 | ok |
| video-04 | 1825,1 MB |  87,0 MiB × 20 | ok | 90 MiB × 20 | ok |

GitHub weist einzelne Blobs ab 100 MiB hart zurück. Für Video 02 wäre der
Push mit 20 Teilen abgewiesen worden. Mit 90 MiB je Teil hält jede
Dateigröße die Grenze ein — und Video 04 ergibt genau die erwarteten
20 Teile.

## Grenze dieses Verfahrens

Das Repo trägt die Videos nicht dauerhaft:

| | Summe |
|---|---:|
| Videos 01–04 fertig | 6,83 GB |
| alle 8 geplanten Videos (hochgerechnet) | 13,67 GB |

GitHub empfiehlt unter 1 GB je Repository und setzt bei **5 GB** eine harte
Grenze. Schon die vier fertigen Videos reißen sie. Das Verfahren trägt also
**zwei bis drei Videos**, danach braucht es einen anderen Ort — Git LFS mit
Datenpaket, ein Release-Asset (2 GB je Datei, zählt nicht gegen die
Repo-Größe) oder Objektspeicher. Bis dahin gilt: nur das jeweils **noch
nicht hochgeladene** Video hier ablegen und den Ordner nach dem Upload zu
YouTube wieder entfernen.

## Stand

| Video | MP4 im Container | hier gesichert | Anmerkung |
|---|---|---|---|
| video-01 | nein | nein | Tonspur fehlt, siehe unten |
| video-02 | nein | nein | Tonspur fehlt |
| video-03 | nein | nein | Tonspur fehlt |
| video-04 | nein | nein | Tonspur fehlt |

Keines der vier fertigen Videos liegt noch im Container, und **keines ist
ohne neue TTS wiederherstellbar**. Die Montage (`schritt5_video.py`) braucht
`produktion/arbeit/video-NN/mix.wav`; `produktion/arbeit/` steht in der
`.gitignore` und wurde nie eingecheckt — in der gesamten Git-Historie liegt
keine einzige `.wav`. Erhalten sind nur SRT, Standbild, Thumbnail und
Metadaten je Video sowie die KI-Bildketten unter
`produktion/motive/loops/`; das Klangbett `produktion/klang/bett_pad_feuer.flac`
ist die Musik, nicht die Stimme.

**Konsequenz für die Pipeline:** die Tonspur ist das einzige teure und
zugleich einzige nicht gesicherte Zwischenergebnis. Sie gehört gesichert,
bevor das nächste Video gerendert wird — `stimme.wav` als FLAC ist rund ein
Drittel der MP4-Größe und übersteht damit jede Neumontage kostenlos.
