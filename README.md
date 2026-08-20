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
| `produktion/auslieferung/` | **Fertige MP4s, in Teilen <100 MiB** — `zusammensetzen.sh` stellt sie wieder her |

## Fertige Videos: ins Repo, nicht zu einem Filehoster

**GoFile-Links verfallen.** Die Videos 01–03 lagen dort und sind darüber
nicht mehr erreichbar. Ein Hoster-Link ist keine Sicherung.

Fertige MP4s gehören ab sofort **in Teilen ins Repo**, nach
`produktion/auslieferung/`:

```bash
produktion/auslieferung/zerlegen.sh produktion/video-04/video-04.mp4
git add produktion/auslieferung/video-04 && git commit && git push
```

Zurück kommt die Datei mit Prüfsummenkontrolle über
`produktion/auslieferung/zusammensetzen.sh video-04`. Geschnitten wird nach
**Bytes** (`split -b 90M`), nicht nach fester Teilezahl: bei 20 Teilen wäre
Video 02 mit 115 MiB je Teil über GitHubs harter 100-MiB-Grenze gelandet.

Zwei Einschränkungen, beide in `produktion/auslieferung/README.md` belegt:

- **Das Repo trägt das nicht dauerhaft.** Die vier fertigen Videos sind
  zusammen 6,83 GB, die acht geplanten 13,67 GB — GitHubs harte Grenze
  liegt bei 5 GB. Das Verfahren trägt zwei bis drei Videos; danach braucht
  es Git LFS, Release-Assets oder Objektspeicher. Bis dahin: nur das noch
  nicht hochgeladene Video ablegen und den Ordner nach dem YouTube-Upload
  wieder entfernen.
- **Die Tonspur ist wichtiger als das Video.** `produktion/arbeit/` steht in
  der `.gitignore`, also wurde nie eine `stimme.wav` eingecheckt. Damit ist
  keines der vier fertigen Videos ohne **neue, kostenpflichtige** TTS
  wiederherstellbar, obwohl Text, Standbild, Bildkette und SRT alle im Repo
  liegen. Die Tonspur ist das einzige teure Zwischenergebnis der Pipeline —
  sie gehört gesichert, bevor das nächste Video gerendert wird.

## Was an Kanal 2 ging

Verschoben (Inhalt): das gesamte frühere `recherche/`-Verzeichnis — 51 Dateien,
193 MB.

Kopiert (Technik, liegt bewusst in beiden Repos): `produktion/pipeline/*.py`,
`produktion/pipeline/README.md`, `produktion/motive/README.md`. Änderungen an
diesen Skripten gleichen sich **nicht** automatisch ab.

Hier geblieben: `produktion/pipeline/qa/` — gemessene F3-Formant-Referenzwerte
der Kanal-1-Stimme. Das Verfahren (`rhotik.py`) ist mitgekopiert, die Messwerte
nicht.
