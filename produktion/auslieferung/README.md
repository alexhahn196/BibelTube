# Auslieferung

**Angelegt 2026-08-23.** V01–V04 wurden von Hand zu GoFile hochgeladen; im Repo
gab es dafür keinen Code und kein Manifest. Beides steht jetzt hier.

## Skript

```bash
export GOFILE_TOKEN=...                              # nie ins Repo
produktion/pipeline/gofile_hochladen.sh V5           # lädt hoch
produktion/pipeline/gofile_hochladen.sh V5 --nur-pruefen   # rechnet nur Prüfsummen
```

Ohne `GOFILE_TOKEN` legt das Skript ein **Gastkonto** an und lädt mit dessen
Wegwerf-Token hoch. Die Dateien hängen dann an keinem Konto des Kanalinhabers.
Der Gast-Token wird am Ende ausgegeben und **nirgends gespeichert** — nur mit
ihm sind die Dateien später noch zu verwalten oder zu löschen. Das Skript sagt
es an und fragt nicht nach.

> **Korrektur 2026-08-26.** Hier stand: „Ohne `GOFILE_TOKEN` läuft der Upload
> **anonym**: GoFile nimmt die Dateien an." Das stimmt nicht mehr. Der erste
> V05-Upload scheiterte mit `error-createGuestAccount`: der Upload-Endpunkt
> weist inzwischen jede Anfrage **ohne** `Authorization`-Header ab.
> Nachgeprüft statt vermutet — `POST https://api.gofile.io/accounts` legt
> weiterhin ohne Weiteres ein Gastkonto an und liefert einen Token; nur der
> tokenlose Upload ist weggefallen. Genau diesen Umweg geht das Skript jetzt.

Hochgeladen wird, was im Paketordner liegt — fehlende Rollen werden
übersprungen, nicht erfunden:

| Rolle | Datei | |
|---|---|---|
| `video` | `video-0N.mp4` | Videospur mit Ton |
| `ton` | `video-0N.flac` | reine Tonspur, für Neumontage ohne neue TTS-Kosten |
| `untertitel` | `video-0N.srt` | |

## Zwei Gegenproben je Datei

1. **Größe.** Die von GoFile gemeldete Bytezahl muss byte-genau mit der lokalen
   übereinstimmen, sonst bricht das Skript ab. Das ist die Prüfung, die schon
   bei V01–V03 von Hand gemacht wurde.
2. **`sha256`.** Steht im Manifest. Eine Größe allein kann zufällig stimmen,
   eine Prüfsumme nicht — und nur mit ihr lässt sich Monate später beantworten,
   ob die Datei hinter einem Link noch dieselbe ist.

## Manifest-Format

`produktion/auslieferung/manifest.json`, append-only — jede Auslieferung hängt
sich hinten an, nichts wird überschrieben. So bleibt auch ein erneuter Upload
derselben Datei nachvollziehbar.

```json
{
  "format": 1,
  "auslieferungen": [
    {
      "video": "V5",
      "titel": "You're Tired, I Know… Luke's Whole Story, Read Slowly Until Morning",
      "hochgeladen_am": "2026-08-25T14:02:11Z",
      "dateien": [
        {
          "rolle": "video",
          "name": "video-05.mp4",
          "bytes": 1913455104,
          "sha256": "9f2c…",
          "gofile": {
            "fileId": "…",
            "downloadPage": "https://gofile.io/d/…",
            "server": "store-eu-par-1"
          }
        }
      ]
    }
  ]
}
```

| Feld | Bedeutung |
|---|---|
| `format` | Formatversion. Steigt nur, wenn sich die Struktur ändert. |
| `video` | Kennung wie in `config.md` und `plan.json` (`V1`…`V8`). |
| `titel` | Wörtlich aus `produktion/video-0N/titel.txt` zum Zeitpunkt des Uploads — der Titel kann sich später ändern, das Manifest hält den ausgelieferten fest. |
| `hochgeladen_am` | UTC, ISO 8601. |
| `dateien[].rolle` | `video`, `ton` oder `untertitel`. |
| `dateien[].bytes` | Lokale Größe, gegen GoFiles Meldung geprüft. |
| `dateien[].sha256` | Prüfsumme der lokalen Datei. |
| `dateien[].gofile` | Was GoFile zurückgemeldet hat. `downloadPage` ist der Link zum Weitergeben. |

**Nicht im Manifest:** der Token, und die Dateien selbst. `produktion/video-*/*.mp4`
und `*.wav` sind gitignored — das Repo trägt die Beschreibung der Auslieferung,
nicht die Auslieferung.

## Nachträglich prüfen

```bash
sha256sum produktion/video-05/video-05.mp4
jq -r '.auslieferungen[] | select(.video=="V5") | .dateien[] | "\(.rolle) \(.sha256)"' \
   produktion/auslieferung/manifest.json
```
