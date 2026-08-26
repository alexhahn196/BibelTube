# Erfolgsregeln: Warum 2 Kanäle gewinnen und 8 Klone verlieren

> **Lebendes Dokument.** Stand: 2026-08-23 (Fremddaten-Teil: 2026-08-02).
> Datengrundlage: 10 Kanäle (2 Gewinner, 8 dokumentierte Verlierer), 150 Langform-Videos
> + 141 Shorts aus den Kanal-Listings, 12 vollständige Transkripte, 90 Thumbnails,
> 4 multimodale Video-Stichproben, About-Seiten aller 10 Kanäle, Voll-Metadaten
> (Tags/Captions/Kapitel/exakte Upload-Daten) für 19 von 21 Gewinner-Videos.
> Ergänzt `teardown/produktions-spec.md` (Lauf 1, 8 etablierte Kanäle) — ersetzt sie nicht.
> **Validierung:** Ab Video 10 des eigenen Kanals werden diese Regeln gegen die eigenen
> Kanaldaten geprüft (Hypothesen-Prüfkriterien in Abschnitt 4). Regeln, die die eigenen
> Daten widerlegen, werden hier gestrichen — nicht verteidigt.
> **Erste Auswertung schon nach Video 4:**
> [`produktion/workflow-gates.md`](../produktion/workflow-gates.md), Gate 2 — CTR,
> Absprungstelle und Traffic-Quellen. Kernregel dort: *eigene Daten schlagen Fremddaten.*
> Gate 1 im selben Dokument hält die harten Prüfungen vor jedem Renderlauf fest.
>
> **2026-08-23 — Gate 2 ausgewertet. Ab hier stehen eigene Zahlen im Dokument.**
> Kanal *The Nightly Word* (`UCai4rcN45WKqNvPdSJGADPg`), 25.07.–22.08.2026:
> 4 Videos, 151 Aufrufe, 69,4 Wiedergabestunden, 2 Abonnenten, 5.535 Impressionen,
> CTR 2,71 %. Rohwerte: `regeln/daten/gate2_eigene_kanaldaten.json`.
> Alles, was aus diesen Zahlen folgt, trägt die Marke **„eigene Kanaldaten Gate 2"**
> und ein Datum — Fremdbefunde bleiben ohne diese Marke, damit beide unterscheidbar
> bleiben. Neu daraus: **M8** (die erste Regel dieses Dokuments überhaupt aus eigenen
> Daten), die Kadenz-Entscheidung unter M1 und die Teilantwort auf offene Frage 3.

**Die Kanäle:**
| | Kanal | Start (1. Upload) | Langform | Shorts | Ø Views (Langform) | Status |
|---|---|---|---|---|---|---|
| A | Hush Little Lamb | 08.05.26 | 8 | 0 | 121.250 | GEWINNER |
| B | Rest in Grace | 31.05.26 | 13 | 0 | 25.997 | GEWINNER |
| C | The Bible Sacred | Juni 26 | 35 | 29 | 39 | Grinder, tot |
| D | God Message Today | Juli 26 | 19 | 14 | 16 | Grinder, tot |
| E | Quiet Mind | Juli 26 | 19 | 0 | 169 | umgewidmet, tot |
| F | God's Peaceful Sleep | 21.07.26 | 10 | 0 | 9 | Titel-Kopist, tot |
| G | The Silent Shepherd | Mai 26 | 13 | 59 | 62 | Mittelmaß |
| H | Time For God | Mai 26 | 24 | 17 | 1.190* | umgewidmet |
| I | Deep Rest Bible | 19.07.26 | 4 | 0 | 90 | aufgegeben |
| J | Jesus Loves You | 19.07.26 | 5 | 22 | 34 | Sonderfall Shorts |

*H: Ø verzerrt durch einen 27K-Ausreißer (Lehr-Video, nicht Schlaf-Format); Median 52.
Abweichungen zu den Briefing-Zahlen sind in Abschnitt 5 dokumentiert.

---

## 1. MUSS-Regeln

Nur was **beide Gewinner tun UND die Mehrheit der Verlierer nicht tut.**
Checkliste — jedes künftige Video/jede Kanalentscheidung wird dagegen geprüft.

### M1 — Maximal 2 Langform-Uploads pro Woche, Ziel: 1
- [ ] Diese Woche ≤2 Uploads?
- **Beleg (exakte Upload-Daten):** A = 1,3/Woche im aktiven Zeitraum (8 Videos, 08.05.–21.06.),
  B = 1,4/Woche (13 Videos seit 31.05., stabiler ~4-Tage-Rhythmus). **Alle 8 Verlierer liegen
  bei 2,0–13,5/Woche** (C 7,3 · D 7,5 · F 5,8 · G 5,5 · J 13,5 · E 4,3 · H 3,1 · I 2,0).
  n=10, sauberster Trenner im ganzen Datensatz: die Verteilungen überlappen nicht.
- **Ehrliche Randnotiz:** A lädt seit 21.06. nichts mehr hoch, und A's letzte zwei Videos
  fielen auf ~12,6K (vorher 36K–245K). Auch der Musterkanal ist kein Perpetuum mobile.
- **Entscheidung 2026-08-23 — Kadenz bleibt bei 5 Tagen** *(eigene Kanaldaten Gate 2)*.
  Die Frage wurde gestellt, weil eine **Fremdkohorte klar dagegen spricht**: in 74
  Wissenschafts-Schlafkanälen unter 2 Jahren war die Kadenz der stärkste Treiber —
  Median **311 $/Monat** bei 0–1,5 Uploads/Woche gegen **1.770 $** bei 6+.
  **Dagegen steht M1 selbst:** beide Gewinner liegen bei 1,3–1,4/Woche, alle 8 Verlierer
  bei 2,0–13,5, und die Verteilungen überlappen nicht. Ein Dreitagesrhythmus wäre
  2,33/Woche — mitten im Verliererband. Die Fremdkohorte misst außerdem **Monatsumsatz,
  nicht Reichweite je Video** (mehr Videos ergeben mehr Umsatz auch ohne besseres Video)
  und stammt aus einer anderen Nische.
  **Entschieden: bei 5 Tagen (1,4/Woche) bleiben** — auch aus Versuchsdisziplin:
  V05–V08 sollen den Korpuswechsel nach M8 als **einzige** geänderte Variable testen.
  Die Kadenzfrage wird danach aufgemacht, nicht gleichzeitig.

### M2 — Null Shorts auf dem Kanal
- [ ] Kein einziger Short geplant/hochgeladen?
- **Beleg:** A und B: 0 Shorts. 5 von 8 Verlierern mischen 41–82 % Shorts
  (C 45 %, D 42 %, G 82 %, H 41 %, J 81 %). Der Extremfall J beweist, dass Shorts-Reichweite
  nicht überträgt: 856.688 Shorts-Views, 2.210 Subs — und **171 Langform-Views gesamt** (n=5 Videos).

### M3 — Eine Bildwelt, als Serie wiedererkennbar
- [ ] Thumbnail nutzt die EINE Kanal-Bildwelt (gemalter Stil, warme Lichtquelle gegen Nachtblau, wiederkehrendes Motiv)?
- [ ] Ruhige Typo (Serifen, wenige Worte) statt Versalien-Geschrei?
- **Beleg:** B verwendet in 13/13 Thumbnails dasselbe Motiv (schlafender Jesus, weiß-rotes
  Gewand, Lamm, Lagerfeuer) — wie ein Markenlogo. A: eine malerische Welt, 3/8 ganz ohne Text.
  Dagegen G und H: Stil-Zickzack (Fotoreal-Porträt neben Gemälde neben Foto), E: New-Age-Kristalle,
  D: Drohungs-Versalien. 5/8 Verlierer inkonsistent oder genrefremd.
- **Grenze der Regel:** C und F kopieren die Gewinner-Bildwelt und sind trotzdem tot.
  Konsistente Bildwelt ist **notwendig für Kanalidentität, nicht hinreichend für Erfolg** —
  siehe Regel M5 und Abschnitt 4.

### M4 — Titel adressiert den Gefühlszustand des Hörers
- [ ] Titel nennt Zustand („You're Tired", „If You're Anxious", „No More Thinking") + Zusage + „Tonight"?
- **Ausgezählt 2026-08-02:** Zustands-Anker in **9 von 10 Treffern** (>30K). Ein konkreter
  Eigenname (Buch/Kapitel) dagegen nur in **1 von 21** Gewinner-Titeln — bei B in 0 von 13.
  Das steht im Gegensatz zu Lauf 1, wo alle Treffer über 20× einen Eigennamen trugen; dort
  ging es um etablierte Kanäle mit Such-Traffic. **Für einen Neustarter trägt der Zustand,
  nicht der Eigenname.**
- **Beleg:** A 8/8 und B 13/13 Titel folgen dem Zustand-plus-Zusage-Muster. Verlierer-Mehrheit nicht:
  D („GOD SAYS: …" Drohkulisse), E (Frequenz-Titel „963Hz"), H (History-Titel), G gemischt.
- **Grenze der Regel:** C/F kopieren das Muster wörtlich und scheitern — der Titel muss zur
  eigenen Serie gehören, nicht von fremden Kanälen geklaut sein (siehe V3).

### M5 — Skript klingt wie ein Mensch, der MIT dem Hörer spricht
- [ ] Hook in den ersten 60 s: direkte, warme Ansprache in zweiter Person?
- [ ] Bibeltext ist eine echte Übersetzung, KEINE Paraphrase durch KI/Übersetzungstool?
- [ ] Laut vorgelesen: Würde ein Muttersprachler jeden Satz so sagen?
- **Beleg Gewinner:** A: *„Hey child of God, you're safe here."* — B: *„If you're still awake
  tonight, I'm really glad you're here."* Beide binnen 10 Sekunden persönlich.
- **Beleg Verlierer:** C paraphrasiert Psalm 3 maschinell: *„Strike all of my opponents on the
  mandible. Punish the wicked by shattering their teeth"* („mandible" = anatomisch „Unterkiefer";
  echte Übersetzungen: „smite … upon the cheek bone") und produziert Sätze wie *„It is needless
  to move all of your belongings from today to tomorrow."* C's CTA ist erkennbar verstümmelt:
  *„please specify the source of your listening tonight"* (gemeint war „comment where you're
  listening from" — wie bei den Gewinnern). F liefert 3+ Minuten generische Atem-Meditation ohne
  Schriftbezug. D droht (*„Before you scroll away, God wants you to hear this"*). 4/8 Verlierer
  klar generisch/maschinell; bei A+B kein einziger solcher Befund in 4 geprüften Transkripten.

### M6 — Erst das Video tragfähig machen, dann hochladen: Laufzeit ≥ 3,0 h
> **Nachgeschärft 2026-08-02** (Details: `formel/video-formel.md` P2). Schwelle von 2,5 h auf
> 3,0 h angehoben, und die Regel ist ein **Tor, kein Motor**: B #8 hat 3,2 h, dieselbe Serie,
> denselben Thumbnail-Text wie der 166K-Treffer #7 — und 1.300 Views. Innerhalb der Klasse
> ≥3 h liegt die Spanne bei Faktor 297. Länge qualifiziert das Video, sie erklärt den Treffer
> nicht.
- [ ] Video ist mindestens 3,0 h lang (Zielband 3,2–4,0 h)?
- **Beleg:** Alle 11 Videos beider Gewinner mit >30K Views sind ≥3,2 h. B's Breakout fällt
  exakt mit dem Formatwechsel zusammen: Videos #1–6 (31.05.–21.06., 1,1–2,8 h) blieben alle
  <2.600 Views; #7 am 25.06. springt auf 3,4 h und 166K, danach durchgehend 3,2–3,6 h mit
  den Hits 96K/35K/32K. Verlierer F (starr 1,0 h, sd 0,02), I (0,9–1,9 h), J-Langform
  (0,7–3,8 h, tot) liegen fast komplett darunter.
  Deckt sich mit Lauf 1 (Untergrenze ~1,5 h; oberhalb kein Zusatznutzen belegbar) — hier
  liegt die belegte Schwelle der Gewinner-Hits höher, darum konservativ ≥2,5 h.
  Vorsicht: teilweise Auswahleffekt möglich (B wechselte Länge UND Zeitpunkt zugleich, n=1 Kanal).

### M7 — Kanal-Hygiene: Beschreibung, Keywords und Backkatalog gehören zur Nische
- [ ] Kanalbeschreibung + Kanal-Keywords beschreiben AUSSCHLIESSLICH Bibel-Schlaf-Inhalte?
- [ ] Kein themenfremdes Video im Katalog sichtbar?
- **Beleg:** E's About-Seite wirbt bis heute für *„Tibetan Singing Bowls"* (Keywords: „tibetan,
  singing, bowls, healing, music"), während die Videos „Jesus Healing 963Hz" heißen — 40 Subs.
  H's Kanal-Keywords: *„mythology for sleep, greek mythology, history for sleep"*; Atlantis-,
  Trojanisches-Pferd- und WWII-Videos stehen neben Jesus-Content online — Median 52 Views.
  Beide Gewinner: Beschreibung deckungsgleich mit Inhalt (2/2 vs. 2/8 Verlierer mit Altlasten,
  Rest der Verlierer scheitert an anderem).

### M8 — Der Textkorpus muss durchlaufender Erzählstoff sein

> **Die erste Regel dieses Dokuments aus EIGENEN Kanaldaten** — 2026-08-23, Gate 2,
> Quelle *eigene Kanaldaten Gate 2*. M1–M7 stammen aus 10 fremden Kanälen und kennen
> weder Impressionen noch Retention. M8 ist aus beidem gebaut.

- [ ] Hauptkorpus ist **durchlaufender Erzählstoff** — Evangelien, Apostelgeschichte,
      Genesis-Erzählungen?
- [ ] **Spruchsammlungen** (Psalmen, Sprüche, Prediger) und **prophetische Rede** nur als
      Beigabe, nie als Hauptkorpus?
- **Beleg (eigene Kanaldaten Gate 2, n=4 Videos, 2 Retentionskurven):**
  Endretention nach 3,5 Stunden — **V3 Johannes (Erzählung) 14,4 %** gegen
  **V2 Psalmen 90–150 + Sprüche 2,4 %**. **Faktor 6.**

  | | V3 Johannes (Erzählung) | V2 Psalmen + Sprüche |
  |---|---|---|
  | Endretention nach 3,5 h | **14,4 %** | 2,4 % |
  | `relativeRetentionPerformance` Anfang | 0,33 | 0,29 |
  | · Mitte | **0,46** | **0,04** |
  | · Ende | 0,40 | 0,42 |
  | Ø Sehdauer | **36,5 min** | 13,8 min |

  YouTubes `relativeRetentionPerformance` misst gegen ähnlich lange Videos: V2 liegt
  über weite Strecken **im untersten Zwanzigstel** aller vergleichbaren Videos, V3
  durchgehend im Mittelfeld und in der Mitte am stärksten — genau dort, wo eine
  Spruchsammlung auseinanderfällt und eine Erzählung trägt.
  Ø Sehdauer aller vier: V3 36,5 min · V1 17,2 min · V4 14,6 min · V2 13,8 min.
  **V3 allein trägt 55,4 der 69,4 Wiedergabestunden des Kanals — 80 %.**
- **Warum das schwerer wiegt als eine View-Zahl:** Wiedergabezeit ist die Größe, nach
  der YouTube ausliefert. V3 hat mit 1,82 % den zweitschlechtesten CTR des Kanals und
  bekam trotzdem 3.130 der 5.535 Impressionen (Beleg unter Abschnitt 5, Frage 3).
  Der Korpus wirkt nicht über den Klick, sondern über das, was nach dem Klick passiert.
- **Nachtrag 2026-08-23 — M8 hat dabei die Titel-Erklärung überholt.** V3 war zunächst
  als Beleg für den Eigennamen im Titel geführt. Dieselbe CTR-Zahl schlägt aber gegen
  den Titel aus: ein Titel, der zieht, müsste sich **zuerst** im CTR zeigen, und V3's
  CTR ist der zweitschlechteste des Kanals. Die Impressionen folgen damit sparsamer
  erklärt der **Retention** als dem Titel — also M8. Ausgeführt in
  [`formel/video-formel.md`](../formel/video-formel.md) §1, „die sparsamere Erklärung".
  Der Eigenname bleibt Pflicht, aber als billige Konvention ohne belegten Mechanismus.
- **Grenze der Regel — was hier NICHT belegt ist:** n=4, und Retentionskurven liegen nur
  für V2 und V3 vor. **V4 ist Erzählstoff (Matthäus) und kommt trotzdem nur auf 14,6 min
  Ø Sehdauer.** V4 ist allerdings das jüngste Video im Messfenster; der Alterseffekt ist
  nicht abgetrennt. Die Regel steht damit auf **einem Paar** — V3 gegen V2. V1 und V4
  stützen sie nicht unabhängig.
- *Prüfkriterium:* V05–V08 laufen mit Erzählstoff als Hauptkorpus, bei sonst
  unveränderten Parametern (Kadenz, Stimme, Bildwelt, Länge — siehe Entscheidung unter
  M1). Liegt die Endretention dieser vier nicht deutlich über den 2,4 % von V2, war V3
  ein Einzelfall und **M8 wird hier gestrichen, nicht verteidigt.**

---

## 2. DARF-NICHT-Regeln (dokumentierte Todesursachen)

### V1 — Nicht fluten
≥4 Uploads/Woche ist das Muster der toten Grinder: C (7,3/Wo, Ø 39 Views),
D (7,5/Wo, Ø 16), F (täglich, Ø 9), J (13,5/Wo inkl. Shorts). Masse hat in keinem
der 4 Fälle Reichweite erzeugt.

### V2 — Keine Shorts auf dem Langform-Kanal
Todesursache bei G (82 % Shorts, Langform Ø 62) und J (Shorts 857K Views, Langform 171 gesamt).
Shorts-Publikum konvertiert nachweislich nicht zu Langform-Schlafhörern (J: 2.210 Subs, 0 Übertrag).

### V3 — Keine fremden Titel wörtlich kopieren
F kopierte A's 233K-Titel inklusive Tippfehler: *„I Know You're **Tried**... Jesus Watches Over
you Tonight"* — 18 Views. C baut Mashups aus A-Titeln (*„You're tired, I know… Rest to the
Gospel of John"*) — 17 Views. Beide Kanäle tot (Ø 9 bzw. 39). Der Titel-Stil funktioniert nur
als Teil einer eigenen, konsistenten Serie.

### V4 — Keine KI-/MT-paraphrasierte Bibel
C's „mandible"-Psalm (Beleg unter M5) ist die am klarsten dokumentierte Einzeltodesursache:
gewinnergleiche Optik, tote Zahlen. Bibeltext aus einer echten Übersetzung nehmen,
Eigenformulierungen nur für Rahmung/Gebet, von Muttersprachler-Ohr geprüft.

### V5 — Kein Dringlichkeits-/Droh-Framing
D's Rezept — *„YOU WILL LOSE EVERYTHING IF YOU IGNORE… I AM VERY SERIOUS!"*, *„DON'T CLICK
AWAY"*, 7 CTAs im Video, 0,1–0,5 h Länge — erzeugte Ø 16 Views bei 33 Uploads. Das
„God Message"-Genre ist die Anti-These zur Schlaf-Nische: Es erzeugt Anspannung, nicht Ruhe.

### V6 — Keinen umgewidmeten Kanal mit sichtbaren Altlasten nutzen
E (Klangschalen-Beschreibung + 432/963Hz-Hybrid-Titel): Ø 169. H (Mythologie-Keywords +
History-Videos online): Median 52. Wenn umwidmen, dann vollständig: Beschreibung, Keywords,
Backkatalog (löschen/privat), Handle.

### V7 — Nicht vor Video 10 aufgeben, nicht nach Woche 1 urteilen
I lud 4 solide Videos (Optik + Skript in Ordnung), Views stiegen 26 → 106 → 78 → 149 —
und stellte ein. B brauchte **6 Flops** (788/140/304/660/1.800/2.500), bevor #7 mit 166K
einschlug. Wer B's Kurve nicht kennt, hätte B nach Video 6 für einen Verlierer gehalten.

---

## 3. EGAL-Liste (plausibel, trennt aber nachweislich nicht)

| Faktor | Befund | Fallzahl |
|---|---|---|
| **Sprechtempo** | Gewinner 120–160 WPM, Verlierer 141–163 WPM — volle Überlappung. (Nur G fällt mit 36 WPM heraus: anderes Format mit Musiklücken.) | 11 Transkripte |
| **Sprechbeginn** | Alle Kanäle starten in 0,0–3,1 s. Kein Unterschied. | 11 |
| **KJV vs. moderne Übersetzung** | Beide Gewinner modern (0 KJV-Marker/1k Wörter) — aber fast alle Verlierer auch. Nur G nutzt KJV (27,9/1k). Übersetzungswahl trennt nicht; die QUALITÄT der Übersetzung schon (→ V4). | 11 |
| **Kanalalter** | A-Konto 6 Monate alt: gewinnt. B-Konto 9 Jahre alt (2017!): gewinnt — aber erst nach 6 Flops, Alter hat nichts beschleunigt. G seit Januar, E frisch: beide tot. | 4 |
| **Thumbnail-Handwerk allein** | C (gewinnergleiche Optik) und I (saubere Serie) sind trotzdem tot. | 2 Gegenbeispiele |
| **Genaue Hit-Länge oberhalb der Schwelle** | Gewinner-Hits liegen bei 3,2–5,0 h ohne erkennbares Optimum darin. Deckt sich mit Lauf 1 (rho +0,09). | 11 Hit-Videos |
| **Tags** | A: 0 Tags auf allen 8 Videos. B: Tags NUR in der Flop-Phase (5–22 Tags auf den Videos mit 140–2.567 Views), **0 Tags auf allen drei Hits** (166K/96K/35K) — B hat Tags beim Breakout abgelegt. Tags korrelieren hier sogar negativ. | 19 Videos |
| **Kapitelmarken** | A's drei größte Hits (245K/233K/201K): KEINE Kapitel. B: Kapitel in allen 11 geprüften Videos (40–93 Stück, Psalm für Psalm). Beide Muster gewinnen. | 19 |
| **Untertitelspur** | 0 von 19 Gewinner-Videos hat eine Caption-Spur — die 0-von-8-Lücke aus Lauf 1 gilt auch bei den Neustartern. Kein Erfolgsfaktor, bleibt aber unsere unbesetzte Chance (Discoverability). | 19 |

---

## 4. HYPOTHESEN (plausibel, bei n=2 nicht beweisbar)

**H1 — Die ≥3h-Schwelle ist kausal, nicht nur korreliert.**
B's Breakout fiel mit dem Sprung auf 3,4 h zusammen — aber B wechselte gleichzeitig
Woche und Thumbnail-Feinheiten. *Prüfkriterium: Eigene Videos abwechselnd 2,5 h und 3,5 h
produzieren; wenn nach 10 Videos die ≥3h-Gruppe >2x Median-Views hält, bestätigt.*

**H2 — Textarme Thumbnails schlagen textreiche.**
A's zwei beste Videos (245K, 233K) tragen keinen bzw. minimalen Text; B's Serie trägt
Versalien und gewinnt auch. Widersprüchlich bei n=2. *Prüfkriterium: A/B-Test über
YouTube-Thumbnail-Test ab Kanalstart; Entscheid nach 10 Videos per CTR.*

**H3 — Früher Community-CTA („comment where you're listening from") wirkt.**
A Top1 und B Top2 bringen ihn binnen 40 s; A Top2 und B Top1 haben KEINEN CTA — beide
Varianten gewinnen. Die toten Kanäle D (7 CTAs) und C (4, verstümmelt) übertreiben oder
verpatzen ihn. *Prüfkriterium: eigene Videos mit/ohne Community-CTA vergleichen
(Kommentarrate + Views nach 30 Tagen).*

**H4 — Ein-Szenen-Loop schlägt Szenen-Rotation.**
Gewinner-Stichproben (Lauf 1: A, B; heute bestätigt an B #3: ein statisches Gemälde,
einzige Bewegung Feuerflackern, 2:30 ohne Schnitt) zeigen EINE Szene; der tote C
rotiert 8 Szenen, G schneidet Stock-Footage. *Prüfkriterium: ab Video 10 einmal
Szenen-Rotation testen; Retention-Kurven vergleichen.*

**~~H5 — Die Stimme ist der verdeckte Unterschied zwischen C und den Gewinnern.~~
WIDERLEGT am 2026-08-03** (6 Audio-Stichproben à 80 s, Details in
`regeln/daten/stimm_stichprobe.json`).

Die Stimme trennt nicht. Verlierer C nutzt praktisch dasselbe Profil wie die Gewinner:
tiefe, resonante, stark behauchte Männerstimme, langsam-meditativ, close-mic, Ambient-Pad,
Stimme klar über dem Bett. Alle drei Gewinner sind **synthetisch** (hohe Konfidenz) — KI-Stimme
trägt nachweislich bis 245.000 Views. Der einzige im Test **menschlich** gesprochene Kanal (G)
ist ein Verlierer mit 156 Views.

Übrig bleibt ein enger, anderer Befund: C hat als einziger **Wortbetonungsfehler**
(„solace" als so-LACE, „supervise" als super-VISE). Das ist Aussprache-QA an ungeprüftem
Maschinen-Output — dieselbe Wurzel wie C's MT-paraphrasierte Bibel (V4), kein Stimmmodell-Problem.
Als Regel gehört es zu V4, nicht in eine eigene Stimm-Hypothese.

> ### 2026-08-23 — V01 bis V04 verletzen die einzige harte Abmisch-Regel
>
> Dieselbe Stimm-Stichprobe vom 2026-08-03 hat **einen** Befund geliefert, der als
> Abmisch-Regel taugt: *Stimme in 6/6 Fällen klar über dem Bett — Musik verschluckt sie
> nie.* Das ist die einzige, die die Gewinnerdaten überhaupt hergeben; die Zahl 12 dB
> ist daraus abgeleitet, nicht gemessen.
>
> **Die eigenen Videos halten sie nur in Mono ein.** Gemessen am 2026-08-23:
>
> | | Bett | Stimme | Abstand |
> |---|---|---|---|
> | Mono-Summe (Handy, TV — 80 % des Publikums) | −31,0 dBFS | −19,0 dBFS | **12,0 dB** ✓ |
> | je Kanal (Kopfhörer, Tablet, Desktop) | −25,8 dBFS | −19,0 dBFS | **6,8 dB** ✗ |
>
> Ursache ist der Stereoaufbau des Klangbetts, nicht die Pegelwahl: `bett_pad_feuer.flac`
> trug R als L um 240 Samples versetzt, verlor dadurch beim Mono-Downmix 5,2 dB — und die
> Pipeline normierte auf genau diesen Downmix. Die Stimme wird identisch in beide Kanäle
> addiert und verliert nichts. Ausgeführt in
> [`formel/video-formel.md`](../formel/video-formel.md) §5b.
>
> **Warum es niemandem auffiel:** Gate 1, Prüfung 1.11 hat den Mono-Wert gemessen und
> 12,0 dB gemeldet. Der Wert war richtig — er war nur nicht der einzige. Seit 2026-08-23
> prüft 1.11 beide Fälle, und das alte Bett fällt damit durch.
>
> **Nicht reparierbar:** V01–V04 sind mit diesem Bett gerendert und veröffentlicht. Ab
> V05 gilt das korrigierte Bett (`bett_mono_feuer_leise.flac`, echt mono). Ob der Fehler
> etwas gekostet hat, ist aus diesen Daten nicht zu sehen — mit 6,8 dB steht die Stimme
> immer noch über dem Bett, nur weniger deutlich als beabsichtigt.

**H6 — Wenige CTAs (0–2) sind Teil des Gewinner-Musters.**
Gewinner: 0–2 CTAs pro Video. Tote: C 4, D 7, H 3. Überlappt mit Genre-Problemen —
nicht isolierbar. *Prüfkriterium: eigene Videos konstant ≤2 CTAs; nur ändern, wenn
Kommentarrate nach 20 Videos unter Benchmark liegt.*

---

## 5. OFFENE FRAGEN (wo die Daten schweigen)

1. ~~**Stimmcharakter der Gewinner**~~ — **erledigt am 2026-08-03.** 6 Audio-Stichproben
   (3 Gewinner, 3 Verlierer) je 80 s aus der Videomitte. Ergebnis unter H5 und in
   `regeln/daten/stimm_stichprobe.json`. Kurz: alle Gewinner synthetisch, Profil deckungsgleich
   mit den Verlierern C und F, der einzige menschliche Sprecher (G) ist ein Verlierer.
   Ebenfalls dabei erstmals gemessen: **Musikbett** — Ambient-Synth-Pad bei 3/3 Gewinnern
   (und 3/3 Verlierern, also Tischeinsatz), knisterndes Lagerfeuer bei 2/3 Gewinnern,
   Grillen nur bei Verlierern. Weder „Delta-Wellen" noch „Klavier+Regen" aus dem Briefing
   hörbar bestätigt.
2. **Externe Traffic-Quellen** (Community-Posts, Social, Embeds): mit den verfügbaren
   Tools nicht abrufbar. A's „ministry"-Framing + Spendenlink deutet auf Community-Pflege,
   beweist aber keinen Traffic.
3. **Impressions/CTR:** Ohne YouTube-Analytics-Zugriff auf fremde Kanäle bleibt unbeweisbar,
   ob C an der Klickrate (Thumbnail/Titel im Feed) oder an der Retention (Stimme/Skript)
   stirbt. Die eigenen Kanaldaten werden diese Lücke ab Video 1 schließen.
   > **Teilantwort 2026-08-23 (eigene Kanaldaten Gate 2).** Für *fremde* Kanäle bleibt die
   > Frage offen — für den eigenen zeigt sie in Richtung Retention. V3 hat mit **1,82 %**
   > den zweitschlechtesten CTR des Kanals und bekam trotzdem **3.130 von 5.535
   > Impressionen**, 91 von 151 Aufrufen und 1 von 2 Abonnenten. Ausliefern nach
   > Wiedergabezeit schlägt hier Klickrate. Der Kanal-CTR von 2,71 % ist bei 5.535
   > Impressionen ohnehin keine belastbare Größe. Ausgeführt in
   > [`formel/thumbnail-checkliste.md`](../formel/thumbnail-checkliste.md),
   > Abschnitt „Was diese Analyse nicht beantwortet".
4. **D's fehlende Videos:** Briefing nennt 49 Uploads, auffindbar sind 33 — vermutlich
   gelöscht. Ob D löscht, was floppt, ist nicht feststellbar.
5. **Warum A ohne Anlauf traf und B 6 Videos brauchte:** A war mit Video #1 am 08.05.
   (201K) der Erste im Stil; B startete 23 Tage später (31.05.) mit eigener Handschrift,
   floppte 6 Videos lang und traf am 25.06. mit #7. Ob A's Sofort-Erfolg First-Mover-Timing,
   Zufall oder externer Push war — nicht entscheidbar. **Nicht kopierbar:** A's
   Zeitvorsprung. **Kopierbar:** B's Weg — eigene Handschrift im bewährten Format plus
   Durchhalten bis mindestens Video 10 (V7).
6. **Upload-Datumspräzision:** Daten älterer Videos sind monatsgebuckelt („2 months ago");
   Reihenfolgen innerhalb der Kanäle sind verlässlich, Wochengenauigkeit bei älteren
   Uploads nicht.
7. **Gewinner-Metadaten:** Vollerhebung liegt vor für 19 von 21 Videos (2 B-Videos fehlen,
   Datensammlung brach am Tool-Session-Limit ab; Ergebnisse in Abschnitt 3 eingearbeitet).
8. **Wie viel der Fernseher trägt** — *2026-08-23 erstmals gemessen, aber n=1 Kanal und
   n=4 Videos.* Beim eigenen Kanal liefert der Fernseher **12 % der Aufrufe und 30 % der
   Wiedergabezeit** (70,4 min gegen 23,0 min am Handy). Ob das ein Merkmal der Nische ist
   — 3,5-Stunden-Material läuft am TV eher durch als am Handy — oder eine Eigenheit dieser
   vier Videos, ist aus einem Kanal nicht entscheidbar. Der Fremddatensatz kennt keine
   Gerätedaten, also gibt es nichts zum Vergleichen.
   *Prüfkriterium:* wenn V05–V08 denselben TV-Anteil zeigen, ist es ein Nischenmerkmal
   und gehört in die Produktionsentscheidungen (Bildqualität auf großen Schirmen).
9. **A's Pause:** A lädt seit 21.06. nicht mehr hoch, letzte zwei Videos fielen auf ~12,6K.
   Ob Sommerpause, Burnout oder Strategiewechsel — unbekannt. Beobachten: Wenn A zurückkommt
   und wieder trifft, spricht das für Katalog-Langzeitwirkung statt Upload-Momentum.

---

## Abgleich mit Lauf 1 (`teardown/produktions-spec.md`)

**Bestätigt:** Laufzeit-Untergrenze (dort ~1,5 h; hier liegen die Gewinner-Hits sogar ≥3,2 h) ·
Stimme läuft durch · moderne, direkte Ansprache · dunkle Nachtpalette mit warmer Lichtquelle ·
Ein-Motiv-Bildwelt · Tags/Untertitel sind kein Erfolgsfaktor.
**Präzisiert:** Lauf 1 fand „Länge oberhalb 1,5 h egal" über etablierte Kanäle; die
Neustarter-Daten deuten auf eine höhere wirksame Schwelle (~3 h) beim Kanalaufbau — als M6
konservativ mit 2,5 h angesetzt, als H1 zu validieren.
**Neu und nur hier:** Kadenz-Regel (M1), Shorts-Verbot (M2), Kopier-Verbot (V3),
MT-Paraphrase-Verbot (V4), Durchhalte-Regel (V7).
**Kein Widerspruch gefunden.**

**Aus keinem der beiden Läufe, sondern aus eigenen Daten (2026-08-23):** die
Korpus-Regel **M8**. Weder Lauf 1 noch Lauf 2 konnten sie finden — beide sehen nur
Views, und M8 hängt an Retention und Wiedergabezeit. Ein Widerspruch zu Lauf 1
entsteht nicht, aber eine Einschränkung: die dort belegten Anker-Werte für
`Psalms` (0,26–1,38×, n=32) sind View-Werte etablierter Kanäle und sagen nichts
darüber, wie lange jemand zuhört.

---

*Rohdaten: `regeln/daten/` (Kataloge, About-Seiten, Kadenz, Skript-Anatomie mit Zitaten,
Thumbnail-Forensik, Kontaktbögen `sheet_GEWINNER.png` / `sheet_VERLIERER.png`,
Stimm-Stichproben-Notizen). Analyse-Population Lauf 1: `teardown/`.*
