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
# Gemessen an den vier gerenderten Videos (wortgewichtet ueber 122.864
# Woerter / 51.287 s): produktion/korpus/wpm_gemessen.json, erzeugt von
# produktion/wpm_messen.py. Der frueher hier stehende Wert 145.9 war eine
# Schaetzung ohne Beleg. DIES IST DIE EINZIGE STELLE, an der ein Sprechtempo
# steht - plan.json und die Dokumentation verweisen hierher.
# Spanne der Einzelvideos 140,4-146,6 WPM; die Spanne ist Textsorte, nicht
# Streuung: Poesie (V01/V02) 141,1 - Prosa (V03/V04) 146,4.
wpm_erwartet       = 143.7

# --- Text ---
uebersetzung       = webbe
bibel_api          = https://bible-api.com
# "LORD"/"GOD" werden für die TTS zu "Lord"/"God" normalisiert,
# sonst buchstabiert das Modell die Versalien.
versalien_normalisieren = ja

# --- Chunking ---
# Psalm 136 = 23 Semikolon-Verse = 1827 Zeichen; kein Fish-Audio-Limit,
# Pipeline-eigene Wahl.
chunk_max_zeichen  = 1900
chunk_nur_satzende = ja
# Die TTS normalisiert jeden Chunk einzeln -> Pegeldrift an den Nähten.
chunk_pegel_angleichen = ja
tts_parallel       = 12

# --- Pegel (Formel §5b: Stimme in 6/6 Fällen klar über dem Bett) ---
pegel_stimme_dbfs  = -19.0
pegel_bett_dbfs    = -31.0
abstand_soll_db    = 12.0
# Video 02 landete mit -0,13 dBFS ueber der eigenen Vorgabe von -0,3: die
# Normalisierung skaliert nur nach unten, und der gemessene Spitzenwert lag
# schon darunter. -1,0 gibt Reserve, ohne hoerbar leiser zu sein.
peak_max_dbfs      = -1.0
ducking            = nein

# --- Klangbett (Runde 2, dauerhaft) ---
# Bitidentische FLAC-Kopie des in Runde 2 gehörten Betts. Bewusst als
# ARTEFAKT abgelegt und nicht als Rezept: stimmtest/musikbett.py zieht die
# Pad-Schicht aus einem UNGESEEDETEN np.random.randn - ein erneuter Lauf
# ergäbe ein anderes Bett. Diese Datei nicht neu erzeugen.
# 2026-08-30 auf echt mono umgestellt (Vorgabe V06). Abgeleitet aus dem
# bestehenden Artefakt, NICHT neu erzeugt: genommen ist der LINKE Kanal, nicht
# der Stereo-Downmix. Grund: die Kanaele sind mit -0,40 dekorreliert, ein
# Downmix loescht 5,2 dB aus und verschiebt die Balance (Bass -1,0 dB,
# Mitten/Hoehen +1,9 bis +3,7 dB) - also ein anderes Bett, nicht dasselbe in
# mono. Das "-6 dB" im Dateinamen ist reine Dateieigenschaft und wirkt im Mix
# NICHT: schritt3_bett.py normalisiert das Bett ohnehin auf pegel_bett_dbfs.
# Die Stereofassung bleibt als bett_pad_feuer.flac liegen.
bett_datei         = produktion/klang/bett_mono_feuer_leise.flac
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
# Die Clips gehoeren zum Standbild ihres Videos und sind mit keinem anderen
# Motiv verwendbar. Deshalb je Video ein eigener Ordner; ki_clip_ordner_V<n>
# schlaegt den allgemeinen Wert.
ki_clip_ordner     = produktion/motive/loops/ki
ki_clip_ordner_V1  = produktion/motive/loops/ki
ki_clip_ordner_V2  = produktion/motive/loops/ki-v02
ki_clip_ordner_V3  = produktion/motive/loops/ki-v03
ki_clip_ordner_V4  = produktion/motive/loops/ki-v04
ki_clip_ordner_V6  = produktion/motive/loops/ki-v06

# Kapitelmarken sind je Video entschieden, nicht global: videos-01-08.md
# empfiehlt ja bei 01/02/06/08 und nein bei 03/04/05/07 (Formel §7 fuehrt sie
# als optional - A's drei groesste Treffer haben null). Schritt 6 erzeugt sie
# immer; nur die hier genannten Videos bekommen sie ins Upload-Paket.
kapitelmarken_videos = V1,V2,V6,V8
# Formel §5: "Standmotiv mit sanfter Bewegung" ist PFLICHT (11/11 Stichproben).
# Ein völlig statisches Bild wäre ein Dokumentverstoß.
zoom               = ja
zoom_faktor        = 1.04
# Atemzyklus: Zoom faehrt in 300 s von 1,0 auf den Faktor und zurueck.
# Ein Zyklus ist nahtlos schleifbar, die vollen 3,5 h entstehen per
# Bitstrom-Kopie statt per Kodierung.
zoom_zyklus_s      = 300
# Vorgabe V06: 8-Bit-Farbraum erzwingen, damit die Datei auf allen Geraeten
# dekodiert (TV-Sitzungen sind 12 % der Aufrufe und die laengsten).
video_pixelformat  = yuv420p
video_crf          = 28
video_preset       = medium
audio_bitrate      = 192k

# --- Laufzeit (Formel §2) ---
laufzeit_min_h     = 3.0
laufzeit_ziel_von_h = 3.4
laufzeit_ziel_bis_h = 3.8

# --- Qualitätsschwellen (Formel §3) ---
# Kalibriert 2026-08-06 nach drei eigenen Videos (95,6 / 95,3 / 95,3 %): die
# eigene Huellkurvenmessung liest rund 1,5 Punkte strenger als die 97 % aus
# Lauf 1, deren Messmethode nicht bekannt ist. Die eigentliche Schutzregel
# gegen Leerlauf bleibt laengste_pause_max_s - gemessen 1,38-1,46 s gegen die
# 20-s-Grenze. Dies hier ist eine Warnschwelle, kein Abbruchkriterium.
sprachanteil_min_pct = 95.0
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
