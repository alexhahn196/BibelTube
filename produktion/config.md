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
# Gemessen, nicht geschaetzt: produktion/video-05/qa.json, schritt2_tts
# (30.220 Woerter / 3,402 h = 148,1). Vorher stand hier 145.9 ohne Quelle,
# und produktion/wortzahlen.py rechnete mit 140 - zwei Zahlen fuer dieselbe
# Groesse. Beide waren Punkte DERSELBEN Geraden, siehe unten.
#
# Die Sprechgeschwindigkeit haengt am Korpus, nicht an der Zeit. Ueber die
# fuenf gerenderten Videos gegen den Erzaehlanteil aus korpus_pruefung.py:
#     WPM = 141,15 + 0,0769 x Erzaehlanteil%      r = 0,972   r^2 = 0,946
#     V01   0,0 % -> 140,4      V02   0,0 % -> 141,8
#     V03  62,3 % -> 146,3      V04  83,0 % -> 146,6      V05  81,7 % -> 148,1
# Vers-Korpora (Psalmen, Sprueche) liegen bei rund 141, Erzaehlstoff bei
# 147-148. Gate 1.13 (M8) verlangt seit Gate 2 fuer JEDES kuenftige Video
# >= 80 % Erzaehlanteil - damit gilt nur noch der Erzaehl-Ast, und dort sind
# 146,6 und 148,1 die einzigen zwei Messungen. Faellt ein Korpus je unter
# 80 %, ist dieser Wert zu hoch und die Gerade oben die bessere Schaetzung.
wpm_erwartet       = 148.1

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
# Der Abstand wird seit 2026-08-23 in BEIDEN Wiedergabefällen geprüft:
# Mono-Summe und je Kanal, beide >= abstand_soll_db. Vorher wurde nur die
# Mono-Summe gemessen, und weil das alte Bett dort 5,2 dB verlor, meldete
# qa_mix.json 12,0 dB, wo am Kopfhörer 6,8 dB standen (V01-V04).
pegel_stimme_dbfs  = -19.0
pegel_bett_dbfs    = -31.0
abstand_soll_db    = 12.0
# Korrigiert 2026-08-26. Hier stand: "Video 02 landete mit -0,13 dBFS ueber
# der eigenen Vorgabe von -0,3: die Normalisierung skaliert nur nach unten,
# und der gemessene Spitzenwert lag schon darunter." Der zweite Halbsatz
# widerspricht dem eigenen Code: schritt3_bett.py misst die Rohspitze, bildet
# skal = min(1.0, ziel_peak/spitze) und protokolliert nur den Peak NACH der
# Skalierung. Video 02 steht in upload.md auf exakt -0,3 dBFS - das ist genau
# der Fall "Rohspitze lag DARUEBER und wurde heruntergezogen"; laege sie
# darunter, bliebe der niedrigere Istwert stehen (V01 -1,61, V04 -1,18).
# Die -0,13 ist die Rohspitze vor der Skalierung. Sie geht nur nach stdout
# und in keine eingecheckte Datei - nicht nachpruefbar, deshalb hier ohne
# Zahl. Belegt und nachpruefbar ist: V02 landete auf der Grenze, ohne jede
# Reserve. -1,0 gibt Reserve, ohne hoerbar leiser zu sein.
peak_max_dbfs      = -1.0
ducking            = nein

# --- Klangbett (Runde 2; Stereoaufbau korrigiert 2026-08-23) ---
# Das Pad bleibt ein ARTEFAKT und kein Rezept: stimmtest/musikbett.py zieht
# die Luftschicht aus einem UNGESEEDETEN np.random.randn, ein erneuter Lauf
# ergäbe ein anderes Bett. Nicht neu erzeugen.
#
# 2026-08-23: bett_pad_feuer.flac trug R = L um 240 Samples versetzt (5,442 ms).
# In der Mono-Summe - was 80 % des Publikums hört, 68 % Handy und 12 % TV -
# ergab das einen Kammfilter mit der ersten Kerbe bei 91,9 Hz. Der drückte die
# Quinte des Pads (82,5 Hz) 10,9 dB unter den Bauplan: ein anderer Akkord als
# der im Hörtest ausgewählte. Details in formel/video-formel.md §5b.
#
# Das neue Bett ist ECHT MONO (L = R, kein Versatz) und trägt die Feuerschicht
# 6 dB leiser mit Tiefpass bei 1,1 kHz (Variante e, entschieden vom
# Kanalinhaber). Es ist AUS dem alten Artefakt herausgetrennt, nicht neu
# erzeugt - das Pad ist dasselbe. Erzeugt mit
#   python3 produktion/klang/klang_proben.py --produktionsbett
# V01-V04 sind mit dem alten Bett gerendert; es bleibt deshalb liegen.
bett_datei         = produktion/klang/bett_mono_feuer_leise.flac
# nur zur Nachvollziehbarkeit von V01-V04, wird von der Pipeline nicht gelesen:
bett_datei_alt     = produktion/klang/bett_pad_feuer.flac
# Formel §3: Sprache beginnt in Sekunde 0-3 (n=11, regeln/daten/
# skript_anatomie.json: 0,0-3,1 s). Bis 2026-08-26 stand hier "n=24" mit
# Verweis auf teardown/.../matrix_voll.csv - die Datei hat 24 Zeilen, aber
# 0,0-7,8 s und 6 Werte ueber 3,0 s; sie belegt die Regel nicht.
# Deshalb 1,5 s statt der
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
# 2026-08-23 auf standbild zurueckgestellt (Entscheidung des Kanalinhabers):
# Formel Paragraph 5 verlangt ein Standmotiv mit sanfter Bewegung ohne
# Szenenschnitt, belegt an 11/11 Stichproben. V3 - der einzige Treffer des
# Kanals - lief so. KI-Clips waeren eine zusaetzliche Variable ohne Beleg,
# und V05-V08 sollen den Korpuswechsel als einzige Aenderung testen.
videoquelle        = standbild
# Die Clips gehoeren zum Standbild ihres Videos und sind mit keinem anderen
# Motiv verwendbar. Deshalb je Video ein eigener Ordner; ki_clip_ordner_V<n>
# schlaegt den allgemeinen Wert.
ki_clip_ordner     = produktion/motive/loops/ki
ki_clip_ordner_V1  = produktion/motive/loops/ki
ki_clip_ordner_V2  = produktion/motive/loops/ki-v02
ki_clip_ordner_V3  = produktion/motive/loops/ki-v03
ki_clip_ordner_V4  = produktion/motive/loops/ki-v04

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
video_crf          = 28
video_preset       = medium
# Pixelformat der Videospur. yuv420p = 8 Bit, yuv420p10le = 10 Bit.
#
# Umgestellt auf 10 Bit am 2026-08-23 (Entscheidung des Kanalinhabers).
# Gemessener Banding-Befund, produktion/motive/bandingtest/: bei CRF 28
# verliert der Nachthimmel in 8 Bit sieben der 48 Luma-Stufen im dunklen
# Bereich - das ist Wertebereichs-Arithmetik (48 x 219/255 = 41,2) und durch
# keine Bitrate zu beheben. In 10 Bit bleiben alle 48, die groesste einfarbige
# Flaeche faellt von Faktor 90 auf 15 gegenueber dem Quellbild, und die Datei
# wird KLEINER (4,92 statt 6,62 MB je 300-s-Zyklus).
#
# WICHTIGER VORBEHALT: YouTube encodiert alles neu, meist VP9/AV1 in 8 Bit.
# Der lokal gemessene Wert ist NICHT das, was der Zuschauer sieht. 10 Bit hilft
# nur indirekt - ein bandingfreier Quellstrom gibt dem YouTube-Encoder nichts
# zum Verstaerken. Ob das ankommt, ist erst nach dem Upload nachweisbar.
#
# Zweiter offener Punkt: yuv420p10le ist H.264 High 10. Ob YouTubes Ingest das
# annimmt, ist von hier aus nicht pruefbar. Faellt der Upload durch, ist der
# getestete Rueckfallweg yuv420p bei video_crf = 22 (0,99 GB statt 0,55 GB,
# Fleckenfaktor 28 statt 90). Dither ist KEIN Rueckfallweg - gemessen
# schlechter als der Ist-Zustand.
video_pixelformat  = yuv420p
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
