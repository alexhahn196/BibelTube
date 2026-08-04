# Kanal-Konfiguration

Dies ist die **einzige** Quelle für die festen Kanal-Parameter. Die Pipeline liest
den Block unten maschinell (`produktion/pipeline/gemeinsam.py`) — was hier steht,
wird gerendert. Kein Wert doppelt irgendwo anders pflegen.

## Die Stimme

**MILO SOOTHING VOICE**, Fish Audio `cb6381fb822345bd89c207fb49551d24`.

Ausgewählt im Blindtest Runde 1 (`stimmtest/aufloesung.txt`, Datei 01) und vom
Kanalinhaber am 2026-08-04 als feste Kanalstimme bestimmt. **Wechselt nicht.**
Eine Stimme über Hunderte Stunden ist Teil der Kanalidentität, genauso wie die
Thumbnail-Serie und das Klangbett.

### Akzentprüfung vor der Festlegung

Verfahren identisch zu Stimmtest Runde 2 (F3-Formant-Minimum über postvokalischem
/r/, Grenze 2100 Hz — darunter wird das r gesprochen = amerikanisch/neutral).
Gemessen mit `produktion/pipeline/rhotik.py`.

| Datei | Tokens | rhotisch | F3-Median | Urteil |
|---|---|---|---|---|
| **MILO, volle 29-min-Produktion** (`_milo.wav`, speed 0.88) | 17 | **17/17** | **1575 Hz** | rhotisch |
| MILO, Kurzprobe (Text wie Runde 2) | 5 | 5/5 | 1583 Hz | rhotisch |
| Referenz Jameson „neutral american" | 5 | 5/5 | 1635 Hz | rhotisch |
| Referenz Calm (britisch gefärbt, das abgelehnte 03) | 5 | 0/5 | 2268 Hz | nicht-rhotisch |
| Kontrolle Calm, volle 29 min (`_calm.wav`) | 17 | 2/17 | 2274 Hz | nicht-rhotisch |

Das Verfahren wurde vor der Messung an den beiden veröffentlichten Referenzwerten
aus Runde 2 nachvollzogen (Calm 2268,4 vs. publiziert 2269,0 · Jameson 1634,7 vs.
publiziert 1638,0) — die Werte sind also direkt vergleichbar.

**Ergebnis: nicht britisch.** MILO liegt sogar unter der amerikanischen Referenz.
Der in Runde 2 gefundene Fallstrick — Stimmen, die in der Kurzprobe rhotisch sind
und bei langsam gelesenem Volltext umkippen — greift hier nicht: gemessen wurde am
vollen 29-Minuten-Lauf bei Produktionsgeschwindigkeit, und die Quote ist dort
sauberer als in der Kurzprobe.

## Werte

```ini
# --- Stimme (fest, nicht ändern) ---
stimme_name        = MILO SOOTHING VOICE
stimme_id          = cb6381fb822345bd89c207fb49551d24
tts_modell         = s2.1-pro-free
tts_endpoint       = https://api.fish.audio/v1/tts
prosody_speed      = 0.88
wpm_erwartet       = 145.9

# --- Text ---
uebersetzung       = webbe
bibel_api          = https://bible-api.com
# "LORD"/"GOD" werden für die TTS zu "Lord"/"God" normalisiert,
# sonst buchstabiert das Modell die Versalien.
versalien_normalisieren = ja

# --- Chunking ---
chunk_max_zeichen  = 1800
chunk_nur_satzende = ja
# Die TTS normalisiert jeden Chunk einzeln -> Pegeldrift an den Nähten.
chunk_pegel_angleichen = ja
tts_parallel       = 12

# --- Pegel (Formel §5b: Stimme in 6/6 Fällen klar über dem Bett) ---
pegel_stimme_dbfs  = -19.0
pegel_bett_dbfs    = -31.0
abstand_soll_db    = 12.0
peak_max_dbfs      = -0.3
ducking            = nein

# --- Klangbett (Runde 2, dauerhaft) ---
# Bitidentische FLAC-Kopie des in Runde 2 gehörten Betts. Bewusst als
# ARTEFAKT abgelegt und nicht als Rezept: stimmtest/musikbett.py zieht die
# Pad-Schicht aus einem UNGESEEDETEN np.random.randn - ein erneuter Lauf
# ergäbe ein anderes Bett. Diese Datei nicht neu erzeugen.
bett_datei         = produktion/klang/bett_pad_feuer.flac
# Formel §3: Sprache beginnt in Sekunde 0-3 (n=24). Deshalb 1,5 s statt der
# 4 s aus stimmtest/musik-prompt.md — siehe Konflikt-Notiz in der README.
vorlauf_s          = 1.5
einblende_s        = 1.5
nachlauf_s         = 6.0
ausblende_s        = 3.0

# --- Bild und Video (Formel §5) ---
breite             = 1920
hoehe              = 1080
fps                = 24
# Quelle der Videospur:
#   ki_clips  = echte Bild-zu-Video-Clips (Seedance, start=end=Standbild),
#               4 Clips à 12 s als 48-s-Zyklus, Montage per Bitstrom-Kopie.
#               Der Atem-Zoom entfällt hier: Formel §5 verlangt "Standmotiv
#               mit sanfter Bewegung" - die liefern die Clips selbst, und
#               ein Zoom obendrauf würde den kopierfähigen Bitstrom in einen
#               vollständigen Re-Encode verwandeln (LCM-Zyklus 1200 s).
#   standbild = bisheriger Weg: Standbild + Atem-Zoom (300-s-Zyklus)
videoquelle        = ki_clips
ki_clip_ordner     = produktion/motive/loops/ki
# Formel §5: "Standmotiv mit sanfter Bewegung" ist PFLICHT (11/11 Stichproben).
# Ein völlig statisches Bild wäre ein Dokumentverstoß.
zoom               = ja
zoom_faktor        = 1.04
# Atemzyklus: Zoom faehrt in 300 s von 1,0 auf den Faktor und zurueck.
# Ein Zyklus ist nahtlos schleifbar, die vollen 3,5 h entstehen per
# Bitstrom-Kopie statt per Kodierung.
zoom_zyklus_s      = 300
video_crf          = 28
video_preset       = medium
audio_bitrate      = 192k

# --- Laufzeit (Formel §2) ---
laufzeit_min_h     = 3.0
laufzeit_ziel_von_h = 3.4
laufzeit_ziel_bis_h = 3.8

# --- Qualitätsschwellen (Formel §3) ---
sprachanteil_min_pct = 97.0
laengste_pause_max_s = 20.0
sprachstart_max_s    = 3.0
cta_max              = 2
```

## Was hier bewusst NICHT steht

- **Kein Thumbnail-Pfad.** Thumbnails entstehen außerhalb der Pipeline und werden
  vor dem Upload manuell eingesetzt. Die Pipeline erzeugt nur ein Platzhalterbild
  für die Videospur.
- **Kein Upload-Zugang.** Der Upload läuft von Hand, unter anderem weil die
  KI-Kennzeichnung dabei gesetzt werden muss (siehe `upload.md` je Video).
- **Kein API-Schlüssel.** Der Fish-Audio-Schlüssel steht ausschließlich in der
  Umgebungsvariable `FISH_KEY` und darf nicht ins Repository.
