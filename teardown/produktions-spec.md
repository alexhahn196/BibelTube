# Produktions-Spec: englischer Einschlafgebet-Kanal

Abgeleitet aus der Vermessung von 8 Konkurrenzkanälen (24 Videos als Top/Median/Flop)
plus der vollständigen Videoliste dieser Kanäle (454 Videos mit Views und Laufzeit).

Stand: 2026-08-02. Rohdaten im selben Ordner:
`teardown_batch_20260802_090410/matrix_voll.csv`, `auswertung_matrix.txt`,
`auswertung_population.txt`, `thumbs/`, `sheet_TOP|MEDIAN|FLOP.png`.

---

## 0. Datengrundlage — was wirklich gemessen wurde

Das ist wichtig, weil zwei Spalten der Matrix **nicht** so entstanden sind wie im Skript vorgesehen.

| Messgröße | Quelle | Abdeckung |
|---|---|---|
| Views, Likes, Laufzeit, Titel | yt-dlp + unabhängige API | 24/24 |
| Tags, Untertitel-Spur, Kategorie | yt-dlp (5) + unabhängige API (9) | **14/24**, alle 8 Kanäle |
| Auflösung, fps | yt-dlp | **5/24** — schwächster Teil |
| `sprache_bis_pct` | **exakt aus Caption-Zeitstempeln** | 24/24 |
| Bildkonzept | multimodale Videoanalyse, 11 Stichproben | 7/8 TOP, 4/8 FLOP |
| Thumbnails | i.ytimg.com | 24/24 |

Zwei Abweichungen vom Skript-Plan, beide bewusst:

1. **Der Medien-Download war unmöglich.** YouTube liefert an die Egress-IPs dieser
   Maschine keine Video-/Audio-Bytes aus (403 auf allen `googlevideo`-URLs, über
   jeden Player-Client, IPv4 wie IPv6; Metadaten und Thumbnails gehen). Ursache ist
   nicht das Skript. Damit entfallen `frames/` und die Audio-Messung. Die
   `visuell`-Spalte im Original-`matrix.csv` steht deshalb auf dem Startwert
   `statisch` — **dieser Wert ist keine Messung und darf nicht gelesen werden.**
2. **`sprache_bis_pct` wurde ersetzt, nicht geschätzt.** Das Skript hätte die
   Sprechdauer aus fünf 15-Sekunden-Stichproben über Peak-minus-RMS geschätzt.
   Stattdessen sind es jetzt Caption-Zeitstempel auf Millisekunden-Ebene über die
   volle Laufzeit — für die Frage nach den TTS-Kosten die deutlich belastbarere Zahl.
   Die Werte in `matrix_voll.csv` sind diese, nicht die des Skripts.

Ebenfalls beachten: nach ca. 5 Videos hat YouTube die Metadaten-Abfragen dieser
Maschine mit 429 abgewiesen. Deshalb die zweite Quelle. Ein erneuter Lauf von
einer normalen Wohn-IP würde `matrix.csv` vollständig füllen (Skript und
`refill_metadata.sh` liegen bereit).

---

## a) UNTERSCHEIDER — was Top von Flop trennt

**Nur ein Faktor trägt: das Thema.** Alles andere hält der Prüfung nicht stand.

Der Nachweis kommt aus der Grundgesamtheit, normiert auf den jeweiligen
Kanal-Median (roher Kanalvergleich ist durch die Kanalgröße verzerrt):

| Kanal | Median | größter Treffer | Faktor | Thema des Treffers |
|---|---|---|---|---|
| SleepCodex | 3.200 | 883.000 | **276x** | Book of Enoch, "Banned from the Bible" |
| Rest in Grace | 1.300 | 165.000 | **127x** | "No More Thinking Tonight… Rest With Jesus" |
| Night Psalms | 8.700 | 551.000 | **63x** | Book of Enoch COMPLETE |
| Grace Beyond Prayer | 25.500 | 1.000.000 | **39x** | "I Am Here—You're Not Alone" |
| Rest In Faith | 24.000 | 773.000 | **32x** | Isaiah, "Like Never Before" |
| The Sleep Bible | 184.000 | 1.900.000 | **10x** | Gospel of John |

Produktion, Auflösung, Stimme, Klangbett sind innerhalb eines Kanals konstant —
die Spanne von 276x entsteht **allein** aus Thema, Titel und Thumbnail.

Themen-Effekte innerhalb des Kanals (nur Kanäle mit ≥4 Videos je Stichwort):

- `enoch`: **2,33x** (SleepCodex, n=40), **33x** (Night Psalms, n=4)
- `banned`: **2,02x** (SleepCodex, n=40)
- `gospel`: **3,33x** (Rest In Faith, n=20), **2,84x** (The Sleep Bible, n=6)
- `john`: **3,04x** (Rest In Faith, n=5)
- `angel`: **6,90x** (Night Psalms, n=8), 1,38x (SleepCodex, n=25)
- `psalm`: **0,26x / 0,76x / 1,38x** — kein Effekt, in zwei von drei Kanälen negativ
- `jesus`: 0,31x bis 3,33x über sieben Kanäle — **unbrauchbar als Signal**

Achtung, hier steckt eine Falle: Über alle 454 Videos gerechnet liegt `enoch` bei
**0,79x** und sähe wie ein Verlierer aus. Das ist ein Kanal-Confounder — SleepCodex
hat einen sehr niedrigen Kanal-Median, seine 40 Enoch-Videos drücken den globalen
Median, obwohl sie ihren eigenen Kanal um Faktor 2,33 schlagen. **Nur die
kanal-normierte Zahl ist gültig.**

**Thumbnail** (Kontaktbögen `sheet_TOP.png` vs `sheet_FLOP.png`): TOP zeigt
durchgehend hohen Kontrast, große fette Versalien, dunkle Nachtszene mit einer
warmen Lichtquelle. FLOP zeigt dünne Serifen, kleinen Text, flauere Helligkeit
(z. B. Grace Beyond Prayer TOP in Gelb/Cyan/Rot gegen FLOP in gedecktem Grau mit
Mini-Signatur — gleicher Kanal, gegensätzliche Bildsprache). Das ist ein klarer
optischer Befund, aber ich habe ihn **nicht** quantifiziert; 8 Bildpaare sind zu
wenig, um einen Kontrastwert als Zielgröße festzuschreiben.

### Was NICHT unterscheidet, obwohl es plausibel klingt

**Laufzeit — der wichtigste Negativbefund.** In den 24 Stichproben sieht es
eindeutig aus: TOP-Median 3,71 h gegen FLOP-Median 1,39 h, und in 7 von 8 Kanälen
ist das TOP-Video länger. Gegen die Grundgesamtheit geprüft bricht das zusammen:

- Spearman rho(Dauer, Views) über alle 454 Videos: **+0,09**
- pro Kanal: +0,72 / +0,47 / +0,43 / +0,39 / −0,01 / −0,02 / −0,07 / −0,33
  → 4 positiv, 4 null oder negativ
- die beiden größten Kataloge (SleepCodex n=131, Rest In Faith n=120) liegen bei rho ≈ 0
- Laufzeiten der größten Treffer: 1,9 h / 2,0 h / 2,1 h / 2,3 h / 3,0 h / 3,4 h /
  4,0 h / 6,7 h / 9,0 h — kein Optimum erkennbar

Der Top/Flop-Kontrast ist ein **Auswahleffekt**: Das Flop-Video ist per Definition
das schwächste, und schwache Videos sind in diesen Kanälen zufällig kürzer. Länge
kaufen bringt keine Views.

Was bleibt, ist eine **Untergrenze**: Videos unter 1,5 h liegen in 3 von 4
testbaren Kanälen deutlich zurück (Faktor 6,4x / 4,9x / 7,1x zugunsten der langen
Gruppe) — bei Rest In Faith aber umgekehrt (0,53x). Also: nicht unter 1,5 h gehen,
darüber ist Länge keine Stellschraube.

Ebenfalls kein Unterscheider: Auflösung, fps, Tags, Untertitel, Sprechanteil,
Sprechtempo, Kategorie — siehe (b).

---

## b) IRRELEVANTES — bei Top und Flop gleich

| Wert | Befund | Belegt an |
|---|---|---|
| `sprache_bis_pct` | 98,6–100 % — überall | 24/24 |
| Sprechanteil netto | 97,3–100 % — überall | 24/24 |
| Sprechtempo | TOP 121–160 WPM, FLOP 119–175 WPM | 24/24 |
| Untertitel-Spur | **NEIN in 8 von 8 Kanälen** | 14 Videos, alle Kanäle |
| Kategorie | People & Blogs (6), Education (2) — kein Muster | 14/24 |
| Like-Rate | TOP 1,89 % < MEDIAN 1,98 % < **FLOP 3,36 %** | 14/24 |

Die **Like-Rate ist invertiert** und darf keine Zielgröße sein. Flops werden fast
nur von Stamm-Abonnenten gesehen, die eher liken; Hits laufen über kalten Traffic
mit niedrigerer Like-Quote. Eine hohe Like-Rate ist hier ein Symptom für geringe
Reichweite, nicht für Qualität.

**Tags** sind bei den Kanälen, wo ich alle drei Rollen habe, in *allen* Rollen
gesetzt (Grace Beyond Prayer, The Sleep Bible: TOP=JA, MEDIAN=JA, FLOP=JA). Sie
trennen also nicht. Drei Kanäle verzichten ganz darauf, darunter Night Psalms mit
**551.916 Views bei null Tags** und Rest in Grace mit 165.774 Views bei null Tags.

**Auflösung und fps** kann ich nur für 5 Videos belegen (1920x1080 @ 24/25/30 fps,
einmal 3840x2160 @ 30). Das reicht nicht für eine Aussage. Was ich sagen kann: Der
4K-Wert steht beim 1.025.839-Views-Video von Grace Beyond Prayer, aber `4k` im
Titel bringt bei SleepCodex nur **1,20x** (n=16) — 4K ist kein Verkaufsargument.

---

## c) LAUFZEIT DER STIMME — die Antwort ist eindeutig

**Die Erzählstimme läuft durch. Über die volle Laufzeit, in allen 24 Videos, ohne
Ausnahme.** Gemessen an Caption-Zeitstempeln, nicht geschätzt:

- letzter Sprecheinsatz bei **98,6–100 %** der Laufzeit (Median 100,0 %)
- Netto-Sprechanteil **97,3–100 %** der Laufzeit
- Sprechbeginn nach **0,0–7,8 s**
- längste Pause im ganzen Video: **0,2–16,7 s** (Median 1,3 s)

Es gibt in dieser Nische **kein** Modell "Stimme hört nach der Hälfte auf, Ambient
läuft weiter". Auch nicht bei den 10-Stunden-Formaten (ZXgtJSgIvto: 10,00 h,
Sprache bis 99,9 %, Sprechanteil 97,3 %).

### TTS-Budget — direkt kalkulierbar

Sprechtempo Median **141 WPM**, Median **46.428 Zeichen pro Stunde**:

| Videolänge | Zeichen TTS | Wörter |
|---|---|---|
| 2 h | ~92.900 | ~16.900 |
| 3 h | ~139.300 | ~25.400 |
| 4 h | ~185.700 | ~33.900 |

Plane mit **~46.500 Zeichen pro Stunde Video**. Bei 2–4 h sind das 93k–186k Zeichen
pro Video — das ist die Kostenbasis, es gibt keine Abkürzung über eine kürzere
Sprechspur.

Ein Spartipp aus den Daten: Mehrere Top-Videos wiederholen denselben Text.
`rbZHUqXDHHc` (1,9 Mio. Views, 6,67 h) enthält laut eigener Kapitelliste **drei
Durchläufe** desselben Johannes-Evangeliums (0:02:44, 2:26:10, 4:28:20). Das sind
6,67 h Laufzeit für ~2,2 h TTS. Legitimes Muster in der Nische und ein Drittel der
Kosten.

---

## d) BILDKONZEPT

Die `frames/` sind leer (siehe Abschnitt 0). Grundlage sind stattdessen 11
multimodale Stichproben aus dem laufenden Video (7 der 8 TOP-Videos, 4 FLOPs),
jeweils 60–120 s, plus alle 24 Thumbnails.

**Standbild oder Bewegung? — Nie ein echtes Standbild.** In 11 von 11 Stichproben
gibt es Bewegung, aber immer *ruhige* Bewegung: flackerndes Feuer, driftende
Wolken, funkelnde Sterne, schwebende Partikel, langsamer Zoom, leichte Parallaxe.
Zwei Bauformen:

- **Ein-Szenen-Loop, keine Schnitte** — Hush Little Lamb, The Sleep Bible,
  Rest In Faith, Rest in Grace (5 der 11 Stichproben)
- **Szenenfolge mit Schnitten** — Grace Beyond Prayer ~25 s, SleepCodex 10–20 s,
  Night Psalms ~35 s. Der Ausreißer nach unten ist ein **FLOP**: Grace Beyond
  Prayer schneidet dort alle **3–5 s** durch einen Marktplatz — deutlich unruhiger
  als alles andere im Sample.

Beides funktioniert. Sehr schnelle Schnitte tauchen im Sample nur beim Flop auf —
bei n=1 ist das ein Hinweis, kein Beweis.

**Bildaufbau.** Ein Motiv, groß, mittig oder leicht links, im unteren bis mittleren
Drittel; darüber ein weiter Nachthimmel, der die oberen zwei Drittel füllt.
Wiederkehrend eine warme Lichtquelle im Bild (Lagerfeuer, erleuchtetes Fenster,
Mond) gegen kalten Hintergrund.

**Farbpalette — bemerkenswert einheitlich.** Tiefes Blau und Schwarz für Himmel und
Wasser, dagegen warmes Orange/Gold/Gelb aus der Lichtquelle. Hoher Kontrast,
satte Farben, insgesamt dunkles Bild. Abweichungen: SleepCodex (TOP) arbeitet in
Gold/Braun/Weiß mit Lichtstrahlen, Night Psalms (TOP) in entsättigtem Braun/Grau —
beides ebenfalls dunkel und kontrastreich.

**Text im Bild.**

- **Eingebrannte Untertitel** in 6 der 11 Stichproben, weiß, zentriert, unteres
  Drittel; teils als Versalien (Grace Beyond Prayer), teils gemischt.
- **Kanal-Wasserzeichen** in 6 der 11: "HLL" unten rechts, "SLEEP BIBLE" oben links,
  "SLEEPCODEX", "Night Psalms" unten rechts.
- **Fortschrittsbalken ins Bild gerendert** bei Grace Beyond Prayer, SleepCodex,
  Night Psalms (3 von 11).
- Kapitelzeilen im Bild bei The Sleep Bible ("Chapter 6: The Verdict Was Illegal")
  und SleepCodex.
- SleepCodex blendet zeitweise Like/Share/Subscribe-Icons ein.

**Wiederkehrende Motive.** Das mit Abstand häufigste: **schlafender Jesus mit Lamm
am Lagerfeuer unter Sternenhimmel** — bei drei verschiedenen Kanälen fast
identisch (Hush Little Lamb, Rest in Grace, plus im Thumbnail bei Hush Little
Lamb FLOP). Weiter: Mond und Sternenhimmel (fast überall), Wasser mit Spiegelung,
Lagerfeuer, aufgeschlagenes Buch, einsame Hütte, Engel.

**Ein Befund zur Produktionsqualität, der die These aus (a) stützt:** Das
erfolgreichste Video im ganzen Sample — `rbZHUqXDHHc`, The Sleep Bible, **1,9 Mio.
Views** — zeigt bei ca. 87 % der Laufzeit (Sekunde 21.000) eine Strecke **reinen
grünen Greenscreens**, ohne Bild, ohne Text. Bei Sekunde 9.000 und 22.500 läuft
dieselbe Datei wieder als normale illustrierte Szene. Das ist ein grober
Produktionsfehler in einem Millionen-Video. Bildpolitur ist nicht der Hebel.

---

## e) METADATEN — wo die Lücken sind

| Kanal | Tags | Untertitel-Spur |
|---|---|---|
| Hush Little Lamb | **NEIN** (alle 3 Rollen) | NEIN |
| Grace Beyond Prayer | JA (alle 3 Rollen, ~25) | NEIN |
| The Sleep Bible | JA (alle 3 Rollen, 25–30) | NEIN |
| Rest in Jesus | JA (31) | NEIN |
| Rest In Faith | JA (26) | NEIN |
| SleepCodex | JA (14) | NEIN |
| Night Psalms | **NEIN** (0 Tags bei 551.916 Views) | NEIN |
| Rest in Grace | **NEIN** (0 Tags bei 165.774 Views) | NEIN |

**Tags: 5 von 8 Kanälen.** Aber Tags trennen Top nicht von Flop (dort wo alle drei
Rollen belegt sind, haben alle drei Tags), und zwei der drei tag-losen Kanäle haben
Videos im sechsstelligen Bereich. Tags sind Hygiene, kein Hebel.

**Untertitel-Spur: 0 von 8 Kanälen.** Das ist die auffälligste Lücke im ganzen
Datensatz — vollständig unbesetzt. Gleichzeitig brennen 6 der 11 Stichproben
Untertitel **ins Bild**. Der Bedarf ist also da und wird bedient, aber auf die
Art, die YouTube nicht lesen kann: kein durchsuchbarer Text, keine automatische
Übersetzung, keine Barrierefreiheit, kein Nutzen für die Empfehlung.

**Besetzbare Lücken, nach Aufwand-Ertrag:**

1. **Echte Untertitelspur (.srt) hochladen** — 8 von 8 Kanälen lassen das liegen.
   Aus deinem TTS-Skript fällt der zeitgestempelte Text ohnehin ab; die Datei
   kostet dich fast nichts. Zusätzlich übersetzte Spuren (ES, PT, TL) — die
   Nische ist englischsprachig, aber das Publikum ist es nur teilweise.
2. **Tags setzen**, wenn du sowieso 3 von 8 Konkurrenten dort schlägst. Geringer
   Effekt, aber Kosten nahe null.
3. **Kapitelmarken in der Beschreibung** — machen bereits The Sleep Bible,
   Rest in Jesus, Rest In Faith, SleepCodex, Night Psalms, Rest in Grace. Das ist
   *keine* Lücke, sondern Standard; wer es weglässt, fällt auf.

---

## Produktionsvorgaben für deine Pipeline

### Video

| Größe | Zielwert | Begründung |
|---|---|---|
| Laufzeit | **2,5–3,5 h** | Untergrenze 1,5 h belegt; darüber kein Effekt (rho +0,09). Der Bereich hat die meisten Treffer bei geringsten Kosten. Nicht über 4 h, ohne dass die Views es rechtfertigen. |
| Auflösung | **1920x1080** | Nur 5 Videos belegt (4x 1080p, 1x 4K). 4K ist nicht nachweisbar besser, `4k` im Titel bringt 1,20x. Kein Grund für die vierfache Renderzeit. |
| fps | **24–30** | Belegt: 24, 25, 30 — ohne erkennbaren Unterschied. Nimm 24 für kleinere Dateien; das Bild bewegt sich kaum. |
| Bewegung | **Langsamer Loop, kein Standbild** | 11/11 Stichproben haben Bewegung. Feuer, Partikel, Wolkendrift, langsamer Zoom. |
| Schnitte | **entweder gar keine, oder alle 20–35 s** | Beide Bauformen liefern Top-Videos. Unter 10 s nicht gehen. |

### Sprache / TTS

| Größe | Zielwert |
|---|---|
| Sprache läuft bis | **100 % der Laufzeit** — durchgehend, keine stille zweite Hälfte |
| Sprechbeginn | **innerhalb der ersten 5 s** (Sample: 0,0–7,8 s) |
| Sprechtempo | **135–145 WPM** (Sample-Median 141) |
| längste Pause | **unter 20 s** |
| TTS-Budget | **~46.500 Zeichen je Stunde Video** → 3 h ≈ 139.000 Zeichen |
| Kostenhebel | Text 2–3x wiederholen statt 3 h Unikat-Text — belegt beim 1,9-Mio.-Video |

### Bild

- Ein großes Motiv, mittig/leicht links, unteres bis mittleres Drittel
- Nachthimmel füllt die oberen zwei Drittel
- **Eine warme Lichtquelle im Bild** (Lagerfeuer, Fenster, Mond) gegen kalten Hintergrund
- Palette: tiefes Blau/Schwarz + Orange/Gold, hoher Kontrast, dunkles Gesamtbild
- Untertitel weiß, zentriert, unteres Drittel — ins Bild gerendert
- Kanal-Wasserzeichen klein in einer Ecke, halbtransparent
- Sicheres Motiv-Set: schlafende Figur mit Lamm am Feuer, Mond und Sterne,
  Wasserspiegelung, aufgeschlagenes Buch, einsame Hütte

Zum Motiv "schlafender Jesus mit Lamm am Lagerfeuer": Es funktioniert bei drei
Kanälen und ist sofort als Nische erkennbar — aber es ist auch bereits dreifach
besetzt. Das ist eine Positionierungsentscheidung, keine Datenfrage; die Daten
sagen nur, dass es nicht schadet.

### Metadaten

- **Untertitel-Spur (.srt) immer hochladen** — einzige echte Lücke, 0 von 8
- 15–30 Tags setzen
- Kapitelmarken in die Beschreibung (Standard, kein Vorteil, aber Pflicht)
- Kategorie: egal (People & Blogs und Education liefern beide Hits)

### Titel — hier liegt der ganze Hebel

- **Ein konkretes, benennbares Thema in den Titel**, nicht nur Stimmung.
  Alle Treffer über 20x tragen einen Eigennamen: *Gospel of John, Isaiah, Daniel,
  Book of Enoch, Sermon on the Mount*. Reine Stimmungstitel funktionieren nur bei
  Grace Beyond Prayer und Rest in Grace, und auch dort mit klarer Zuspitzung
  ("I Am Here—You're Not Alone", "No More Thinking Tonight").
- Belegte Verstärker innerhalb des Kanals: `gospel` 2,8–3,3x, `john` 3,0x,
  `angel` 1,4–6,9x, `enoch` 2,3x, `banned` 2,0x
- Belegte Nieten: `psalm` 0,26–1,38x, `jesus` 0,31–3,33x (streut zu stark),
  `4k` 1,20x
- Thumbnail dazu: große fette Versalien, hoher Kontrast, dunkle Nachtszene mit
  einer warmen Lichtquelle

### Was NICHT optimiert werden soll

- **Like-Rate** — invertiert, hohe Werte bedeuten wenig Reichweite
- **Länge über 4 h** — kein Zusammenhang mit Views (rho +0,09)
- **4K** — nicht nachweisbar besser
- **Bildpolitur** — das 1,9-Mio.-Video hat einen Greenscreen-Fehler im laufenden Bild

---

## Wo die Daten keine Antwort geben

Ausdrücklich offen, nicht geraten:

1. **Auflösung und fps.** Nur 5 von 24 Videos belegt. Die Empfehlung 1080p/24–30
   stützt sich auf diese fünf plus das Fehlen eines 4K-Effekts im Titel. Ein
   erneuter Lauf von einer Wohn-IP schließt die Lücke.
2. **Tags und Untertitel für 10 der 24 Videos** (jeweils MEDIAN und FLOP der
   Kanäle 4–8). Die Kanal-Aussage in (e) steht auf je einem TOP-Video bei
   Rest in Jesus, Rest In Faith, SleepCodex, Night Psalms, Rest in Grace.
3. **Klangbett.** Vollständig ungemessen. Die Audio-Analyse war Teil des
   blockierten Downloads. Delta-Wellen gegen Piano+Regen — dazu sagen diese Daten
   nichts. Nur aus Beschreibungen ablesbar: Rest in Jesus nennt "piano and rain".
4. **Thumbnail-Kontrast als Zahl.** Der optische Unterschied Top/Flop ist deutlich,
   aber 8 Bildpaare tragen keinen Schwellenwert.
5. **Schnittfrequenz als Hebel.** Der 3–5-s-Schnitt liegt beim Flop, aber n=1.
6. **Warum die Enoch-Videos gewonnen haben.** Innerhalb ihrer Kanäle wirkt das
   Thema (2,3x bei n=40), aber die 276x- und 63x-Ausreißer sind Einzelereignisse.
   Ob das reproduzierbar ist oder ein Algorithmus-Zufall war, lässt sich aus
   Views-Zahlen allein nicht entscheiden — dafür bräuchte es Impressions und
   CTR aus YouTube Analytics.
7. **Upload-Frequenz und Kanalalter** als Faktoren — nicht Teil der Messung.
