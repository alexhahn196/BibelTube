# BibelTube

Faceless-YouTube-Kanal, christliche Schlafinhalte: englischsprachige
Bibellesungen mit ruhiger Stimme über einem Klangbett, **3,5 Stunden** Laufzeit
je Video.

> **Kanal 2 (Erklärkanal) liegt in https://github.com/alexhahn196/explainer-channel
> — Regeln nicht vermischen.**
>
> Die Regeln und die Formel dieses Repos sind aus **zehn christlichen
> Schlafkanälen** abgeleitet: 3,5 Stunden Laufzeit, Versalhöhe 11,5 % im
> Thumbnail, Sprachanteil 95 %, durchgehendes Serienmotiv, Titelanker. Für einen
> **10-Minuten-Erklärkanal ist jede dieser Zahlen falsch.** Deshalb liegen die
> beiden Kanäle in getrennten Repositories — damit keine Sitzung versehentlich
> die falsche Formel liest. Die gesamte Kanal-2-Recherche wurde am 2026-08-08
> dorthin verschoben und hier gelöscht; sie liegt nicht doppelt.

## Wo was steht

| Ort | Inhalt |
|---|---|
| `bibeltube-wissen.md` | Einstieg — die vier Arbeitsdokumente aneinandergehängt |
| `regeln/erfolgsregeln.md` | Erfolgsmuster aus 10 Kanälen (2 Gewinner, 8 Verlierer) |
| `formel/video-formel.md` | Die Videoformel · `formel/thumbnail-*.md` Thumbnail-Regeln |
| `teardown/` | Analysen fremder Kanäle |
| `produktion/config.md` | **Einzige Quelle** der festen Kanalparameter, maschinell gelesen |
| `produktion/pipeline/` | Siebenschritt-Pipeline: Text → TTS → Bett → Bild → Video → SRT → Paket |
| `produktion/videos-01-08.md`, `produktion/video-0*/` | Die geplanten und produzierten Videos |
| `stimmtest/` | Blindtests zur Kanalstimme (MILO SOOTHING VOICE) |
| `produktion/auslieferung/` | **Sicherung der Tonspuren** als Release-Asset — Skripte und Prüfsummen-Manifeste |

## Sicherung: Tonspur als Release-Asset

**GoFile-Links verfallen.** Die Videos 01–03 lagen dort und sind darüber
nicht mehr erreichbar. Ein Hoster-Link ist keine Sicherung.

Gesichert wird **die Tonspur, nicht das fertige MP4.** `stimme.wav` ist das
einzige Zwischenergebnis der Pipeline, das Geld kostet (TTS, rund 160.000
Zeichen je Video) und sich nicht aus dem Repo neu erzeugen lässt — Text,
Standbild, Bildkette, Klangbett und SRT liegen alle hier. Aus der Tonspur
sind Mischung und Montage jederzeit kostenlos wiederholbar: **das MP4 ist
reproduzierbar, die TTS-Ausgabe nicht.**

**Die Bytes liegen als Release-Asset, die Prüfsummen im Repo.** Ein Release
je Video, Tag `v04`, `v05`, … Ins Repo kommt nur `video-NN.manifest`,
wenige hundert Byte mit Größe, `sha256` und `pcm_md5` jedes Assets.

Standard nach jeder Vertonung, verbindlich ab Video 04:

```bash
produktion/auslieferung/tonspur_sichern.sh V4        # FLAC, geprüft, ins Release v04
git add produktion/auslieferung/video-04.manifest && git commit && git push
```

Zurück, ohne einen Cent TTS:

```bash
produktion/auslieferung/tonspur_zurueck.sh V4
python3 produktion/pipeline/render.py V4 --nur 3 5
```

Das fertige MP4 geht denselben Weg (`asset_sichern.sh V4 …`) und darf nach
dem YouTube-Upload aus dem Release gelöscht werden — die Tonspur bleibt.
Voraussetzung ist die GitHub-CLI (`gh auth login`); ohne sie brechen die
Skripte mit klarer Meldung ab, bevor sie etwas anfassen.

**Warum nicht ins Repo:** Acht Tonspuren wären 4,1–5,5 GB, dazu die heute
schon belegten 0,66 GB — gegen GitHubs harte Grenze von 5,0 GB. Das bricht
im ungünstigen Fall bei Video 7, mitten im Block. Und Git gibt Platz nie
wieder frei: was einmal gepusht wurde, bleibt in der Historie, auch nach
`git rm`. Ein Release-Asset erlaubt 2 GB je Datei, zählt nicht gegen die
Repo-Größe, und Löschen wirkt wirklich — eine Zerlegung in Teile unter
100 MiB entfällt damit vollständig.

Details, Zahlen und der Stand je Video: `produktion/auslieferung/README.md`.

## Was an Kanal 2 ging

Verschoben (Inhalt): das gesamte frühere `recherche/`-Verzeichnis — 51 Dateien,
193 MB.

Kopiert (Technik, liegt bewusst in beiden Repos): `produktion/pipeline/*.py`,
`produktion/pipeline/README.md`, `produktion/motive/README.md`. Änderungen an
diesen Skripten gleichen sich **nicht** automatisch ab.

Hier geblieben: `produktion/pipeline/qa/` — gemessene F3-Formant-Referenzwerte
der Kanal-1-Stimme. Das Verfahren (`rhotik.py`) ist mitgekopiert, die Messwerte
nicht.
