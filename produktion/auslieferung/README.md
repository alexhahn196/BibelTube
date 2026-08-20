# Auslieferung — was gesichert wird und wo es liegt

**Gesichert wird die Tonspur. Die Bytes liegen als Release-Asset, die
Prüfsummen im Repo.**

`stimme.wav` ist das einzige Zwischenergebnis der Pipeline, das Geld kostet
(Fish-Audio-TTS, rund 160.000 Zeichen je Video) und sich nicht aus dem Repo
neu erzeugen lässt. Text, Standbild, Bildkette, Klangbett und SRT liegen
alle hier. Aus `stimme.wav` sind Schritt 3 (Mischung) und Schritt 5
(Montage) jederzeit kostenlos wiederholbar — **das MP4 ist reproduzierbar,
die TTS-Ausgabe nicht.**

GoFile-Links verfallen; die Links zu den Videos 01–03 waren bereits tot.
Ein Hoster-Link ist keine Sicherung.

## Warum Release-Assets und nicht das Repo

Der frühere Plan — fertige Dateien in Teile unter 100 MiB zerlegen und ins
Repo pushen — trägt die Serie nicht zu Ende:

| Posten | Größe |
|---|---:|
| Repo heute (`.git`) | 0,66 GB |
| acht Tonspuren als FLAC (0,51–0,68 GB je Video) | 4,1–5,5 GB |
| **Summe** | **4,8–6,2 GB** |
| GitHubs harte Repo-Grenze | 5,0 GB |

Im ungünstigen Fall bricht das bei Video 7, also mitten im Block. Dazu
kommt: **Git gibt Platz nie wieder frei.** Was einmal gepusht wurde, bleibt
in der Historie, auch nach `git rm` — ein MP4 „kurz zum Hochladen
reinlegen" kostet seine vollen 1,8 GB dauerhaft.

Ein Release-Asset erlaubt **2 GB je Datei**, zählt **nicht** gegen die
Repo-Größe, und Löschen gibt den Platz wirklich frei. Die Zerlegung in
Teile entfällt damit vollständig: eine FLAC von 0,51–0,68 GB und ein MP4
von 1,8 GB passen jeweils als **eine** Datei.

Im Repo bleibt je Video nur `video-NN.manifest` — wenige hundert Byte mit
Größe und Prüfsumme jedes Assets. Damit ist versioniert nachvollziehbar,
welches Release welche Datei mit welcher Prüfsumme hält, und die Prüfung
funktioniert unabhängig davon, ob das Asset noch existiert.

## Ein Release je Video

Tag `v04`, `v05`, … Assets darin:

| Asset | Bleibt | Zweck |
|---|---|---|
| `stimme-video-NN.flac` | **dauerhaft** | die teure TTS-Ausgabe, verlustfrei |
| `video-NN.mp4` | bis zum YouTube-Upload | danach löschbar, die Montage ist wiederholbar |
| `mix.wav` | optional | spart beim Neumontieren Schritt 3; aus der Tonspur neu erzeugbar |

## Standard nach jeder Vertonung

```bash
produktion/auslieferung/tonspur_sichern.sh V4
git add produktion/auslieferung/video-04.manifest
git commit -m "Tonspur Video 04 gesichert" && git push
```

`tonspur_sichern.sh` wandelt `produktion/arbeit/video-04/stimme.wav` nach
FLAC, **weist die Verlustfreiheit nach**, schreibt Größe, `sha256` und
`pcm_md5` ins Manifest, legt das Release `v04` an, falls es fehlt, lädt die
FLAC hoch und prüft anschließend, dass das Asset mit der erwarteten Größe
im Release liegt.

## Tonspur zurückholen

```bash
produktion/auslieferung/tonspur_zurueck.sh V4
python3 produktion/pipeline/render.py V4 --nur 3 5     # ohne TTS-Kosten
```

Holt die FLAC aus dem Release, prüft Größe und `sha256` gegen das Manifest,
dekodiert nach `stimme.wav` im Format, das Schritt 3 erwartet (44100 Hz,
mono, PCM_16), und vergleicht die Audiodaten gegen `pcm_md5`.

Ein Byte-Vergleich der ganzen WAV taugt dafür **nicht**: der WAV-Kopf trägt
je nach Schreiber unterschiedliche Zusatzfelder (ffmpeg schreibt ein
`LIST/INFO/ISFT`-Feld, 34 Byte), die Samples sind trotzdem gleich. Geprüft
werden deshalb die Audiodaten ohne Kopf — das ist der Grund, warum
`pcm_md5` im Manifest steht und nicht nur `sha256`.

## MP4 und andere Dateien

```bash
produktion/auslieferung/asset_sichern.sh V4 produktion/video-04/video-04.mp4
produktion/auslieferung/asset_holen.sh   V4 video-04.mp4
```

Legt die Datei unverändert ins selbe Release und schreibt ihre Prüfsumme
ins Manifest. Bei `.wav` und `.flac` zusätzlich die PCM-Prüfsumme.

Nach dem YouTube-Upload darf das MP4 weg:

```bash
gh release delete-asset v04 video-04.mp4
```

Der Manifesteintrag bleibt als Beleg stehen, was einmal ausgeliefert wurde.
Die Tonspur bleibt im Release — damit ist die Montage jederzeit
wiederholbar.

## Voraussetzung: `gh`

Hoch- und Herunterladen von Release-Assets geht nur über die GitHub-CLI:

```bash
gh auth login          # einmalig
```

Ohne `gh` brechen die Skripte mit einer klaren Meldung ab, bevor sie etwas
anfassen. Die Wandlung nach FLAC und alle Prüfungen laufen auch ohne.

## Stand

| Video | auf YouTube | Tonspur gesichert | Release |
|---|---|---|---|
| video-01 | online | **nein** | — |
| video-02 | online | **nein** | — |
| video-03 | online | **nein** | — |
| video-04 | nein | **nein** | — |

Für 01–03 ist nichts zu tun; ihre Tonspuren sind unwiederbringlich weg,
das ist akzeptiert. Video 04 ist noch nicht vertont — `FISH_KEY` fehlt.
Ab Video 04 greift dieser Weg.

## Warum `produktion/arbeit/` weiter ignoriert bleibt

Der Ordner enthält je Video mehrere Gigabyte Zwischenstände (Chunks,
`stimme.wav`, `mix.wav`, `zyklus.mp4`). Davon ist nur `stimme.wav`
unersetzlich, und die geht als FLAC ins Release. Alles andere ist aus dem
Repo neu erzeugbar.
