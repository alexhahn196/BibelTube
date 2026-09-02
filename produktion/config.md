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
# ENTSCHIEDEN 2026-09-02 bei der Zusammenfuehrung der beiden Zweige: 143.7.
# Gemessen an den vier gerenderten Videos, wortgewichtet ueber 122.864 Woerter
# / 51.287 s: produktion/korpus/wpm_gemessen.json, erzeugt von
# produktion/wpm_messen.py. DIES IST DIE EINZIGE STELLE, an der ein Sprechtempo
# steht - plan.json und die Dokumentation verweisen hierher.
#
# Die verworfene Alternative war 148.1 aus einem einzigen Video (V05,
# produktion/video-05/qa.json: 30.220 W / 3,402 h). Sie ist nicht falsch
# gemessen, sie ist nur EINE Messung; 143.7 mittelt vier. Wer 148.1 sucht,
# findet sie dort weiter.
#
# Das Tempo haengt an der Textsorte, nicht an der Zeit. Beide Zweige haben das
# unabhaengig gefunden:
#   Spanne der Einzelvideos 140,4-148,2 WPM - Poesie (V01/V02) 141,1,
#   Prosa (V03/V04) 146,4, Erzaehlstoff (V06 gerendert) 148,2.
#   Regression ueber fuenf Videos gegen den buchweisen Erzaehlanteil:
#   WPM = 141,15 + 0,0769 x Erzaehlanteil%   (r = 0,972, r^2 = 0,946)
# Die V06-Rendermessung (148,2, produktion/korpus/v06_render.json) bleibt als
# Messdatei stehen und AENDERT DIESEN WERT NICHT. Sie ist ein Hinweis auf die
# Textsorte, kein neuer Kanalwert: ein Erzaehlkorpus laeuft rund 3 % schneller
# als der Kanalschnitt, und wer eine Laufzeit auf 0,05 h genau braucht, rechnet
# mit dem Ast statt mit dem Mittel.
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

# --- Klangbett (Runde 2; Stereoaufbau korrigiert 2026-08-23, mono seit 2026-08-30) ---
# Das Pad bleibt ein ARTEFAKT und kein Rezept: stimmtest/musikbett.py zieht die
# Luftschicht aus einem UNGESEEDETEN np.random.randn, ein erneuter Lauf ergaebe
# ein anderes Bett. Nicht neu erzeugen.
#
# 2026-08-23: bett_pad_feuer.flac trug R = L um 240 Samples versetzt (5,442 ms).
# In der Mono-Summe - was 80 % des Publikums hoert, 68 % Handy und 12 % TV -
# ergab das einen Kammfilter mit der ersten Kerbe bei 91,9 Hz. Der drueckte die
# Quinte des Pads (82,5 Hz) 10,9 dB unter den Bauplan: ein anderer Akkord als
# der im Hoertest ausgewaehlte. Details in formel/video-formel.md §5b.
#
# ENTSCHIEDEN 2026-09-02: das Produktionsbett ist der LINKE KANAL des alten
# Stereo-Artefakts, herausgetrennt und nicht neu erzeugt.
#
# Warum der linke Kanal und nicht der Downmix: die beiden Kanaele des
# Stereo-Artefakts sind mit -0,3958 DEKORRELIERT, also fast gegenphasig
# (nachgemessen 2026-09-02 ueber die vollen 56,0 s). Bei dieser Korrelation
# loescht eine Mono-Summe sich teilweise selbst aus: gemessen -5,20 dB
# gegenueber dem linken Kanal allein. Der Verlust ist nicht gleichmaessig ueber
# das Spektrum, und genau das ist der Punkt - nach Pegelangleich, also so wie
# es im Mix ankommt (schritt3_bett.py normalisiert auf pegel_bett_dbfs):
#     Bass   20-250 Hz    -0,3 dB
#     Mitten 250-2000 Hz  +2,0 dB
#     Hoehen 2-16 kHz     +2,3 dB
# Ein Downmix waere also ein ANDERES Bett, heller und duenner, nicht dasselbe
# in mono. Der linke Kanal ist das, was im Hoertest der Runde 2 auf dem linken
# Ohr lag - unveraendert bis auf -6,00 dB Pegel (Korrelation zum linken Kanal
# 1,000000, Restfehler -69 dB unter dem Signal).
#
# (Frueher stand hier "Bass -1,0 dB, Mitten/Hoehen +1,9 bis +3,7 dB". Dieselbe
# Sache, andere Bandgrenzen; die drei Werte oben sind mit den angegebenen
# Grenzen nachrechenbar.)
#
# Verworfen wurde die zweite Mono-Fassung, "Variante e" aus
# produktion/klang/klang_proben.py --produktionsbett (Feuerschicht 6 dB leiser,
# Tiefpass 1,1 kHz). Sie lag auf dem anderen Zweig UNTER DEMSELBEN DATEINAMEN -
# zwei verschiedene Betten, ein Name. Sie liegt jetzt als
# produktion/klang/verworfen_bett_mono_variante_e.flac, und klang_proben.py
# schreibt nur noch dorthin; die Produktionsdatei kann es nicht mehr
# ueberschreiben (harte Sperre in produktionsbett()).
#
# Die beiden Kandidaten lagen naeher beieinander, als die Namen vermuten
# lassen: Variante e korreliert mit 0,9929 mit dem linken Kanal (mit dem
# Downmix nur 0,5285). Entschieden ist also nicht "mono gegen stereo", sondern
# ob die Feuerschicht 6 dB leiser und tiefpassgefiltert laufen soll. Sie soll
# nicht. Nebenbefund: Variante e ist trotz ihrer Beschreibung ZWEIKANALIG
# (L = R), das Produktionsbett ist einkanalig.
#
# Das "-6 dB" im Namen der Stereofassung ist reine Dateieigenschaft und wirkt
# im Mix NICHT: schritt3_bett.py normalisiert das Bett ohnehin auf
# pegel_bett_dbfs.
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
#
# 2026-08-26 zurueck auf ki_clips (Entscheidung des Kanalinhabers). Die
# Begruendung von 08-23 war in einem Punkt falsch herum gedacht: V01, V02,
# V03 und V04 liefen ALLE mit ki_clips (Belege: die vier Clipsaetze in
# produktion/motive/loops/ und je vier Seedance-Buchungen am 2026-08-04,
# 08-06, 08-06 und 08-07 im Higgsfield-Transaktionsprotokoll). Damit war
# standbild bei V05 nicht die Konstante, sondern die zweite Aenderung neben
# dem Korpus. Der Ruecksprung auf ki_clips entfernt eine Variable, er fuegt
# keine hinzu.
#
# Kosten: die tatsaechlich gebuchten Betraege stehen in
# produktion/motive/README.md, Abschnitt "KI-Clips Video 05" - dort steht der
# Wert aus dem Transaktionsprotokoll, nicht der Vorabpreis. Fuer die Planung
# von V06-V08 gilt der Vorabpreis von Seedance 1.5 Pro (1080p, 12 s), nicht
# der historische Satz von V01-V04.
videoquelle        = ki_clips
# Die Clips gehoeren zum Standbild ihres Videos und sind mit keinem anderen
# Motiv verwendbar. Deshalb je Video ein eigener Ordner; ki_clip_ordner_V<n>
# schlaegt den allgemeinen Wert.
ki_clip_ordner     = produktion/motive/loops/ki
ki_clip_ordner_V1  = produktion/motive/loops/ki
ki_clip_ordner_V2  = produktion/motive/loops/ki-v02
ki_clip_ordner_V3  = produktion/motive/loops/ki-v03
ki_clip_ordner_V4  = produktion/motive/loops/ki-v04
ki_clip_ordner_V5  = produktion/motive/loops/ki-v05
ki_clip_ordner_V6  = produktion/motive/loops/ki-v06

# Kapitelmarken sind je Video entschieden, nicht global: ja bei 01/02/06/08,
# nein bei 03/04/05/07 (Formel §7 fuehrt sie als optional - A's drei groesste
# Treffer haben null). Schritt 6 erzeugt sie immer; nur die hier genannten
# Videos bekommen sie ins Upload-Paket.
#
# Der Nutzen liegt dort, wo viele kurze, in sich geschlossene Einheiten stehen
# und ein Hoerer gezielt springen will: 89 bzw. 61 Psalmen (01, 02) und
# 42 Genesis-Kapitel (08).
#
# 2026-08-31: V6 bleibt in der Liste, die BEGRUENDUNG ist nachgezogen. Sie hing
# an "52 Jesaja-Kapitel"; der Jesaja-Korpus ist gestrichen. V06 liest jetzt
# Rut + 1 Samuel + Ester = 45 Kapitel, gerendert mit 46 Marken (45 Kapitel plus
# "Opening prayer", siehe produktion/video-06/upload.md). Der Nutzen liegt bei
# V06 zusaetzlich darin, dass es DREI eigenstaendige Buecher sind, zwischen
# denen ein Hoerer springen koennen soll - nicht nur darin, dass ein langes
# Buch viele Kapitel hat.
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
# Harte Untergrenze. Unangetastet - kein Video darunter, egal was der Korpus ist.
laufzeit_min_h     = 3.0
# Zielband. 3,4-3,8 h ist der Median der Fremd-Treffer (Formel §2), also eine
# Beobachtung an anderen Kanaelen, keine eigene Messung.
laufzeit_ziel_von_h = 3.4
laufzeit_ziel_bis_h = 3.8
# 2026-09-02: die untere Bandgrenze faellt auf 3,0 h, WENN das dominante Buch
# selbst Erzaehlwerk ist und in voller Laenge im Korpus steht. Grund: Gate 1.13
# und das Band klemmten sich gegenseitig ein - ein ganzes Erzaehlbuch von
# 14.000-18.000 W kam bei 3,4 h nie auf die geforderte Dominanz und fiel an der
# Groesse aus, nicht an seiner Struktur. Sonst bleibt 3,4 h.
#
# ACHTUNG, Nebenwirkung der Strukturfassung von 1.13 (siehe unten): dort ist
# "Erzaehlwerk in voller Laenge" bereits BEDINGUNG. Jeder Korpus, der 1.13
# haelt, bekommt damit automatisch das tiefere Band - die 3,4 h greifen nur
# noch bei Korpora, die ohnehin schon durchgefallen sind. Der Wert bleibt
# stehen, weil er die Bandgrenze der Formel ist und weil eine spaetere
# Rueckkehr zur Prozentfassung ihn wieder wirksam machen wuerde. Wer 3,0 h
# nicht will, hebt laufzeit_ziel_von_h_vollwerk, nicht laufzeit_min_h.
laufzeit_ziel_von_h_vollwerk = 3.0

# --- Schwellen Gate 1.13 / Regel M8 ---
# DIES IST DIE EINZIGE STELLE, an der diese Schwellen stehen.
# produktion/erzaehlanteil.py und produktion/korpus_pruefung.py lesen sie hier;
# produktion/workflow-gates.md und regeln/erfolgsregeln.md verweisen hierher.
#
# ENTSCHIEDEN 2026-09-02: Gate 1.13 ist die STRUKTURFASSUNG. Es prueft die
# Bauart des Korpus, nicht seinen Prozentwert:
#     dominantes Buch >= gate_dominanz_min der Woerter
#     UND dieses Buch ist selbst Erzaehlwerk (>= gate_erzaehlanteil_min,
#         kapitelweise gemessen)
#     UND es steht in voller Laenge im Korpus
#     UND es liegt >= gate_abstand_min vor dem zweitgroessten Buch
# Der Erzaehlanteil des GESAMTEN Korpus wird weiterhin kapitelweise gemessen
# und gemeldet - er gatet nicht. Grund: die 80 % sind von keiner eigenen
# Messung beruehrt (V01-V05 liegen bei 0,0-47,6 %), und V03, das einzige
# Video des Kanals, das funktioniert hat, faellt in jeder Messung durch.
# Belegt ist die STRUKTUR - Evangelium gegen Spruchsammlung -, nicht 80 gegen 79.
#
# gate_erzaehlanteil_min ist damit die Schwelle EINER Ja/Nein-Frage: ist das
# dominante Buch ueberhaupt Erzaehlwerk. In dieser Rolle ist sie belastbar -
# dass 1 Samuel Erzaehlung ist und Jesaja nicht, haengt nicht an der Koernung.
gate_erzaehlanteil_min = 0.80
# Dominanz: 2026-09-02 von 0,60 auf 0,50 gesenkt. Die 60 % waren selbstgesetzt
# und durch nichts belegt - sie sollten sichern, dass ein Eigenname aus dem
# dominanten Buch Titel und Thumbnail tragen kann. Das traegt er bei 50 % genauso.
gate_dominanz_min      = 0.50
# Mindestabstand des dominanten Buchs zum zweitgroessten, in Anteilspunkten
# des Korpus. NEU am 2026-09-02, entschieden vom Kanalinhaber.
#
# Warum: die Dominanzschwelle allein sagt nur, dass EIN Buch ueber der Haelfte
# liegt - nicht, dass es die Hauptsache ist. Bei 50,1 gegen 45,0 verkauft der
# Eigenname im Titel und auf dem Thumbnail ein Buch, das knapp die Haelfte der
# Laufzeit traegt; der Hoerer bekommt zur anderen Haelfte etwas anderes.
# 15 Punkte heisst: das dominante Buch traegt mindestens die Haelfte, und der
# zweite hoechstens gut ein Drittel.
#
# Gemessen, bevor die Schwelle festgeschrieben wurde - zwei Bezugsmengen, beide
# richtig, sie zaehlen nicht dasselbe:
#   gegen die 50 Korpora der Prozentfassung (Stand vor dem 02.09.):
#       neun fallen weg, 41 bleiben.
#   gegen die 50 Korpora der Strukturfassung (Stand danach):
#       fuenf fallen weg, 45 bleiben - das ist der Inhalt von
#       produktion/korpus/v07_v08_moeglichkeiten.json.
# Der knappste ausgeschiedene Fall lag bei 9,9 Punkten (Genesis 55,0 % gegen
# Markus 45,0 %), der knappste gehaltene bei 15,6.
# Fuer V07 und V08 bleibt in beiden Rechnungen reichlich uebrig; die Schwelle
# musste nicht aufgeweicht werden.
gate_abstand_min       = 0.15
# Wo die Erzaehlnaehte stehen. Ein geteiltes Buch qualifiziert seit dem
# 2026-09-02 als dominantes Erzaehlwerk, wenn ZWEI Bedingungen zusammen gelten:
#   1. jede offene Kante des gelesenen Bereichs liegt an einer Naht, die in
#      dieser Datei mit ist_naht=true UND einer Begruendung steht
#      (Buchanfang und Buchende sind keine offenen Kanten),
#   2. der gelesene Teil haelt fuer sich gate_erzaehlanteil_min.
# Sonst gilt weiter: volles Buch.
#
# Die Datei ist die einzige Quelle fuer Naehte; erzaehlanteil.py und
# korpus_pruefung.py lesen den Pfad hier. Eine Naht, die nicht drinsteht, zaehlt
# nicht - damit bleibt Wegschneiden zur Laufzeitanpassung ausgeschlossen. Wer
# eine Naht braucht, traegt sie mit Begruendung ein und entscheidet damit
# sichtbar, statt eine Zahl passend zu machen. Verworfene Nahtstellen stehen mit
# ist_naht=false ebenfalls drin, damit sie nicht zweimal vorgeschlagen werden.
erzaehlnaehte_datei    = produktion/korpus/erzaehlnaehte.json

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
