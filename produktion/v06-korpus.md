# Video 06 — drei Korpusvarianten nach Regel M8

> **Stand: 2026-08-30.** Der bisherige V06-Korpus (Jesaja 1–25 + 40–66 + Daniel 4–6)
> ist gestrichen: 10,2 % Erzählanteil, reißt Gate 1.13 / Regel M8.
> Alle Wortzahlen sind **gemessen**, nicht geschätzt — gleiche Abrufquelle und
> gleiche Zählmethode wie [`produktion/wortzahlen.py`](wortzahlen.py)
> (bible-api.com, `translation=webbe`, Verstexte mit Leerzeichen verbunden, dann
> `str.split()`), damit die Zahlen mit V01–V05 vergleichbar bleiben.
> Erzeugt und nachrechenbar mit [`produktion/erzaehlanteil.py`](erzaehlanteil.py)
> (Rückgabewert 0 = alle drei Varianten bestehen Zielband, 80-%-Gate und Dominanz).
> Rohdaten: [`korpus/erzaehlanteil.json`](korpus/erzaehlanteil.json) (250 Kapitel
> einzeln eingestuft) und [`korpus/v06_varianten.json`](korpus/v06_varianten.json).
> **`plan.json` ist unverändert.** Kein Titel, kein Gebet, kein Thumbnail, kein TTS,
> kein Rendering.

**Vorgaben, gegen die gerechnet wurde:** Erzählanteil ≥ 80 % der Wörter · Zielband
30.215–33.767 W (3,4–3,8 h bei 148,1 WPM) · ein dominantes Buch ≥ 60 % der Wörter ·
ganze Bücher bevorzugt, Schnitte nur an Erzählnähten.

---

## Vergleich

| Variante | Korpus | Wörter | Erzählanteil | Laufzeit | dominantes Buch | Nachttauglichkeit *(Einschätzung, keine Messung)* | was danach für V07+ übrig bleibt |
|---|---|---:|---:|---:|---|---|---|
| **V06-A**<br>Anthologie | 1 Samuel 1–31 + Rut 1–4 + Ester 1–10 | 31.482 | **89,03 %** | 3:33 h | **1 Samuel** (75 %) | Rut ist der ruhigste Stoff im ganzen Vorrat. Gegen den Zweck: 1 Sam 15 (Bann an Amalek), 17 (Enthauptung), 18,25–27 (zweihundert Vorhäute), 22 (85 erschlagene Priester), 28 (Totenbeschwörerin), 31 (Selbstmord, Leichenschändung), Ester 9 (75.000 Erschlagene). Alles im Mittelteil. | 170.132 W. **Apostelgeschichte bleibt ganz frei** — das einzige noch unverplante NT-Buch. Dazu 2 Samuel, beide Königsbücher, Josua, Richter, Exodus, Jona, Daniel 4–12, Genesis 43–50. **Kein Torso.** |
| **V06-B**<br>Lebensbogen | 1 Samuel 16–31 + 2 Samuel 1–24 | 31.929 | **88,55 %** | 3:36 h | **2 Samuel** (61 %) | Die schwerste Stelle im ganzen Vorrat: 2 Sam 13 (Vergewaltigung Tamars) ist um 2 Uhr nachts nicht zumutbar. Dazu 2 Sam 4, 11, 12, 18, 21 und aus dem ersten Teil 1 Sam 17, 22, 28, 31. Der Stoff wird nach hinten **düsterer statt ruhiger**. | 169.685 W, davon **1 Samuel 1–15 als Torso** (11.156 W: Eli, Samuels Berufung, Sauls Aufstieg — ohne Fortsetzung zu kurz). Apostelgeschichte, Königsbücher, Josua, Richter, Exodus, Rut, Ester, Jona, Daniel 4–12, Genesis 43–50 frei. |
| **V06-C**<br>AT + NT | Apostelgeschichte 1–12 + 1 Samuel 1–31 | 33.460 | **83,63 %** | 3:46 h | **1 Samuel** (71 %) | Apg 1–12 ist der ruhigste NT-Stoff im Vorrat; kritisch dort nur Apg 5 (Hananias und Saphira), 7,54–60 (Steinigung), 12 (Enthauptung, Herodes von Würmern gefressen). Der 1-Samuel-Teil bringt dieselben Stellen wie V06-A mit. | 168.154 W, davon **Apostelgeschichte 13–28 als Torso** (13.321 W: die Paulusreisen ohne Anfang). 2 Samuel, Königsbücher, Josua, Richter, Exodus, Rut, Ester, Jona, Daniel 4–12, Genesis 43–50 frei. |

Alle drei bestehen alle drei Gates. Die Nachttauglichkeits-Spalte ist ausdrücklich
**keine Messung** — sie benennt Stellen, von denen ich annehme, dass sie gegen den
Zweck arbeiten. Es gibt dazu keine eigenen Kanaldaten.

---

## Je Variante

**V06-A — 1 Samuel + Rut + Ester.**
*Stark:* höchster Erzählanteil der drei und drei vollständige Bücher ohne einen
einzigen Schnitt — es bleibt kein Torso für später übrig, und der Vorrat für V07+
ist der größte. Drei abgeschlossene Geschichten mit je eigenem Ende geben dem
Nachthörer drei Ruhepunkte statt eines.
*Risiko:* der Eigenname „Samuel" trägt den Titel schwächer als „David" oder
„Esther", und die drei Bücher haben außer der Richterzeit keine gemeinsame
Klammer — als Serie erzählt das Video drei Dinge statt einem.

**V06-B — 1 Samuel 16–31 + 2 Samuel (Davids Leben).**
*Stark:* ein einziger durchlaufender Erzählbogen von der Salbung bis zum Tod, ohne
Themenwechsel — formal am nächsten an V03 (Johannes), also an dem Video, aus dem
Regel M8 überhaupt stammt. „David" ist der stärkste Eigenname im ganzen Vorrat.
*Risiko:* die Dominanz liegt mit 60,9 % nur knapp über der Grenze, und der Buchname
„Second Samuel" taugt nicht als Titelwort — der Korpus läuft faktisch unter „David",
also unter einem Personennamen statt einem Buchnamen. Dazu die Nachtproblematik
oben, die hier die schwerste der drei ist.

**V06-C — Apostelgeschichte 1–12 + 1 Samuel.**
*Stark:* die einzige Variante mit NT-Anteil, die das Gate hält, und mit 33.460 W die
längste; Apg 1–12 endet mit einer echten Schlusskadenz (Tod des Herodes, „das Wort
Gottes wuchs und mehrte sich"), ist also kein abgeschnittener Torso, sondern eine
erzählerisch geschlossene Hälfte.
*Risiko:* mit 83,63 % der niedrigste Erzählanteil — Apg 1–12 trägt selbst nur 70,6 %,
weil Pfingstpredigt, Tempelrede und Stephanusrede darin liegen. Der Sprung zwischen
Jerusalem und der Richterzeit hat keine erzählerische Brücke, und bei dem Tempo, das
`config.md` erwartet (145,9 WPM), läuft die Variante auf **3,82 h** und damit knapp
über das Zielband.

---

## Was nicht geht: ein NT-geführter Korpus

Es gibt **keine Variante mit der vollständigen Apostelgeschichte als dominantem Buch,
die Zielband und 80-%-Gate gleichzeitig hält.** Die Zahlen:

- Apostelgeschichte gesamt: **23.143 W, davon 16.890 erzählend = 73,0 %.** Der Rest
  sind Pfingst-, Tempel-, Stephanus-, Areopag-, Abschieds- und Verteidigungsreden
  sowie zwei eingelegte Briefe. Fünf Kapitel liegen unter 40 % (Apg 3, 7, 22, 24, 26),
  Apg 2 bei 45 %.
- Damit das Gate hält, müsste der übrige Korpus bei voller Bandausschöpfung
  (10.624 W) **mindestens 95,3 % Erzählanteil** tragen — oder, bei reinem
  Erzählstoff ohne jeden Abzug, **mindestens 8.122 W**. Die reinsten ganzen Bücher im
  Vorrat sind Rut (95,4 %), Jona (86,4 %) und Ester (86,1 %) — zusammen 9.116 W bei
  88,6 %. Das reicht in beiden Richtungen nicht.
- Bester tatsächlich erreichbarer Wert im Band: **79,76 % bei 33.620 W**
  (Apostelgeschichte + Jona + 1 Könige 17–22 + Richter 13–16). Es fehlen **80
  erzählende Wörter**. Diese Kombination stützt sich außerdem auf zwei Buchfragmente,
  die die Gegenprüfung (siehe unten) nicht durchlaufen haben — der wahre Wert liegt
  eher darunter.
- Apostelgeschichte + Rut + Ester + Daniel 4–6 käme auf 34.107 W und liegt damit
  **340 W über dem Band** — und trüge nur 76,6 %.

Acts-dominante Kombinationen bestehen nur, wenn man die Apostelgeschichte vorn
abschneidet (ab Apg 3, 4, 6 oder 7). Das ist keine Erzählnaht, sondern ein Schnitt am
Wortzähler entlang: das Video begönne mitten in der Handlung und ohne Pfingsten.
Deshalb steht keine solche Variante hier. **V06-C ist der einzige Weg, das NT
überhaupt in V06 zu bekommen** — als Nebenstoff, nicht als Titelgeber.

Ebenfalls ausgeschieden, weil sie die 60-%-Dominanz im Band gar nicht erreichen
können: Josua (17.835 W) und Richter (17.922 W) — beide zu klein, um in einem
30.000-W-Korpus auf 60 % zu kommen. Und Exodus scheitert am Gate selbst: **46,5 %**
(Exodus 20–31 und 35–40 sind Gesetz, Kult- und Bauvorschrift), 1 Könige an **58,9 %**
(Tempelbau Kap. 6–7, Weihgebet Kap. 8), Daniel 4–12 an **27,2 %** (Kap. 7–12 sind
apokalyptische Vision).

---

## Wie eingestuft wurde

Regel (Wortlaut der Vorgabe): erzählend = fortlaufende Handlung mit Akteuren,
Ortswechsel und Zeitverlauf; nicht erzählend = Gesetzestexte, Kult- und
Bauvorschriften, Genealogien, eingelegte Lieder und Gebete, prophetische Rede,
apokalyptische Vision, Briefe und Lehrreden.

Drei Präzisierungen musste ich selbst treffen, weil die Regel sie offen lässt — sie
stehen als `regel` in `korpus/erzaehlanteil.json`:

1. **Direkte Rede innerhalb einer laufenden Szene** (Dialog, Befehl, Botenwort)
   bleibt erzählend. Sonst wäre fast jedes Erzählkapitel der Bibel nicht erzählend.
2. Ein Kapitel, dessen **Wortmehrheit** aus zusammenhängender Rede ohne
   Handlungsfortschritt besteht, ist nicht erzählend — außer der Bruch lässt sich
   sauber an Versgrenzen ziehen.
3. **Regierungs- und Rahmenformeln mit Quellenverweis** („X regierte N Jahre … ist
   das nicht geschrieben im Buch der Chronik") sind Chroniknotiz, nicht Erzählung.

**250 Kapitel** wurden einzeln eingestuft, jedes mit Wortzahl und einer Zeile
Begründung. **85 Kapitel sind an Versgrenzen geteilt**; die Wortzahl beider Teile ist
in beiden Fällen **gemessen**, nicht geschätzt — jeder Versbereich wurde einzeln
abgerufen und gezählt (Zwischenspeicher `korpus/kapitel_verse.json`).

**Die Selbstprüfung, auf die es ankommt:** `erzaehlanteil.py` verwirft jede Teilung,
deren Teile nicht exakt das ganze Kapitel ergeben — Summe der Teilwortzahlen muss der
Kapitelwortzahl entsprechen **und** Summe der Verse der Kapitelversanzahl. Eine
Teilung mit Lücke oder Überlappung fällt durch und das Kapitel zählt dann konservativ
komplett als nicht erzählend. Aktuell fällt keine der 85 Teilungen durch.

### Wo die Einstufung unsicher ist

- Sie ist **zweistufig** entstanden: je Buch zwei unabhängige Einstufungen, bei
  Widerspruch eine dritte Instanz am Wortlaut. Danach lief für die sieben Bücher, die
  die drei Varianten tragen (Apostelgeschichte, 1./2. Samuel, 2. Könige, Rut, Ester,
  Daniel), eine **einseitige Gegenprüfung**: gesucht wurde nur nach zu hoch
  angesetzten Erzählanteilen, entschieden hat wieder eine unabhängige Instanz.
  Das hat **22 Kapitel** nach unten korrigiert. Am stärksten Daniel 4 (von 100 % auf
  38 % — das Kapitel ist formal ein Rundbrief Nebukadnezars) und die
  Regierungsformeln in 2. Könige.
- **Diese Gegenprüfung lief nicht für Exodus, Josua, Richter, 1. Könige, Jona und
  Genesis 43–50.** Deren Anteile oben sind also nach einem etwas milderen Maßstab
  gemessen und eher zu hoch als zu niedrig. **Alle drei Varianten benutzen
  ausschließlich gegengeprüfte Bücher** — die Zahlen in der Vergleichstabelle sind
  die konservativen.
- Die Einstufung bleibt eine Ermessensfrage. Die Fälle, an denen es hängt, sind
  benannt: ob eine Ratsrede (Apg 15), eine Verhörantwort (Apg 4) oder ein
  Botenbericht (Apg 10,30–33) Handlung ist oder Rede. Bei allen dreien ist zugunsten
  der Erzählung entschieden, mit Begründung im JSON. Zusammen hängen daran gemessene
  **542 Wörter**; kippten alle drei, läge V06-C bei **82,0 %** statt 83,63 % — immer
  noch über dem Gate, aber mit deutlich weniger Luft.

---

## Abweichungen zu den Projektdokumenten

**Gemeldet, nicht stillschweigend korrigiert.**

1. **Wortzahlen: keine Abweichung.** Jede prüfbare Zahl in den Dokumenten stimmt mit
   meiner Messung exakt überein — Apostelgeschichte 23.143 W (`videos-01-08.md`
   Zeile 60 und `bibeltube-wissen.md` Zeile 920), Jesaja 26–39 = 7.984, Daniel 7–12 =
   5.182, Offenbarung 12–22 = 5.949, Genesis 43–50 = 5.992. Auch alle acht
   Wortsummen in `plan.json` rechnen sich auf das Wort genau nach.

2. **Laufzeiten: die Dokumente rechnen mit 140 WPM, die Vorgabe mit 148,1 WPM.**
   `wortzahlen.py` schreibt das Feld `stunden_140wpm`, und `plan.json` sowie
   `videos-01-08.md` führen dieselben Werte als Laufzeit. Bei 148,1 WPM sind dieselben
   Korpora rund 5 % kürzer, und **fünf der acht geplanten Videos fallen unter das
   Zielband von 3,4 h**:

   | | Wörter | Doku (140 WPM) | bei 148,1 WPM | |
   |---|---:|---:|---:|---|
   | V01 | 29.670 | 3,53 h | **3,34 h** | unter Band |
   | V02 | 30.260 | 3,60 h | 3,41 h | im Band |
   | V03 | 30.009 | 3,57 h | **3,38 h** | unter Band |
   | V04 | 31.112 | 3,70 h | 3,50 h | im Band |
   | V05 | 29.880 | 3,56 h | **3,36 h** | unter Band |
   | V07 | 29.123 | 3,47 h | **3,28 h** | unter Band |
   | V08 | 29.835 | 3,55 h | **3,36 h** | unter Band |

   Das betrifft V01–V05 nachträglich und V07/V08 in der Planung. Ich habe nichts
   davon geändert.

3. **148,1 WPM liegt über jedem gemessenen Wert im Repo.** Die vier gerenderten
   Videos liegen bei 140,4 · 141,8 · 146,3 · 146,6 WPM (`video-0X/upload.md`), und
   `config.md` erwartet 145,9. Woher 148,1 stammt, steht nirgends. Gerechnet ist wie
   vorgegeben mit 148,1; bei 145,9 wären die drei Varianten **3,60 / 3,65 / 3,82 h** —
   V06-C läge dann knapp über dem Band.

4. **M8 und Gate 1.13 stehen nicht in den Dokumenten.** `regeln/erfolgsregeln.md`
   (Stand 2026-08-02) kennt M1–M7, `produktion/workflow-gates.md` kennt Gate 1.1–1.12.
   Auch die Gate-2-Auswertung vom 23.08.2026 (V03 14,4 % gegen V02 2,4 % Endretention)
   ist nirgends eingetragen — `workflow-gates.md` beschreibt Gate 2 nur als geplanten
   Ablauf. Die Zahl, auf der diese ganze Rechnung steht, existiert im Repo also nicht.
   Nachtragen wäre ein eigener Auftrag; ich habe es nicht getan.

5. **Die Verfügbarkeitsliste stimmt mit `plan.json` überein — aber nur, wenn man
   V07/V08 als reserviert behandelt.** Tatsächlich *verbraucht* haben V01–V05:
   Psalmen, 1. Petrus, Jakobus, Sprüche, Johannes, Hebräer, 1. Johannes, Kolosser,
   Matthäus, Epheser, Philipper, Daniel 1–3, Lukas, Prediger. Markus, Römer,
   Offenbarung und Genesis 1–42 sind für V07/V08 **geplant, aber nicht verbraucht** —
   streng nach deiner Anweisung („halte dich an das, was V01–V05 tatsächlich
   verbraucht haben") wären sie frei. Ich habe sie trotzdem nicht angefasst, weil
   deine Liste sie ausschließt. Falls V07/V08 mit neu geplant werden dürfen, ändert
   sich das Bild: Markus (14.261 W) ist durchlaufende Erzählung und wäre der
   natürlichste NT-Partner für ein M8-Video.

6. **Nur V01–V04 sind gerendert** (`produktion/video-01` bis `-04`). V05 existiert
   bisher nur in `plan.json` und `videos-01-08.md`. Ich habe V05 wie vorgegeben als
   verbraucht behandelt.

7. **Jesaja fällt durch die Streichung zurück in den Vorrat** (35.557 W, der größte
   freie Block überhaupt). Unter M8 ist es als Hauptstoff unbrauchbar — prophetische
   Rede ist per Regel nicht erzählend. Ich habe Jesaja **nicht** kapitelweise
   eingestuft; die 10,2 % aus deinem Auftrag sind hier nicht nachgerechnet.

---

## Was hier nicht drinsteht

Kein Titel, kein Eingangsgebet, kein Hook, kein Thumbnail, kein TTS, kein Rendering,
keine Änderung an `plan.json`, `videos-01-08.md` oder den Regeldateien. Sobald eine
Variante gewählt ist, sind das die nächsten Schritte — und Gate 1.2/1.3
(Titelähnlichkeit und Anker) sind dann gegen `produktion/titel_pruefung.py` zu prüfen,
nicht hier.
