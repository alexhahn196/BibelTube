# Video 06 — Titelrunde

> **Stand: 2026-08-30.** Korpus steht: **Rut → 1 Samuel → Ester**, 31.482 W,
> 89,03 % Erzählanteil ([`v06-korpus.md`](v06-korpus.md), in `plan.json` als
> „geplant, Titel offen"). Kein Gebet, kein Hook, kein Thumbnail-Motiv, kein TTS,
> kein Rendering. Alle Ähnlichkeiten gemessen mit
> [`produktion/titel_pruefung.py`](titel_pruefung.py), Grenze 45 %,
> Rückgabewert **0**. Ich entscheide nichts — die Empfehlung ganz unten ist als
> solche markiert.

---

## Vorarbeit: der Prüfer lief gegen eine Liste, nicht gegen drei

Drei Befunde, bevor gemessen werden konnte:

1. **`gewinner_titel.json` (21) war da und ist vollständig.** Unverändert.
2. **Die Kopisten-Liste fehlte ganz.** C und F waren nur als YouTube-Rohabzüge in
   `regeln/daten/listings/` vorhanden, nie als Vergleichsliste. Neu angelegt:
   [`produktion/kopisten_titel.json`](kopisten_titel.json) — **45 Titel**
   (C: 35, F: 10) mit Aufrufzahlen und Begründung, warum sie die Gegenprobe sind.
   Darin steht auch F's Kopie mit Tippfehler („I Know You're **Tried**…", 18 Aufrufe).
3. **Der Prüfer verglich nur gegen die Gewinner, mit Grenze 50 %.** Jetzt drei
   Listen und zwei Grenzen: **45 % für die Kandidaten**, 50 % für den Bestand —
   das ist die Grenze, unter der V01–V08 seinerzeit freigegeben wurden.

Zwei kleinere Korrekturen am Prüfer: der Sonderfall `isaiah's → isaiah` (er hing am
gestrichenen V06-Titel) ist durch eine generische Genitiv-Regel ersetzt — auf allen
damals 74 vorhandenen Titeln **0 Abweichungen** (bei der Zusammenführung am
2026-09-02 über alle 147 Titel der vier Listen erneut nachgerechnet: ebenfalls 0), die Messung verschiebt sich also nicht.
Und ein Titel wird nicht mehr mit sich selbst verglichen.

> **Meldung:** Am Bestand gemessen liegen **V01, V07 und V08 bei exakt 50,0 %**
> und würden die 45-%-Grenze der Kandidaten reißen. Sie hielten die 50 %, unter der
> sie freigegeben wurden. Ich habe nichts daran geändert — ein Neuschnitt des
> Bestands ist ein eigener Auftrag. Der Prüfer weist sie als Warnung aus.
>
> > **Berichtigt 2026-09-02.** Hier stand **V05** mit in der Liste. Der Wert
> > stammte aus einer Tabelle, die vor dem V05-Titelwechsel gerechnet und danach
> > nicht neu gefahren wurde. Gemessen liegt V05 („Rest Your Eyes… The Whole
> > Gospel of Luke, Read Slowly Until Morning Comes") bei **27,3 %** — dem
> > niedrigsten Wert des ganzen Bestands.

---

## Messung vorab: trägt „David" den Korpus?

**Nein.** Die David-Erzählung (1 Sam 16–31) ist **12.482 W = 39,6 %** des
Gesamtkorpus — weniger als die Hälfte.

| Block | Wörter | Anteil |
|---|---:|---:|
| Rut 1–4 (Rahmen vorn) | 2.436 | 7,7 % |
| 1 Sam 1–15 — Eli, Hanna, Samuels Berufung, Sauls Aufstieg | 11.156 | 35,4 % |
| **1 Sam 16–31 — David-Erzählung** | **12.482** | **39,6 %** |
| Ester 1–10 (Rahmen hinten) | 5.408 | 17,2 % |

Wer wegen „David" klickt, bekommt **60 % anderen Stoff**: erst gut anderthalb
Stunden Eli, Hanna, Samuel und Saul, am Ende eine Dreiviertelstunde Persien.
Zum Vergleich, wie weit die anderen Namen tragen: **Samuel als Figur 63,5 %**
(1 Sam 1–25, er stirbt in 25,1), **Saul 58,9 %** (1 Sam 9–31), **1 Samuel als
Buch 75,1 %**. „David and Goliath" wären **5,2 %** — ein Kapitel von 45.

**Antwort auf deine Frage: „David" allein überverkauft.** Es ist der Name mit der
größten Wiedererkennung und der kleinsten Deckung. Nur K6 setzt ihn, und dort ist
die zweite Titelhälfte („waited years for the throne") bewusst auf das *Warten*
gelegt — das ist der Teil, den 1 Sam 16–31 wirklich erzählt, und er passt zum
Zweck des Kanals besser als der Kampf.

---

## Die Schreibweisen nebeneinander

| Schreibweise | trifft den Inhalt | 4 Thumbnail-Wörter | im Vorschlagsband zuordenbar |
|---|---:|---|---|
| **First Samuel** | **75,1 %** — exakt | ja (2 W) | eindeutig, aber kühl; liest sich wie eine Stellenangabe |
| **Samuel** | 75,1 % Buch / 63,5 % Figur | ja (1 W) | schwach: kann als Personen- oder Kanalname gelesen werden, signalisiert nicht „Bibel" |
| **Samuel, Saul and David** | **75,1 %** — exakt | ja (3 W ohne Kommas) | stark: benennt den Bogen, längste Variante |
| **Saul and David** | 58,9 % | ja (3 W) | stark: signalisiert Konflikt und Handlung; lässt 1 Sam 1–8 und beide Rahmenbücher weg |
| **David** | 39,6 % | ja (1 W) | am stärksten wiedererkennbar — und **überverkauft am deutlichsten** |
| ~~David and Goliath~~ | **5,2 %** | ja (3 W) | höchste Wiedererkennung, grober Etikettenschwindel — **ausgeschlossen** |
| ~~the Book of Samuel~~ | 75,1 % | ja (4 W) | **doppelt ausgeschlossen:** die verbotene Bauform *Werkbezeichnung of X* (Kanal F, 18 Aufrufe) — und sachlich falsch, es gibt zwei Samuelbücher, hier läuft nur das erste |
| ~~the Story of David~~ | 39,6 % | ja (4 W) | ausgeschlossen: gleiche Bauform, dazu die Überdeckung von David |

**Rut und Ester tauchen in keinem Kandidaten auf** — 7,7 % und 17,2 %, sie sind
Rahmen, nicht Hauptsache.

---

## Die Kandidaten

| | Titel | Anker (Beleg) | Eigenname (Deckung) | Zeichen | Name ab | Gewinner | eigener Katalog | Kopisten | Thumbnail |
|---|---|---|---|---:|---:|---:|---:|---:|---|
| **K1** | If You're Anxious, Let Saul and David Take the Night Shift | `If You're Anxious,` (**245K**, unbenutzt) | Saul and David (58,9 %) | 58 | 23 | 33,3 % | 33,3 % | 33,3 % | `SAUL AND DAVID` |
| **K2** | Lord, I Feel Tired — Stay With Samuel Until Morning Comes | `Lord, I Feel Tired` (**184K**, unbenutzt) | Samuel (75,1 %) | 57 | 31 | 37,5 % | 12,5 % | 12,5 % | `SAMUEL TILL MORNING` |
| **K3** | I Know You're Tired… First Samuel Runs All the Way to Morning | `I Know You're Tired…` (**233K**, aus V01) | First Samuel (75,1 %) | 61 | 21 | 37,5 % | 37,5 % | 37,5 % | `ALL OF FIRST SAMUEL` |
| **K4** | No More Thinking Tonight… Follow Samuel, Saul and David Till Dawn | `No More Thinking Tonight…` (**166K**, aus V04) | Samuel, Saul and David (75,1 %) | 65 | 33 | 33,3 % | 33,3 % | 33,3 % | `SAMUEL SAUL DAVID` |
| **K5** | Stop Thinking For A Moment, and Stay With Samuel Till Dawn | `Stop Thinking For A Moment,` (**96K**, aus V02) | Samuel (75,1 %) | 58 | 42 | 42,9 % | 42,9 % | 14,3 % | `STAY WITH SAMUEL` |
| **K6** | You Deserve Some Rest… David Waited Years for the Throne Too | `You Deserve Some Rest…` (**559**, unbenutzt) | David (39,6 %) | 60 | 23 | 37,5 % | 12,5 % | 37,5 % | `DAVID WAITED` |

Alle sechs: unter 70 Zeichen, Eigenname beginnt vor Zeichen 60, alle drei Listen
unter 45 %, Thumbnail höchstens 4 Wörter und trägt den Namen. Sechs verschiedene
Anker, drei davon wiederverwendet — nach §1 ausdrücklich erlaubt, seit das
Wiederholungsverbot gestrichen ist (B #4 und B #7 tragen denselben Anker, die
Wiederholung war der Durchbruch).

Der jeweils schlechteste Einzeltreffer je Liste steht mit den geteilten Wörtern im
Prüflauf; hier die kritischen:

- **K1** teilt `anxiou · if · you` mit A's 245K-Titel *und* mit C's Kopie davon.
- **K3** teilt `know · tir · you` gleich dreifach — mit einem Gewinner, mit dem
  eigenen V01 und mit C's Kopie. Der Anker ist stark und breit abgeschrieben.
- **K5** teilt `moment · stop · think` mit dem Gewinner und mit V02 — 42,9 %, der
  engste Wert im Feld.
- **K4** teilt `no · think · tonight`, ebenfalls dreifach, aber nur bei 33,3 %.

---

## Je Kandidat: was ihn trägt, woran er scheitert

**K1 — If You're Anxious, Let Saul and David Take the Night Shift**
*Stark:* der stärkste der 13 Anker (245K) und bisher unbenutzt, dazu die einzige
zweite Hälfte, die eine echte Entlastung verspricht statt nur den Text anzukündigen
— „take the night shift" nimmt dem Hörer die Nacht ab. Zwei Namen, 58,9 % Deckung,
und das Thumbnail `SAUL AND DAVID` ist mit drei kurzen Wörtern gut lesbar.
*Risiko:* der Anker steckt auch in C's Kopistenkatalog, K1 liegt gegen beide Listen
bei 33,3 % — nicht zu nah, aber der Anker ist verbraucht genug, dass er im Feed
neben mehreren fast gleich beginnenden Titeln stehen kann. Und „night shift" ist
idiomatisch modern; ob das in einer Bibelnische trägt, ist ungeprüft.

**K2 — Lord, I Feel Tired — Stay With Samuel Until Morning Comes**
*Stark:* mit 12,5 % gegen den eigenen Katalog und 12,5 % gegen die Kopisten der
mit Abstand freieste Titel im Feld — der Anker (184K) ist unbenutzt und wurde von
niemandem abgeschrieben. Er ist außerdem der einzige Anker ohne „Tonight" und ohne
Du-Ansprache, ein Gebetssatz in erster Person; das hebt ihn im Feed sichtbar ab.
*Risiko:* „Samuel" allein ist die schwächste Zuordnung aller Schreibweisen — im
Vorschlagsband kann es als Personen- oder Kanalname gelesen werden und signalisiert
nicht, dass hier Bibel gelesen wird. Und der Anker ist bei A ein Volltitel, kein
Auftakt; ihn mit einem Gedankenstrich zu verlängern ist eine Bauform, für die es
keinen Beleg gibt.

**K3 — I Know You're Tired… First Samuel Runs All the Way to Morning**
*Stark:* der zweitstärkste Anker (233K), und „First Samuel" ist die einzige
Schreibweise, die den Korpus exakt und ohne Deutungsspielraum benennt — 75,1 %,
kein Überverkauf. „Runs all the way to morning" ist eine Zusage über die Länge, die
genau das verkauft, was das Video kann.
*Risiko:* dreifach 37,5 % — gegen Gewinner, eigenen V01 **und** Kopisten C, alle
über `know · tir · you`. Der Titel steht damit im Feed am dichtesten neben dem
eigenen V01, das denselben Anker trägt. Und „First Samuel" liest sich kühl, fast
wie eine Bibelstellenangabe.

**K4 — No More Thinking Tonight… Follow Samuel, Saul and David Till Dawn**
*Stark:* nennt als einziger den vollständigen Bogen und deckt damit exakt die
75,1 %, die 1 Samuel ausmacht — kein Name ist zu viel oder zu wenig versprochen.
Der Anker (166K) ist bei B belegt der Durchbruch nach Wiederholung, also genau der
Fall, für den §1 das Wiederholungsverbot gestrichen hat.
*Risiko:* mit 65 Zeichen der zweitlängste, und drei Namen hintereinander sind im
Feed viel zu lesen — mobil (68 % der Aufrufe) bricht der Titel früh ab, und was
abbricht, ist gerade die Namensreihe ab Zeichen 33. Dazu steht derselbe Anker schon
über V04; zwei eigene Videos mit gleichem Auftakt können sich gegenseitig
kannibalisieren.

**K5 — Stop Thinking For A Moment, and Stay With Samuel Till Dawn**
*Stark:* der einzige Kandidat, der gegen die Kopisten praktisch frei ist (14,3 %) —
C und F haben diesen Anker nie abgeschrieben. Kurz, ruhig, und die zweite Hälfte
ist eine schlichte Zusage ohne Bild, das schiefgehen kann.
*Risiko:* 42,9 % gegen Gewinner **und** gegen den eigenen V02 — der engste Wert im
ganzen Feld, nur 2,1 Punkte unter der Grenze. Der Eigenname beginnt außerdem erst
bei Zeichen 42, so spät wie bei keinem anderen; mobil steht er hinter dem Abschnitt,
der abgeschnitten wird.

**K6 — You Deserve Some Rest… David Waited Years for the Throne Too**
*Stark:* der einzige Kandidat mit dem Namen, der im Feed am stärksten zieht, und
die zweite Hälfte biegt ihn ins Thema des Kanals — nicht der Kampf, sondern das
Warten, und „too" spricht den Hörer direkt an, ohne ihn zu nennen. Gegen den
eigenen Katalog mit 12,5 % fast frei.
*Risiko:* **„David" deckt nur 39,6 % des Korpus** — der dokumentierte Überverkauf,
und wer nach anderthalb Stunden Eli und Saul noch wartet, hat das Versprechen
gegen sich. Dazu der schwächste Anker im Feld: 559 Aufrufe, laut §10 belegt als
*verwendet*, nicht als *wirksam*, und C hat ihn fast wörtlich („You deserve some
rest, hear the Teachings of Jesus", 89 Aufrufe) — daher 37,5 % gegen die Kopisten.

---

## Empfehlung

> **Das ist eine Empfehlung, keine Entscheidung. Du entscheidest.**

**K2 — „Lord, I Feel Tired — Stay With Samuel Until Morning Comes"**, mit
**K1 als Gegenprobe**, falls ein A/B-Test möglich ist.

Begründung in der Reihenfolge, in der die Daten belastbar sind:

1. **Abstand ist das einzige belegte Titelkriterium.** Der eine dokumentierte
   Todesfall in der ganzen Formel ist Nähe: F kopierte und bekam 18 Aufrufe. K2
   liegt gegen den eigenen Katalog und gegen die Kopisten bei je 12,5 % — kein
   anderer Kandidat kommt in die Nähe. Der Anker ist unbenutzt und, anders als
   „If You're Anxious," und „You Deserve Some Rest…", von C und F nicht
   abgeschrieben worden.
2. **184K ist stark genug.** Der Abstand zu den 245K von K1 ist bei n=1 je Anker
   kein belastbarer Unterschied; der Unterschied in der Ähnlichkeit ist es.
3. **Kein Überverkauf.** „Samuel" deckt das dominante Buch mit 75,1 %. Ich habe
   K6 bewusst mit ins Feld genommen, weil du nach David gefragt hast — aber
   39,6 % gegen 75,1 % ist der Unterschied zwischen einer Zusage und einer, die
   im zweiten Drittel bricht.
4. **Der Anker passt zum Stoff.** „Lord, I Feel Tired" ist ein Gebetssatz in
   erster Person, und 1 Samuel beginnt mit Hanna, die genau das tut: erschöpft
   im Tempel beten. Das ist keine Messung, aber es ist die einzige Stelle im
   Feld, an der Anker und Korpus dieselbe Bewegung machen.

**Was gegen die Empfehlung spricht und was du dagegenhalten solltest:** „Samuel"
ist im Vorschlagsband die schwächste Zuordnung — ein Wort, das ohne Kontext nicht
nach Bibel klingt. Wenn dir die Erkennbarkeit im Feed wichtiger ist als der
Abstand, ist **K3** die Wahl: „First Samuel" ist unmissverständlich und trifft die
75,1 % genauso — aber du bezahlst mit dreifach 37,5 % und stehst neben deinem
eigenen V01. Und wenn du den stärksten Anker ausspielen willst, ist es **K1** —
mit dem Vorbehalt, dass C denselben Auftakt schon benutzt.

**Nicht empfohlen:** K5 (42,9 %, nur 2,1 Punkte Luft, Name erst ab Zeichen 42) und
K4 (65 Zeichen mit drei Namen, mobil bricht genau die Namensreihe ab).

---

## Was hier nicht drinsteht

Kein Eingangsgebet, kein Hook, kein Thumbnail-Motiv, kein TTS, kein Rendering.
`eigene_titel.json` ist **nicht** geändert — dort steht bei V6 weiterhin der
gestrichene Jesaja-Titel. Er wird ersetzt, sobald du entschieden hast; bis dahin
wäre jeder Eintrag dort eine Entscheidung, die ich nicht treffe.
Offen bleibt außerdem Gate 1.3 (Titelanker) — alle sechs Kandidaten nutzen einen
der 13 belegten Anker, die Prüfung ist damit erfüllt, aber sie ist SOLL, nicht MUSS.
