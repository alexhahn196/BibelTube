# Video-Formel — Arbeitsdokument

> **Stand: 2026-08-02.** Datengrundlage: `regeln/daten/` (21 Gewinner-Videos aus 2 Kanälen,
> 129 Verlierer-Videos aus 8 Kanälen, 19 Voll-Metadatensätze, 4 Gewinner-Transkripte,
> 90 Thumbnails) plus `teardown/produktions-spec.md` (454 Videos, 8 etablierte Kanäle)
> und `regeln/erfolgsregeln.md`.
>
> **Wichtig zur Nutzung:** Abschnitt A ist eine **Qualifikations-Checkliste**, kein
> Hit-Prädiktor. Die Daten zeigen ausdrücklich, dass sie den Unterschied zwischen
> Treffer und Flop *innerhalb* eines Kanals **nicht** erklärt (Beleg unten, P2).
> Sie sorgt dafür, dass jedes Video überhaupt ins Rennen kommt.
>
> **Deine Formel selbst ist in der Aufgabe nicht angekommen** (nur der Platzhalter
> `[hier meine Formel von oben einfügen]`). Element-für-Element-Abgleich steht noch aus —
> dieses Dokument ist aus den Rohdaten heraus gebaut, nicht gegen deine Fassung geprüft.

---

## Prüfergebnisse deiner drei Fragen

### P1 — Tragen die Gewinner-Titel wirklich beide Anker? **Nein, das ist hineingelesen.**

Ausgezählt über alle 21 Gewinner-Titel, zwei Definitionen getrennt:

| | Zustands-Anker | Enger Eigenname (konkretes Buch/Kapitel) |
|---|---|---|
| A Hush Little Lamb (n=8) | 6/8 | **1/8** |
| B Rest in Grace (n=13) | 11/13 | **0/13** |
| Nur Treffer >30K (n=10) | **9/10** | **1/10** |

Der einzige Titel mit engem Eigennamen ist A's *„If You're Anxious, Rest to the **Gospel of
John** Tonight"* (245K). Alle anderen 20 nennen höchstens „Jesus", „God" oder „Psalms" —
Gattungsbegriffe, keine Eigennamen. B nennt in 13 Titeln **kein einziges Mal** ein konkretes
Buch.

**Der Zustands-Anker ist dagegen hart belegt: 9 von 10 Treffern.** Die einzige Ausnahme
(*„Come Little Lamb, Find Rest With Jesus"*, 47K) ist A's schwächster Treffer.

**Das widerspricht Lauf 1 direkt** — dort trugen *alle* Treffer über 20× einen Eigennamen
(Gospel of John, Isaiah, Daniel, Book of Enoch, Sermon on the Mount). Auflösung: Das waren
**etablierte Kanäle** (n=8, 454 Videos) mit gewachsenem Such-Traffic. A und B sind
**Neustarter**, die über Browse/Vorschlag laufen. Für einen neuen Kanal ist der Zustands-Anker
belegt, der Eigenname nicht.

### P2 — Hat sich bei B #7 nur die Länge geändert? **Ja — und genau das entwertet die Regel als Hit-Erklärung.**

Alles, was sich bei #7 (166.000 Views) gegenüber #6 (2.500) messbar änderte:

| Variable | #6 | #7 | geändert? |
|---|---|---|---|
| Länge | 1,9 h | **3,4 h** | **JA** |
| Titelmuster | Zustand + Psalms | Zustand + Jesus | nein (beides Serie) |
| Thumbnail-Stil | B-Serie | B-Serie | nein |
| Kapitelmarken | 50 | 93 | skaliert mit Länge |
| Upload-Abstand | 4 Tage | 4 Tage | nein |

**Aber die Gegenprobe kippt die kausale Lesart.** Video #8, sechs Tage später:
3,2 h, 91 Kapitel, dieselbe Serie, **derselbe Thumbnail-Text „TIME TO REST" wie #7** —
und **1.300 Views**. Faktor 128 bei praktisch identischen Messwerten.

Über alle 7 B-Videos ≥3,0 h: Spanne **559 bis 166.000 Views = Faktor 297.**

**Was die Länge trotzdem ist: ein Tor, kein Motor.**
- Von 6 B-Videos unter 3,0 h hat **keines** je 2.500 Views überschritten.
- Alle 10 Treffer beider Kanäle (>30K) liegen bei **≥3,2 h**.
- Natürliches Experiment: #4 *„No More Thinking Tonight… Jesus Is With You"* (1,2 h → **660**)
  gegen #7 *„No More Thinking Tonight… Rest With Jesus"* (3,4 h → **166.000**). Nahezu
  identischer Titel, derselbe Kanal, 12 Tage Abstand.

**Verdikt:** Die Regel ist haltbar — aber als **Mindestlänge (≥3,0 h, nicht 2,5 h)**, nicht als
Erfolgsursache. `regeln/erfolgsregeln.md` M6 ist entsprechend zu schärfen: Schwelle auf 3,0 h
anheben, Formulierung „Breakout fällt mit Formatwechsel zusammen" entschärfen.

### P3 — Stimmt der Zeitaufbau über mehrere Gewinner-Videos? **Nein, nur bei einem von vier.**

Gemessen an Caption-Zeitstempeln:

| Video | Rahmung bis | erster CTA | Aufbau |
|---|---|---|---|
| A 245K | 107 s (243 Wörter) | 26 s | Hook → CTA → Lesung |
| A **233K** | **2 s (0 Wörter)** | **keiner** | **startet kalt mit „John chapter 15"** |
| B 166K | 32 s (53 Wörter) | keiner | kurze Rahmung → Lesung |
| B 96K | 59 s (117 Wörter) | 33 s | Hook → CTA → Lesung |

Das zweiterfolgreichste Video im ganzen Datensatz (**233.704 Views**) hat **keine Rahmung,
keinen Hook, keinen CTA** — es beginnt nach 2,1 Sekunden direkt mit Schrifttext.

Ein Gebetsblock als fester Bestandteil ist ebenfalls nicht belegt: Wo überhaupt ein Gebet
auftaucht, liegt es bei 15 min, 66 min oder 158 min — ohne erkennbares Muster.

**Verdikt:** Ein fester Zeitaufbau Hook→CTA→Gebet→Lesung ist **nicht belegt**. Belegt ist nur:
Sprechbeginn in den ersten 0–3 s, danach überwiegend Schrifttext. Rahmung 0–110 s ist
Spielraum, kein Pflichtteil.

### Der Befund, der alles rahmt

**#7 und #8 unterscheiden sich in keiner messbaren Produktionsvariable — und um Faktor 128
in den Views.** Gleiche Serie, gleicher Thumbnail-Text, gleiche Länge, gleiche Kapitelzahl,
gleiches Titelmuster, gleiche Beschreibungsstruktur, 6 Tage Abstand.

Deckt sich mit Lauf 1 (SleepCodex: 276× Streuung innerhalb desselben Kanals bei konstanter
Produktion). **Kein Element dieser Formel — und vermutlich keines deiner Formel — sagt den
Einzeltreffer vorher.** Was die Formel leistet: das Video für den Treffer *qualifizieren*.

Trefferquote als Planungsgröße: **A 6/8, B 4/13, zusammen 10 von 21 (48 %)** der Videos, die
alle Tore passieren, kommen über 30.000 Views. Rechne mit etwa **jedem zweiten bis dritten
Upload**, nicht mit jedem.

---

## A) Checkliste vor jedem Upload

Jeder Punkt ist datenbelegt; Fallzahl in Klammern. Alle Tore müssen offen sein — dann ist
das Video qualifiziert, mehr garantiert die Datenlage nicht.

**Format**
- [ ] Laufzeit **≥ 3,0 h** (Zielband 3,2–4,0 h) — 0 von 6 kürzeren B-Videos je über 2.500 Views; alle 10 Treffer ≥3,2 h
- [ ] **1080p**, 24–30 fps (Lauf 1, n=5 belegt; 4K ohne Nachweis)
- [ ] Erzählstimme läuft bis **100 %** der Laufzeit durch, längste Pause <20 s (n=24, Lauf 1)
- [ ] Sprechbeginn in den **ersten 0–3 s** (n=24)
- [ ] Sprechtempo **120–160 WPM** (n=21)

**Bild**
- [ ] **Ein** Standmotiv mit sanfter Bewegung (Feuer, Wolken, langsamer Zoom) — kein Szenenschnitt (n=3 Gewinner-Stichproben; der tote C rotiert 8 Szenen)
- [ ] Palette: tiefes Nachtblau + **eine warme Lichtquelle** im Bild (n=11 Stichproben)
- [ ] Thumbnail gehört sichtbar zur **eigenen Serie** — gleiches Motiv, gleiche Typo wie die letzten Uploads (B: 13/13 identisches Motiv)

**Text**
- [ ] Titel trägt einen **Zustands-Anker** (9/10 Treffer)
- [ ] Titel ist **nicht** von einem anderen Kanal kopiert (F kopierte A-Titel inkl. Tippfehler → 18 Views)
- [ ] Bibeltext ist eine **echte Übersetzung** (NIV o. ä.), keine KI-Paraphrase — laut vorgelesen gegengeprüft (C's Todesursache: *„Strike all of my opponents on the mandible"*)
- [ ] Maximal **2 CTAs** im ganzen Video (Gewinner 0–2; tote Kanäle 4–7)

**Kanal**
- [ ] Dieser Upload ist der **erste oder zweite diese Woche** (Gewinner 1,3–1,5/Wo; alle 8 Verlierer 2,0–13,5)
- [ ] Abstand zum letzten Upload **≥ 4 Tage** (B: 10 von 10 Abständen liegen bei 4–7 Tagen)
- [ ] **Kein Short** auf diesem Kanal (Gewinner 0; J: 857K Shorts-Views → 171 Langform-Views)
- [ ] Kanalbeschreibung/Keywords ohne Altlasten (E trägt bis heute „Tibetan Singing Bowls" → 40 Subs)

**Bewusst NICHT auf der Liste** (siehe Abschnitt D und `erfolgsregeln.md` §3): Tags,
Kapitelmarken, Untertitelspur, 4K, KJV-vs-NIV, Kanalalter.

---

## B) Titel-Baukasten

**Bauform der Treffer:** `[Zustands-Anker] + [Zusage] + [Tonight]`
Beispiele aus den Daten: *„No More Thinking Tonight… Rest With Jesus"* (166K) ·
*„I Know You're Tired… Jesus Watches Over You Tonight"* (233K) ·
*„Stop Thinking For A Moment, Sleep To These Psalms Tonight"* (96K)

### 20 Zustands-Anker

**Belegt — wörtlich aus Gewinner-Titeln (13):**
1. `You're Tired, I Know…` (201K)
2. `I Know You're Tired…` (233K)
3. `If You're Anxious,` (245K)
4. `Lord, I Feel Tired` (184K)
5. `No More Thinking Tonight…` (166K)
6. `Stop Thinking For A Moment,` (96K)
7. `Fall Asleep Without Stress…` (35K)
8. `Don't Go to Sleep Worried…` (32K)
9. `You Need Rest…` (36K)
10. `If You're Overwhelmed,` (1,3K)
11. `Rest Your Eyes…` (915)
12. `God Knows You're Tired…` (140)
13. `You Deserve Some Rest…` (559)

**Ungeprüft — von mir aus dem Muster abgeleitet, ohne Datenbeleg (7):**
14. `If Your Mind Won't Slow Down,`
15. `When Sleep Won't Come…`
16. `You've Carried Enough Today…`
17. `If Tonight Feels Heavy,`
18. `Too Tired to Pray? …`
19. `When Tomorrow Feels Too Big…`
20. `If You're Lying Awake Again…`

> Anker 10–13 stammen aus **Flop**-Videos desselben Kanals — sie sind belegt als *verwendet*,
> nicht als *wirksam*. Bei B trugen Treffer und Flops dasselbe Muster (P2).

### 15 Eigennamen

**Wichtige Einschränkung:** Für A und B sind Eigennamen **nicht** belegt (1 von 21 Titeln, P1).
Die folgende Liste stammt aus **Lauf 1** (etablierte Kanäle, kanal-normiert) und ist für einen
**Neustarter ungeprüft**. Faktoren = Median-Views gegen den Kanal-Median.

| Eigenname | Beleg | Fallzahl |
|---|---|---|
| Gospel of John | 3,0–3,3× · A's einziger Eigennamen-Titel = 245K | n=14 |
| Gospels (gesammelt) | 2,8–3,3× | n=31 |
| Isaiah | Top-Video Rest In Faith 773K | n=10 |
| Book of Enoch | 2,3× (SleepCodex n=40), 33× (Night Psalms n=4) | n=46 |
| Angels / Watchers | 1,4–6,9× | n=36 |
| Daniel | 536K bei Rest In Faith | n=11 |
| Sermon on the Mount | 413K bei Night Psalms | n=1 |
| Proverbs | 93K bei Rest in Jesus | n=1 |
| Revelation | 1,5× global | n=12 |
| Ephesians / Galatians / Colossians | 1,0 Mio. bei The Sleep Bible | n=1 |
| Genesis | 0,43× global — **schwach** | n=13 |
| Psalms | 0,26–1,38× — **kein Effekt nachweisbar** | n=32 |
| Matthew / Luke / Mark | nur als „Gospels" belegt, einzeln nicht | — |
| Jeremiah | 1,17× global | n=4 |
| Lamentations / Job | **keine Daten** | 0 |

**Praktische Lesart:** Für die ersten ~10 Videos den Zustands-Anker führen lassen (das ist die
belegte Neustarter-Mechanik). Eigennamen als *Testreihe* dazunehmen, nicht als Grundregel —
Prüfkriterium in Abschnitt D.

---

## C) Textbausteine

### Hook (0–60 s)

**Belegt:** Rahmung ist **optional** — A's 233K-Video hat keine. Wenn du eine nimmst, dann
warm, zweite Person, unter 110 s.

*Wörtlich aus Gewinner-Videos:*
> „Hey child of God, you're safe here. If you're tired, anxious, or need some peace, this
> space was made for you. In a moment, we'll begin calmly reading the word of God from the
> Gospel of John to help you rest and find comfort." — A, 245K

> „If you're still awake tonight, I'm really glad you're here. Set every worry aside tonight
> and allow God's word to quiet your mind as you fall asleep. As you listen to these psalms,
> don't worry about tomorrow. Right now, simply rest in God's presence and receive the peace
> that only he can give." — B, 96K

> „Welcome back. Tonight, allow God's word to quiet your mind and lead you into the most
> peaceful sleep. Leave today's worries behind. And let God's word be the last thing on your
> mind before you drift off to sleep. Now, get comfortable, close your eyes, and rest in
> God's presence." — B, 166K

*Bauteile, die in allen dreien vorkommen:* Begrüßung → Zustand benennen → Erlaubnis zum
Loslassen → Ankündigung des Textes → Körperanweisung („get comfortable, close your eyes").

**Nicht tun** (Belege aus toten Kanälen): Dringlichkeit (*„Before you scroll away…"*, D, Ø 16
Views), reine Atemmeditation ohne Schriftbezug über Minuten (F, Ø 9 Views).

### CTA (maximal 2, in den ersten 60 s oder gar nicht)

> „I'd love for you to comment below where you're listening from and leave a prayer, too, so
> that we can all lift each other up." — A, 245K

> „If these nightly verses have become part of your bedtime routine, I'd love for you to
> subscribe and become part of this community." — B, 96K

> „If you enjoy these nightly Bible readings, consider subscribing so you can return whenever
> you need a peaceful place to rest in God's word." — B #3

**Nicht tun:** *„type amen in the comments"*, *„Share this message with someone who…"* (D, 7
CTAs, Ø 16 Views). Kein CTA nach der Rahmung — ab da nur noch Schrift.

### Beschreibung

Struktur aus den Gewinner-Beschreibungen (n=19, 1.160–3.581 Zeichen):

```
[Titel wörtlich wiederholen]

[2–4 Sätze: Zustand ansprechen, was das Video tut, was der Hörer bekommt]

[optional: „Focused on:" Liste mit 4–6 Stichpunkten]

Chapters:
0:00:29 - Intro
0:00:32 - Psalm 9
…

[2–3 Sätze Segenswunsch + Abo-Einladung]

#sleepwithpsalms #restwithjesus #bibleversesforsleep #christiansleep …
```

**Kapitelmarken:** B setzt sie durchgehend (40–93 Stück, Psalm für Psalm). A's drei größte
Treffer haben **null**. Beide Muster gewinnen — nimm sie für die Nutzbarkeit, nicht für die
Reichweite.

---

## D) Ungeprüft — ohne Datenbeleg

Alles hier ist plausibel, aber **nicht** aus den Daten belegt. Nicht als Regel behandeln.

| Annahme | Warum ungeprüft | Prüfkriterium |
|---|---|---|
| **Eigennamen im Titel helfen einem Neustarter** | Bei A/B 1 von 21; Beleg stammt aus etablierten Kanälen | Ab Video 10: je 5 Videos mit/ohne Eigenname, Median-Views vergleichen |
| **Zustands-Anker 14–20** (meine Ableitungen) | Nie verwendet worden | Erst nach den 13 belegten einsetzen, einzeln testen |
| **0 Tags helfen** | B's 3 gemessene Treffer haben 0 Tags, die 2 Flops ≥3h haben 6 und 22 — aber n=5, und frühe Flops hatten auch 0 | Ab Video 10 abwechselnd 0/20 Tags |
| **Warme Rahmung schlägt Kaltstart** | A's 233K-Video widerlegt es einzeln | 5 Videos mit/ohne Rahmung, Retention der ersten 60 s vergleichen |
| **Kuratierte Psalm-Reihenfolge** (23/91/121 zuerst) | Nur #10 (96K) macht das; #7 (166K) geht numerisch vor | Ab Video 10 abwechseln |
| **Untertitelspur bringt Reichweite** | 0 von 19 Gewinnern hat eine — unbesetzt, aber deshalb auch unbewiesen | Ab Video 1 mitliefern, Traffic-Quelle „Suche" in Analytics beobachten |
| **Textwiederholung 2–3× spart Kosten ohne Schaden** | Bei The Sleep Bible belegt (1,9 Mio. mit 3 Durchläufen), bei A/B ungeprüft | Ein Video mit 2 Durchläufen, Retention vergleichen |
| **Musikbett-Art (Delta/Piano/Regen)** | Vollständig ungemessen — Audio-Download blockiert | Nur über eigene Analytics |
| **Stimmcharakter der Gewinner** | Tool-Quota; für morgen geplant | Steht aus |

---

## Was die Daten nicht hergeben

1. **Warum #7 traf und #8 nicht.** Kein messbarer Unterschied. Ohne Impressions und CTR aus
   YouTube Analytics nicht auflösbar — für fremde Kanäle nicht zugänglich.
2. **Ob die Formel für einen dritten Kanal funktioniert.** n=2 Gewinner. B beweist, dass ein
   Nachzügler mit eigener Handschrift gewinnen kann; das ist ein Fall, kein Gesetz.
3. **Die Wirkrichtung bei Länge.** Belegt ist nur: kein Treffer unter 3 h (n=6). Ob 3 h
   *ursächlich* wirken oder ob längere Videos aus anderen Gründen besser gemacht wurden,
   ist mit Beobachtungsdaten nicht zu trennen.
4. **A's Sofort-Erfolg.** Video #1 traf mit 201K ohne Anlauf. First-Mover, externer Push oder
   Zufall — nicht entscheidbar. A's Zeitvorsprung ist ohnehin nicht kopierbar.
5. **Optimale Kadenz innerhalb des Sicherheitsbandes.** Belegt ist nur die Obergrenze
   (Verlierer ab 2,0/Woche). Ob 1×/Woche besser ist als 2×, sagen die Daten nicht.

---

*Änderungen an diesem Dokument gehören zusammen mit dem Beleg hier hinein. Regeln, die die
eigenen Kanaldaten ab Video 10 widerlegen, werden gestrichen — nicht verteidigt.*
