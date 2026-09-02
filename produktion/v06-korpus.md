# Video 06 — drei Korpusvarianten nach Regel M8

> **Stand: 2026-08-30.** Der bisherige V06-Korpus (Jesaja 1–25 + 40–66 + Daniel 4–6)
> ist gestrichen: 10,2 % Erzählanteil laut Auftrag, reißt Gate 1.13 / Regel M8.
> *(Nachgemessen sind es **7,3 %** — siehe „Zwei Abweichungen" weiter unten. An der
> Streichung ändert das nichts.)*
> Alle Wortzahlen sind **gemessen**, nicht geschätzt — gleiche Abrufquelle und
> gleiche Zählmethode wie [`produktion/wortzahlen.py`](wortzahlen.py)
> (bible-api.com, `translation=webbe`, Verstexte mit Leerzeichen verbunden, dann
> `str.split()`), damit die Zahlen mit V01–V05 vergleichbar bleiben.
> Erzeugt und nachrechenbar mit [`produktion/erzaehlanteil.py`](erzaehlanteil.py).
> Rohdaten: [`korpus/erzaehlanteil.json`](korpus/erzaehlanteil.json) (250 Kapitel
> einzeln eingestuft) und [`korpus/v06_varianten.json`](korpus/v06_varianten.json).
> Kein Titel, kein Gebet, kein Thumbnail, kein TTS, kein Rendering.
>
> **Nachtrag 2026-08-30, zweiter Durchgang.** Das Sprechtempo ist inzwischen an den
> vier Renderläufen **gemessen** (143,7 WPM statt der unbelegten 148,1 aus dem
> Auftrag, siehe [`korpus/wpm_gemessen.json`](korpus/wpm_gemessen.json)). Damit
> verschiebt sich das Zielband nach unten — und **Variante V06-C fällt heraus**
> (3:53 h gegen die Obergrenze 3,8 h). `erzaehlanteil.py` meldet das und gibt
> seither **1** statt 0 zurück. **Variante A ist als V06 in `plan.json`
> eingetragen** (Status „geplant, Titel offen"), in kanonischer Lesereihenfolge
> Rut → 1 Samuel → Ester.

**Vorgaben, gegen die gerechnet wurde** *(Stand 30.08.; Dominanz und untere
Bandgrenze sind am 02.09. geändert — siehe den letzten Abschnitt. Die Wahl für V06
bleibt davon unberührt: Variante A hält auch die neuen Schwellen)*: Erzählanteil
≥ 80 % der Wörter · Zielband 3,4–3,8 h · ein dominantes Buch ≥ 60 % der Wörter · ganze Bücher bevorzugt,
Schnitte nur an Erzählnähten. Tempo und Zielband liest das Skript aus
[`config.md`](config.md); bei 143,7 WPM sind das **29.315–32.764 Wörter**
(bei der ursprünglich vorgegebenen 148,1: 30.215–33.767).

---

## Vergleich

| Variante | Korpus | Wörter | Erzählanteil | Laufzeit | dominantes Buch | Nachttauglichkeit *(Einschätzung, keine Messung)* | was danach für V07+ übrig bleibt |
|---|---|---:|---:|---:|---|---|---|
| **V06-A**<br>Anthologie | 1 Samuel 1–31 + Rut 1–4 + Ester 1–10 | 31.482 | **89,03 %** | 3:39 h | **1 Samuel** (75 %) | Rut ist der ruhigste Stoff im ganzen Vorrat. Gegen den Zweck: 1 Sam 15 (Bann an Amalek), 17 (Enthauptung), 18,25–27 (zweihundert Vorhäute), 22 (85 erschlagene Priester), 28 (Totenbeschwörerin), 31 (Selbstmord, Leichenschändung), Ester 9 (75.000 Erschlagene). Alles im Mittelteil. | 170.132 W. **Apostelgeschichte bleibt ganz frei** — das einzige noch unverplante NT-Buch. Dazu 2 Samuel, beide Königsbücher, Josua, Richter, Exodus, Jona, Daniel 4–12, Genesis 43–50. **Kein Torso.** |
| **V06-B**<br>Lebensbogen | 1 Samuel 16–31 + 2 Samuel 1–24 | 31.929 | **88,55 %** | 3:42 h | **2 Samuel** (61 %) | Die schwerste Stelle im ganzen Vorrat: 2 Sam 13 (Vergewaltigung Tamars) ist um 2 Uhr nachts nicht zumutbar. Dazu 2 Sam 4, 11, 12, 18, 21 und aus dem ersten Teil 1 Sam 17, 22, 28, 31. Der Stoff wird nach hinten **düsterer statt ruhiger**. | 169.685 W, davon **1 Samuel 1–15 als Torso** (11.156 W: Eli, Samuels Berufung, Sauls Aufstieg — ohne Fortsetzung zu kurz). Apostelgeschichte, Königsbücher, Josua, Richter, Exodus, Rut, Ester, Jona, Daniel 4–12, Genesis 43–50 frei. |
| **V06-C**<br>AT + NT | Apostelgeschichte 1–12 + 1 Samuel 1–31 | 33.460 | **83,63 %** | **3:53 h** | **1 Samuel** (71 %) | Apg 1–12 ist der ruhigste NT-Stoff im Vorrat; kritisch dort nur Apg 5 (Hananias und Saphira), 7,54–60 (Steinigung), 12 (Enthauptung, Herodes von Würmern gefressen). Der 1-Samuel-Teil bringt dieselben Stellen wie V06-A mit. | 168.154 W, davon **Apostelgeschichte 13–28 als Torso** (13.321 W: die Paulusreisen ohne Anfang). 2 Samuel, Königsbücher, Josua, Richter, Exodus, Rut, Ester, Jona, Daniel 4–12, Genesis 43–50 frei. |

**A und B bestehen alle drei Gates. C reißt das Zielband** — mit dem gemessenen
Tempo läuft der Korpus 3:53 h statt der zunächst gerechneten 3:46 h und liegt damit
über der Obergrenze von 3,8 h. Erzählanteil und Dominanz hält C weiterhin; es ist
allein die Länge. Umgebaut wurde nichts.

Die Nachttauglichkeits-Spalte ist ausdrücklich **keine Messung** — sie benennt
Stellen, von denen ich annehme, dass sie gegen den Zweck arbeiten. Es gibt dazu
keine eigenen Kanaldaten.

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
Jerusalem und der Richterzeit hat keine erzählerische Brücke, und beim Tempo aus
`config.md` (143,7 WPM) läuft die Variante auf **3,88 h** und damit über das
Zielband. *(Hier stand 145,9 WPM und 3,82 h — ein Tempowert, den `config.md` nie
geführt hat; korrigiert am 02.09.2026. Beide Zahlen führen zum selben Urteil: über
der Obergrenze.)*

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

> **Der ganze Abschnitt rechnet gegen das Band 30.215–33.767 W, das damals aus der
> Vorgabe von 148,1 WPM folgte.** Gültig ist seit dem 02.09.2026 **29.315–32.764 W**
> (143,7 WPM, `config.md`). Die genannten 33.620 W und 34.107 W liegen damit
> **856 bzw. 1.343 W über der Obergrenze** statt knapp darunter beziehungsweise
> knapp darüber — das Urteil „geht nicht" wird dadurch nur deutlicher. Der zweite
> Grund fällt dagegen ganz weg: der Erzählanteil des Gesamtkorpus **gatet nicht
> mehr** (Strukturfassung). Was heute gegen einen Apostelgeschichte-Korpus spricht,
> ist Bedingung 2 von Gate 1.13 — die Apostelgeschichte hält mit **73,0 %**
> kapitelweise das Erzählwerk-Kriterium nicht.

Acts-dominante Kombinationen bestehen nur, wenn man die Apostelgeschichte vorn
abschneidet (ab Apg 3, 4, 6 oder 7). Das ist keine Erzählnaht, sondern ein Schnitt am
Wortzähler entlang: das Video begönne mitten in der Handlung und ohne Pfingsten.
Deshalb steht keine solche Variante hier. **V06-C ist der einzige Weg, das NT
überhaupt in V06 zu bekommen** — als Nebenstoff, nicht als Titelgeber.

Ebenfalls ausgeschieden, weil sie die 60-%-Dominanz im Band gar nicht erreichen
können: Josua (17.835 W) und Richter (17.922 W) — beide zu klein, um in einem
30.000-W-Korpus auf 60 % zu kommen. *(Genau dieser Satz ist der Anlass der
Schwellenänderung vom 02.09.: Richter trägt jetzt zwanzig der 47 möglichen Korpora,
2 Samuel 25 und Genesis 12–50 die übrigen zwei. Siehe letzter Abschnitt.)* Und Exodus scheitert am Gate selbst: **46,5 %**
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
Begründung. **94 Kapitel sind an Versgrenzen geteilt** *(85 waren es beim Stand von
250 eingestuften Kapiteln; die 162 Kapitel der Runde vom 02.09. haben neun weitere
Teilungen gebracht)*; die Wortzahl beider Teile ist
in beiden Fällen **gemessen**, nicht geschätzt — jeder Versbereich wurde einzeln
abgerufen und gezählt (Zwischenspeicher `korpus/kapitel_verse.json`).

**Die Selbstprüfung, auf die es ankommt:** `erzaehlanteil.py` verwirft jede Teilung,
deren Teile nicht exakt das ganze Kapitel ergeben — Summe der Teilwortzahlen muss der
Kapitelwortzahl entsprechen **und** Summe der Verse der Kapitelversanzahl. Eine
Teilung mit Lücke oder Überlappung fällt durch und das Kapitel zählt dann konservativ
komplett als nicht erzählend. Aktuell fällt keine der 94 Teilungen durch.

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

## Nachtrag: was die eigenen Videos V01–V05 tragen

Gemessen mit derselben Regel und derselben Messlogik wie oben — 
[`produktion/eigene_videos_erzaehlanteil.py`](eigene_videos_erzaehlanteil.py) importiert
sie aus `erzaehlanteil.py`, das dabei unverändert bleibt. Ergebnis je Kapitel in
[`korpus/eigene_videos_erzaehlanteil.json`](korpus/eigene_videos_erzaehlanteil.json)
(311 zusätzlich eingestufte Kapitel). Gezählt ist der Bibelkorpus aus `plan.json`;
Eingangsgebet, Hook und CTA fallen in keine der beiden Kategorien der Regel und
sind nicht enthalten.

| Video | Korpus | Wörter | Erzählanteil | was ihn trägt | Regel M8 |
|---|---|---:|---:|---|---|
| **V01** | Psalmen 1–89 + 1 Petrus + Jakobus | 29.670 | **0,0 %** | — | reißt |
| **V02** | Psalmen 90–150 + Sprüche | 30.260 | **0,0 %** | — | reißt |
| **V03** | Johannes + Hebräer + 1 Johannes + Kolosser | 30.009 | **38,2 %** | Johannes 61,3 % | reißt |
| **V04** | Matthäus + Epheser + Philipper + Daniel 1–3 | 31.112 | **45,8 %** | Matthäus 52,5 % · Daniel 1–3 76,0 % | reißt |
| **V05** | Lukas + Prediger | 29.880 | **47,6 %** | Lukas 58,3 % | reißt |

**Alle fünf reißen das 80-%-Gate — V03 eingeschlossen, das Video, aus dem die Regel
abgeleitet wurde.** V03 kommt auf 38,2 %: Hebräer, 1 Johannes und Kolosser sind
Briefe und tragen null, und Johannes selbst hält nur 61,3 %, weil Prolog (1,1–18),
Brotrede (6,26–59), Streitreden (5,19–47; 8,12–58; 10,1–18) und die Abschiedsreden
samt hohepriesterlichem Gebet (Kap. 14–17) zusammen mehr als ein Drittel des Buches
ausmachen. Das ist so gemessen und nicht repariert worden: weder wurde die Regel
angepasst noch ein Kapitel umgestuft.

Was daraus folgt, steht in [`regeln/erfolgsregeln.md`](../regeln/erfolgsregeln.md)
bei M8 und nicht hier — kurz: der Kanal hat die 80-%-Schwelle nie getestet. Das
beste eigene Video liegt bei 47,6 %. Belegt ist ein Abstand zwischen *etwas*
Erzählstoff (V03, 38,2 %, 14,4 % Endretention) und *keinem* (V02, 0 %, 2,4 %).
Die Schwelle 80 % ist eine Planungsentscheidung mit Sicherheitsabstand, keine
Ableitung. Variante A liegt mit 89,03 % weit jenseits von allem, was der Kanal
bisher gezeigt hat — das ist ihre Chance und zugleich der Grund, warum ihre
Wirkung ungeprüft ist.

---

## Abweichungen zu den Projektdokumenten

**Gemeldet, nicht stillschweigend korrigiert.**

1. **Wortzahlen: keine Abweichung.** Jede prüfbare Zahl in den Dokumenten stimmt mit
   meiner Messung exakt überein — Apostelgeschichte 23.143 W (`videos-01-08.md`
   Zeile 60 und `bibeltube-wissen.md` Zeile 920), Jesaja 26–39 = 7.984, Daniel 7–12 =
   5.182, Offenbarung 12–22 = 5.949, Genesis 43–50 = 5.992. Auch alle acht
   Wortsummen in `plan.json` rechnen sich auf das Wort genau nach.

2. **Laufzeiten standen auf drei verschiedenen Tempi — inzwischen aufgelöst.**
   `wortzahlen.py` rechnete mit fest verdrahteten 140 WPM, `config.md` erwartete
   145,9, der V06-Auftrag gab 148,1 vor, und keiner der drei Werte war belegt.
   Seit dem 23.08.-Nachtrag steht **ein** gemessener Wert in `config.md`
   (**143,7 WPM**); `wortzahlen.py`, `plan.json` und `erzaehlanteil.py` lesen ihn
   von dort, statt eigene Zahlen zu führen. Die Laufzeiten in `plan.json` sind
   entsprechend neu ausgewiesen — die Wortzahlen sind unverändert:

   | | Wörter | vorher (140 WPM) | jetzt (143,7 WPM) | tatsächlich gerendert |
   |---|---:|---:|---:|---:|
   | V01 | 29.670 | 3,53 h | 3,44 h | 3:34:48 = 3,58 h |
   | V02 | 30.260 | 3,60 h | 3,51 h | 3:37:23 = 3,62 h |
   | V03 | 30.009 | 3,57 h | 3,48 h | 3:27:54 = 3,47 h |
   | V04 | 31.112 | 3,70 h | 3,61 h | 3:34:40 = 3,58 h |
   | V05 | 29.880 | 3,56 h | 3,47 h | **3,40 h** (`video-05/qa.json`) |
   | V07 | 29.123 | 3,47 h | **3,38 h** | nicht gerendert |
   | V08 | 29.835 | 3,55 h | 3,46 h | nicht gerendert |

   **V07 liegt mit 3,38 h weiterhin unter dem Zielband** — das ist der einzige
   Planwert, der nach der Umstellung noch danebenliegt. Nicht geändert.
   Die Spalte ganz rechts zeigt zugleich, dass die Planzahl die echte Laufzeit
   systematisch **unterschätzt**: sie zählt nur den Bibelkorpus, während
   Eingangsgebet, Hook und CTA in den vier Läufen 354–561 Wörter dazugelegt haben
   (rund 0,05 h).

3. **Die vorgegebenen 148,1 WPM waren zu hoch — und das kostet Variante C.**
   Nachgemessen an den vier Renderläufen: **143,7 WPM** wortgewichtet, Spanne der
   Einzelvideos 140,4–146,6. Mit dem gemessenen Tempo läuft V06-C auf **3:53 h** und
   liegt damit über der Obergrenze von 3,8 h; A (3:39 h) und B (3:42 h) halten.
   Die Entscheidung für A ist davon nicht berührt — sie ist die kürzeste der drei
   und hat mit 1.282 Wörtern den größten Abstand zur Obergrenze.

   Die Spanne ist dabei **nicht Streuung, sondern Textsorte**: `prosody_speed` war
   über alle vier Läufe konstant 0,88, aber Poesie läuft langsamer als Prosa —
   V01/V02 (Psalmen, Sprüche) 141,1 WPM, V03/V04 (Evangelien) 146,4 WPM. Ein reiner
   Erzählkorpus wie Variante A liegt näher am Prosawert, würde also eher **3:35 h**
   laufen als 3:39 h. Als eigener Parameter ist das bei n=2 je Gruppe nicht
   belastbar, deshalb steht in `config.md` der Gesamtwert und nicht der Prosawert.

4. ~~**M8 und Gate 1.13 stehen nicht in den Dokumenten.**~~ *Erledigt am
   2026-08-30:* Die Gate-2-Rohzahlen stehen als Messdatei in
   [`regeln/daten/gate2_2026-08-23.json`](../regeln/daten/gate2_2026-08-23.json)
   (alle Werte als `abgetippt` gekennzeichnet, CSV-Export steht aus), **M8** in
   `regeln/erfolgsregeln.md` und **Gate 1.13** in `produktion/workflow-gates.md`,
   beide mit Verweis auf die Datei und mit der Fallzahl im Text.

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

6. ~~**Nur V01–V04 sind gerendert.** V05 existiert bisher nur in `plan.json` und
   `videos-01-08.md`.~~ **Falsch, berichtigt am 02.09.2026 nach der
   Zusammenführung.** V05 ist gerendert **und ausgeliefert**: das Paket liegt in
   `produktion/video-05/` (`qa.json`, `titel.txt`, `upload.md`, `video-05.srt`,
   Thumbnail), `qa.json` führt einen vollständigen Renderlauf über 3:24:14 = 3,404 h,
   und `produktion/auslieferung/manifest.json` drei GoFile-Auslieferungen. Der Satz
   stand hier, weil das V05-Paket auf dem anderen Zweig lag. **Gerendert sind
   V01–V06.**

7. **Jesaja fällt durch die Streichung zurück in den Vorrat** (35.557 W, der größte
   freie Block überhaupt). Unter M8 ist es als Hauptstoff unbrauchbar — prophetische
   Rede ist per Regel nicht erzählend. Ich habe Jesaja **nicht** kapitelweise
   eingestuft; die 10,2 % aus dem Auftrag waren hier zunächst nicht nachgerechnet.
   **Nachgetragen 2026-09-02: gemessen sind es 7,3 %.**

---

## Wo diese Runde liegt — Stand 2026-08-31, nachgeprüft

**Nichts aus der V06-Runde ist im Hauptzweig.** `origin/main` steht auf
`5a750a4`; weder die Messdateien noch die Werkzeuge noch das Video-Paket sind
dort. Wer eine Zahl aus dieser Runde zitiert, zitiert vom Branch
`claude/bibeltube-v06-korpus-m8-rz2oce`.

**Damals neu auf dem Branch, im Hauptzweig nicht vorhanden (34 Dateien):**

| | Dateien |
|---|---|
| Erzählanteil | `erzaehlanteil.py` · `eigene_videos_erzaehlanteil.py` · `korpus/erzaehlanteil.json` · `korpus/eigene_videos_erzaehlanteil.json` · `korpus/kapitel_verse.json` |
| Tempo | `wpm_messen.py` · `korpus/wpm_gemessen.json` |
| V06-Runde | `v06-korpus.md` · `v06-titel.md` · `v06_titel_kandidaten.json` · `korpus/v06_varianten.json` · `videos-06.md` |
| Render | `render_messung.py` · `korpus/v06_render.json` · `klang/bett_mono_feuer_leise.flac` · `motive/motiv-V6.png` (+`_160x90`) |
| Vergleichsliste | `kopisten_titel.json` |
| Gate-2-Rohdaten | `regeln/daten/gate2_2026-08-23.json` |
| Paket und Clips | `produktion/video-06/` (9 Dateien) · `produktion/motive/loops/ki-v06/` (6 Dateien) |

**Gegenüber dem Hauptzweig geändert (13 Dateien):** `config.md` ·
`eigene_titel.json` · `korpus/plan.json` · `korpus/kapitel.json` ·
`korpus/wortzahlen.json` · `wortzahlen.py` · `titel_pruefung.py` ·
`pipeline/vorlage.py` · `pipeline/schritt5_video.py` · `videos-01-08.md` ·
`workflow-gates.md` · `regeln/erfolgsregeln.md` · `bibeltube-wissen.md`.

### Zwei Korrekturen an einer verbreiteten Annahme

**`kopisten_titel.json` ist nicht im Hauptzweig.** Sie existiert zweimal —
auf diesem Branch (`f31ac14`) und auf
`origin/claude/historien-fund-messdatei-w4hjlc` (`1d2440b`) — und beide
Fassungen sind **byte-identisch** (SHA-256 `f98dddc6…`, je 45 Titel). Es gibt
also keine Divergenz, die aufzulösen wäre, aber auch keinen Hauptzweig-Stand,
gegen den man messen könnte.

**`.claude/skills/bibeltube-video/SKILL.md` ist ebenfalls nicht im
Hauptzweig**, sondern nur auf `historien-fund-messdatei-w4hjlc`. Die Tabelle
dort, die `kopisten_titel.json` als „im Hauptzweig" führt, ist nach dieser
Prüfung falsch und gehört korrigiert — das kann nur auf jenem Branch
geschehen.

> **Erledigt am 2026-09-02** (Commit `40d5600` auf
> `historien-fund-messdatei-w4hjlc`, nach ausdrücklicher Freigabe): Die Tabelle
> im Skill ist auf drei Spalten umgebaut — `origin/main`, jener Zweig, dieser
> Zweig — und verweist für die Vollinventur hierher. Dabei kam heraus, dass
> **beide Zweige fünfzehn Dateien anfassen und vierzehn davon verschieden
> führen**; bitgleich ist nur `kopisten_titel.json`. Drei dieser Unterschiede
> ändern Ergebnisse: `wpm_erwartet` 148,1 gegen 143,7 · zwei verschiedene
> Fassungen von Gate 1.13 · zwei verschieden hergeleitete Mono-Klangbetten
> unter demselben Dateinamen `bett_mono_feuer_leise.flac`. **Welche Fassung
> gilt, ist eine offene Entscheidung, keine Messfrage.**

> Geprüft mit `git fetch origin`, `git cat-file -e origin/main:<pfad>` und
> `git diff --name-status origin/main...HEAD`, nicht aus der Erinnerung.

> ### Überholt am 02.09.2026 — die Zweige sind zusammengeführt
>
> Der Abschnitt oben beschreibt den Zustand vor der Zusammenführung. Seither gibt
> es **einen** Stand: `claude/historien-fund-messdatei-w4hjlc` ist nach
> `claude/bibeltube-v06-korpus-m8-rz2oce` vereinigt, mit dem Skill, der
> vollständigen Pipeline, V05 und V06. Vier Kollisionen hat der Kanalinhaber
> entschieden — Klangbett (linker Kanal), Gate 1.13 (Strukturfassung),
> `wpm_erwartet` (143,7) und, daraus folgend, eine einzige Bandrechnung.
> Die Liste der Dateien, bei denen zu wählen war, steht in der Commit-Nachricht
> der Zusammenführung.

---

## Was mit den Entscheidungen vom 02.09.2026 baubar wird — V07 und V08

**Das ist eine Messung, kein Vorschlag.** Hier steht keine Empfehlung, keine
Reihenfolge und keine Bewertung der Nachttauglichkeit — nur, was Gate 1.13
durchlässt. Erzeugt von `produktion/v07_v08_moeglichkeiten.py`, vollständig in
[`korpus/v07_v08_moeglichkeiten.json`](korpus/v07_v08_moeglichkeiten.json).
`plan.json` ist **nicht** angefasst: V07 und V08 stehen dort unverändert.

**Gate 1.13, Strukturfassung** (alle Schwellen aus `config.md`): dominantes Buch
≥ 50 % · selbst Erzählwerk (≥ 80 %, kapitelweise) · in voller Länge im Korpus ·
≥ 15 Punkte vor dem zweitgrößten Buch. **Der Erzählanteil des Gesamtkorpus wird
gemessen und gemeldet, er gatet nicht.** Zielband 29.315–32.764 W (3,40–3,80 h),
beziehungsweise 25.866–32.764 W (3,00–3,80 h), sobald das dominante Buch
Erzählwerk in voller Länge ist — was 1.13 ohnehin verlangt, das tiefere Band
gilt also für jeden Korpus, der überhaupt besteht.

### Zuerst: die Planfassungen aus plan.json

| | Korpus | Wörter | Erzählanteil | Dominanz | Abstand | Ergebnis |
|---|---|---:|---:|---:|---:|---|
| **V07** | Markus + Römer + Offenbarung 1–11 | 29.123 | **38,9 %** | **49,0 %** | 16,6 | reißt Band, Dominanz und Erzählwerk |
| **V08** | Genesis 1–42 | 29.835 | 87,7 % | 100,0 % | 100,0 | reißt NUR die Vollständigkeit |

**V07 scheitert am Stoff, nicht an der Größe.** Römer (9.431 W) und Offenbarung
1–11 (5.431 W) tragen zusammen **null** erzählende Wörter — Brief und
apokalyptische Vision stehen wörtlich im Ausschluss der Regel. Markus hält mit
**79,4 %** das Erzählwerk-Kriterium um 0,6 Punkte nicht und liegt mit 49,0 %
auch unter der Dominanzschwelle; jedes Wort, das die Laufzeit ins Band hebt,
drückt ihn weiter darunter. **V07 war nie ein Zangen-Fall.**

**V08 hält alles außer „in voller Länge".** Laufzeit 3,46 h, Dominanz 100 %,
Abstand 100 Punkte, Erzählanteil 87,7 % — Genesis 1–42 ist nur nicht das ganze
Buch. Das hängt mit dem Band zusammen: das tiefere Band gilt nur bei voller
Länge, also bekommt ein Korpus, der die Vollständigkeit reißt, es nie.

### Passt Genesis über eine Teilung an einer Erzählnaht hinein?

**Ja — seit dem 02.09.2026 auch nach der Regel.** Genesis 12–50 sind 29.421 W
bei **91,4 %** Erzählanteil und 100 % Dominanz; die Naht nach Gen 11 steht mit
Begründung in `korpus/erzaehlnaehte.json`, und der gelesene Teil hält die 80 %
für sich. Ganz Genesis (35.827 W) sprengt weiterhin das Band.

| Teilung | Wörter | Erzählanteil | Laufzeit | Naht |
|---|---:|---:|---:|---|
| Genesis 12–50 | 29.421 | 91,4 % | 3,41 h | Ende der Urgeschichte — Gen 11 schließt mit Terachs Tod in Haran, Gen 12 setzt mit Abrams Ruf neu an |
| Genesis 1–36 | 24.835 | 85,2 % | 2,88 h | vor der Josephsnovelle; Gen 36 ist Listenabschluss |
| Genesis 37–50 | 10.992 | 91,7 % | 1,27 h | die Josephsnovelle am Stück |
| Genesis 1–42 *(Planfassung)* | 29.835 | 87,7 % | 3,46 h | liegt mitten in der Hungersnot-Sequenz |

> **Überholt am 02.09.2026 — die Vollständigkeitsbedingung ist gelockert.**
> Eine Teilung qualifiziert jetzt, wenn ihre offenen Kanten mit Begründung in
> [`korpus/erzaehlnaehte.json`](korpus/erzaehlnaehte.json) stehen **und** der
> gelesene Teil für sich die 80 % hält. **Genesis 12–50 erfüllt beides** und ist
> damit der dritte mögliche Titelgeber. **Genesis 1–42 bleibt draußen** — die
> Naht nach Gen 42 ist ausdrücklich als *keine* Naht eingetragen: dort ist
> Simeon gerade als Geisel in Ägypten zurückgeblieben.

**Als Nebenstoff steht Genesis in fünfzehn der 47 möglichen Korpora, als
dominantes Buch in zwei.**

> **Die Nähte sind Urteil, keine Messung.** Es gibt im Repo weder eine Nahtliste
> noch ein Werkzeug dafür. Gen 11/12 und Gen 36/37 sind die beiden Stellen, an
> denen das Buch selbst neu ansetzt; Gen 42/43 ist es nicht — dort sind die
> Brüder einmal in Ägypten gewesen und müssen wieder hin.

### Die 47 Korpora, die Gate 1.13 halten

**Getragen werden sie von drei Büchern:** 2 Samuel (25 Korpora), Richter (20)
und — seit der Naht-Lockerung vom 02.09.2026 — **Genesis 12–50** (2). Mehr
qualifiziert nicht: 1 Samuel steckt in V06, Markus reißt das
Erzählwerk-Kriterium um 0,6 Punkte, ganz Genesis sprengt das Band, und jede
andere Teilung hat keinen Eintrag in
[`korpus/erzaehlnaehte.json`](korpus/erzaehlnaehte.json).
**336 Paare aus je zwei dieser Korpora sind materialfrei gegeneinander**, taugen
also als Paar für V07 und V08.

| Korpus | Wörter | Erzählanteil | Dominanz | Abstand | dominant | Laufzeit |
|---|---:|---:|---:|---:|---|---:|
| Genesis 12–50 | 29.421 | 91,4 % | 100,0 % | 100,0 | Genesis | 3,41 h |
| Genesis 12–50 + Jona | 30.693 | 91,2 % | 95,9 % | 91,7 | Genesis | 3,56 h |
| Genesis 37–50 + Richter | 28.914 | 88,3 % | 62,0 % | 24,0 | Richter | 3,35 h |
| Genesis 37–50 + Richter + Jona | 30.186 | 88,2 % | 59,4 % | 23,0 | Richter | 3,50 h |
| Josua 1–12 + Richter | 26.989 | 88,0 % | 66,4 % | 32,8 | Richter | 3,13 h |
| Josua 1–12 + Richter + Jona | 28.261 | 87,9 % | 63,4 % | 31,3 | Richter | 3,28 h |
| Genesis 37–50 + 2 Samuel + Jona | 31.711 | 85,5 % | 61,3 % | 26,7 | 2 Samuel | 3,68 h |
| Genesis 37–50 + 2 Samuel | 30.439 | 85,4 % | 63,9 % | 27,8 | 2 Samuel | 3,53 h |
| Genesis 43–50 + Richter 17–21 + 2 Samuel | 29.917 | 85,2 % | 65,0 % | 45,0 | 2 Samuel | 3,47 h |
| Josua 1–12 + 2 Samuel + Jona | 29.786 | 85,0 % | 65,3 % | 34,8 | 2 Samuel | 3,46 h |
| Josua 1–12 + 2 Samuel | 28.514 | 85,0 % | 68,2 % | 36,4 | 2 Samuel | 3,31 h |
| Richter + 1 Könige 12–22 + Jona | 30.302 | 83,2 % | 59,1 % | 22,5 | Richter | 3,51 h |
| Richter + 1 Könige 12–22 | 29.030 | 83,1 % | 61,7 % | 23,5 | Richter | 3,37 h |
| Genesis 43–50 + 2 Samuel + Jona | 26.711 | 82,7 % | 72,8 % | 50,4 | 2 Samuel | 3,10 h |
| Genesis 1–11 + Genesis 43–50 + Richter | 30.320 | 82,1 % | 59,1 % | 18,2 | Richter | 3,52 h |
| Genesis 43–50 + Richter + 2 Könige 18–25 | 31.020 | 82,1 % | 57,8 % | 34,9 | Richter | 3,60 h |
| Exodus 1–18 + 2 Samuel | 32.706 | 81,8 % | 59,5 % | 18,9 | 2 Samuel | 3,79 h |
| Richter + 2 Könige 18–25 + Jona | 26.300 | 81,6 % | 68,1 % | 41,1 | Richter | 3,05 h |
| Genesis 1–11 + Richter 17–21 + 2 Samuel | 30.331 | 81,6 % | 64,1 % | 43,0 | 2 Samuel | 3,52 h |
| Richter 17–21 + 2 Samuel + 2 Könige 18–25 | 31.031 | 81,6 % | 62,7 % | 39,8 | 2 Samuel | 3,60 h |
| Richter + Jona + Apostelgeschichte 1–12 | 29.016 | 80,9 % | 61,8 % | 27,9 | Richter | 3,37 h |
| 2 Samuel + 1 Könige 12–22 + Jona | 31.827 | 80,7 % | 61,1 % | 26,2 | 2 Samuel | 3,69 h |
| Richter + Apostelgeschichte 1–12 | 27.744 | 80,6 % | 64,6 % | 29,2 | Richter | 3,22 h |
| 2 Samuel + 1 Könige 12–22 | 30.555 | 80,5 % | 63,6 % | 27,3 | 2 Samuel | 3,54 h |
| Genesis 43–50 + 2 Samuel + 2 Könige 18–25 | 32.545 | 79,7 % | 59,8 % | 37,9 | 2 Samuel | 3,77 h |
| Genesis 1–11 + Genesis 43–50 + 2 Samuel | 31.845 | 79,7 % | 61,1 % | 22,1 | 2 Samuel | 3,69 h |
| 2 Samuel + 2 Könige 18–25 + Jona | 27.825 | 78,9 % | 69,9 % | 44,4 | 2 Samuel | 3,23 h |
| Genesis 1–11 + 2 Samuel + Jona | 27.125 | 78,8 % | 71,7 % | 48,1 | 2 Samuel | 3,15 h |
| Genesis 1–11 + Richter + 2 Könige 18–25 | 31.434 | 78,7 % | 57,0 % | 34,4 | Richter | 3,65 h |
| 2 Samuel + 2 Könige 18–25 | 26.553 | 78,5 % | 73,2 % | 46,5 | 2 Samuel | 3,08 h |
| 2 Samuel + Jona + Apostelgeschichte 1–12 | 30.541 | 78,4 % | 63,7 % | 31,5 | 2 Samuel | 3,54 h |
| 2 Samuel + Apostelgeschichte 1–12 | 29.269 | 78,1 % | 66,4 % | 32,9 | 2 Samuel | 3,40 h |
| Genesis 43–50 + Richter + Daniel 4–12 | 32.216 | 70,7 % | 55,6 % | 29,9 | Richter | 3,74 h |
| Richter 17–21 + 2 Samuel + Daniel 4–12 | 32.227 | 70,3 % | 60,3 % | 34,6 | 2 Samuel | 3,74 h |
| Richter + Jona + Daniel 4–12 | 27.496 | 68,3 % | 65,2 % | 35,0 | Richter | 3,19 h |
| Genesis 1–11 + Richter + Daniel 4–12 | 32.630 | 67,6 % | 54,9 % | 29,5 | Richter | 3,79 h |
| Richter + Daniel 4–12 | 26.224 | 67,5 % | 68,3 % | 36,7 | Richter | 3,04 h |
| 2 Samuel + Jona + Daniel 4–12 | 29.021 | 66,4 % | 67,0 % | 38,4 | 2 Samuel | 3,37 h |
| 2 Samuel + Daniel 4–12 | 27.749 | 65,5 % | 70,1 % | 40,2 | 2 Samuel | 3,22 h |
| Richter + Jona + Römer | 28.625 | 57,8 % | 62,6 % | 29,7 | Richter | 3,32 h |
| Richter + Römer | 27.353 | 56,4 % | 65,5 % | 31,0 | Richter | 3,17 h |
| 2 Samuel + Jona + Römer | 30.150 | 56,4 % | 64,5 % | 33,2 | 2 Samuel | 3,50 h |
| 2 Samuel + Römer | 28.878 | 55,1 % | 67,3 % | 34,7 | 2 Samuel | 3,35 h |
| Richter + Jona + Offenbarung | 30.574 | 54,1 % | 58,6 % | 21,4 | Richter | 3,55 h |
| 2 Samuel + Jona + Offenbarung | 32.099 | 53,0 % | 60,6 % | 25,1 | 2 Samuel | 3,72 h |
| Richter + Offenbarung | 29.302 | 52,7 % | 61,2 % | 22,3 | Richter | 3,40 h |
| 2 Samuel + Offenbarung | 30.827 | 51,6 % | 63,1 % | 26,2 | 2 Samuel | 3,58 h |

### Vier Nebenwirkungen, die ich nicht nachgeschärft habe

Gefragt war, Unsinn zu melden statt still zu reparieren. Keine Schwelle ist
deswegen angefasst worden.

**1. Der Erzählanteil gatet nicht mehr — und das sieht man der Liste an.**
**23 der 47 Korpora liegen unter 80 %**, der niedrigste bei **51,6 %**. Ganz
unten stehen `2 Samuel + Offenbarung` (51,6 %), `Richter + Offenbarung` (52,7 %)
und `2 Samuel + Römer` (55,1 %) — vollständiges Erzählbuch plus nicht-erzählende
Beigabe.

*Korrigiert am 02.09.2026:* Hier stand, das sei „das Gegenteil dessen, was M8
belegt". Das ist zu scharf. **Diese Bauform ist die von V03** — Johannes plus
Hebräer, 1 Johannes und Kolosser —, dem einzigen Video des Kanals, das
funktioniert hat, und V03 liegt kapitelweise bei **38,2 %**. `2 Samuel +
Offenbarung` liegt mit 51,6 % **darüber**. Die brauchbare Linie ist deshalb
nicht 80 %, sondern V03:

| Erzählanteil | Einordnung |
|---|---|
| über **38,2 %** | die **belegte Bauform** — V03 hat mit weniger funktioniert |
| unter **38,2 %** | **unbelegtes Neuland**; nichts spricht dagegen, aber nichts dafür |

Wer eine Variante vorschlägt, nennt den gemeldeten Erzählanteil und sagt, was
den Rest füllt — nicht weil der Wert eine Grenze wäre, sondern weil er die
Größe ist, über die M8 überhaupt redet.

**2. Der Mindestabstand von 15 Punkten kostet neun Korpora — gemessen, bevor er
festgeschrieben wurde** — und zwar gegen zwei Bezugsmengen, weil die
Strukturfassung eine andere Menge durchlässt als die Prozentfassung davor:

| Bezugsmenge | fallen weg | bleiben |
|---|---:|---:|
| die 50 Korpora der **Prozentfassung** (Stand vor dieser Runde) | 9 | 41 |
| die 50 Korpora der **Strukturfassung** (Stand danach) | 5 | **45** |

Der knappste ausgeschiedene Fall lag bei **9,9 Punkten** (`Genesis 1–11 +
Genesis 37–50 + Markus`: Genesis 55,0 % gegen Markus 45,0 %), der knappste
gehaltene bei 15,6. **In beiden Rechnungen blieb für V07 und V08 reichlich
übrig; die Schwelle musste nicht aufgeweicht werden.**

**3. Das tiefere Band ist jetzt das einzige Band.** „Erzählwerk, ganz oder an
einer eingetragenen Naht geteilt" ist unter der Strukturfassung ohnehin
Bedingung von 1.13 — jeder Korpus, der
1.13 hält, bekommt damit automatisch 3,0–3,8 h. Die 3,4 h greifen nur noch bei
Korpora, die schon durchgefallen sind. `laufzeit_ziel_von_h` bleibt trotzdem
stehen: es ist die Bandgrenze der Formel und würde bei einer Rückkehr zur
Prozentfassung wieder wirken.

**4. Die Gates messen keine Zusammengehörigkeit und keine Nachttauglichkeit.**
`Genesis 1–11 + Richter 17–21 + 2 Samuel` hält alles und ist eine Sammlung ohne
inneren Zusammenhang: Schöpfung und Sintflut, der Anhang des Richterbuchs,
David. **24 der 47 Korpora enthalten Richter 19** — die Vergewaltigung und
Zerstückelung der Nebenfrau. Das ist kein Fehler der neuen Schwellen; es war
vorher genauso, und es folgt daraus, dass Richter eines von nur zwei möglichen
dominanten Büchern ist. „In voller Länge" lässt kein Auslassen zu.

### Was diese Runde über die Sackgasse ergibt

Die Zange war real, aber sie war nicht der einzige Grund und nicht der erste.
**Fünf Korpora hätten schon vor dieser Runde die alten Schwellen gehalten** — mit
Material, das damals bereits eingestuft war, etwa *2 Samuel + 1 Könige 12–22*
(30.555 W, 80,5 % Erzählanteil, Dominanz 63,6 %, Abstand 27,3 Punkte — es hält
auch die heutigen Prüfungen). Sie sind niemandem aufgefallen, weil nur ganze
Bücher als dominantes Buch geprüft wurden und die Nebenstoffe nicht als
Teilblöcke durchgerechnet.

Der zweite Grund war eine Lücke in der Messung, nicht in der Regel: Genesis war
bis heute nur in den Kapiteln 43–50 eingestuft, Markus, Jesaja, Römer und
Offenbarung gar nicht. Wer „ganz Genesis ist zu groß" schreibt, ohne Genesis 12–50
zu rechnen, kommt zum falschen Schluss — dieser Korpus hält alle Gates und hätte
sie immer gehalten.

**Neu eingestuft in dieser Runde: 162 Kapitel** (Genesis 1–42, Markus 1–16,
Jesaja 1–66, Römer 1–16, Offenbarung 1–22). Von den 250 vorher eingestuften
Kapiteln hat sich **keines** geändert — nachgeprüft durch Vergleich mit der
Vorgängerfassung von `erzaehlanteil.json`.

| Buch | Wörter | Erzählanteil | |
|---|---:|---:|---|
| Genesis 1–50 | 35.827 | **87,2 %** | hält die 80 % als ganzes Buch |
| Markus 1–16 | 14.261 | **79,4 %** | 0,6 Punkte darunter |
| Jesaja 1–66 | 35.557 | **5,6 %** | nur 36–39 tragen Handlung |
| Römer 1–16 | 9.431 | **0,0 %** | Brief |
| Offenbarung 1–22 | 11.380 | **0,0 %** | apokalyptische Vision |

### Zwei Abweichungen zu dokumentierten Zahlen

**Der gestrichene Jesaja-Korpus liegt bei 7,3 %, nicht bei 10,2 %.** Jesaja 1–25 +
40–66 + Daniel 4–6 sind 30.693 W, davon 2.254 erzählend — alle aus Daniel, denn
Jesaja trägt außerhalb von 36–39 nichts bei. Die 10,2 % stehen seit dem
V06-Auftrag in mehreren Dokumenten; sie stammen aus einer Zeit, in der Jesaja
noch gar nicht eingestuft war. **Das ändert an der Streichung nichts** — beide
Werte reißen das Gate um mehr als 70 Punkte.

**Das Zielband beginnt bei 29.315 W, nicht bei 29.722 W.** 3,4 h × 60 × 143,7 WPM
= 29.315. Die höhere Zahl kam aus `korpus_pruefung.py`, wo `band_fuer(n)` die
Kapitelansagen und den Rahmen abzog und mit 148,1 WPM rechnete. **Beides ist am
02.09.2026 vereinigt:** ein Sprechtempo (143,7) und eine Bandrechnung
(`round(h × 60 × WPM)`, reine Korpuswörter). `band_fuer()` und
`erzaehlanteil.band()` geben seither dasselbe zurück — vorher gab dieselbe
Prüfung 1.1 zwei Fenster aus, und ein Korpus dazwischen bestand beim einen und
riss beim anderen. Rahmen und Kapitelansagen sind damit aus dem *Gate* heraus,
nicht aus der Rechnung: `_video_h()` druckt die erwartete Videolaufzeit weiter,
und `schritt1_text.py` prüft die echte Laufzeit nach dem Textbau ein zweites Mal.

Für die Zange ändert das die Größenordnung nicht: die Mindestgröße des dominanten
Buchs war 17.589 W statt 17.833 W, Markus fällt so wie so darunter.

**Ein dritter Widerspruch, bei der Zusammenführung gefunden und behoben:**
`korpus_pruefung.py` las aus `erzaehlanteil.json` die Ja/Nein-Flagge
`erzaehlend` statt der gemessenen `erzaehlend_woerter` und kam damit für V06 auf
**94,0 %**, wo `erzaehlanteil.py` aus derselben Datei **89,0 %** ausweist. Die
Datei sagt in ihrem eigenen Feld `hinweis_flagge`, dass bei geteilten Kapiteln
nur die Wortzahl maßgeblich ist. Beide Werkzeuge melden jetzt 89,0 %.

---

## Was hier nicht drinsteht

Kein Titel, kein Eingangsgebet, kein Hook, kein Thumbnail, kein TTS, kein Rendering.
`plan.json` trägt seit dem 30.08. Variante A als V06 mit dem Status
„geplant, Titel offen" — mehr nicht. Die nächsten Schritte sind Titel und Thumbnail,
und Gate 1.2/1.3 (Titelähnlichkeit und Anker) sind dann gegen
`produktion/titel_pruefung.py` zu prüfen, nicht hier.
