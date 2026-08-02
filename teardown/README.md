# teardown — Konkurrenzanalyse Einschlafgebet-Nische

Ergebnis: **[produktions-spec.md](produktions-spec.md)** — konkrete Zielwerte für die
eigene Pipeline. Alles andere hier sind Rohdaten und Auswertungsskripte.

## Ablauf

```bash
./teardown_batch.sh kanaele.txt        # 8 Kanäle -> Top/Median/Flop je Kanal
python3 analyse.py                     # -> matrix_voll.csv (+ auswertung_matrix.txt)
python3 analyse_population.py          # Gegenprobe an allen 454 Videos
```

Voraussetzungen: `yt-dlp` (aktuell, via pip), `ffmpeg`/`ffprobe`, `python3`, `bc`,
sowie eine JS-Runtime für yt-dlp (`--js-runtimes node`) — ohne die liefert YouTube
keine vollständigen Formate mehr.

## Wichtig für einen erneuten Lauf

Auf dieser Maschine hat YouTube **keine Medien-Bytes ausgeliefert** (403 auf allen
`googlevideo`-URLs, jeder Player-Client, IPv4 wie IPv6) und ab ca. 5 Videos auch die
Metadaten mit 429 abgewiesen. Ursache ist die Egress-IP des Containers, nicht das
Skript. Folgen:

- `frames/` ist leer, die Spalte `visuell` in `matrix.csv` steht auf ihrem
  Startwert `statisch` — **keine Messung, nicht auswerten**
- `sprache_bis_pct` stammt **nicht** aus der Audio-Heuristik des Skripts, sondern
  exakt aus Caption-Zeitstempeln (siehe `analyse.py`)
- `matrix.csv` enthält nur 5 vollständige Zeilen; `matrix_voll.csv` ist die
  zusammengeführte Fassung aller 24 Videos

Von einer normalen Wohn-IP läuft das Skript durch. `refill_metadata.sh` holt
fehlende Zeilen mit Pacing und Backoff nach.

## Dateien

| Datei | Inhalt |
|---|---|
| `produktions-spec.md` | **Das Ergebnis** — Zielwerte, Antworten a–e, offene Punkte |
| `teardown_batch.sh` | Originalskript (unverändert) |
| `kanaele.txt` | Kanalliste |
| `refill_metadata.sh` | Nachholen fehlender Metadaten bei Ratelimit |
| `analyse.py` | Baut `matrix_voll.csv` aus Skript-Output + Transkripten |
| `analyse_population.py` | Prüft die Hypothesen an allen 454 Videos |
| `nexlev_supplement.json` | Metadaten aus unabhängiger Quelle (Ratelimit-Ersatz) |
| `auswertung_matrix.txt` | Ausgabe von `analyse.py` |
| `auswertung_population.txt` | Ausgabe von `analyse_population.py` |
| `teardown_batch_*/matrix_voll.csv` | Vollständige Vergleichsmatrix, 24 Videos |
| `teardown_batch_*/matrix.csv` | Was das Skript selbst schaffte (5 Zeilen) |
| `teardown_batch_*/*_videos.jsonl` | Vollständige Videolisten, 454 Einträge |
| `teardown_batch_*/thumbs/` | 24 Thumbnails, 1280x720 |
| `teardown_batch_*/sheet_*.png` | Kontaktbögen TOP / MEDIAN / FLOP |

## Kernbefunde in drei Sätzen

1. Der einzige belastbare Unterscheider ist das **Thema im Titel** — innerhalb
   desselben Kanals liegen zwischen Median und Treffer bis zu **276x**, bei
   identischer Produktion.
2. **Laufzeit ist kein Hebel** (rho +0,09 über 454 Videos), nur eine Untergrenze
   bei ~1,5 h; der Top/Flop-Kontrast der Stichprobe ist ein Auswahleffekt.
3. Die **Erzählstimme läuft in allen 24 Videos bis 98,6–100 %** der Laufzeit durch —
   das TTS-Budget ist ~46.500 Zeichen pro Stunde Video.
