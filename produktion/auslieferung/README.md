# Auslieferung — welcher Weg wofür

**Drei Wege, drei Zwecke. Sie werden regelmäßig verwechselt — deshalb hier
zuerst die Entscheidungstabelle.**

| Was | Wohin | Wozu | Lebensdauer |
|---|---|---|---|
| **Tonspur** `stimme.flac` | **Release-Asset** (`v04`, `v05`, …) | die einzige *Sicherung*. Sie hat Geld gekostet und ist nicht reproduzierbar. | dauerhaft |
| **Fertiges MP4** | **GoFile** | *Transport* zur eigenen Maschine für den YouTube-Upload | vergänglich, siehe unten |
| irgendetwas davon | **Repo, zerlegt** | **Notfall.** Nur wenn beide Wege oben ausfallen. | dauerhaft — und unumkehrbar |

## Standard: das fertige MP4 geht zu GoFile

So lief es bei Video 01–03, und so läuft es weiter. Der Container hat
Netzzugang; ein Upload braucht keinen Schlüssel und kein Konto:

```bash
SRV=$(curl -s https://api.gofile.io/servers \
      | python3 -c "import json,sys; print(json.load(sys.stdin)['data']['servers'][0]['name'])")
curl -F "file=@produktion/video-04/video-04.mp4" \
     "https://${SRV}.gofile.io/contents/uploadfile"
```

Die Antwort enthält `downloadPage` — das ist der Link. Datei herunterladen,
zu YouTube hochladen, fertig.

> **GoFile ist Transport, keine Sicherung.** Genau diese Verwechslung hat den
> Vorfall vom 2026-08-20 ausgelöst: die Links zu Video 01–03 waren verfallen,
> und weil sonst nichts gesichert war, wären alle drei Videos nur durch eine
> neue, kostenpflichtige Vertonung wiederherstellbar gewesen. Ein Gast-Upload
> ohne Konto wird nach einiger Zeit ohne Zugriff gelöscht.
>
> **Deshalb gilt beides gleichzeitig:** MP4 zu GoFile, damit man es in die
> Hand bekommt — **und** Tonspur ins Release, damit die teure Arbeit
> überlebt. Der Link darf ablaufen. Die Tonspur nicht.

## Warum die Sicherung ins Release gehört und nicht ins Repo

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

## Ausnahme: Video 04 liegt zerlegt im Repo

`video-04/` enthält das fertige MP4 in **20 Teilen à 90 MiB**, dazu
`manifest.txt` und `pruefsummen.sha256`. Zurück kommt es mit:

```bash
produktion/auslieferung/zusammensetzen.sh video-04 /pfad/video-04.mp4
```

Das ist eine **einmalige Ausnahme auf ausdrückliche Entscheidung**, kein
Vorbild. Sie kostet 1,83 GB dauerhaft in der Historie — Git gibt den Platz
auch nach `git rm` nicht wieder frei. Das Repo wächst damit von 0,66 GB auf
rund 2,5 GB gegen eine harte Grenze von 5,0 GB.

Für V05–V08 bleibt es beim Weg oben: **Tonspur als Release-Asset, MP4 gar
nicht ins Repo.** Ein zweites Video dieser Größe im Repo, und der Deckel ist
in Reichweite.

`zerlegen.sh` und `zusammensetzen.sh` sind für diesen Fall wieder da. Sie
sind der Ausnahmeweg, nicht der Standard.

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

## Ausgeliefert

| Video | MP4 zu GoFile | Link | Kontrolle |
|---|---|---|---|
| video-04 | 2026-08-20 | `https://gofile.io/d/IUFqrfej` | md5 `28e52149…`, 1.825.899.455 B — von GoFile unabhängig gemeldet und deckungsgleich mit dem lokalen Wert |

Der Link ist **vergänglich** und steht hier nur als Beleg der Auslieferung,
nicht als Sicherung. Wenn er irgendwann nicht mehr geht, ist das erwartet —
dann kommt das MP4 aus der Tonspur zurück, nicht aus diesem Link.

## Stand

| Video | auf YouTube | Tonspur gesichert | Release |
|---|---|---|---|
| video-01 | online | **nein** | — |
| video-02 | online | **nein** | — |
| video-03 | online | **nein** | — |
| video-04 | nein | **nein** (als Teile beim Nutzer) | — · MP4 zerlegt im Repo |

Für 01–03 ist nichts zu tun; ihre Tonspuren sind unwiederbringlich weg,
das ist akzeptiert. Video 04 ist noch nicht vertont — `FISH_KEY` fehlt.
Ab Video 04 greift dieser Weg.

## Warum `produktion/arbeit/` weiter ignoriert bleibt

Der Ordner enthält je Video mehrere Gigabyte Zwischenstände (Chunks,
`stimme.wav`, `mix.wav`, `zyklus.mp4`). Davon ist nur `stimme.wav`
unersetzlich, und die geht als FLAC ins Release. Alles andere ist aus dem
Repo neu erzeugbar.
