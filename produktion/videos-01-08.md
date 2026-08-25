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
bestehen Gate-1-Prüfung 1.1 und 1.13 und überschneiden sich mit keinem anderen Video.
**Die Reihenfolge in der Spalte „Korpus" ist Teil des Vorschlags, nicht Zufall** —
Begründung unten.*

| | Korpus, in Lesereihenfolge | Wörter | Erzählanteil | Laufzeit @140 | endet auf |
|---|---|---|---|---|---|
| **V06-A** | Apostelgeschichte → Ester → Rut | **30.987** | **100,0 %** | 3,69 h | Rut 4,22 (Genealogie auf David) |
| **V06-B** | Apostelgeschichte → Ester 1–8 → Rut | **29.940** | **100,0 %** | 3,56 h | Rut 4,22 |
| **V07-A** | Markus → 1. Könige 3–16 → Jona | **29.564** | 99,3 % | 3,52 h | Jona 4,11 (offene Frage) |
| **V07-B** | Markus → 1. Könige 3–19 | **30.880** | **100,0 %** | 3,68 h | 1. Kön 19,21 (Elisa folgt Elija) |

**Alle vier Kombinationen sind kollisionsfrei.** V06 belegt Ester und Rut, V07-A
zusätzlich Jona, V07-B gar kein Kurzbuch — es gibt keine Kopplung zu beachten.

#### Warum die Reihenfolge in der Tabelle steht

Der **Schlussblock ist die teuerste Position im Video**. Er läuft, wenn der Hörer
entweder schläft oder im leichtesten Schlaf liegt, und er ist das Letzte, was von
3,5 Stunden hängenbleibt. Dieselben drei Bücher in anderer Reihenfolge sind deshalb
nicht dieselbe Entscheidung. Konkret, alles im WEBBE-Text nachgelesen:

- **Ester am Schluss** hieße, das Video auf 9,5–16 enden zu lassen — 500 Erschlagene in
  Susa, Hamans zehn Söhne gehängt, insgesamt 75.000 Tote. Mit **Rut am Schluss** endet
  es auf *„and Obed became the father of Jesse, and Jesse became the father of David"*.
- **Daniel 4–6 am Schluss** wäre 6,24: die Ankläger *„them, their children, and their
  wives; and the lions mauled them, and broke all their bones in pieces"*. Deshalb steht
  Daniel in keiner der beiden V06-Varianten mehr.
- **1. Könige am Schluss** wäre 16,34 (Hiel verliert beim Bau Jerichos seinen ältesten
  und seinen jüngsten Sohn) — in V07-A fängt Jona das ab, in V07-B verschiebt der
  Schnitt bei 19 das Ende auf Elisas Berufung.

#### Was die beiden V06-Varianten unterscheidet: Ester 9

Beide sind identisch bis auf die letzten zwei Kapitel Esters. **A** liest Ester
vollständig — drei ganze Bücher, kein einziger Schnitt, kanonisch die sauberste
Variante. **B** endet Ester bei 8,17: *„the Jews had gladness, joy, a feast and a
holiday"*. Die Rettung ist vollzogen, die Vergeltung fällt weg. Kosten: ein Schnitt im
Buchinneren und 1.047 Wörter (7,5 min).

#### Was die beiden V07-Varianten unterscheidet: ob ein Kurzbuch mitkommt

**A** braucht Jona, um ins Band zu kommen, und gewinnt dadurch den besten Schluss im
ganzen Feld — Jona 4,11 ist eine offene Frage Gottes über eine Stadt und ihr Vieh, kein
Gericht. **B** kommt mit zwei Bausteinen aus und lässt alle Kurzbücher frei; der
Schnitt bei 1. Könige 19 ist ein echter Erzählabschluss (Elijas Nachfolge geregelt,
vor dem Ahab-Kriegszyklus in 20–22).

Beide beginnen 1. Könige bei **3,1** und nicht bei 1,1. Das ist Absicht: Kapitel 1–2
sind Abischag und die Säuberung an Adonija, Joab und Schimi. Der Einstieg bei 3,5 —
*„In Gibeon, the LORD appeared to Solomon in a dream by night"* — ist für einen Kanal
namens *The Nightly Word* die passendste Übergangsstelle, die das Material hergibt.
In V07-B kommt 19,11–12 dazu, die Stimme, die weder im Sturm noch im Erdbeben noch im
Feuer ist.

**Was in beiden V07-Varianten drinbleibt und nicht wegzuschneiden ist:** 18,40, Elija
lässt die 450 Baalspropheten am Bach Kischon töten. Es liegt in der Videomitte, nicht
am Schluss — aber es ist da.

#### Was hier verworfen wurde und warum

Ein erster Vorschlag lautete **V07 = Markus + Exodus 1–20 + Jona** bzw.
**Markus + 1. Samuel 1–20**. Beide sind arithmetisch einwandfrei und beide sind an der
Tonprüfung gescheitert — auch das im Text nachgelesen:

- **Exodus 1–20** trägt 1,22 (*„You shall cast every son who is born into the river"*),
  4,24–26 (*„the LORD met Moses and wanted to kill him"* — der Blutbräutigam), die
  Plagen 7–10 und den Tod der Erstgeburt. Das ist die angsterzeugendste zusammenhängende
  Strecke im ganzen verfügbaren Material, und sie läge vollständig im Schlaffenster.
- **1. Samuel 1–20** trägt 15,3: *„kill both man and woman, infant and nursing baby"* —
  ein Ausrottungsbefehl im Gottesmund, bei rund 3 Stunden Laufzeit mit warmer
  Flüsterstimme gelesen. 1. Samuel 1–22 wäre schlimmer: es endet auf 22,18–19, dem
  Priestermord von Nob einschließlich *„children and nursing babies"*.

Das ist **kein Regelbruch** — M5 und V5 regeln die *Rahmung*, nicht den Bibeltext, und
der Text wird nach V4 wörtlich gelesen, nicht geglättet. Es ist eine Nischenfrage: der
Kanal verkauft Ruhe.

#### Ein struktureller Befund, der für jede V07-Variante gilt

Markus hat 14.261 Wörter. Damit der Korpus die Untergrenze von 29.000 erreicht, muss der
Rest mindestens 14.739 beitragen — **mehr als Markus selbst.** Markus liegt in jeder
gültigen V07-Variante zwischen **45,3 % und 49,2 %** des Korpus und kann die Hälfte
rechnerisch nie tragen. Der Titel nennt also unvermeidlich den kleineren Teil. Das ist
kein Fehler der Auswahl, sondern eine Folge davon, dass Markus das kürzeste Evangelium
ist; die Beschreibung muss den zweiten Block deshalb ausdrücklich benennen.

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

**Titel:** `You're Tired, I Know… Luke's Whole Story, Read Slowly Until Morning`
**Eigenname im Titel:** ⚠ **fehlt — seit 2026-08-23 Pflicht** (Formel §1). Titel muss
vor dem Bau angepasst werden; „Gospel of Luke" ist der Name des eigenen Korpus.
Thumbnail-Text, Beschreibung und Tags ziehen mit.
**Korpusart nach M8:** erfüllt — Lukas 81,7 %, Prediger als Beigabe.
**Anker:** „You're Tired, I Know…" (belegt, A 201K)
**Hook:** Variante **(a), kurze Begrüßung** *(geändert am 2026-08-23 — war (b);
Hook-Test auf V09+ verschoben, siehe Upload-Plan)*

> **Abgrenzung, Stand 2026-08-23 (freigegeben).** Zwei Runden:
>
> 1. Ursprünglich „…Sleep to the Story of Jesus Tonight" — 71,4 % gegen A's 233K-Titel.
>    „Jesus" und „Tonight" gestrichen → „…Sleep to the Whole Story, Read Slowly",
>    **50,0 %**. Das lag genau auf der Gate-Grenze (`<= 50 %`) und wäre bei der für
>    V05 vorgegebenen 45-%-Schranke durchgefallen.
> 2. Dazu kam die Eigennamen-Pflicht (Formel §1). Die naheliegende Fassung
>    „…The Gospel of Luke, Read Slowly Until Morning" hält zwar 33,3 % gegen die
>    Gewinner, liegt aber bei **44,4 % gegen C's totes Mashup** *„You're tired, I
>    know… Rest to the Gospel of John"* (17 Aufrufe) — näher an der Kopie als an
>    jedem Original. Es ist das Wort **„Gospel"**, das die Nähe erzeugt, nicht der
>    Anker.
>
> **Gewählt:** „Luke's Whole Story" statt „The Gospel of Luke". Der belegte Anker
> (A, 201K) bleibt, der Eigenname bleibt, und alle drei Messungen fallen auf
> **30,0 / 30,0 / 30,0 %** (Gewinner / eigener Katalog / Kopisten) — der
> ausgeglichenste Wert im ganzen Feld. Gemessen mit
> `produktion/titel_kandidaten.py`.

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
