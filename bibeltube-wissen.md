# BibelTube — Wissensstand

Die vier Arbeitsdokumente, ungekürzt aneinandergehängt.
**Erzeugt am 23.08.2026 von `produktion/wissen_zusammenstellen.py`** — nicht von Hand
pflegen, sondern neu bauen.

1. `regeln/erfolgsregeln.md`
2. `formel/video-formel.md`
3. `formel/thumbnail-checkliste.md`
4. `produktion/videos-01-08.md`

> **Momentaufnahme, keine Quelle.** Verbindlich sind immer die vier Originaldateien.
> Wer hier liest und etwas ändern will, ändert das Original und lässt diese Datei
> danach neu erzeugen.
>
> Der Text ist wörtlich übernommen. Einzige Abweichung: **relative Links sind auf die
> Repo-Wurzel umgeschrieben**, damit sie aus dieser Datei heraus funktionieren; in den
> Originalen stehen sie relativ zum jeweiligen Ordner.

---

# regeln/erfolgsregeln.md

---

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
> [`produktion/workflow-gates.md`](produktion/workflow-gates.md), Gate 2 — CTR,
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
  [`formel/video-formel.md`](formel/video-formel.md) §1, „die sparsamere Erklärung".
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
   > [`formel/thumbnail-checkliste.md`](formel/thumbnail-checkliste.md),
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
8. **A's Pause:** A lädt seit 21.06. nicht mehr hoch, letzte zwei Videos fielen auf ~12,6K.
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

---

# formel/video-formel.md

---

# Video-Formel v2.2 — Arbeitsdokument

> **Stand: 2026-08-23.** v2.1 = deine v2, Element für Element gegen die **Fremd**daten
> geprüft (2026-08-02). **v2.2 = die erste Revision aus eigenen Kanaldaten.**
> Datengrundlage: `regeln/daten/` (21 Gewinner-Videos aus 2 Kanälen, 129 Verlierer-Videos aus
> 8 Kanälen, 19 Voll-Metadatensätze, 4 Gewinner-Transkripte, 90 Thumbnails) plus
> `teardown/produktions-spec.md` (454 Videos, 8 etablierte Kanäle) und `regeln/erfolgsregeln.md`.
>
> **Vor jedem Rendern:** [`produktion/workflow-gates.md`](produktion/workflow-gates.md)
> fasst die harten Prüfungen dieses Dokuments als Gate 1 zusammen — Kernregel dort:
> *kein Rendering, bevor Titel und Thumbnail stehen.* Gate 2 ersetzt nach Video 4
> Fremdbefunde durch eigene CTR- und Retention-Daten.
>
> **2026-08-23 — Gate 2 ausgewertet, eigene Zahlen eingearbeitet.** Kanal
> *The Nightly Word*, 4 Videos, 25.07.–22.08.2026: 151 Aufrufe, 69,4 Wiedergabestunden,
> 5.535 Impressionen, CTR 2,71 %, 2 Abonnenten.
> Geändert: **§1** (Eigenname von Testreihe zu Pflicht) · **§4** (Korpus-Regel M8 neu) ·
> **§6** (Kadenz-Entscheidung) · **§7** (Traffic-Quellen) · **§9** (Anfangsabfall als
> Beobachtung, Eigennamen-Frage geschlossen) · **§10** (Eigennamenliste ist keine
> Testreihenliste mehr).
> Jede dieser Stellen trägt die Marke *eigene Kanaldaten Gate 2* und ein Datum; alles
> **ohne** diese Marke stammt weiterhin aus den 10 Fremdkanälen. Rohwerte:
> `regeln/daten/gate2_eigene_kanaldaten.json`.
>
> **Status: Qualifikations-Checkliste, kein Hit-Rezept.** Beleg: B #7 und #8 unterscheiden sich
> in keiner messbaren Variable und um Faktor 128 in den Views. Erfüllung verhindert Scheitern,
> garantiert keinen Treffer. Planungsgröße: 10 von 21 Gewinner-Videos über 30.000 Views —
> jeder zweite bis dritte.

## Prüfprotokoll v2 → v2.1

| # | Element | Verdikt |
|---|---|---|
| 1 | Zustands-Anker als Pflicht | **bleibt** — 9/10 Treffer |
| 2 | „Tonight" im Pflichtmuster | **schärfen** — nur 6/10 Treffer |
| 3 | Deine drei Titel-Beispiele | **schärfen** — alle drei aus meiner *ungeprüft*-Liste |
| 4 | „Gospel of John = zweitbestes Video" | **Faktenfehler** — es ist A's **bestes** (245K) |
| 5 | Verbot: Zustand in 8 Videos wiederholen | **RAUS — widerlegt**, der Wiederholer war der 166K-Durchbruch |
| 6 | Verbot: „Psalm" als Anker | **schärfen** — 2 von B's 4 Treffern tragen Psalms |
| 7 | Länge ≥3,0 h, Tor statt Motor | **bleibt** unverändert |
| 8 | „3,0–3,5 h Kostenoptimum" | **schärfen** — Treffer-Median liegt bei 3,6 h |
| 9 | Eingangsgebet 400 Wörter als PFLICHT | **umetikettieren** — Policy-Absicherung, kein Reichweiten-Beleg |
| 10 | World English Bible | **schärfen** — Gewinner nutzen NIV; klassische WEB sagt „Yahweh" |
| 11 | „Kanal C: 256 Ø-Views bei 64 Videos" | **Faktenfehler** — gemessen: Ø 39 bei 35 Langform-Videos |
| 12 | Klangbett-Signatur als Regel | **umetikettieren** — vollständig ungemessen, gehört nach §9 |
| 13 | „Echte Tags gesetzt" | **Widerspruch** — kein Gewinner tut das |
| 14 | Kapitelmarken als Pflicht | **schärfen** — A's drei größte Treffer haben null |
| 15 | „Bildkonzept unbekannt" | **Faktenfehler** — bestdokumentierter Teil des Datensatzes |
| 16 | Thumbnail-Serie | **fehlt komplett** — war MUSS-Regel M3 |

---

## 1. TITEL

**PFLICHT — Zustands-Anker in Du-Ansprache.** 9 von 10 Treffern (>30K). Einzige Ausnahme ist
A's schwächster Treffer („Come Little Lamb", 47K).

**Muster:** `[Gefühlszustand] + [Zusage mit Jesus/Gott]`, „Tonight" **optional**.
> *Korrektur zu v2:* „Tonight" steht in **6 von 10** Treffern, nicht in allen. A's 184K-Video
> heißt schlicht **„Lord, I Feel Tired"** — kein „Tonight", keine Handlung, nur der Zustand.
> B's Treffer #11 (35K) und #12 (32K) haben ebenfalls kein „Tonight". Nimm es als häufiges
> Element, nicht als Pflichtbestandteil.

**Verwende zuerst die 13 belegten Anker** (Abschnitt 10). Deine drei v2-Beispiele
(*„If Your Mind Won't Stop Tonight…"*, *„When Tomorrow Feels Too Heavy…"*, *„I Know Today Took
Everything…"*) stammen alle aus meiner **ungeprüft**-Liste — nie von einem Gewinner verwendet.
Sie sind plausibel, aber es gibt 13 Anker mit Beleg; die gehören zuerst ins Rennen.

**PFLICHT (seit 2026-08-23) — Eigenname in JEDEM Titel.**

> **~~TESTREIHE (ungeprüft, ~jedes 4. Video): Eigenname ergänzen.~~ — ersetzt.**
> Die Testreihe ist gelaufen und **bestätigt, aber aus einem anderen Grund als vermutet**
> *(eigene Kanaldaten Gate 2, 2026-08-23)*.
>
> V3 ist das einzige der vier eigenen Videos mit einem Eigennamen im Titel („Gospel of
> John") und hält **3.130 von 5.535 Impressionen, 91 von 151 Aufrufen und 1 von 2
> Abonnenten** — bei einem CTR von 1,82 %, dem zweitschlechtesten des Kanals.
>
> **Der Wirkungsweg ist nicht die Suche.** Die Traffic-Quellen zeigen **null
> Suchverkehr** (YouTube-Suche: 0 Aufrufe in 28 Tagen, kanalweit — Tabelle in §7). Der
> Eigenname wirkt über die **kontextliche Zuordnung im Vorschlagsband**: er sagt dem
> Empfehlungssystem, neben welche Videos dieses gehört. Genau deshalb gehört er in
> **jeden** Titel und nicht in jeden vierten — ein Zuordnungssignal wirkt nicht als
> Stichprobe.
>
> **Der Zustands-Anker bleibt Pflicht — das ist ein UND, kein ODER.** V3 trägt beides:
> *„If You're Overwhelmed, Let the Gospel of John Quiet Your Mind"*.
>
> **Was diese Daten NICHT hergeben:** ein eigenes Video mit Eigennamen gegen drei ohne.
> V3 unterscheidet sich zusätzlich im **Korpus** (Erzählstoff statt Spruchsammlung, M8) —
> Eigenname und Erzählstoff sind hier **nicht getrennt**, dasselbe Video trägt beides.
> V05–V08 tragen ebenfalls beides und stellen die Trennung damit auch künftig nicht her.
> Sie entstünde erst durch ein Erzählvideo **ohne** Eigennamen im Titel — und dieser
> Test steht hinter dem Korpuswechsel an, nicht neben ihm (eine Variable pro Runde).
> Der frühere Einwand bleibt formal richtig: 20 von 21 Gewinner-Titeln kommen ohne
> Eigennamen aus. Die eigenen Impressionen schlagen ihn trotzdem — Gate 2, Kernregel.
>
> *Faktenkorrektur aus v2.1, weiterhin gültig:* *„If You're Anxious, Rest to the
> **Gospel of John** Tonight"* ist mit 245.000 Views A's **bestes** Video, nicht das
> zweitbeste.

> ### Einschränkung, nachgetragen am 2026-08-23: die sparsamere Erklärung
>
> *(eigene Kanaldaten Gate 2 — diese Einschränkung schwächt die Regel darüber
> bewusst ab, statt sie zu verteidigen.)*
>
> Die 3.130 Impressionen von V3 sind oben als Argument **für** den Eigennamen
> geführt. Sie können aber genauso gut die **Folge der besseren Retention** sein
> statt die Folge des Titels. YouTube liefert nach Wiedergabezeit aus — und V3 trägt
> 80 % der Kanal-Wiedergabezeit (M8).
>
> **Was die Zahlen ausschließen und was nicht.** Drei Erklärungen stehen im Raum:
>
> | | Kette | Status |
> |---|---|---|
> | A | Eigenname → attraktiverer Titel → **höhere Klickrate** → mehr Impressionen | **widerlegt** |
> | B | Eigenname → bessere kontextliche Zuordnung → mehr Impressionen | möglich, **unbelegt** |
> | C | Erzählstoff → mehr Wiedergabezeit → mehr Impressionen | möglich, **belegt** (M8) |
>
> **A fällt, und zwar an einer einzigen Zahl:** V3 hat mit **1,82 %** den
> *zweitschlechtesten* CTR des Kanals. Ein Titel, der zieht, müsste sich **zuerst
> im CTR zeigen** — dort und nirgends sonst wirkt ein Titel unmittelbar. Er tut es
> nicht. Damit ist die naheliegendste Lesart des Befunds erledigt.
>
> **B und C trennen die eigenen Daten nicht.** Beide sagen dasselbe voraus, was man
> sieht: viele Impressionen bei unauffälligem CTR. Aber sie sind nicht gleich gut
> gestützt — **C beruft sich auf einen Mechanismus, der hier gemessen ist**
> (Retention, Faktor 6, M8), **B auf einen zusätzlichen, der es nicht ist.** Nach
> dem sparsameren Prinzip gewinnt C.
>
> **Was daraus folgt:**
> - **Der Eigenname bleibt Pflicht** — er kostet nichts, er ist plausibel, und er
>   wegzulassen würde eine Variable ändern, ohne dass etwas dafür spräche.
> - **Er ist aber kein belegter Hebel, sondern eine billige Konvention.** Wer diese
>   Regel liest, soll nicht glauben, hier sei ein Wirkmechanismus nachgewiesen.
> - **Der belegte Hebel dieses Kanals ist M8, nicht der Titel.** Wenn Arbeitszeit
>   zwischen Titelfeilen und Korpuswahl verteilt wird, gehört sie in den Korpus.
> - Getrennt würden B und C erst durch ein Video mit Erzählstoff **ohne** Eigennamen
>   im Titel. Das steht hinter dem Korpuswechsel an — eine Variable pro Runde.

**VERBOTEN — belegt:**
- Titel von Konkurrenten wörtlich übernehmen. Kanal F kopierte A's 233K-Titel inklusive
  Tippfehler („I Know You're **Tried**…") → 18 Views.

**~~VERBOTEN: Gefühlszustand innerhalb von 8 Videos wiederholen~~ — GESTRICHEN, widerlegt.**
> Die Daten sagen das Gegenteil. B #4 *„No More Thinking Tonight… Jesus Is With You"* (660 Views)
> und B #7 *„No More Thinking Tonight… Rest With Jesus"* (**166.000**) tragen denselben Anker,
> drei Videos auseinander — **die Wiederholung war der Durchbruch.** Bei A wiederholt sich
> „You're Tired, I Know" in #1 (201K) und #7 (12K), „I Know You're Tired" in #4 (233K).
> Ein bewährter Anker ist wiederverwendbar; die Streuung liegt woanders.

**„Psalm" als Anker — entschärft.**
> Der Wert 0,26–1,38× stammt aus **Lauf 1** (etablierte Kanäle). Bei B tragen **2 von 4 Treffern
> Psalms im Titel**: #10 „Stop Thinking For A Moment, Sleep To These Psalms Tonight" (96K) und
> #12 „Don't Go to Sleep Worried… Let These Psalms Calm Your Heart" (32K). Ein Psalms-Verbot
> hätte B's zweitgrößten Treffer verhindert. Die tatsächliche Regel ist bereits als PFLICHT
> abgedeckt: **nie ohne Zustands-Anker.** B #3 „Sleep To THESE Psalms And See What God Does"
> (304 Views) ist genau der Fall ohne Zustand.
>
> *Ergänzung 2026-08-23 (eigene Kanaldaten Gate 2):* Der Punkt ist durch **M8** praktisch
> stillgelegt. Psalms bleiben als Anker erlaubt — aber der Titel benennt den Korpus, und
> Psalmen dürfen nicht mehr Hauptkorpus sein. Ein Psalms-Titel ohne Psalmen-Korpus wäre
> eine Falschauskunft an Zuschauer und Empfehlungssystem. Also: bis auf Weiteres kein
> Psalms-Anker.

---

## 2. LÄNGE

**Harte Untergrenze 3,0 h.** Kein Video unter 3 h je über 2.500 Views (n=6); alle 10 Treffer
≥3,2 h. Natürliches Experiment: fast identischer Titel bei 1,2 h = 660 Views, bei 3,4 h = 166.000.

**Tor, kein Motor.** ≥3 h garantiert nichts — Spanne innerhalb der Klasse: Faktor 297.

> *Schärfung zu v2:* Die Treffer liegen bei **3,4–5,0 h, Median 3,6 h**. Nur 3 von 10 sind
> ≤3,5 h. Dein Band 3,0–3,5 h ist als **Kostenentscheidung** vertretbar, liegt aber an der
> Unterkante dessen, wo die Treffer tatsächlich sitzen. Ein Zielband von **3,4–3,8 h** trifft
> die Datenlage besser, bei ~46.500 Zeichen TTS je Stunde also rund 160.000–177.000 Zeichen.
> Eine Obergrenze ist weiterhin nicht belegt (A trifft auch bei 5,0 h).

---

## 3. AUFBAU

**PFLICHT — Sprache beginnt in Sekunde 0–3.** Kein Musikintro, kein Logo, kein Vorspann.
(n=24 aus Lauf 1: 0,0–3,4 s; Gewinner 0,1–3,1 s.)

**PFLICHT — Sprachanteil 97–100 % der Lauftzeit**, längste Pause <20 s. (n=24.)

> **2026-08-06 — kalibriert, nicht gestrichen (n=3 eigene Videos).** Die Regel
> bleibt stehen; die Warnschwelle der Pipeline liegt jetzt bei 95,0 % statt
> 97,0 % (`config.md`, `sprachanteil_min_pct`).
>
> | | Sprachanteil (vergleichbar) | längste Pause |
> |---|---|---|
> | Video 01 | 95,6 % | 1,42 s |
> | Video 02 | 95,3 % | 1,38 s |
> | Video 03 | 95,3 % | 1,46 s |
>
> Drei Videos, dreimal derselbe Abstand von rund 1,5 Punkten zur 97-%-Marke —
> bei längsten Pausen von unter 1,5 Sekunden gegen eine Grenze von 20. Ein
> Video, dessen längste Stille anderthalb Sekunden dauert, hat keinen
> Leerlauf; die 95,3 % entstehen aus rund 4.900 kurzen Atempausen von je 0,25
> bis 0,4 s, nicht aus Löchern.
>
> **Was hier belegt ist und was nicht:** Gemessen sind die drei Werte oben.
> **Nicht** gemessen ist, wie die 97 % aus Lauf 1 zustande kamen — die
> Messmethode der 24 Konkurrenzvideos ist unbekannt, es gibt keinen
> gemeinsamen Prüfkörper. Dass die eigene Hüllkurvenmessung „1,5 Punkte
> strenger liest", ist deshalb die **plausibelste Erklärung des systematischen
> Abstands, kein nachgewiesener Messversatz**. Wer das sauber klären will,
> müsste ein Konkurrenzvideo durch dieselbe Messung schicken und die Werte
> vergleichen.
>
> Die eigentliche Schutzregel gegen Leerlauf ist und bleibt die
> **20-Sekunden-Pausengrenze**. Sie ist eindeutig definiert, unabhängig von
> der Hüllkurvenschwelle und wird mit Faktor 13 unterschritten.

**NICHT belegt: festes Schema Hook→CTA→Gebet→Lesung.** Frei gestaltbar. A's zweitgrößtes
Video (233.704 Views) startet nach 2,1 s kalt mit „John chapter 15" — ohne Rahmung, ohne CTA.

**CTA: maximal 2 pro Video.** (Gewinner 0–2; tote Kanäle 4–7.)

**Eigenes Eingangsgebet, ~400 selbst geschriebene Wörter — umetikettiert.**
> Das ist eine **Geschäfts-/Policy-Entscheidung, kein Reichweiten-Element.** Kein Datenbeleg
> dafür, dass eigener Text Views bringt — im Gegenteil: A's 233K-Video enthält **null** eigene
> Rahmungsworte, und die Rahmungen der übrigen Gewinner sind mit 53–243 Wörtern deutlich kürzer
> als 400. Als Absicherung der Monetarisierung gegen „inauthentic content"-Kriterien ist es
> nachvollziehbar und kostet fast nichts — aber es gehört unter Geschäftsentscheidungen (§8),
> nicht unter datenbelegte Pflicht. **Ich kann die aktuelle YPP-Richtlinienlage aus diesem
> Datensatz nicht verifizieren**; wenn das die Begründung trägt, lass sie uns separat gegen die
> Originalrichtlinie prüfen statt gegen Kanaldaten.

---

## 4. TEXT

> **Korpusart — neu geregelt am 2026-08-23, siehe M8 in
> [`regeln/erfolgsregeln.md`](regeln/erfolgsregeln.md)** *(eigene Kanaldaten Gate 2)*.
> Der **Hauptkorpus muss durchlaufender Erzählstoff sein** — Evangelien,
> Apostelgeschichte, Genesis-Erzählungen. **Spruchsammlungen** (Psalmen, Sprüche,
> Prediger) und **prophetische Rede** nur als Beigabe, nie als Hauptkorpus.
> Beleg: Endretention nach 3,5 h bei den eigenen Videos — V3 Johannes 14,4 % gegen
> V2 Psalmen+Sprüche 2,4 %, **Faktor 6**, dazu 80 % der Kanal-Wiedergabezeit auf V3.
> Dieses Dokument hatte zur Korpusart bis dahin **nichts** zu sagen, und das war kein
> Versehen: Fremddaten geben sie nicht her, weil aus ihnen nur Views ablesbar sind.

**Wörtlich gelesen, niemals maschinell paraphrasiert.** Todesursache bei Kanal C:
*„Strike all of my opponents on the mandible."*
> *Faktenkorrektur:* C hat gemessen **Ø 39 Views bei 35 Langform-Videos**. Die Zahlen „256 Ø bei
> 64 Videos" stammen aus deinem Ursprungsbriefing und enthalten 29 Shorts. Der Befund wird
> dadurch eher stärker, nicht schwächer.

**Übersetzung — wichtige Schärfung gegenüber v2.**

Die Gewinner lesen **NIV**, über vier Videos eindeutig belegt an übersetzungsspezifischen
Formulierungen:

| Stelle | Gewinner-Wortlaut | NIV | WEB (klassisch) |
|---|---|---|---|
| Joh 15,1 | „my Father is the **gardener**" | gardener | farmer |
| Ps 91,1 | „**Whoever dwells in the shelter**" | ebenso | „secret place" |
| Ps 23,1 | „**I lack nothing**" | ebenso | „I shall lack nothing" |

Deine Wahl **World English Bible ist juristisch der sichere Weg** (gemeinfrei; NIV ist
urheberrechtlich geschützt, und 3 h Volltext-Audio kommerziell ist kein Zitat mehr). Das ist
ein guter Grund, bewusst von den Gewinnern abzuweichen.

**Aber: nimm die British Edition (WEBBE), nicht die klassische WEB.** Die klassische WEB
übersetzt den Gottesnamen im Alten Testament durchgehend als **„Yahweh"** — aus
*„The LORD is my shepherd"* wird *„Yahweh is my shepherd"*. Über 3 Stunden Psalmen ist das ein
deutlich anderes Register als alles, was die Gewinner und die Nische sonst tun. Die **World
English Bible British Edition** ist textgleich, verwendet aber „LORD"/„GOD". ([Quelle](https://ebible.org/details.php?id=eng-web), [Übersicht](https://worldenglish.bible/))

**Ungeprüft bleibt**, ob WEBBEs formellerer Ton („thee/thou" hat sie nicht, aber sie liegt
näher an der ASV als am NIV) bei diesem Publikum gleich gut trägt. Prüfkriterium in §9.

---

## 5. BILD *(in deiner v2 komplett ausgefallen — das ist die größte Lücke)*

Das Bildkonzept steht **nicht** unter „offen": Es ist der bestdokumentierte Teil des ganzen
Datensatzes (11 multimodale Stichproben aus Lauf 1, 4 Szenenanalysen aus Lauf 2, 90 Thumbnails).
Nur der `frames/`-Ordner blieb wegen 403 leer — die Frage selbst ist beantwortet.

> **Motiv-Auswertung aller 90 Thumbnails (2026-08-04): [`thumbnail-motive.md`](formel/thumbnail-motive.md).**
> Kernergebnis: Das Motiv ist als Erfolgshebel **widerlegt** (C und F tragen das
> Gewinnermotiv bei ≤113 Views); alle 10 Treffer teilen aber eine Bildwelt —
> gemalter Jesus ruht in dunkler Nachtszene, **0/10 mit Blickkontakt** — und
> mehrere Bauformen kommen ausschließlich bei Verlierern vor. Dort auch die
> zwei belegten Motivrichtungen samt Generierungs-Prompts und die
> Serienkonsistenz-Prüfung (Konsistenz ist Nischen-Standard, kein Differenzierer).

**PFLICHT — Ein Standmotiv mit sanfter Bewegung, kein Szenenschnitt.**
11 von 11 Stichproben zeigen Bewegung, aber immer ruhige: Feuerflackern, driftende Wolken,
funkelnde Sterne, langsamer Zoom. Der tote Kanal C rotiert 8 Szenen, G schneidet Stock-Footage.

**PFLICHT — Palette: tiefes Nachtblau/Schwarz + genau eine warme Lichtquelle im Bild**
(Lagerfeuer, erleuchtetes Fenster, Mond). Hoher Kontrast, dunkles Gesamtbild.

**PFLICHT — Thumbnail gehört sichtbar zur eigenen Serie.** B verwendet in **13 von 13**
Thumbnails dasselbe Motiv (schlafender Jesus in weiß-rotem Gewand, Lamm, Lagerfeuer, blaue
Nacht) mit großen weißen Serifen-Versalien. Wiedererkennbar wie ein Logo.
> Wichtige Einschränkung: B's Thumbnails sind bei 166.000 und bei 140 Views praktisch identisch.
> Die Serie trägt die **Kanalidentität**, sie erklärt den Einzeltreffer nicht.

**PFLICHT — 1920×1080, 24–30 fps.** 4K nicht nachweisbar besser; „4k" im Titel bringt 1,20×.

**Belegtes Motiv-Set:** schlafende Figur mit Lamm am Feuer, Mond und Sterne, Wasserspiegelung,
aufgeschlagenes Buch, einsame Hütte. Untertitel weiß, zentriert, unteres Drittel, ins Bild
gerendert; Kanal-Wasserzeichen klein in einer Ecke.

---

## 5b. STIMME UND KLANGBETT *(gemessen 2026-08-03, 6 Audio-Stichproben à 80 s)*

**KI-Stimme ist belegt tragfähig.** Alle drei Gewinner-Videos sind **synthetisch** gesprochen
(hohe Konfidenz) — bis 245.000 Views. Der einzige menschlich gesprochene Kanal im Test (G) ist
ein Verlierer mit 156 Views. Du brauchst keinen menschlichen Sprecher, und er wäre kein Vorteil.

**Zielprofil (bei allen drei Gewinnern identisch):**
- tiefe, resonante **Männerstimme**
- langsam und meditativ, bewusste Pausen zwischen den Versen
- **stark behaucht, close-mic**, warm und intim — fast Bühnenflüstern
- gemessenes Gesamttempo **120–160 WPM** über die volle Laufzeit

**Klangbett — erstmals gemessen, ersetzt die bisherige Angabe „ungemessen":**
- **Ambient-Synth-Pad: 3/3 Gewinner — aber auch 3/3 Verlierer.** Tischeinsatz, kein Unterscheider.
- **Knisterndes Lagerfeuer: 2/3 Gewinner** (passt zum Lagerfeuer-Motiv im Bild), 1/3 Verlierer.
- **Grillen: 0/3 Gewinner, 2/3 Verlierer.** n zu klein für eine Regel, aber im Zweifel weglassen.
- **Stimme in 6/6 Fällen klar über dem Bett** — Musik verschluckt sie nie. Das ist die einzige
  harte Abmisch-Regel, die die Daten hergeben.
- Weder „Delta-Wellen" noch „Klavier+Regen" aus dem Ursprungsbriefing waren hörbar zu bestätigen.
  Klavier trat nur bei Verlierer F auf.

**PFLICHT — Aussprache-QA vor dem Rendern.** Der einzige stimmseitige Mangel mit Trennschärfe:
Verlierer C betont „solace" als *so-LACE* und „supervise" als *super-VISE*. Gleiche Wurzel wie
C's maschinenparaphrasierte Bibel — ungeprüfter Maschinen-Output. Eigennamen und seltenere
Wörter vor dem Rendern gegenhören, bei Bedarf per Lexikon/SSML korrigieren.

> Leichte TTS-Artefakte sind **kein** Ausschlusskriterium: Auch die Gewinner zeigen abgeschnittene
> Wortenden, gelegentlich mechanische Kadenz und sehr repetitive Phrasenmelodie — bei 245.000
> Views. Falsche Betonung ist das Problem, nicht synthetische Prosodie.

### Männlich oder weiblich? *(geprüft 2026-08-03)*

**Empfehlung: männlich bleiben — aber ausdrücklich NICHT, weil weibliche Stimmen nicht
funktionieren.** Sie funktionieren nachweislich.

**Was belegt ist:**
- In der **exakten Zielformel** (gemalte Nachtszene + durchgehende Bibellesung) sind
  **8 von 8** per Audio geprüften Stimmen männlich — inklusive Divine Rest (menschlich,
  männlich, **1.888.269 Views** im formatgleichen „Gospel of John mit Regen").
- Frauenstimmen sind in der christlichen Einschlaf-Nische **sehr erfolgreich, nur in anderen
  Sub-Formaten**: SOAKSTREAM (**918.000 Abos, 548 Videos, 164,3 Mio. Views**, Ø ~300.000 je
  Video) bewirbt „FEMALE VOICE" explizit im Titel; Spitzenvideo **1.464.812**. Dazu
  Calming Truth (684.939), Melody Joy Williams (397.964), Loisa ASMR (149.610).
  Das ist **größer als jeder Männerstimmen-Kanal in unserem Datensatz.**
- **Der Gegentest fällt negativ aus:** In der weltlichen Sleep-Story-Nische (n=20 Top-Videos)
  dominieren ebenfalls Männerstimmen — Dan Jones 2.348.594, Get Sleepy/Thomas Jones 1.189.671,
  Jason Stephenson 398.550, Stephen Dalton 322.591 gegen Michelle's Sanctuary (weiblich)
  764.335. Die Männerhäufung ist also **keine Eigenheit der christlichen Nische** und liefert
  keinen Hinweis auf eine Konvention, die gegen die Publikumspräferenz läuft.
  Einzige Ausnahme: das **ASMR-/Flüster-Subgenre**, dort führen weibliche Kanäle.

**Die drei Gründe für „männlich" sind damit:** (a) 8/8 in der Zielformel, (b) kein Hinweis aus
dem Gegentest auf ungenutztes Potenzial, (c) eine Stimmumstellung wäre eine zusätzliche
Variable in einem Setup, dessen Trefferquote ohnehin nur bei 10/21 liegt.

**Weiblich ist damit nicht widerlegt, sondern in dieser Formel schlicht ungetestet.**
*Prüfkriterium:* Ab Video 10 zwei bis drei Videos mit identischem Bild, Titelmuster und Länge,
nur die Stimme weiblich. Wenn deren Median-Views nach 30 Tagen nicht unter 70 % der
Männerstimmen-Videos liegen, ist die Stimme auch hier kein Faktor — dann entscheidet die
Verfügbarkeit der besseren TTS-Stimme, nicht das Geschlecht.

> **Randnotiz zur Recherche:** Der als „einziger Kanal mit weiblicher Stimme" gemeldete
> Kanal *Fall Asleep with God's Word* ist keiner. Sein Hauptvideo (404 Views) ist **männlich**
> gesprochen; nur ein einziges Video (7 Views) nutzt eine Frauenstimme. Er ist ohnehin kein
> Testfall: 3 Wochen alt, 5 Videos, 3 Abos, 490 Views gesamt, 4 von 5 Videos unter der
> 3-Stunden-Schwelle, 3 davon am selben Tag hochgeladen.

---

## 6. RHYTHMUS

**Upload-Abstand 4–7 Tage** (B: 10 von 10 Abständen). **Maximal 2 Videos pro Woche**
(Gewinner 1,3–1,5/Wo; alle 8 Verlierer 2,0–13,5). **Null Shorts** (J: 856.688 Shorts-Views →
171 Langform-Views bei 2.210 Subs).

> **Kadenz-Entscheidung 2026-08-23 — bleibt bei 5 Tagen** *(eigene Kanaldaten Gate 2)*.
> Dafür sprach eine **Fremdkohorte**: 74 Wissenschafts-Schlafkanäle unter 2 Jahren,
> Kadenz dort der stärkste Treiber (Median 311 $/Mon. bei 0–1,5 Uploads/Woche gegen
> 1.770 $ bei 6+). Dagegen sprach die eigene M1-Verteilung — beide Gewinner 1,3–1,4/Woche,
> alle 8 Verlierer 2,0–13,5, keine Überlappung; alle drei Tage wären 2,33/Woche und damit
> im Verliererband. Ausschlaggebend war die Versuchsdisziplin: V05–V08 sollen den
> Korpuswechsel nach M8 als **einzige** geänderte Variable testen. Kadenz erst danach.
> Beide Seiten ausgeführt unter M1 in
> [`regeln/erfolgsregeln.md`](regeln/erfolgsregeln.md).

**Ergänzung aus den Daten:** Kanalbeschreibung und Kanal-Keywords müssen ausschließlich die
Nische beschreiben. E wirbt bis heute für „Tibetan Singing Bowls" (40 Subs), H trägt
Mythologie-Keywords und Atlantis-Videos im Katalog (Median 52 Views).

---

## 7. METADATEN

**SRT-Untertitelspur hochladen.** 0 von 19 Gewinner-Videos hat eine — echte, unbesetzte Lücke.
Wirkung ungeprüft, Kosten nahe null (fällt aus dem TTS-Skript ohnehin ab).

**Beschreibung: Wert zuerst, Spendenlink danach.** Konsistent mit A (Kanalbeschreibung nennt
erst den Nutzen, dann buymeacoffee) — n=1, schwacher Beleg.

**Kapitelmarken — optional, nicht Pflicht.**
> A's drei größte Treffer (245K/233K/201K) haben **null** Kapitelmarken. B setzt sie durchgehend
> (40–93 Stück). Beide Muster gewinnen. Nimm sie für die Nutzbarkeit, nicht für die Reichweite.

**„Echte Tags gesetzt" — steht im Widerspruch zum Gewinner-Verhalten.**
> A: 0 Tags auf **allen 8** Videos. B: die drei gemessenen Treffer (166K/96K/35K) haben **0 Tags**,
> die beiden ≥3h-Flops haben 6 und 22. Bei n=5 ist das keine belastbare Negativregel — aber
> „echte Tags" als Pflicht zu führen, behauptet einen Nutzen, den kein Gewinner belegt. Setz sie,
> weil sie nichts kosten; erwarte nichts davon.

**Optimiert wird auf das Vorschlagsband, nicht auf die Startseite.**
*(eigene Kanaldaten Gate 2, 2026-08-23 — Traffic-Quellen des Kanals über 28 Tage,
146 von 151 Aufrufen zugeordnet.)*

| Quelle | Aufrufe | Ø Sehdauer |
|---|---|---|
| Vorgeschlagene Videos | 102 | **29,7 min** |
| Startseite / Abo-Feed | 36 | **10,2 min** |
| Direkt oder extern | 6 | 89,8 min |
| Sonstige YouTube-Seiten | 2 | 104 min |
| **YouTube-Suche** | **0** | — |

Die Startseite liefert die **schlechtesten Zuschauer des Kanals**: 10,2 min gegen 29,7 min
aus dem Vorschlagsband, gut ein Drittel. Wo Titel und Thumbnail zwischen beiden abwägen
müssten — Anschlussfähigkeit an ähnliche Videos gegen Auffälligkeit im offenen Feed —,
gewinnt das Vorschlagsband. Praktisch heißt das: Eigenname (§1) und Serienmotiv (§5)
wiegen schwerer als ein Titel, der isoliert auf der Startseite auffällt.

**Suchoptimierung ist bei diesem Kanalstand kein Hebel.** Null Suchaufrufe in 28 Tagen.
Tags und Beschreibungs-Keywords bleiben trotzdem, weil sie nichts kosten — aber es ist
nichts von ihnen zu erwarten (siehe den Tag-Befund oben). Die beiden hohen Ø-Sehdauern
(89,8 und 104 min) hängen an 6 bzw. 2 Aufrufen und tragen nichts.

> **Zahlenwarnung — die Traffic-Quelle „SUBSCRIBER" ist keine Abonnentenzahl.**
> Die YouTube-API meldet **Startseite und Abo-Feed** unter dem Label `SUBSCRIBER`. Das
> bedeutet **nicht** „Aufrufe durch Abonnenten". Der Kanal hatte im ganzen Zeitraum
> **2 Abonnenten**. Wer das Label wörtlich liest, hält 36 Aufrufe für Abo-Traffic,
> den es nicht gibt.

**KI-Kennzeichnung aktivieren** — Compliance-Entscheidung, kein Datenbeleg in beide Richtungen.
Gehört zu §8.

---

## 8. Geschäfts- und Compliance-Entscheidungen (bewusst außerhalb der Daten)

Diese Punkte sind legitim, aber **nicht** aus Kanaldaten begründet. Getrennt halten, damit die
Checkliste nicht mit ungeprüften Annahmen verwässert.

- Eigenes Eingangsgebet (~400 Wörter, je Video anders) als Absicherung der Monetarisierung
- KI-Kennzeichnung
- World English Bible statt NIV aus Urheberrechtsgründen → **WEBBE wählen** (§4)

---

## 9. OFFEN — wo die Daten schweigen

- ~~Klangbett~~ und ~~Stimmfarbe~~ — **beides am 2026-08-03 gemessen, siehe §5b.** Offen bleibt
  nur, ob das Lagerfeuer-Geräusch wirklich wirkt (2/3 Gewinner, 1/3 Verlierer — n zu klein) und
  ob das Weglassen von Grillen etwas ändert.
- **Was #7 von #8 unterscheidet.** In keiner messbaren Variable erfassbar. Ohne Impressions und
  CTR aus fremden Analytics nicht auflösbar.
- **Ob WEBBE so gut trägt wie NIV.** Prüfkriterium: dieselbe Psalmenauswahl einmal in beiden
  Fassungen als 2-Minuten-Probe sprechen lassen, gegen Muttersprachler-Ohr prüfen.
- **Ob Eigennamen einem Neustarter helfen** — **am 2026-08-23 nur teilweise geklärt**
  *(eigene Kanaldaten Gate 2)*. Sicher ist: **nicht über die Suche** (0 Suchaufrufe in
  28 Tagen) und **nicht über die Klickrate** (V3 hat den zweitschlechtesten CTR des
  Kanals). Beides ist ausgeschlossen. Ob der Eigenname über die kontextliche Zuordnung
  im Vorschlagsband wirkt oder ob V3's Impressionen schlicht der besseren Retention
  folgen, **trennen die eigenen Daten nicht** — V3 trug Eigenname und Erzählstoff
  zugleich, und die Retention ist die gemessene der beiden Größen. Ausgeführt in §1
  unter „die sparsamere Erklärung". Der Eigenname ist trotzdem Pflicht, aber als
  billige Konvention, nicht als belegter Hebel.
  *Prüfkriterium:* ein Video mit Erzählstoff-Korpus **ohne** Eigennamen im Titel —
  frühestens nach V08, wenn der Korpuswechsel ausgewertet ist.
- **Optimale Kadenz innerhalb 4–7 Tagen.** Belegt ist nur die Obergrenze. Die Frage,
  ob häufiger besser wäre, ist am 2026-08-23 **gestellt und vertagt** worden, nicht
  beantwortet — siehe §6 und M1.

### Beobachtung, ausdrücklich noch KEINE Regel: der Anfangsabfall

*(eigene Kanaldaten Gate 2, 2026-08-23)*

Beide Videos mit Retentionskurve verlieren im selben Fenster den größten Teil ihres
Publikums — **zwischen Minute 2 und Minute 4**:

| | Minute 2 | Minute 4 |
|---|---|---|
| V3 Johannes | 100 % | **40 %** |
| V2 Psalmen + Sprüche | 100 % | **29 %** |

In diesem Fenster liegen **Hook (~20 s) und Eingangsgebet (~80 s)**.

**Warum daraus jetzt keine Regel wird — drei Gründe:**
1. YouTubes Messpunkte sind bei 3,5 h Laufzeit **2-Minuten-Blöcke**. Der Abfall ist
   nicht auf die Sekunde lokalisierbar und trifft Hook und Gebet gemeinsam; welches
   von beidem kostet, sagen die Daten nicht.
2. Ein **steiler Anfangsabfall ist bei Long-Form normal** — er ist kein Befund, solange
   nichts Vergleichbares dagegensteht.
3. **n=91** Aufrufe für die stärkere der beiden Kurven ist klein.

Die Rahmung jetzt zu kürzen hieße raten — und das Eingangsgebet steht ohnehin als
Policy-Absicherung in §8, nicht als Reichweiten-Element.

*Prüfkriterium:* Zeigen **V05–V08 dasselbe Muster**, wird **ein** Video mit gekürzter
Rahmung getestet. **Eine Variable pro Runde** — solange der Korpuswechsel nach M8 läuft,
bleibt die Rahmung unverändert.

---

## 10. Titel-Baukasten

**Belegt — wörtlich aus Gewinner-Titeln (13). Diese zuerst verwenden.**

| Anker | Beleg |
|---|---|
| `If You're Anxious,` | 245K |
| `I Know You're Tired…` | 233K |
| `You're Tired, I Know…` | 201K |
| `Lord, I Feel Tired` | 184K |
| `No More Thinking Tonight…` | 166K |
| `Stop Thinking For A Moment,` | 96K |
| `You Need Rest…` | 36K |
| `Fall Asleep Without Stress…` | 35K |
| `Don't Go to Sleep Worried…` | 32K |
| `If You're Overwhelmed,` | 1,3K |
| `Rest Your Eyes…` | 915 |
| `You Deserve Some Rest…` | 559 |
| `God Knows You're Tired…` | 140 |

Die letzten vier stammen aus Flop-Videos desselben Kanals — belegt als *verwendet*, nicht als
*wirksam*. Bei B trugen Treffer und Flops dasselbe Muster.

**Ungeprüft — abgeleitet, ohne Beleg (7):** `If Your Mind Won't Slow Down,` ·
`When Sleep Won't Come…` · `You've Carried Enough Today…` · `If Tonight Feels Heavy,` ·
`Too Tired to Pray? …` · `When Tomorrow Feels Too Big…` · `If You're Lying Awake Again…`

**Eigennamen — seit 2026-08-23 Pflichtbestandteil jedes Titels (§1), nicht mehr Testreihe.**
Die folgenden Faktoren stammen aus Lauf 1 (etablierte Kanäle, kanal-normiert) und sind
**View**-Werte; sie sagen nichts über Sehdauer und nichts über das Vorschlagsband, über das
der Eigenname bei diesem Kanal wirkt. Als Rangfolge für die Auswahl brauchbar, als Beleg
für die Pflicht nicht — der steht in §1. Achtung auf die Wechselwirkung mit **M8**:
`Psalms`, `Proverbs` und die prophetischen Bücher sind als **Hauptkorpus** ausgeschlossen,
unabhängig von ihrem Anker-Faktor.

Gospel of John 3,0–3,3× (n=14) · Gospels 2,8–3,3× (n=31) ·
Isaiah (773K-Video, n=10) · Book of Enoch 2,3× (n=46) · Angels 1,4–6,9× (n=36) ·
Daniel (536K, n=11) · Sermon on the Mount (413K, n=1) · Proverbs (93K, n=1) ·
Revelation 1,5× (n=12) · Ephesians/Galatians/Colossians (1,0 Mio., n=1) ·
Jeremiah 1,17× (n=4) · Genesis 0,43× — schwach (n=13) · Psalms 0,26–1,38× — kein Effekt (n=32) ·
Matthew/Luke/Mark einzeln nicht belegt · Lamentations/Job keine Daten.

---

## 11. Textbausteine

**Hook (0–60 s, optional).** A's 233K-Video hat keinen. Wenn du einen nimmst: warm, zweite
Person, unter 110 s. Bauteile aus allen drei Gewinner-Hooks: Begrüßung → Zustand benennen →
Erlaubnis zum Loslassen → Ankündigung des Textes → Körperanweisung.

> „Hey child of God, you're safe here. If you're tired, anxious, or need some peace, this space
> was made for you. In a moment, we'll begin calmly reading the word of God from the Gospel of
> John to help you rest and find comfort." — A, 245K

> „If you're still awake tonight, I'm really glad you're here. Set every worry aside tonight and
> allow God's word to quiet your mind as you fall asleep." — B, 96K

> „Welcome back. Tonight, allow God's word to quiet your mind and lead you into the most peaceful
> sleep. Now, get comfortable, close your eyes, and rest in God's presence." — B, 166K

**Nicht tun:** Dringlichkeit (*„Before you scroll away…"* — D, Ø 16 Views), minutenlange
Atemmeditation ohne Schriftbezug (F, Ø 9 Views).

**CTA (max. 2, in den ersten 60 s oder gar nicht).**

> „I'd love for you to comment below where you're listening from and leave a prayer, too, so that
> we can all lift each other up." — A, 245K

> „If these nightly verses have become part of your bedtime routine, I'd love for you to subscribe
> and become part of this community." — B, 96K

**Nicht tun:** *„type amen in the comments"*, *„Share this message with someone who…"*
(D: 7 CTAs, Ø 16 Views).

**Beschreibung.**
```
[Titel wörtlich wiederholen]
[2–4 Sätze: Zustand ansprechen, was das Video tut, was der Hörer bekommt]
[optional „Focused on:" mit 4–6 Stichpunkten]
Chapters: 0:00:29 - Intro / 0:00:32 - Psalm 9 / …
[2–3 Sätze Segenswunsch + Abo-Einladung]
[Spendenlink NACH dem Wert]
#sleepwithpsalms #restwithjesus #bibleversesforsleep #christiansleep
```

---

*Änderungen gehören zusammen mit dem Beleg hier hinein. Regeln, die die eigenen Kanaldaten ab
Video 10 widerlegen, werden gestrichen — nicht verteidigt.*

---

# formel/thumbnail-checkliste.md

---

# Thumbnail-Checkliste

> **Stand: 2026-08-23** (Messteil unverändert seit 2026-08-03).
> Grundlage: 90 Thumbnails (21 Gewinner, 69 Verlierer aus 8 Kanälen),
> maschinell vermessen plus visueller Test auf 160×90 px (Feed-Größe am Handy).
> Rohdaten: `regeln/daten/thumb_messung.json`, `thumb_textmessung.json`,
> `feedtest_GEWINNER.png`, `feedtest_VERLIERER.png`, `zoom_B_figur.png`.
>
> Alle Vorgaben liegen **innerhalb** der belegten Muster (Serienmotiv, Nachtfarbwelt, warme
> Lichtquelle). Nichts hier bricht ein Muster.
>
> **2026-08-23 — Gate 2 ausgewertet** *(eigene Kanaldaten Gate 2)*. An den Zielwerten
> ändert sich **nichts**: sie sind weiter belegt und weiter unwiderlegt. Geändert hat sich
> die offene Frage am Dokumentende — *ob Thumbnails überhaupt der Engpass sind*, ist mit
> eigenen Daten **vorläufig mit NEIN beantwortet.** Praktische Folge: hier nicht mehr
> investieren, als die Checkliste unten verlangt.

---

## Zuerst: wo die Daten KEINE Mängel zeigen

Damit du dort keine Zeit investierst. Diese drei Verdachtspunkte habe ich gemessen und
**widerlegt**:

| Geprüft | Ergebnis | Fallzahl |
|---|---|---|
| **Auflösung** | 89 von 90 liegen nativ in 1280×720 vor. Der eine Ausreißer (480×360) ist der Fallback **meines Downloads**, kein Kanal-Mangel. Kein Hochskalieren, keine Streckung. | 90 |
| **Kompression** | Median 201–237 KB bei 1280×720 in allen drei Gruppen. Ein einziger Ausreißer (19 KB) ist derselbe Fallback. Keine sichtbaren JPEG-Blöcke. | 90 |
| **Bildschärfe** | Nur 2 von 90 auffällig weich (Laplace-Varianz <150) — je einer bei Gewinnern und Verlierern. Kein Muster. | 90 |

**Wichtig gegen einen Fehlschluss:** Die Gewinner sind *unschärfer* als die Verlierer
(Median 704 gegen 853–906). Das ist kein Mangel, sondern Folge des gemalten Stils —
fotorealistische Thumbnails haben mehr Hochfrequenzdetail. **Jage keine Schärfewerte.**

---

## Die Zielwerte, ausgemessen an der bewährten Serie

Gemessen an allen 13 Thumbnails von Rest in Grace — der Serie mit dem konsistentesten
Erfolg und dem geringsten Streuungsrisiko:

| Größe | Zielwert | Belegte Spanne | Fallzahl |
|---|---|---|---|
| **Versalhöhe** | **≥ 11,5 % der Bildhöhe** (≈ 83 px bei 720p, ≈125 px bei 1080p) | 9,9–12,1 %, Median 11,9 % | 13 |
| **Kontrast Text/Hintergrund** | **≥ 10:1** | 10,1–17,5:1, Median 15,4:1 | 13 |
| **Wortzahl** | **maximal 4 Wörter** | Gewinner 0–4 | 21 |

Zum Vergleich die Verlierergruppen: Versalhöhe Median **9,0–9,5 %** — also rund ein Viertel
kleiner als bei den Gewinnern (n=69). Das ist der einzige typografische Messwert, der Gewinner
und Verlierer sauber trennt.

Der Kontrastwert 10:1 ist bewusst hoch angesetzt: WCAG verlangt 4,5:1, die Gewinner-Serie
liefert aber durchgehend das Doppelte bis Dreifache. Du hast keinen Grund, unter ihren
schlechtesten Wert (10,1) zu gehen.

---

## Feed-Test 160×90: was hält, was zusammenbricht

Visuell geprüft, alle 90 auf echte Feed-Größe heruntergerechnet.

**Hält zuverlässig:**
- Fette Versalien, 2–4 Wörter, eine Zeile oder zwei — bei **allen** geprüften Fällen lesbar
  (B-Serie 13/13, dazu „SLEEP DEEP", „JUST SLEEP", „REST NOW", „PRAY THIS TONIGHT")

**Bricht zusammen:**
- **Ab 6 Wörtern.** Härtester Fall: Kanal D mit *„DO NOT SKIP THIS. God Says: Watch This Today.
  The Waiting Is Over."* — 12 Wörter in einem Kasten, bei Feed-Größe nur noch ein gelber Fleck
  (54 Views).
- **Dünne Serifen in Gemischtschreibung** verlieren deutlich gegenüber fetten Versalien.
  Betrifft **auch Gewinner**: A's *„Time To Sleep."* (233K) und *„Peaceful Sleep."* (12K)
  sind bei 160×90 noch erkennbar, aber merklich schwächer als B's Versalien. Bei Kanal C
  (*„Hear the Teachings of Jesus"*, 89 Views) kippt derselbe Stil ins Unlesbare.
- **Heller Text auf hellem Grund.** Kanal F setzt „Just Sleep" in hellem Grau auf helle
  Wolken — bei Feed-Größe praktisch verschwunden (14 Views).

**Ein echter Mangel bei einem Gewinner:** A's Video mit **201.000 Views** trägt unten links
die Mikroschrift *„we are"* — bei Feed-Größe vollständig unlesbar und inhaltlich sinnlos
(vermutlich ein abgeschnittener Textrest). Das Video lief trotzdem. **Lesbarkeitsmängel sind
also nicht tödlich** — aber es gibt keinen Grund, sie zu kopieren.

---

## KI-Artefakte

Geprüft an Ausschnitten in voller Auflösung, Schwerpunkt auf den bekannten Schwachstellen.

**Im gemalten Stil (A, B, C, F, I) verstecken sich die typischen Fehler weitgehend** — keine
verformten Hände, keine sechsten Finger in der Stichprobe. Der weiche Pinselduktus verzeiht
Anatomie.

**Aber die bewährte B-Serie hat drei sichtbare Schwächen** (geprüft am 166.000-Views-Motiv,
das du kopieren würdest):
1. Der **Arm unter dem Kopf** verschmilzt mehrdeutig mit Kissen und Haar — man sieht nicht,
   wo er endet.
2. **Fuß und Beinlänge** rechts unten lesen sich seltsam, Zehen undeutlich, Unterkörper wirkt
   gegenüber dem Rumpf zu lang.
3. **Das Lagerfeuer beleuchtet die Figur nicht.** Das Feuer steht rechts, die Figur wird von
   vorn-links beleuchtet. Der warme Akzent ist da, aber physikalisch unstimmig — und das
   wiederholt sich über die Serie.

Bei fotorealistischen Motiven war die klassische Schwachstelle unauffällig: D's ausgestreckte
Hand (77 Views) ist sauber gerendert, Finger zählbar.

**Einordnung, damit du nicht überinvestierst:** Alle drei B-Mängel stecken in einem Thumbnail
mit 166.000 Views und sind bei Feed-Größe unsichtbar. Prüfen ja — nachbessern nur, wenn es
schnell geht.

---

## Checkliste vor dem Upload

**Typografie**
- [ ] Maximal **4 Wörter** im Bild
- [ ] Versalien, fett — keine dünnen Serifen in Gemischtschreibung
- [ ] Versalhöhe **≥ 11,5 % der Bildhöhe** (bei 1920×1080: **≥ 125 px**)
- [ ] Kontrast Text zu direktem Hintergrund **≥ 10:1** (weißer Text nur über dem dunklen
      Nachthimmel, nie über Feuerschein, Mond oder heller Wolke)
- [ ] Kein zweiter, kleinerer Textblock — keine Mikroschrift, keine Textreste
- [ ] Text sitzt im oberen Drittel, Figur und Lichtquelle darunter (B-Serie: 13/13)

**Motiv (Serienbindung — nicht verhandelbar)**
- [ ] Gleiches Motiv wie die letzten Uploads: **sitzende Jesus-Figur, allein in
      dunkler Nachtlandschaft, kein Blickkontakt** *(Serienentscheidung
      2026-08-04, `thumbnail-motive.md` Richtung 2 — ersetzt die frühere
      „schlafende Figur, Lamm, Lagerfeuer")*
- [ ] Tiefes Nachtblau als Grundton, genau **eine** warme Lichtquelle
- [ ] Keine Grelltöne, kein Tageslicht, keine gesättigten Neonfarben

**Bildprüfung (2 Minuten, in dieser Reihenfolge)**
- [ ] **Auf 160×90 verkleinern und ansehen.** Ist der Text in einer Sekunde erfassbar? Wenn
      nein: Wörter streichen, nicht die Schrift verkleinern.
- [ ] Hände, Arme, Füße der Figur einzeln prüfen — verschmilzt etwas mehrdeutig?
- [ ] Beleuchtet die warme Lichtquelle die Figur tatsächlich aus ihrer Richtung?
- [ ] Lammbeine und Gesichtszüge auf Verformung prüfen
- [ ] Export als **1280×720 oder 1920×1080 JPEG, ≥ 150 KB** (Gewinner-Median 237 KB)

**Nicht prüfen — nachweislich irrelevant**
- ~~Schärfe/Detailgrad~~ (Gewinner sind unschärfer als Verlierer)
- ~~Auflösung über 1080p~~
- ~~Kompressionsartefakte~~ (bei keinem Kanal ein Problem)

---

## Was diese Analyse nicht beantwortet

- **Ob die Zielwerte kausal wirken.** Versalhöhe und Kontrast trennen Gewinner und Verlierer
  sauber — aber B's Thumbnails sind bei 166.000 und bei 140 Views praktisch identisch. Die
  Werte qualifizieren das Thumbnail; sie erklären den Einzeltreffer nicht.
- **Ob 4 Wörter besser sind als 0.** A's zwei größte Videos (245K, 184K) haben **gar keinen
  Text**, B's Serie hat durchgehend 2–4 Wörter. Beide Muster gewinnen. Die Obergrenze von 4 ist
  belegt, eine Untergrenze nicht.
- ~~**Klickrate.** Ohne Impressions und CTR aus fremden Analytics bleibt offen, ob Thumbnails
  überhaupt der Engpass sind.~~ — **vorläufig beantwortet am 2026-08-23, mit NEIN**
  *(eigene Kanaldaten Gate 2, `regeln/daten/gate2_eigene_kanaldaten.json`)*.

  Der Kanal *The Nightly Word* lieferte in 28 Tagen **5.535 Impressionen bei 2,71 % CTR**.
  Entscheidend ist die Verteilung darin:

  | | Impressionen | CTR | Wiedergabestunden |
  |---|---|---|---|
  | **V3** (Johannes, Erzählstoff) | **3.130 von 5.535** | **1,82 %** — zweitschlechtester des Kanals | **55,4 von 69,4** |
  | V1, V2, V4 zusammen | 2.405 | im Schnitt höher | 14,0 |

  **Das Video mit dem schlechtesten CTR bekam die meisten Impressionen.** YouTube liefert
  nach **Wiedergabezeit** aus, nicht nach Klickrate — und V3 trägt 80 % der
  Kanal-Wiedergabezeit. Der Engpass dieses Kanals sitzt hinter dem Klick, nicht davor:
  im Textkorpus (→ **M8** in `regeln/erfolgsregeln.md`), nicht im Thumbnail.

  **Warum „vorläufig":** 5.535 Impressionen sind **keine belastbare Grundlage für eine
  CTR-Aussage** — bei dieser Größenordnung bewegen einzelne Aufrufe den Wert. Und die vier
  Thumbnails wurden **nicht gegeneinander getestet**: im Zeitraum lief je Video genau eine
  Variante, jede an einem anderen Korpus und einem anderen Titel. Ein Thumbnail-Effekt ist
  damit nicht ausgeschlossen, sondern **unerkennbar** — er läge in diesen Zahlen unter dem
  Korpuseffekt.

  **Was daraus für die Arbeit folgt:** Die Checkliste oben abarbeiten, weil sie billig ist
  und ihre Werte belegt sind — aber **keine zusätzliche Zeit** in Motivvarianten,
  Feinschliff oder A/B-Runden stecken, solange der Korpuswechsel nach M8 läuft. Neu
  aufmachen, sobald ein Video mit Erzählstoff-Korpus trotzdem wenige Impressionen bekommt.

---

# produktion/videos-01-08.md

---

# Videos 01–08 — Textebene

> **Stand: 2026-08-23.** Verbindlich sind `formel/video-formel.md` (**v2.2**),
> `regeln/erfolgsregeln.md` und `formel/thumbnail-checkliste.md`.
> **Der Textteil unten stammt vom 2026-08-04 und ist für V05–V08 nicht mehr
> vollständig gültig** — was Gate 2 daran geändert hat, steht im nächsten Abschnitt.
> Wortzahlen sind **gemessen**, nicht geschätzt: `produktion/wortzahlen.py` hat alle
> 518 in Frage kommenden WEBBE-Kapitel abgerufen und gezählt
> (`produktion/korpus/kapitel.json`, `produktion/korpus/plan.json`).
> Alle acht Titel sind gegen die 21 bekannten Gewinner-Titel geprüft
> (`produktion/titel_pruefung.py`, Ergebnis am Dateiende).
> Noch kein Rendering, keine Stimme.

## Was Gate 2 an diesem Plan ändert (2026-08-23)

*Quelle: eigene Kanaldaten Gate 2, `regeln/daten/gate2_eigene_kanaldaten.json`.
Auswertung: `produktion/workflow-gates.md`, Gate 2.*

Zwei neue Regeln greifen ab V05 direkt in diesen Plan ein:

- **M8** (`regeln/erfolgsregeln.md`): Hauptkorpus muss **durchlaufender Erzählstoff**
  sein — Evangelien, Apostelgeschichte, Genesis-Erzählungen. Spruchsammlungen
  (Psalmen, Sprüche, Prediger) und **prophetische Rede** nur als Beigabe.
- **Formel §1**: **Eigenname im Titel ist Pflicht — in jedem Video**, nicht mehr
  „~jedes 4.". Ausgeschlossen ist, dass er über die Suche wirkt (0 Suchaufrufe in
  28 Tagen) oder über die Klickrate (V3 hat den zweitschlechtesten CTR des Kanals).
  Ob er überhaupt wirkt, ist offen — **die Pflicht ist eine billige Konvention, kein
  belegter Hebel** (§1, „die sparsamere Erklärung"). Der belegte Hebel ist M8.

### Die vier geplanten Videos gegen die neuen Regeln

| | Korpus laut Plan | Zusammensetzung | M8 | Eigenname im Titel |
|---|---|---|---|---|
| **V05** | Lukas + Prediger | Lukas 24.399 W (**81,7 %**) · Prediger 5.481 W (18,3 %) | **erfüllt** — Erzählstoff trägt, Prediger ist Beigabe | **fehlt** — „…Sleep to the Whole Story, Read Slowly" |
| **V06** | Jesaja 1–25 + 40–66 + Daniel 4–6 | Jesaja 27.573 W (**89,8 %**) · Daniel 3.120 W (10,2 %) | **verletzt** — prophetische Rede ist Hauptkorpus | vorhanden („Isaiah") |
| **V07** | Markus + Römer + Offb. 1–11 | Markus 14.261 W (**49,0 %**) · Römer 9.431 W (32,4 %) · Offenbarung 5.431 W (18,6 %) | **grenzwertig** — Erzählstoff unter der Hälfte, Rest Brief und Apokalyptik | **fehlt** — „…God's Promises for a Quiet Heart" |
| **V08** | Genesis 1–42 | Genesis 29.835 W (100 %) | **erfüllt** — von M8 ausdrücklich genannt | **fehlt** — „…Sleep to the Beginning of Everything" |

**V05 kann so gebaut werden, sobald der Titel einen Eigennamen trägt.** Der Korpus
bleibt, wie er ist; nur die Titelzeile — und mit ihr Thumbnail-Text, Beschreibung und
Tags — muss den Evangeliennamen tragen. Das ist die einzige Änderung, die V05 blockiert.

**V06 muss umgeplant werden**, V07 braucht eine Entscheidung. Je zwei durchgerechnete
Varianten stehen unten; entschieden ist noch nichts.

### Korpusvarianten V06 und V07 — zur Entscheidung, noch nicht übernommen

*Gerechnet am 2026-08-23 mit `produktion/korpus_pruefung.py` gegen die gemessenen
Wortzahlen in `produktion/korpus/kapitel.json` (723 Kapitel, keine Lücken). Alle vier
bestehen Gate-1-Prüfung 1.1 und 1.13 und überschneiden sich mit keinem anderen Video.*

| | Korpus | Wörter | Erzählanteil | Laufzeit @140 | Kapitel |
|---|---|---|---|---|---|
| **V06-A** | Apostelgeschichte + Rut + Ester | **30.987** | **100,0 %** | 3,69 h | 42 |
| **V06-B** | Apostelgeschichte + Rut + Jona + Daniel 4–6 | **29.971** | 99,3 % | 3,57 h | 39 |
| **V07-A** | Markus + Exodus 1–20 + Jona | **30.007** | 99,3 % | 3,57 h | 40 |
| **V07-B** | Markus + 1. Samuel 1–20 | **30.294** | **100,0 %** | 3,61 h | 36 |

Die fehlenden 0,7 % bei B und V07-A sind **Jona 2** — ein Gebet in Psalmenform,
5 Minuten lang. Bei V06-B kommt nichts weiter dazu: Daniel 4–6 ist Erzählung
(Nebukadnezars Wahnsinn, das Menetekel, die Löwengrube), erst Daniel 7–12 sind Visionen.

**Was die beiden V06-Varianten unterscheidet: Ester 9.** Das Kapitel schildert im
Wortlaut, wie 75.000 Menschen getötet und Hamans zehn Söhne gehängt werden — nachgelesen
im WEBBE-Text, nicht behauptet. In einem Video, das Ruhe verkauft, ist das die härteste
Passage, die dieser Kanal je gesendet hätte. **V06-A nimmt sie in Kauf** (dafür drei
vollständige Bücher ohne einen einzigen Schnitt), **V06-B vermeidet Ester ganz** (dafür
vier Bausteine statt drei).
*Dritter Weg, ebenfalls durchgerechnet:* **Apostelgeschichte + Rut + Ester 1–8** —
29.940 W, 100,0 %, 3,56 h. Ester endet bei 8,17, die Rettung ist vollzogen, die
Vergeltung fällt weg. Kostet einen Schnitt im Buchinneren und 1.047 Wörter (7,5 min).

**Was die beiden V07-Varianten unterscheidet: wo geschnitten wird.**
**V07-A** schneidet Exodus nach Kapitel 20 — das ist keine Kürzung, sondern eine
**Gattungsgrenze**: ab 21 folgen Bundesbuch, Stiftshüttenplan und dessen Ausführung,
also genau das Material, das M8 ausschließt. **V07-B** schneidet 1. Samuel nach
Kapitel 20 mitten im Buch (Abschied von David und Jonatan), dafür kommt es mit zwei
Bausteinen aus.

**Kompatibilität — eine Kombination geht nicht:**

| | V07-A (Exodus + Jona) | V07-B (1. Samuel) |
|---|---|---|
| **V06-A** (Rut + Ester) | ✅ | ✅ |
| **V06-B** (Rut + Jona + Daniel) | ❌ Jona doppelt | ✅ |

**Ein struktureller Befund, der für jede V07-Variante gilt:** Markus hat 14.261 Wörter.
Damit der Korpus die Untergrenze von 29.000 erreicht, muss der Rest mindestens 14.739
beitragen — **mehr als Markus selbst.** Markus liegt in jeder gültigen V07-Variante
zwischen **45,3 % und 49,2 %** des Korpus und kann die Hälfte rechnerisch nie tragen.
Der Titel nennt also unvermeidlich den kleineren Teil. Das ist kein Fehler der Auswahl,
sondern eine Folge davon, dass Markus das kürzeste Evangelium ist; die Beschreibung muss
den zweiten Block deshalb ausdrücklich benennen.

Was danach noch fehlt, sobald entschieden ist: neue Titel mit Eigenname, neue
Eingangsgebete, neue Thumbnail-Zeilen, und `produktion/korpus/plan.json` nachziehen.

**Noch nicht verplantes Material, gemessen** (`produktion/korpus/kapitel.json`):

| Buch | Kapitel | Wörter | Art nach M8 |
|---|---|---|---|
| Apostelgeschichte | 28 | 23.143 | **Erzählstoff** — in M8 ausdrücklich genannt |
| Genesis 43–50 | 8 | 5.992 | **Erzählstoff** |
| Jesaja 26–39 | 14 | 7.984 | prophetische Rede — nur Beigabe |
| Offenbarung 12–22 | 11 | 5.949 | Apokalyptik — nur Beigabe |
| Daniel 7–12 | 6 | 5.182 | Visionsbericht — nur Beigabe |

Der einzige verbliebene Erzählblock in Zielgröße ist die **Apostelgeschichte**
(23.143 W); auf 3,4–3,8 h fehlen ihr rund 6.000 Wörter. Genesis 43–50 (5.992 W)
schließt diese Lücke fast genau — dann wäre allerdings V08 neu zu schneiden.

### Zwei Folgefragen, die dieser Plan noch offen trägt

1. ~~**Der Hook-Test ab Video 05 kollidiert mit der Versuchsdisziplin.**~~
   **Entschieden am 2026-08-23: Hook-Test auf V09+ verschoben, V05–V08 laufen alle mit
   Variante (a).** Begründung im Upload-Plan oben — eine Variable pro Runde, und (a)
   ist die Variante, unter der V3 gelaufen ist. Damit bleibt der Korpuswechsel nach M8
   die einzige geänderte Größe zwischen V01–V04 und V05–V08.
2. **Die Kapitelmarken-Empfehlung hängt an den alten Korpora.** „Ja bei 01, 02, 06, 08"
   war mit 89/61 Psalmen und 52 Jesaja-Kapiteln begründet. Fällt der Jesaja-Korpus weg,
   fällt die Begründung für V06 mit — und `kapitelmarken_videos` in
   `produktion/config.md` (aktuell `V1,V2,V6,V8`) ist dann nachzuziehen.

---

## Wo deine Vorgaben von den Dokumenten abweichen

Du hast gesagt, bei Widersprüchen gewinnen die Dokumente. Drei Stellen:

1. **„Eingangsgebet … Zweck: YPP-Absicherung"** — Formel §3 und §8 führen das Gebet
   ausdrücklich als **Geschäfts-/Compliance-Entscheidung, nicht als Reichweiten-Element**.
   A's 233K-Video enthält null eigene Rahmungsworte. Ich schreibe die Gebete wie
   gewünscht, aber sie stehen hier als Absicherung, nicht als Wachstumshebel — und
   §3 hält ausdrücklich fest, dass die YPP-Richtlinienlage **aus diesem Datensatz nicht
   verifizierbar** ist. Wenn die Begründung tragen soll, gehört sie gegen die
   Originalrichtlinie geprüft, nicht gegen Kanaldaten.
2. **„Echte YouTube-Tags"** — Formel §7: A hat **0 Tags auf allen 8 Videos**, B's drei
   gemessene Treffer ebenfalls 0. Ich liefere Tags, weil sie nichts kosten; erwarte
   nichts davon.
3. ~~**`formel/thumbnail-motive.md` existiert nicht.**~~ *Seit 2026-08-04 existiert
   die Datei (Auswertung aller 90 Thumbnails). Die Motivvorgaben unten bleiben
   gültig; die neue Auswertung schärft nur: die Treffer zeigen erkennbar Jesus
   selbst, eine anonyme Gestalt ist unbelegt.* Ursprünglicher Stand: stammen aus
   Formel §5 (belegtes Motiv-Set) und `thumbnail-checkliste.md`.

Kein Widerspruch: dein Längenband 3,4–3,8 h deckt sich mit Formel §2.
~~Und „2 von 8 Titeln mit Eigennamen" entspricht der Testreihe „~jedes 4. Video".~~
**Überholt am 2026-08-23:** Die Testreihe ist ausgewertet, Eigennamen sind seitdem in
**jedem** Titel Pflicht (Formel §1). Von den acht geplanten Titeln erfüllen das zwei —
V03 (gebaut) und V06. Siehe „Was Gate 2 an diesem Plan ändert" oben.

---

## Upload-Plan

Abstand durchgehend **5 Tage** = 1,4 Uploads/Woche. Liegt im belegten Band 4–7 Tage
(B: 10 von 10 Abständen) und unter der Obergrenze von 2/Woche (Formel §6).
Startdatum ist ein Vorschlag — verschiebe den Block, das Muster bleibt.

| Video | Datum | Abstand |
|---|---|---|
| 01 | Mo 10.08.2026 | — |
| 02 | Sa 15.08.2026 | 5 Tage |
| 03 | Do 20.08.2026 | 5 Tage |
| 04 | Di 25.08.2026 | 5 Tage |
| 05 | So 30.08.2026 | 5 Tage |
| 06 | Fr 04.09.2026 | 5 Tage |
| 07 | Mi 09.09.2026 | 5 Tage |
| 08 | Mo 14.09.2026 | 5 Tage |

**Hook-Test — am 2026-08-23 auf V09+ verschoben. V05 bis V08 laufen ALLE mit
Variante (a), kurze Begrüßung.**

> ~~Ab 05 wechseln sich (a) und (b) ab — 05 und 07 kalt, 06 und 08 mit Begrüßung.~~
>
> **Begründung: eine Variable pro Runde.** V05–V08 testen den Korpuswechsel nach
> **M8** — Erzählstoff statt Spruchsammlung. Liefe daneben ein Hook-Test, wären zwei
> Variablen gleichzeitig in Bewegung und keiner der beiden Befunde ließe sich dem
> einen oder anderen zuordnen. Dieselbe Begründung hat an Gate 2 schon die
> Kadenzfrage (M1) und die gekürzte Rahmung (Formel §9) vertagt; sie gilt hier
> genauso.
>
> **Warum (a) und nicht (b):** V01–V04 liefen alle mit (a) — darunter V3, das
> einzige Video des Kanals, das bisher funktioniert (14,4 % Endretention, 80 % der
> Kanal-Wiedergabezeit). (a) beizubehalten hält V05–V08 mit V01–V04 vergleichbar.
> (b) wäre die Abweichung, und Abweichungen kosten in dieser Runde die Aussage.
>
> Beide Varianten bleiben bei jedem Video ausformuliert stehen — der Test wird
> nachgeholt, nicht gestrichen. Formel §3 hält weiterhin fest, dass ein festes
> Aufbauschema **nicht belegt** ist.
>
> *Entschieden vom Kanalinhaber am 2026-08-23, nach der Gate-2-Auswertung.*

**Nicht verplant und für Video 09+ frei:** Apostelgeschichte (23.143 W),
Jesaja 26–39 (7.984 W), Daniel 7–12 (5.182 W), Offenbarung 12–22 (5.949 W),
Genesis 43–50 (5.992 W).
*Seit 2026-08-23 ist dieser Rest keine Reserve mehr, sondern Nachschub für die
Umplanung von V06/V07 — nach M8 taugt davon nur die Apostelgeschichte als
Hauptkorpus, Genesis 43–50 als zweiter Erzählblock. Tabelle oben.*

---

## Gemeinsame Vorgaben für alle acht

**Thumbnail-Serie (Pflicht, Formel §5 / Checkliste).** Ein einziges Motiv über alle
Videos, nur in Details variiert — B nutzt in 13 von 13 Thumbnails dasselbe Bild.
Grundmotiv für diesen Kanal *(entschieden 2026-08-04 nach
`formel/thumbnail-motive.md`, Richtung 2 — die frühere „schlafende Gestalt" ist
ersetzt: eine anonyme Figur kommt in 90 Feld-Thumbnails null Mal als Hauptmotiv
vor, alle 10 Treffer zeigen erkennbar Jesus; die sitzende Bauform trägt 4/10
Treffer plus den stärksten kanal-normierten Einzelwert und ist mit 11/90 im
Feld deutlich seltener kopiert als die liegende mit 22/90)*:

> **Erkennbare sitzende Jesus-Figur** (schlichtes Gewand, Bart), allein in weiter
> dunkler Nachtlandschaft, Augen geschlossen oder gesenkt, im Profil oder halb
> abgewandt — **kein Blickkontakt**. Genau **eine** warme Lichtquelle im Bild,
> darüber tiefblauer Sternenhimmel. Gemalter Stil, hoher Kontrast, dunkles
> Gesamtbild. Kein Innenraum, kein Lamm als Pflichtelement.

Harte Werte je Thumbnail: **max. 4 Wörter**, Versalien, **Versalhöhe ≥ 11,5 % der
Bildhöhe** (≥ 125 px bei 1080p), **Kontrast ≥ 10:1**, Text im oberen Drittel,
weißer Text nur über dem dunklen Himmel — nie über Feuerschein oder Mond.

**Vor jedem Rendern:** Thumbnail auf 160×90 verkleinern und ansehen. Ist der Text
nicht in einer Sekunde erfassbar, Wörter streichen — nicht die Schrift verkleinern.

**Video:** 1920×1080, 24–30 fps, ein Standmotiv mit sanfter Bewegung
(Feuerflackern, driftende Wolken, langsamer Zoom), **kein Szenenschnitt**.

**Audio:** Sprache beginnt in Sekunde 0–3, kein Musikintro. Sprachanteil 97–100 %.
Klangbett durchgehend, Stimme 12 dB darüber.

**Kapitelmarken — Empfehlung: ja bei 01, 02, 06, 08, nein bei 03, 04, 05, 07.**
Begründung: Formel §7 stellt fest, dass A's drei größte Treffer **null** Kapitelmarken
haben und B durchgehend welche setzt — beide Muster gewinnen, es ist also eine
Nutzbarkeits- und keine Reichweitenfrage. Nutzen entsteht dort, wo viele kurze,
eigenständige Einheiten vorliegen und Hörer gezielt springen: 89 bzw. 61 Psalmen
(01, 02), 52 Jesaja-Kapitel (06), 42 Genesis-Kapitel (08). Bei den
Evangelien-Videos ist der Text ein durchlaufender Erzählstrang; dort wären
Kapitelmarken 20–30 Zeilen ohne erkennbaren Nutzen.

**Beim Upload:** KI-Kennzeichnung („altered or synthetic content") setzen —
Compliance-Entscheidung nach Formel §8, kein Datenbeleg in beide Richtungen.
SRT-Untertitelspur hochladen (0 von 19 Gewinner-Videos hat eine, echte Lücke).

**Kanalbeschreibung** (einmalig, nicht je Video):

> „He who keeps you will not slumber." — Psalm 121:4
>
> Peaceful Scripture readings for the hours when sleep won't come. Every video is a
> long, unhurried reading from the World English Bible, spoken slowly over a quiet
> night soundscape — made to be listened to with your eyes closed.
>
> New reading every few nights. Rest well.

---

# Video 01

**Titel:** `I Know You're Tired… Let These Psalms Carry You Through the Night`
**Eigennamen-Test:** nein
**Anker:** „I Know You're Tired…" (belegt, A 233K) · kein „Tonight" (in 6/10 Treffern, kein Muss)

**Textkorpus:** Psalmen 1–89 + 1. Petrus + Jakobus
**Gemessen:** 29.670 Wörter → **3,53 h** bei 140 WPM → ca. 154.600 Zeichen TTS

### Eingangsgebet (182 Wörter)

> Father, I come to you at the end of a long day, and I don't have much left to bring you.
>
> You know how this day went. You know what it asked of me, and you know the part I
> couldn't manage. I'm not going to explain it to you — you were there for all of it.
>
> So I'm setting it down now. Not solving it. Just setting it down, the way a person
> sets down something heavy at the door before coming inside.
>
> Thank you that you don't ask me to be strong here. Thank you that the psalms I'm
> about to hear were written by people who were tired too — who said so plainly, out
> loud, and were not turned away for it.
>
> Quiet the part of me that keeps working after the work is done. Loosen my shoulders.
> Slow my breathing. Let your word do what my own thoughts can't do tonight, which is
> to make me still.
>
> Watch over this house while I sleep. Watch over the people I love, wherever they are.
>
> I'm yours. Amen.

### Hook

**(a) mit kurzer Begrüßung** — *ab Sekunde 0*
> „I know you're tired. You don't have to do anything here — you don't even have to
> stay awake. In a moment I'll begin reading through the Psalms, slowly, from the
> beginning. Let them run under your thoughts until your thoughts go quiet. Get
> comfortable, and let your eyes close."

**(b) kalter Start** — *ab Sekunde 0, direkt in den Text*
> „Psalm 1. Blessed is the man who doesn't walk in the counsel of the wicked…"

### CTA (2, beide in den ersten 60 s)

1. „If there's something you'd like prayed for tonight, leave it in the comments —
   I read them, and others here pray through them too."
2. „If this becomes part of how you fall asleep, subscribing helps you find the next one."

### Thumbnail

**Motiv:** Grundmotiv — sitzende Jesus-Figur auf einem Felsen, Sternenhimmel
besonders weit und klar, Mond hoch links, Lagerfeuer klein und ruhig.
Gewand-Akzent in tiefem Rot.
**Text:** `SO TIRED TONIGHT` (3 Wörter)

### Beschreibung

```
I Know You're Tired… Let These Psalms Carry You Through the Night

If today took more from you than you had to give, this is a quiet place to end it.
Eighty-nine psalms, read slowly and without interruption, so you can stop holding
your thoughts together and let them settle.

Nothing here needs your attention. Let it play, close your eyes, and rest.

Focused on:
• Weariness that sleep alone doesn't fix
• Letting go of the day
• Being carried instead of carrying
• Quiet for a mind that won't stop

Read from the World English Bible (British Edition).

May you sleep held and wake lighter. If these readings help you, subscribing means
you'll find the next one.

Support the channel: [Spendenlink]

#biblesleep #psalmsforsleep #christiansleep #bibleversesforsleep #scriptureforsleep
```

**Tags:** `bible for sleep`, `psalms for sleep`, `christian sleep meditation`,
`scripture for sleep`, `sleep with god's word`, `bible reading for sleep`,
`peaceful bible reading`, `psalms read aloud`, `bedtime bible`, `sleep bible`,
`world english bible`, `book of psalms`, `christian bedtime`, `rest in god`,
`bible audio for sleep`

---

# Video 02

**Titel:** `Stop Thinking For A Moment, and Let God's Wisdom Quiet You Tonight`
**Eigennamen-Test:** nein
**Anker:** „Stop Thinking For A Moment," (belegt, B 96K)

**Textkorpus:** Psalmen 90–150 + Sprüche
**Gemessen:** 30.260 Wörter → **3,60 h** → ca. 157.700 Zeichen TTS

### Eingangsgebet (166 Wörter)

> Lord, my mind is still going, and it has been going for hours.
>
> It keeps turning the same few things over, as if turning them once more will finally
> settle them. It won't. I know that by now, and I still can't stop.
>
> I'm not asking you to answer any of it tonight. Most of it isn't a question, it's just
> noise wearing the shape of a question.
>
> What I'm asking is narrower: let something truer than my own thinking be the last
> thing in my ears. Let these psalms and proverbs run past me slowly. I don't need to
> follow them. I don't need to remember them in the morning.
>
> You made the night for sleeping. You didn't make me to keep watch over things you're
> already watching.
>
> So take the shift from me now. Let my thoughts slow to your pace instead of their own.
>
> Give me sleep, and give it to the people who are lying awake tonight the way I am.
>
> Amen.

### Hook

**(a) mit kurzer Begrüßung**
> „Stop thinking for a moment. Whatever your mind is working on, it will still be there
> tomorrow, and it will be easier then. For the next few hours there's nothing to
> follow and nothing to remember — just the Psalms and Proverbs, read slowly. Close
> your eyes."

**(b) kalter Start**
> „Psalm 90. A Prayer by Moses, the man of God. Lord, you have been our dwelling place
> for all generations…"

### CTA (2)

1. „If your mind is somewhere heavy tonight, put it in the comments — this is a good
   place to be prayed for."
2. „Subscribe if you'd like the next reading to find you."

### Thumbnail

**Motiv:** Grundmotiv, aufgeschlagenes Buch neben der sitzenden Figur (belegt
in A's 245K), Feuer etwas größer und wärmer, Himmel mit dichterem Sternenfeld.
**Text:** `QUIET YOUR MIND` (3 Wörter)

### Beschreibung

```
Stop Thinking For A Moment, and Let God's Wisdom Quiet You Tonight

For the nights when your mind won't stop working. Psalms 90 through 150 and the whole
book of Proverbs, read slowly and without interruption — nothing to follow, nothing
to remember.

Let it play, close your eyes, and let the noise go quiet on its own.

Focused on:
• A mind that keeps circling
• Wisdom instead of worry
• Letting the night be the night
• Falling asleep in God's presence

Read from the World English Bible (British Edition).

Rest well tonight. Subscribing helps you find the next reading.

Support the channel: [Spendenlink]

#biblesleep #proverbs #psalmsforsleep #christiansleep #bibleversesforsleep
```

**Tags:** `proverbs for sleep`, `psalms for sleep`, `bible for sleep`,
`christian sleep meditation`, `wisdom for sleep`, `overthinking help`,
`scripture for sleep`, `book of proverbs`, `bible reading for sleep`,
`sleep with god's word`, `calm my mind`, `bedtime bible`, `world english bible`,
`peaceful scripture`, `christian bedtime`

---

# Video 03

**Titel:** `If You're Overwhelmed, Let the Gospel of John Quiet Your Mind`
**Eigennamen-Test:** **JA** — „Gospel of John" (Testreihe 1 von 2)
**Anker:** „If You're Overwhelmed," (belegt, B 1,3K)

> **Abgrenzung zum Konkurrenten:** A's 245K-Video heißt „If You're Anxious, Rest to the
> Gospel of John Tonight". Ursprünglich stand hier derselbe Anker *und* derselbe
> Eigenname — zu nah am Original. Kanal F ist mit 18 Views genau daran gestorben
> (Formel §1). Der Eigenname bleibt, weil er der Testfall ist; der Anker ist getauscht
> gegen „If You're Overwhelmed," — ebenfalls aus den 13 belegten, kommt in **keinem**
> der 8 A-Titel vor. Die Testfrage (zieht ein Eigenname bei einem neuen Kanal?) bleibt
> damit unverändert.
>
> Der Anker ist mit **1,3K Views** (B) deutlich schwächer belegt als „If You're
> Anxious," mit 245K. Das ist der Preis der Abgrenzung und keine Aussage über die
> Zugkraft: B's Videos streuen von 1,3K bis 166K ohne messbaren Unterschied in den
> Titeln (Formel §1, offene Frage 3).

**Textkorpus:** Johannes + Hebräer + 1. Johannes + Kolosser
**Gemessen:** 30.009 Wörter → **3,57 h** → ca. 156.300 Zeichen TTS

> **Korpus geprüft und unverändert (2026-08-04).** Zwischenzeitlich stand eine
> Erweiterung um 1. Petrus + Jakobus im Raum (aus einem Lauf, in dem Johannes
> Video 01 werden sollte). Sie entfällt: Video 01 liest 1. Petrus und Jakobus
> bereits — die beiden Videos hätten sich überschnitten. Der geplante Korpus
> liegt mit 3,43 h bei 145,9 WPM ohnehin im Zielband und braucht keine
> Ergänzung.

### Eingangsgebet (195 Wörter)

> Jesus, I'm overwhelmed tonight, and I can't argue myself out of it.
>
> It isn't one large thing. It's a dozen small ones standing close together, and from
> where I'm lying they look like a wall.
>
> I know what I'd say to someone else in this bed. I'd tell them most of what they fear
> won't happen, and that the part that does happen won't come alone — you'll be in it
> with them. I believe that for other people more easily than I believe it for myself.
>
> So let me hear it in your own words instead of mine. Let John's account of you be the
> voice in the room tonight: the way you spoke to people who were frightened, the way
> you never once told them they were foolish for it.
>
> You didn't scold the disciples in the storm. You stood up in the boat.
>
> Stand up in this one. Not necessarily to change anything by morning — just to be
> here, so that I stop bracing.
>
> Loosen my jaw. Slow my chest. Take the watch from me.
>
> And be near to everyone listening tonight who is more afraid than they let on.
>
> Amen.

### Hook

**(a) mit kurzer Begrüßung**
> „If you're overwhelmed tonight, you're in a good place to be. Nothing here asks anything
> of you. In a moment I'll begin reading the Gospel of John from the beginning, slowly,
> all the way through. Let it be the last voice you hear. Get comfortable and close
> your eyes."

**(b) kalter Start**
> „John, chapter one. In the beginning was the Word, and the Word was with God, and
> the Word was God…"

### CTA (2)

1. „If something has you overwhelmed tonight, leave it in the comments — you'll be prayed
   for here, and you won't be the only one."
2. „Subscribe if you'd like this to be part of your nights."

### Thumbnail

**Motiv:** Grundmotiv am Wasser — sitzende Figur am stillen Ufer,
Mondspiegelung auf der Oberfläche, Feuer rechts.
**Text:** `GOSPEL OF JOHN` (3 Wörter)

> **2026-08-06, Planungsentscheidung — Motivtausch 03 ↔ 05, und 04 neu.**
> Video 03 bekommt das Wassermotiv, das bisher für Video 05 vorgesehen war;
> Video 05 übernimmt im Gegenzug die bisherige 03-Variante (naher Blickwinkel,
> Kopf gesenkt, Hände im Schoß). Video 04 tauscht „weiter Bildausschnitt,
> Hügelsilhouette" gegen die **einsame Hütte** aus dem belegten Motivset.
>
> Begründung nach `formel/thumbnail-motive.md` Aufgabe 3: Konsistenz der
> **Bildwelt** ist Pflicht, das **Feinmotiv** darf variieren. Gewinner A hält
> sein Feinmotiv nur **4 von 8** Videos durch, seine Bildwelt dagegen 8/8;
> B ebenso — Feinmotiv 10/13, Bildwelt 13/13. Der konsistenteste Kanal der
> Stichprobe (F, 10/10) ist zugleich der toteste. Feinmotiv-Variation kostet
> also nichts und verschafft den Videos untereinander Abgrenzung.
>
> Titel, Korpora, Hooks, CTAs, Beschreibungen und Tags bleiben unverändert.
> Die Thumbnail-Texte bleiben bei ihren Videos.

### Beschreibung

```
If You're Overwhelmed, Let the Gospel of John Quiet Your Mind

For the nights when it's all too much at once. The complete Gospel of John, followed by
Hebrews, 1 John and Colossians — read slowly, without interruption, for anyone who
needs a steadier voice than their own thoughts.

You don't have to follow along. Let it play and let your eyes close.

Focused on:
• Being overwhelmed at the end of the day
• The words of Jesus, read slowly
• Being kept, not fixed
• Peaceful sleep in God's presence

Read from the World English Bible (British Edition).

May you rest tonight. Subscribing helps you find the next reading.

Support the channel: [Spendenlink]

#gospelofjohn #biblesleep #christiansleep #bibleversesforsleep #anxietyrelief
```

**Tags:** `gospel of john`, `john bible for sleep`, `bible for sleep`,
`anxiety bible verses`, `christian sleep meditation`, `scripture for sleep`,
`new testament for sleep`, `bible reading for sleep`, `sleep with god's word`,
`peaceful bible reading`, `book of john`, `bedtime bible`, `world english bible`,
`christian anxiety`, `rest in jesus`

---

# Video 04

**Titel:** `No More Thinking Tonight… Let the Words of Jesus Settle Your Heart`
**Eigennamen-Test:** nein
**Anker:** „No More Thinking Tonight…" (belegt, B 166K — derselbe Anker war B's Durchbruch)

**Textkorpus:** Matthäus + Epheser + Philipper + Daniel 1–3
**Gemessen:** 31.112 Wörter → **3,70 h** → ca. 162.100 Zeichen TTS

### Eingangsgebet (161 Wörter)

> God, it's late, and I'm still deciding things that don't need deciding tonight.
>
> Some of them are real. Most of them are rehearsals — conversations I'll never have,
> arranged and rearranged until they're worn smooth.
>
> I'd like to stop. Not permanently. Just until morning.
>
> You gave the day its own troubles and told us that was enough. I've been trying to
> take on tomorrow's share as well, in the dark, alone, with none of the facts I'd
> need. That's not diligence. It's just fear moving quickly.
>
> So let me hear your Son instead. Let his teaching be the thing my mind runs on for
> the next few hours, until it forgets to run at all.
>
> Take the decisions off the table. They'll keep.
>
> Keep this house through the night. Keep the people I'd worry about if I let myself.
>
> And when morning comes, let me meet it rested, and one step behind you rather than
> three steps ahead of myself.
>
> Amen.

### Hook

**(a) mit kurzer Begrüßung**
> „No more thinking tonight. Nothing you decide at this hour will be better than what
> you decide tomorrow. For the next few hours it's just the Gospel of Matthew, read
> slowly. Let it go past you. Close your eyes."

**(b) kalter Start**
> „Matthew, chapter one. The book of the genealogy of Jesus Christ, the son of David,
> the son of Abraham…"

### CTA (2)

1. „If there's something you'd like prayed over tonight, leave it below — this comment
   section is a quiet one, and people pray through it."
2. „Subscribe if you'd like the next reading."

### Thumbnail

**Motiv:** Grundmotiv mit **einsamer Hütte** — ferne Hütte mit einem warm
erleuchteten Fenster als der **einen** warmen Lichtquelle, **kein Lagerfeuer in
diesem Bild**, Figur sitzt im Vordergrund, sehr dunkler Himmel, Mond als
schmale Sichel.
**Text:** `THINK NO MORE` (3 Wörter)

> **2026-08-07 — Textzeile gekürzt, weil sie nicht ins Bild passt.**
> `NO MORE THINKING` braucht bei der vorgeschriebenen Versalhöhe von 125 px
> **1896 px** Breite; verfügbar sind bei 1920 px Bildbreite und 40 px Rand je
> Seite nur **1840 px** — 56 px zu breit, und zwar in FreeSerif Bold, der
> schmalsten installierten Serife. Die Checkliste lässt hier nur einen Weg:
> „Wörter kürzen — nicht die Schrift verkleinern."
>
> `THINK NO MORE` hält den Anker („No More Thinking Tonight…", B 166K), ist
> mit 13 Zeichen und **1548 px** komfortabel (Rand 186 px je Seite) und bleibt
> im Imperativ wie die Gewinner-Texte. **`STOP THINKING` wurde verworfen**: es
> ist wörtlich der Titelanker von Video 02 („Stop Thinking For A Moment") —
> zwei Videos der Serie mit derselben Thumbnail-Aussage wäre vermeidbare
> Verwechslung.
>
> Der **Titel bleibt unverändert**; gekürzt ist allein die Zeile im Bild.

> **2026-08-06:** ersetzt „weiter Bildausschnitt, Hügelsilhouette hinter dem
> Feuer". Hütte und erleuchtetes Fenster stehen beide in Formel §5 im belegten
> Motivset, das Fenster ausdrücklich als zulässige warme Lichtquelle neben
> Lagerfeuer und Mond. Begründung des Tauschs: siehe Video 03.

### Beschreibung

```
No More Thinking Tonight… Let the Words of Jesus Settle Your Heart

For the nights when your mind keeps deciding things that can wait until morning. The
complete Gospel of Matthew, with Ephesians, Philippians and the opening of Daniel —
read slowly, start to finish.

Nothing to follow. Let it play and let your eyes close.

Focused on:
• A mind that won't stop planning
• The teaching of Jesus, read slowly
• Letting tomorrow wait
• Deep, quiet sleep

Read from the World English Bible (British Edition).

Sleep well tonight. Subscribing helps you find the next one.

Support the channel: [Spendenlink]

#biblesleep #gospelofmatthew #christiansleep #bibleversesforsleep #sleepmeditation
```

**Tags:** `gospel of matthew`, `bible for sleep`, `christian sleep meditation`,
`scripture for sleep`, `matthew bible reading`, `overthinking at night`,
`new testament for sleep`, `bible reading for sleep`, `sleep with god's word`,
`words of jesus`, `bedtime bible`, `peaceful bible reading`, `world english bible`,
`christian bedtime`, `rest in god`

---

# Video 05

**Titel:** `You're Tired, I Know… Sleep to the Whole Story, Read Slowly`
**Eigenname im Titel:** ⚠ **fehlt — seit 2026-08-23 Pflicht** (Formel §1). Titel muss
vor dem Bau angepasst werden; „Gospel of Luke" ist der Name des eigenen Korpus.
Thumbnail-Text, Beschreibung und Tags ziehen mit.
**Korpusart nach M8:** erfüllt — Lukas 81,7 %, Prediger als Beigabe.
**Anker:** „You're Tired, I Know…" (belegt, A 201K)
**Hook:** Variante **(a), kurze Begrüßung** *(geändert am 2026-08-23 — war (b);
Hook-Test auf V09+ verschoben, siehe Upload-Plan)*

> **Abgrenzung:** Die zweite Titelhälfte hieß zuerst „Sleep to the Story of Jesus
> Tonight". Damit lag der Titel bei 71,4 % gemeinsamer inhaltstragender Wörter mit
> A's „You're Tired, I Know... Jesus Watches Over You Tonight" (233K) —
> geteilt: *know, tired, you, jesus, tonight*. Über der 50-%-Grenze. „Jesus" und
> „Tonight" sind gestrichen, der belegte Anker bleibt. Jetzt 50,0 %.

**Textkorpus:** Lukas + Prediger
**Gemessen:** 29.880 Wörter → **3,56 h** → ca. 155.700 Zeichen TTS

### Eingangsgebet (179 Wörter)

> Lord, you know how long this stretch has been.
>
> Not one bad day — a run of them, close enough together that I've stopped counting.
> I keep waiting for the week that finally feels different, and it keeps not arriving.
>
> I'm not asking you to explain the season I'm in. Ecclesiastes says there is a time
> for everything, and I believe it, though I'd rather be past this particular time
> than in the middle of it.
>
> What I need tonight is smaller than an answer. I need to stop straining for a while.
>
> So let Luke's account of your Son go past me slowly — the long walk of it, the meals,
> the people he stopped for. He was never in a hurry. Let some of that reach me.
>
> Take the ache out of my shoulders. Take the argument out of my head.
>
> Let me sleep the way a child sleeps in a house where someone else is awake and
> keeping watch.
>
> And be gentle tonight with everyone else who has run out of ways to fix things.
>
> Amen.

### Hook

**(a) mit kurzer Begrüßung** ← **für Video 05 verwenden** *(seit 2026-08-23)*
> „You're tired — I know. This isn't something you have to listen to, it's just
> something to fall asleep in. The whole Gospel of Luke, read slowly, and then
> Ecclesiastes. Close your eyes."

**(b) kalter Start** *(ausformuliert, für den Hook-Test ab V09 aufgehoben)*
> „Luke, chapter one. Since many have undertaken to set in order a narrative concerning
> those matters which have been fulfilled among us…"

### CTA (2)

1. „If you'd like something carried in prayer tonight, leave it in the comments."
2. „Subscribe if these readings help you sleep."

### Thumbnail

**Motiv:** Grundmotiv, aber Blickwinkel etwas näher an der sitzenden Figur —
Kopf gesenkt, Hände im Schoß; Feuer im Vordergrund rechts, Mond klein und hoch.
**Text:** `GOSPEL OF LUKE` (3 Wörter)

> **2026-08-06:** getauscht mit Video 03, das jetzt das Wassermotiv trägt.
> Begründung: siehe Video 03.
>
> **2026-08-23:** Zeile von ~~`YOU'RE TIRED`~~ auf `GOSPEL OF LUKE` geändert —
> Entscheidung des Kanalinhabers, damit Titel und Thumbnail denselben Eigennamen
> führen (Formel §1). Nachgemessen mit der Methode aus `thumbnail.py`, FreeSerif
> Bold @ 184 px, Versalhöhe 125 px: **1607 px** breit, 156 px Rand je Seite —
> 2 px schmaler als `GOSPEL OF JOHN` bei Video 03 (1609 px). Die Serie bleibt in
> der Zeilenbreite deckungsgleich. Tabelle in `produktion/motive/README.md`.

### Beschreibung

```
You're Tired, I Know… Sleep to the Whole Story, Read Slowly

For the stretch of days that doesn't seem to end. The complete Gospel of Luke,
followed by Ecclesiastes — read slowly, without interruption, from beginning to end.

Nothing to keep up with. Let it play, close your eyes, and rest.

Focused on:
• Tiredness that has been building for a while
• The life of Jesus, told slowly
• A season you didn't choose
• Sleep without straining

Read from the World English Bible (British Edition).

Rest tonight. Subscribing helps you find the next reading.

Support the channel: [Spendenlink]

#biblesleep #gospeloflukeforsleep #christiansleep #bibleversesforsleep #ecclesiastes
```

**Tags:** `gospel of luke`, `bible for sleep`, `christian sleep meditation`,
`ecclesiastes`, `scripture for sleep`, `luke bible reading`,
`new testament for sleep`, `bible reading for sleep`, `sleep with god's word`,
`life of jesus`, `bedtime bible`, `peaceful bible reading`, `world english bible`,
`christian bedtime`, `weary soul`

---

# Video 06

**Titel:** `Don't Go to Sleep Worried… Isaiah's Comfort Until Morning Comes`
**Eigenname im Titel:** vorhanden („Isaiah"). ~~Testreihe 2 von 2~~ — die Testreihe ist
seit 2026-08-23 ausgewertet und zur Pflicht geworden (Formel §1).
**Korpusart nach M8:** ⚠ **verletzt** — Jesaja 89,8 %, also prophetische Rede als
Hauptkorpus. **Dieses Video ist so nicht baubar**, der Korpus muss neu geschnitten
werden. Siehe „Was Gate 2 an diesem Plan ändert" am Dokumentanfang.
**Anker:** „Don't Go to Sleep Worried…" (belegt, B 32K)
**Hook:** Variante **(a), kurze Begrüßung** *(unverändert; Hook-Test seit
2026-08-23 auf V09+ verschoben)*

> **Abgrenzung:** Die zweite Titelhälfte hieß zuerst „Isaiah's Comfort for a Restless
> Heart". Damit lag der Titel bei 62,5 % gemeinsamer inhaltstragender Wörter mit
> B's „Don't Go to Sleep Worried… Let These Psalms Calm Your Heart" (32K) —
> geteilt: *go, heart, not, sleep, worried*. „Heart" ist ersetzt, der belegte Anker
> bleibt. Jetzt 44,4 %.

**Textkorpus:** Jesaja 1–25 + Jesaja 40–66 + Daniel 4–6
**Gemessen:** 30.693 Wörter → **3,65 h** → ca. 159.900 Zeichen TTS

> Jesaja 26–39 bleibt bewusst frei für ein späteres Video.

### Eingangsgebet (166 Wörter)

> Father, I'm carrying something into the night that I can't do anything about until
> morning — and possibly not then either.
>
> That's the part that keeps me awake. Not the trouble itself, but the fact that it
> sits outside my reach, and I keep reaching anyway.
>
> You spoke to a whole nation through Isaiah when things were far past mending, and you
> didn't begin by explaining yourself. You began by saying: comfort my people. Speak
> tenderly. The word came before the repair.
>
> Speak tenderly to me tonight, then. Before anything is fixed.
>
> Let these chapters be a hand on my shoulder rather than an argument. I'm not in a
> state to be convinced of much. But I can be quieted.
>
> Loosen the grip. Take the night shift. Let the thing I'm worried about stay in your
> keeping until it's actually mine to handle again.
>
> And for everyone listening who is worried about someone they love — give them a few
> hours of not carrying it.
>
> Amen.

### Hook

**(a) mit kurzer Begrüßung** ← **für Video 06 verwenden**
> „Don't go to sleep worried. Whatever it is, it isn't yours to hold through the night.
> For the next few hours it's just Isaiah, read slowly — the comfort chapters and the
> ones before them. Get comfortable and let your eyes close."

**(b) kalter Start**
> „Isaiah, chapter one. The vision of Isaiah the son of Amoz, which he saw concerning
> Judah and Jerusalem…"

### CTA (2)

1. „If you're worried about someone tonight, leave their name or just say what's
   weighing on you — people here pray through the comments."
2. „Subscribe if you'd like the next reading to find you."

### Thumbnail

**Motiv:** Grundmotiv, Feuer klein, weiter Horizont mit ferner Hügelkette,
sehr großer Sternenhimmel, Gewand stärker in Rot betont.
**Text:** `ISAIAH TONIGHT` (2 Wörter)

### Beschreibung

```
Don't Go to Sleep Worried… Isaiah's Comfort Until Morning Comes

For the nights when you're carrying something you can't do anything about yet. Isaiah
chapters 1–25 and 40–66, with Daniel 4–6 — read slowly, without interruption.

Nothing here needs following. Let it play and close your eyes.

Focused on:
• Worry you can't act on tonight
• Comfort spoken before anything is fixed
• Being kept through the dark hours
• Deep, unhurried sleep

Read from the World English Bible (British Edition).

Sleep well. Subscribing helps you find the next reading.

Support the channel: [Spendenlink]

#isaiah #biblesleep #christiansleep #bibleversesforsleep #comfortscripture
```

**Tags:** `book of isaiah`, `isaiah for sleep`, `bible for sleep`,
`christian sleep meditation`, `comfort scripture`, `scripture for sleep`,
`old testament for sleep`, `bible reading for sleep`, `sleep with god's word`,
`worry and anxiety`, `bedtime bible`, `peaceful bible reading`,
`world english bible`, `christian bedtime`, `prophets bible`

---

# Video 07

**Titel:** `Fall Asleep Without Stress… God's Promises for a Quiet Heart`
**Eigenname im Titel:** ⚠ **fehlt — seit 2026-08-23 Pflicht** (Formel §1).
**Korpusart nach M8:** ⚠ **grenzwertig** — Markus trägt nur 49,0 %, dazu Römer 32,4 %
(Brief) und Offenbarung 18,6 % (Apokalyptik). Braucht eine Entscheidung, bevor gebaut
wird.
**Anker:** „Fall Asleep Without Stress…" (belegt, B 35K)
**Hook:** Variante **(a), kurze Begrüßung** *(geändert am 2026-08-23 — war (b);
Hook-Test auf V09+ verschoben, siehe Upload-Plan)*

**Textkorpus:** Markus + Römer + Offenbarung 1–11
**Gemessen:** 29.123 Wörter → **3,47 h** → ca. 151.700 Zeichen TTS

### Eingangsgebet (153 Wörter)

> God, I've been braced all day, and my body hasn't been told the day is over.
>
> The pressure wasn't dramatic. It was just constant — one thing after another, none of
> them large, all of them mine to handle. And now I'm lying still and everything in me
> is still moving.
>
> I don't need you to remove anything tonight. I need you to be steady while I stop
> being steady for a few hours.
>
> Your word says nothing separates us from your love — not trouble, not pressure, not
> the parts of me that gave out today. I'd like to hear that said slowly, in full,
> without having to hold onto it.
>
> So take the tension out of my hands. Unclench whatever I'm still gripping.
>
> Let my breathing drop into something slower than my thoughts.
>
> Keep watch over the night, and over everyone lying awake in it.
>
> I'm going to stop now. Amen.

### Hook

**(a) mit kurzer Begrüßung** ← **für Video 07 verwenden** *(seit 2026-08-23)*
> „Fall asleep without stress tonight. Nothing is asked of you here. The Gospel of
> Mark, then Romans — read slowly, all the way through. Close your eyes."

**(b) kalter Start** *(ausformuliert, für den Hook-Test ab V09 aufgehoben)*
> „Mark, chapter one. The beginning of the Good News of Jesus Christ, the Son of God…"

### CTA (2)

1. „If today pressed on you, say so in the comments — you'll be prayed for."
2. „Subscribe if you'd like these readings to keep coming."

### Thumbnail

**Motiv:** Grundmotiv, Feuer als hellster Punkt deutlich rechts, sitzende Figur
in der linken Bildhälfte, dichter Sternenhimmel, kein Mond.
**Text:** `NO MORE STRESS` (3 Wörter)

> **2026-08-07 — Textzeile gekürzt, weil sie nicht ins Bild passt.**
> `REST WITHOUT STRESS` braucht bei der vorgeschriebenen Versalhöhe von 125 px
> **2163 px**; verfügbar sind bei 1920 px Bildbreite und 40 px Rand je Seite
> nur **1840 px** — 323 px zu breit. Die Checkliste lässt hier nur einen Weg:
> „Wörter kürzen — nicht die Schrift verkleinern."
>
> `NO MORE STRESS` misst **1624 px** (Rand 148 px je Seite), bleibt bei 3
> Wörtern und hält das Ankerwort des Titels („Fall Asleep Without **Stress**…",
> B 35K). Gemessene Alternativen: `NO STRESS TONIGHT` mit 1923 px ist selbst
> noch 83 px zu breit; `LET GO TONIGHT` würde mit 1606 px passen, verliert
> aber das Ankerwort und fällt deshalb aus.
>
> Das „NO MORE"-Echo zur Zeile von Video 04 (`THINK NO MORE`) ist **gewollt**:
> Wiederholung innerhalb der eigenen Serie ist Merkmal, nicht Fehler — B trägt
> „Sleep To These Psalms" in 6 von 13 Titeln.
>
> Der **Titel bleibt unverändert**; gekürzt ist allein die Zeile im Bild.

### Beschreibung

```
Fall Asleep Without Stress… God's Promises for a Quiet Heart

For the days that weren't dramatic, just relentless. The Gospel of Mark, the letter
to the Romans, and the opening chapters of Revelation — read slowly, without
interruption.

Nothing to follow. Let it play, close your eyes, and let your body catch up.

Focused on:
• Tension that outlasts the day
• Promises read slowly, in full
• Nothing separating you from God's love
• Sleep without bracing

Read from the World English Bible (British Edition).

Rest well tonight. Subscribing helps you find the next one.

#biblesleep #gospelofmark #romans #christiansleep #bibleversesforsleep
```

**Tags:** `gospel of mark`, `book of romans`, `bible for sleep`,
`christian sleep meditation`, `stress relief scripture`, `scripture for sleep`,
`new testament for sleep`, `bible reading for sleep`, `sleep with god's word`,
`god's promises`, `bedtime bible`, `peaceful bible reading`,
`world english bible`, `christian bedtime`, `rest in god`

---

# Video 08

**Titel:** `You Need Rest… Sleep to the Beginning of Everything`
**Eigenname im Titel:** ⚠ **fehlt — seit 2026-08-23 Pflicht** (Formel §1). „Genesis"
ist der Name des eigenen Korpus.
**Korpusart nach M8:** erfüllt — Genesis-Erzählungen, in M8 ausdrücklich genannt.
**Anker:** „You Need Rest…" (belegt, A 36K)
**Hook:** Variante **(a), kurze Begrüßung** *(unverändert; Hook-Test seit
2026-08-23 auf V09+ verschoben)*

**Textkorpus:** Genesis 1–42
**Gemessen:** 29.835 Wörter → **3,55 h** → ca. 155.400 Zeichen TTS

> Genesis 43–50 bleibt frei — sinnvoller Anschluss für Video 09.

### Eingangsgebet (183 Wörter)

> Lord, before I was here, you were.
>
> That's not a comfort I usually reach for, but tonight it's the right size. Before this
> week existed, before any of what I'm worried about took shape, you were already
> speaking things into being and calling them good.
>
> I've spent today acting as though everything depended on my attention. It doesn't.
> The world held together for a long time before I arrived and will hold together while
> I sleep.
>
> So let me hear how it started. Slowly, from the first line. Light, and water, and land,
> and people who got things badly wrong and were not abandoned for it.
>
> That last part is the one I need. Every person in this book fails somewhere, and you
> stay.
>
> Stay with me tonight. Not because the day earned it — it didn't — but because that's
> what you do.
>
> Put my mind down. Put my body down. Let the first thing I hear in the morning be
> quieter than the last thing I heard today.
>
> And keep everyone listening, wherever they are, however this day treated them.
>
> Amen.

### Hook

**(a) mit kurzer Begrüßung** ← **für Video 08 verwenden**
> „You need rest — that's the whole reason this exists. Tonight we start at the very
> beginning and read straight through Genesis, slowly. You don't have to follow it.
> Get comfortable, and let your eyes close."

**(b) kalter Start**
> „Genesis, chapter one. In the beginning, God created the heavens and the earth…"

### CTA (2)

1. „If there's something you'd like prayed for, the comments are open and people here
   pray through them."
2. „Subscribe if you'd like the next reading."

### Thumbnail

**Motiv:** Grundmotiv, sehr weiter Himmel mit Milchstraßenband, Landschaft kaum
erkennbar dunkel, Feuer und sitzende Figur klein im unteren Drittel.
**Text:** `IN THE BEGINNING` (3 Wörter)

### Beschreibung

```
You Need Rest… Sleep to the Beginning of Everything

Genesis, chapters 1 to 42, read slowly from the very first line — for the nights when
you need to be reminded that the world held together long before you were asked to
hold it.

Nothing to follow. Let it play, close your eyes, and rest.

Focused on:
• Rest for someone who has been carrying too much
• The story from the beginning, told slowly
• People who got it wrong and were not abandoned
• Quiet, unbroken sleep

Read from the World English Bible (British Edition).

Sleep well. Subscribing helps you find the next reading.

Support the channel: [Spendenlink]

#genesis #biblesleep #christiansleep #bibleversesforsleep #bedtimebible
```

**Tags:** `book of genesis`, `genesis for sleep`, `bible for sleep`,
`christian sleep meditation`, `scripture for sleep`, `bible stories for sleep`,
`old testament for sleep`, `bible reading for sleep`, `sleep with god's word`,
`creation story`, `bedtime bible`, `peaceful bible reading`,
`world english bible`, `christian bedtime`, `rest in god`

---

## Titelprüfung gegen die Gewinner-Titel

Kriterium: **kein Titel teilt mehr als die Hälfte seiner inhaltstragenden Wörter mit
einem einzelnen Konkurrenztitel.** Geprüft mit `produktion/titel_pruefung.py` gegen
**21** bekannte Gewinner-Titel (8 von A, 13 von B — die vollständige Liste in
`produktion/gewinner_titel.json`, also mehr als die 17 aus dem Auftrag).

Methodik: Funktionswörter raus, einfaches Stemming (`psalms`→`psalm`, `tired`→`tir`),
Pronomen der zweiten Person werden **bewusst mitgezählt** — die Du-Ansprache ist in
dieser Nische inhaltlich, nicht grammatisch. Alle drei Entscheidungen gehen in die
strenge Richtung: sie machen die gemessene Ähnlichkeit größer, nicht kleiner.

| Video | Ähnlichkeit | Geteilt mit | Gemeinsame Wörter |
|---|---|---|---|
| 01 | 50,0 % | A „God Knows You're Tired... Sleep To These Psalms Tonight" | know, psalm, tired, you |
| 02 | 44,4 % | B „Stop Thinking For A Moment, Sleep To These Psalms Tonight" | moment, stop, think, tonight |
| 03 | 44,4 % | A „If You're Anxious, Rest to the Gospel of John Tonight" | gospel, if, john, you |
| 04 | 44,4 % | B „No More Thinking Tonight… Jesus Is With You" | jesus, no, think, tonight |
| 05 | 50,0 % | A „God Knows You're Tired... Sleep To These Psalms Tonight" | know, sleep, tired, you |
| 06 | 44,4 % | B „Don't Go to Sleep Worried… Let These Psalms Calm Your Heart" | go, not, sleep, worried |
| 07 | 50,0 % | B „Fall Asleep Without Stress… Jesus Is With You" | asleep, fall, stress, without |
| 08 | 50,0 % | A „You Need Rest... Jesus Watches Over You Tonight" | need, rest, you |

**Verstöße: 0.** Vier Titel liegen exakt auf der Grenze (50,0 %) — das ist kein Zufall,
sondern die Bauweise: Der belegte Anker *ist* die erste Titelhälfte, und er kommt aus
den Gewinner-Titeln. Wer den Anker behält, teilt zwangsläufig dessen Wörter. Die Grenze
zwingt damit genau das, was sie soll: **die zweite Hälfte muss vollständig eigen sein.**

Drei Titel mussten dafür geändert werden (03, 05, 06 — Begründung jeweils im Block).
Nachprüfbar mit `python3 produktion/titel_pruefung.py`; Rückgabewert 0 = bestanden.

**Grenze der Prüfung:** Sie misst Wortüberschneidung, nicht Bedeutung. „Quiet Your
Mind" und „Calm Your Heart" zählen als völlig verschieden, obwohl sie dasselbe sagen.
Gegen semantische Nähe schützt das Kriterium nicht — dafür gibt es aus den Daten kein
Maß.

---

## Was hier offen bleibt

- ~~**Ob die Eigennamen-Titel (03, 06) besser laufen**~~ — **an Gate 2 beantwortet
  (2026-08-23).** Eigennamen sind seitdem in jedem Titel Pflicht (Formel §1); die
  Testreihe existiert nicht mehr. Offen bleibt nur, ob der Eigenname oder der
  Erzählstoff wirkt — V3 trug beides, und V05–V08 tragen ebenfalls beides.
- **Ob Hook (a) oder (b) trägt** — nicht belegt (Formel §3), und **seit 2026-08-23
  auch nicht in dieser Runde zu klären**: V05–V08 laufen alle mit (a), damit der
  Korpuswechsel nach M8 die einzige geänderte Variable bleibt. Der Test ist auf V09+
  verschoben, beide Varianten stehen bei jedem Video ausformuliert bereit.
  Aussagekräftig wird er ohnehin erst mit mehr als je zwei Fällen.
- **Ob die Gebete überhaupt etwas bewirken** — weder für Reichweite noch für YPP aus
  diesen Daten belegbar. Sie kosten wenig und stehen als Absicherung drin.
- **Welche Motivvariante innerhalb der Serie wirkt** — B's Thumbnails sind bei 166.000
  und bei 140 Views praktisch identisch (Formel §5). Die Serie trägt die Kanalidentität,
  nicht den Einzeltreffer. Die acht Varianten oben sind Abwechslung im Rahmen, kein Hebel.
- **Beschreibungslänge und Aufbau** — nur schwach belegt (n=1 für „Wert zuerst,
  Spendenlink danach").
