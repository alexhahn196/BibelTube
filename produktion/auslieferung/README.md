# Auslieferung — was gesichert wird und wie

**Gesichert wird die Tonspur, nicht das fertige Video.**

`stimme.wav` ist das einzige Zwischenergebnis der Pipeline, das Geld kostet
(Fish-Audio-TTS, rund 160.000 Zeichen je Video) und sich nicht aus dem Repo
neu erzeugen lässt. Text, Standbild, Bildkette, Klangbett und SRT liegen
alle hier. Aus `stimme.wav` sind Schritt 3 (Mischung) und Schritt 5
(Montage) jederzeit kostenlos wiederholbar — **das MP4 ist reproduzierbar,
die TTS-Ausgabe nicht.**

Deshalb: Tonspur als FLAC dauerhaft ins Repo, MP4 nicht. Das kostet rund
ein Drittel des Platzes und hält den 5-GB-Deckel für alle acht Videos
erreichbar.

GoFile-Links verfallen — die Links zu den Videos 01–03 waren bereits tot.
Ein Hoster-Link ist keine Sicherung.

## Standard nach jeder Vertonung

```bash
produktion/auslieferung/tonspur_sichern.sh V4
git add produktion/auslieferung/stimme-video-04
git commit -m "Tonspur Video 04 gesichert" && git push
```

`tonspur_sichern.sh` wandelt `produktion/arbeit/video-04/stimme.wav` nach
FLAC, **weist die Verlustfreiheit nach** (Prüfsumme der rohen PCM-Daten vor
und nach der Wandlung) und zerlegt das Ergebnis in Teile unter 100 MiB.
Die PCM-Prüfsumme wandert ins `manifest.txt`.

## Tonspur zurückholen

```bash
produktion/auslieferung/tonspur_zurueck.sh V4
python3 produktion/pipeline/render.py V4 --nur 3 5     # ohne TTS-Kosten
```

Fügt die Teile, prüft sie, dekodiert nach `stimme.wav` im Format, das
Schritt 3 erwartet (44100 Hz, mono, PCM_16), und vergleicht die
Audiodaten gegen die `pcm_md5` aus dem `manifest.txt`.

Ein Byte-Vergleich der ganzen WAV taugt dafür **nicht**: der WAV-Kopf
trägt je nach Schreiber unterschiedliche Zusatzfelder (ffmpeg schreibt ein
`LIST/INFO/ISFT`-Feld, 34 Byte), die Samples sind trotzdem gleich. Geprüft
werden deshalb die Audiodaten ohne Kopf.

## Beliebige Datei zerlegen

`zerlegen.sh` und `zusammensetzen.sh` arbeiten auf jeder Datei, nicht nur
auf Tonspuren — etwa für ein MP4, das kurzfristig zum Hochladen gebraucht
wird:

```bash
produktion/auslieferung/zerlegen.sh produktion/video-04/video-04.mp4
produktion/auslieferung/zusammensetzen.sh video-04 /pfad/video-04.mp4
```

`zusammensetzen.sh` prüft dreistufig und bricht bei jedem Fehlschlag ab, ohne eine
halbfertige Datei liegen zu lassen:

1. sind alle im `manifest.txt` gemeldeten Teile da,
2. stimmt jeder Teil gegen `pruefsummen.sha256`,
3. stimmen Größe, SHA-256 und MD5 der gefügten Datei gegen `manifest.txt`.

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

## Platzbudget — und warum das MP4 draussen bleibt

**Git gibt Platz nie wieder frei.** Was einmal gepusht wurde, bleibt in der
Historie, auch nach `git rm`. Der 5-GB-Deckel gilt also **kumulativ über
alles, was je im Repo lag** — nicht über den aktuellen Stand. Ein MP4
„für den Upload kurz reinlegen und danach wieder raus" kostet seine vollen
1,8 GB dauerhaft.

Stand heute und Hochrechnung:

| Posten | Größe |
|---|---:|
| Repo heute (`.git`) | 0,66 GB |
| `stimme.flac` je Video (1,14 GB WAV, FLAC 45–60 %) | 0,51–0,68 GB |
| acht Tonspuren | 4,1–5,5 GB |
| **Summe bei acht Videos** | **4,8–6,2 GB** |
| GitHubs harte Grenze | 5,0 GB |

Das ist **knapp und im ungünstigen Fall zu wenig** — die Tonspuren allein
reichen bis etwa Video 6–8, je nachdem wie gut die Sprache komprimiert.
Ein einziges zusätzliches MP4 von 1,8 GB kippt die Rechnung sicher.

Konsequenzen:

- **Fertige MP4s gehören nicht ins Repo.** Wer die Datei zum Hochladen
  braucht, nimmt ein **GitHub-Release-Asset**: 2 GB je Datei, zählt
  **nicht** gegen die Repo-Größe, und Löschen gibt den Platz wirklich frei.
  Genau der Fall, für den ein Release gedacht ist.
- Wird es trotzdem eng, ist der nächste Schritt **Git LFS** mit Datenpaket
  oder Objektspeicher.
- Ein Blick auf den Stand: `du -sh .git`.

## Teilegröße: nach Bytes, nicht nach fester Teilezahl

`zerlegen.sh` schneidet mit `split -b 90M`, nicht mit `split -n 20`. Eine
feste Teilezahl hält die Grenze nur zufällig ein — sie hängt an der
Dateigröße:

| Datei | Größe | bei `-n 20` | | bei `-b 90M` | |
|---|---:|---:|---|---:|---|
| video-01.mp4 |  666,7 MB |  31,8 MiB × 20 | ok | 90 MiB × 8 | ok |
| video-02.mp4 | 2415,3 MB | **115,2 MiB × 20** | **über der Grenze** | 90 MiB × 26 | ok |
| video-03.mp4 | 1926,4 MB |  91,9 MiB × 20 | knapp ok | 90 MiB × 21 | ok |
| video-04.mp4 | 1825,1 MB |  87,0 MiB × 20 | ok | 90 MiB × 20 | ok |
| stimme-video-04.flac | ~570 MB | 28,5 MiB × 20 | ok | 90 MiB × 7 | ok |

GitHub weist einzelne Blobs ab 100 MiB hart zurück. Für Video 02 wäre der
Push mit 20 Teilen abgewiesen worden. Nach Bytes passt jede Dateigröße.

## Stand

| Video | auf YouTube | Tonspur gesichert | Anmerkung |
|---|---|---|---|
| video-01 | online | **nein** | vor Einführung dieses Verfahrens vertont |
| video-02 | online | **nein** | dito |
| video-03 | online | **nein** | dito |
| video-04 | nein | **nein** | noch nicht vertont — `FISH_KEY` fehlt |

Für 01–03 ist nichts zu tun: sie sind auf YouTube online. Ihre Tonspuren
sind allerdings unwiederbringlich weg — eine Neumontage würde für jedes
eine neue, kostenpflichtige Vertonung bedeuten. Ab Video 04 verhindert
`tonspur_sichern.sh` genau das.

## Warum `produktion/arbeit/` weiter ignoriert bleibt

Der Ordner enthält je Video mehrere Gigabyte Zwischenstände (Chunks,
`stimme.wav`, `mix.wav`, `zyklus.mp4`). Davon ist nur `stimme.wav`
unersetzlich, und die geht als FLAC hierher. Alles andere ist aus dem Repo
neu erzeugbar und bleibt deshalb ignoriert.
