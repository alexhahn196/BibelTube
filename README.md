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
| `produktion/auslieferung/` | **Gesicherte Tonspuren** als FLAC in Teilen <100 MiB — `tonspur_zurueck.sh` holt sie zurück |

## Sicherung: die Tonspur ins Repo, nicht das Video

**GoFile-Links verfallen.** Die Videos 01–03 lagen dort und sind darüber
nicht mehr erreichbar. Ein Hoster-Link ist keine Sicherung.

Gesichert wird ab sofort **die Tonspur, nicht das fertige MP4.**
`stimme.wav` ist das einzige Zwischenergebnis der Pipeline, das Geld kostet
(TTS, rund 160.000 Zeichen je Video) und sich nicht aus dem Repo neu
erzeugen lässt — Text, Standbild, Bildkette, Klangbett und SRT liegen alle
hier. Aus der Tonspur sind Mischung und Montage jederzeit kostenlos
wiederholbar: **das MP4 ist reproduzierbar, die TTS-Ausgabe nicht.**

Standard nach jeder Vertonung, verbindlich ab Video 04:

```bash
produktion/auslieferung/tonspur_sichern.sh V4          # -> FLAC, geprüft, in Teilen
git add produktion/auslieferung/stimme-video-04 && git commit && git push
```

Zurück, ohne einen Cent TTS:

```bash
produktion/auslieferung/tonspur_zurueck.sh V4
python3 produktion/pipeline/render.py V4 --nur 3 5
```

Beide Wege prüfen die Audiodaten gegen eine im `manifest.txt` hinterlegte
PCM-Prüfsumme; FLAC ist verlustfrei, und das Skript weist es nach, statt es
zu behaupten. Geschnitten wird nach **Bytes** (`split -b 90M`), nicht nach
fester Teilezahl: bei 20 Teilen wäre Video 02 mit 115 MiB je Teil über
GitHubs harter 100-MiB-Grenze gelandet.

**Fertige MP4s gehören nicht ins Repo.** Git gibt Platz nie wieder frei —
was einmal gepusht wurde, bleibt in der Historie, auch nach `git rm`. Ein
MP4 „kurz zum Hochladen reinlegen" kostet seine vollen 1,8 GB dauerhaft von
einem 5-GB-Deckel, an dem die acht Tonspuren mit 4,1–5,5 GB ohnehin schon
knapp sind. Wer die Datei zum Upload braucht, nimmt ein
**GitHub-Release-Asset**: 2 GB je Datei, zählt nicht gegen die Repo-Größe,
und Löschen gibt den Platz wirklich frei.

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
