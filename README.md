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
| `regeln/erfolgsregeln.md` | Erfolgsmuster aus 10 Kanälen (2 Gewinner, 8 Verlierer) — plus **M8**, die erste Regel aus eigenen Kanaldaten (Gate 2, 2026-08-23) |
| `formel/video-formel.md` | Die Videoformel (v2.2) · `formel/thumbnail-*.md` Thumbnail-Regeln |
| `regeln/daten/gate2_eigene_kanaldaten.json` | Eigene YouTube-Analytics, 25.07.–22.08.2026 — die einzige Nicht-Fremddatenquelle im Repo |
| `teardown/` | Analysen fremder Kanäle |
| `produktion/config.md` | **Einzige Quelle** der festen Kanalparameter, maschinell gelesen |
| `produktion/pipeline/` | Siebenschritt-Pipeline: Text → TTS → Bett → Bild → Video → SRT → Paket |
| `produktion/videos-01-08.md`, `produktion/video-0*/` | Die geplanten und produzierten Videos |
| `stimmtest/` | Blindtests zur Kanalstimme (MILO SOOTHING VOICE) |

## Was an Kanal 2 ging

Verschoben (Inhalt): das gesamte frühere `recherche/`-Verzeichnis — 51 Dateien,
193 MB.

Kopiert (Technik, liegt bewusst in beiden Repos): `produktion/pipeline/*.py`,
`produktion/pipeline/README.md`, `produktion/motive/README.md`. Änderungen an
diesen Skripten gleichen sich **nicht** automatisch ab.

Hier geblieben: `produktion/pipeline/qa/` — gemessene F3-Formant-Referenzwerte
der Kanal-1-Stimme. Das Verfahren (`rhotik.py`) ist mitgekopiert, die Messwerte
nicht.
