# Video-Formel v2.2 — Arbeitsdokument

> **Stand: 2026-08-23.** v2.1 = deine v2, Element für Element gegen die **Fremd**daten
> geprüft (2026-08-02). **v2.2 = die erste Revision aus eigenen Kanaldaten.**
> Datengrundlage: `regeln/daten/` (21 Gewinner-Videos aus 2 Kanälen, 129 Verlierer-Videos aus
> 8 Kanälen, 19 Voll-Metadatensätze, 4 Gewinner-Transkripte, 90 Thumbnails) plus
> `teardown/produktions-spec.md` (454 Videos, 8 etablierte Kanäle) und `regeln/erfolgsregeln.md`.
>
> **Vor jedem Rendern:** [`produktion/workflow-gates.md`](../produktion/workflow-gates.md)
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
| 1 | Zustands-Anker als Pflicht | **bleibt** — 9/10 Treffer (Anredeform 2026-08-23 nachkorrigiert: Du-Ansprache ist 7/9, nicht 9/9) |
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

**PFLICHT — Zustands-Anker.** 9 von 10 Treffern (>30K). Einzige Ausnahme ist
A's schwächster Treffer („Come Little Lamb", 47K) — der einzige Titel ohne Zustand.

> **Faktenkorrektur 2026-08-23: „in Du-Ansprache" ist zu scharf formuliert gewesen.**
> Bis heute stand hier „Zustands-Anker **in Du-Ansprache**, 9 von 10 Treffern". Die
> 9 von 10 stimmen — sie gelten aber dem **Zustand**, nicht der Anredeform. Die 9
> Zustands-Titel gegen §10 durchgezählt:
>
> | Ansprache | Anzahl | Titel |
> |---|---|---|
> | zweite Person | 4 | `If You're Anxious,` 245K · `I Know You're Tired…` 233K · `You're Tired, I Know…` 201K · `You Need Rest…` 36K |
> | Imperativ (Du mitgemeint) | 3 | `Stop Thinking For A Moment,` 96K · `Fall Asleep Without Stress…` 35K · `Don't Go to Sleep Worried…` 32K |
> | **erste Person** | **1** | **`Lord, I Feel Tired` 184K** |
> | kein Pronomen | 1 | `No More Thinking Tonight…` 166K |
>
> **Du-Ansprache ist also 7 von 9, nicht 9 von 9.** A's 184K-Treffer spricht nicht den
> Hörer an, sondern legt ihm die eigenen Worte in den Mund — und das ist der
> viertstärkste Titel im ganzen Datensatz. Ein Titel in erster Person ist damit
> **belegt, nicht verboten.** Was Pflicht bleibt, ist der **Zustand**; die Anredeform
> ist häufig, aber nicht durchgehend.

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
(**n=11**, `regeln/daten/skript_anatomie.json`: `sprechbeginn_s` 0,0–3,1 s.)

> **Quellenkorrektur 2026-08-26.** Hier stand „n=24 aus Lauf 1: 0,0–3,4 s".
> Das ist falsch: `teardown/teardown_batch_20260802_090410/matrix_voll.csv`
> hat zwar genau 24 Zeilen, `sprache_start_s` läuft dort aber von **0,0 bis
> 7,8 s**, und **6 der 24** liegen über 3,0 s (3,1 · 3,4 · 3,4 · 3,5 · 6,8 ·
> 7,8). Die genannte Spanne schnitt drei ihrer eigenen Datenpunkte ab.
> Die **Regel bleibt** — sie ist durch die andere Messdatei gedeckt:
> `skript_anatomie.json` führt 11 Videos mit 0,0 / 0,0 / 0,0 / 0,1 / 0,2 /
> 0,2 / 0,3 / 0,4 / 2,1 / 2,4 / 3,1 s. Falsch war die Quellenangabe, nicht
> der Wert.

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
> [`regeln/erfolgsregeln.md`](../regeln/erfolgsregeln.md)** *(eigene Kanaldaten Gate 2)*.
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

> **Motiv-Auswertung aller 90 Thumbnails (2026-08-04): [`thumbnail-motive.md`](thumbnail-motive.md).**
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

> ### 2026-08-23 — der Stereoaufbau des Betts ist ein Fehler, kein Merkmal
>
> *(eigene Kanaldaten Gate 2. Rohwerte in `regeln/daten/gate2_eigene_kanaldaten.json`,
> Messung reproduzierbar mit `produktion/klang/klang_proben.py`.)*
>
> **Das Publikum hört mono.** 68 % der Aufrufe kommen vom Handy, 12 % vom Fernseher —
> zusammen 80 %, und beide geben über Handy-, Bluetooth- oder TV-Lautsprecher aus. Der
> Mono-Summenfall ist der **Regelfall**, nicht der Sonderfall.
>
> **Das Bett ist kein echtes Stereo.** `bett_pad_feuer.flac` trägt in R dasselbe Signal
> wie in L, nur um **240 Samples = 5,442 ms** versetzt (`np.roll(sig, 240)` in
> `stimmtest/musikbett.py`). Wer das zu Mono summiert, bekommt einen Kammfilter:
> erste Auslöschung bei **91,9 Hz**, dann alle **183,8 Hz**. Gemessen gegen die Theorie
> |cos(π f T)| — Übereinstimmung auf 0,1 dB.
>
> **Der Schaden ist nicht der Pegel, sondern der Akkord.** Das Pad besteht aus Grundton,
> Quinte, Oktave, Duodezime und Doppeloktave (55 · 82,5 · 110 · 165 · 220 Hz). Die erste
> Kammkerbe sitzt bei 91,9 Hz — zwischen Quinte und Oktave. Pegel relativ zum Grundton:
>
> | | Quinte E2 | Oktave A2 | Duodezime E3 | Doppeloktave A3 | max. Abw. |
> |---|---|---|---|---|---|
> | **Bauplan** | −5,26 | −5,26 | −11,88 | −16,75 | — |
> | **Mono-Summe, wie es jetzt ist** | **−16,18** | −11,78 | −7,99 | −13,49 | **10,9 dB** |
> | **Mono-Summe, Bett echt mono** | −4,86 | −6,12 | −12,19 | −16,28 | 0,9 dB |
>
> Die Quinte, die den Charakter des Betts trägt, liegt am Handylautsprecher **10,9 dB
> unter dem Bauplan**; gleichzeitig rückt die Duodezime 3,9 dB nach oben. Das ist kein
> Lautstärkeproblem — **das ist ein anderer Akkord als der, der im Hörtest ausgewählt
> wurde.** Mit echt monoem Bett stimmt er auf 0,9 dB.
>
> **Die Stimme ist nicht betroffen.** `schritt3_bett.py` addiert sie identisch in beide
> Kanäle (Zeilen 102/103), ohne Versatz. Gemessen: 0,00 dB Verlust in der Mono-Summe.
> Genau deshalb fällt der Fehler nicht auf — die Stimme klingt richtig, das Bett darunter
> nicht.
>
> **Nebenfolge für die 12-dB-Regel.** Die Pipeline normiert das Bett am Mono-Downmix auf
> −31 dBFS. Weil dieser Downmix 5,2 dB leiser ist als ein einzelner Kanal, steht das Bett
> **je Kanal bei −25,8 dBFS**: `qa_mix.json` meldet 12,0 dB Abstand, am Kopfhörer sind es
> **6,8 dB**. Mit echt monoem Bett sind es in beiden Fällen 12,0 dB — die Umstellung
> repariert also auch diese Inkonsistenz.
>
> **Was hier NICHT gemessen ist:** der fertige Mix. `produktion/arbeit/` ist gitignored
> und in dieser Sitzung leer; alle Aussagen zum Mix sind aus dem Bett und aus dem Code
> von `schritt3_bett.py` hergeleitet, nicht am fertigen Video nachgemessen.
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
> [`regeln/erfolgsregeln.md`](../regeln/erfolgsregeln.md).

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

> ### Wie nah jeder Anker an den Kopisten liegt (gemessen 2026-08-31)
>
> Gate 1.2 hat eine zweite Bedingung: *nicht näher an einem Kopisten-Titel als am
> nächsten Gewinner.* Sie ist die einzige Titelregel aus einem dokumentierten
> Todesfall — Kanal F kopierte wörtlich und bekam **18 Aufrufe**. Bis heute stand
> nirgends, **welche der 13 Anker die Kopisten schon benutzt haben.**
>
> Alle 13 gegen `produktion/kopisten_titel.json` gemessen (45 Titel: C 35, F 10),
> mit `produktion/titel_kandidaten.py`, Anteil geteilter inhaltstragender Wörter:
>
> | | Anker | Beleg | vergeben an | Kopisten-Nähe | nächster Kopisten-Titel |
> |---|---|---:|---|---:|---|
> | 1 | `If You're Anxious,` | 245K | — | **100 %** | „If You're Anxious, Sleep To These Psalms Tonight" |
> | 2 | `I Know You're Tired…` | 233K | V01 | **100 %** | „You're tired, I know… Rest by the Fire with Jesus" |
> | 3 | `You're Tired, I Know…` | 201K | — | **100 %** | „You're tired, I know… Rest by the Fire with Jesus" |
> | **4** | **`Lord, I Feel Tired`** | **184K** | — | **33 %** | „If You Feel Empty… Sleep To These Psalms Tonight" |
> | 5 | `No More Thinking Tonight…` | 166K | V04 | **100 %** | „No More Thinking Tonight… Jesus Is With You" |
> | 6 | `Stop Thinking For A Moment,` | 96K | V02 | **33 %** | „Stop Here And Get Some Rest… Jesus Will Keep You Safe" |
> | 7 | `You Need Rest…` | 36K | V08 | **100 %** | „You Need Some Rest, Hear the Miracles of Jesus" |
> | 8 | `Fall Asleep Without Stress…` | 35K | V07 | **100 %** | „Fall Asleep Without Stress… Jesus Is With You" |
> | 9 | `Don't Go to Sleep Worried…` | 32K | V06 | 50 % | „Don't Forget To Sleep Tonight... Jesus Is With You" |
> | 10 | `If You're Overwhelmed,` | 1,3K | V03 | **100 %** | „If You're Overwhelmed, Sleep To These Psalms Tonight" |
> | 11 | `Rest Your Eyes…` | 915 | V05 | 67 % | „Close Your Eyes... Listen to Everything Jesus Ever Said" |
> | 12 | `You Deserve Some Rest…` | 559 | — | **100 %** | „You deserve some rest, hear the Teachings of Jesus" |
> | 13 | `God Knows You're Tired…` | 140 | — | 75 % | „You're tired, I know… Rest by the Fire with Jesus" |
>
> **Acht von dreizehn liegen bei 100 %** — die Kopisten haben sie wörtlich
> übernommen. Das ist keine Randnotiz: wer einen dieser acht setzt, teilt
> **alle** inhaltstragenden Wörter seines Auftakts mit einem Kanal, der daran
> gestorben ist. Die Grenze reißt dadurch nicht automatisch — gemessen wird der
> ganze Titel, und eine eigene zweite Hälfte verdünnt den Wert —, aber die
> Reserve ist aufgebraucht, bevor der Titel überhaupt anfängt.
>
> **Unter den noch freien Ankern (#1, #3, #4, #12, #13) ist `Lord, I Feel Tired`
> der einzige ohne Kopisten-Nachbarn.** #1, #3 und #12 stehen bei 100 %, #13 bei
> 75 %. `You Deserve Some Rest…` ist dabei der ungünstigste Fall überhaupt: C hat
> ihn fast wörtlich („You deserve some rest, hear the Teachings of Jesus",
> 89 Aufrufe).
>
> **Wozu das nicht taugt:** Diese Spalte misst **Nähe zu Toten**, nicht Wirkung.
> Ein Anker mit 100 % ist nicht verbrannt — B hat mit wiederholten Ankern den
> 166K-Durchbruch gehabt (§1, Wiederholungsverbot gestrichen). Sie sagt nur, wo
> die zweite Titelhälfte die ganze Arbeit tun muss.
>
> **Nachmessen statt abschreiben:**
> `python3 produktion/titel_kandidaten.py --grenze 0.45 "Kandidat"` gibt die
> Kopisten-Nähe je Titel mit den geteilten Wörtern aus. Die Liste der Kopisten
> kann wachsen; diese Tabelle ist der Stand vom 2026-08-31.

> ### Auflösungsgrenze des Ähnlichkeitsmaßes (2026-08-26)
>
> `titel_pruefung.py` misst *Anteil geteilter inhaltstragender Wörter* =
> geteilt ÷ eigene Wortzahl. **Der Nenner ist klein.** Über die 21 Gewinner-
> und 8 eigenen Titel liegt er bei 3 bis 11, Median 6 — ein einzelnes Wort
> wiegt damit **9,1 bis 33,3 Prozentpunkte, im Median 16,7**.
>
> Daraus folgt: **Unterschiede unterhalb der Größenordnung eines Wortes sind
> kein Signal.** Als Faustregel — unter etwa 10 Prozentpunkten nichts
> hineinlesen; bei kurzen Titeln liegt die Schwelle noch deutlich höher. Zwei
> Kandidaten mit 27 % und 33 % sind nicht „der eine besser", sie sind gleich.
>
> **Nachgewiesen am V05-Paar.** „…Read Slowly Until Morning **Comes**" misst
> 27,3 %, ohne „Comes" 30,0 %. Der Zähler ist in beiden Fällen **identisch**
> (`eyes, rest, your` — drei Wörter); nur der Nenner fällt von 11 auf 10. Das
> gestrichene Wort teilt der nächste Gewinnertitel gar nicht.
>
> Das heißt: **ein inhaltsleeres Füllwort verbessert den Messwert**, einfach
> weil es den Nenner verdünnt. Das Maß lässt sich in diese Richtung
> beliebig schönen. Wer einen Titel gegen einen anderen ausspielt, muss
> deshalb die **geteilten Wörter** ansehen, nicht den Prozentwert —
> `titel_kandidaten.py` gibt sie deshalb mit aus.
>
> Die Grenze aus Gate 1.2 (< 50 %) bleibt davon unberührt: sie trennt „hat
> die Hälfte gemeinsam" von „hat sie nicht", und dafür reicht die Auflösung.

> ### Offen (2026-08-26): ab Video 09 ist kein belegter Anker mehr frei
>
> Die 13 belegten Anker sind faktisch aufgebraucht. Fünf kommen in **A-Titeln**
> vor (1, 2, 3, 4, 7) und scheiden damit für ein Video aus, das nicht wie eine
> Kopie aussehen soll. Acht sind im Achterplan vergeben: 5→V4 · 6→V2 · 8→V7 ·
> 9→V6 · 10→V3 · **11→V5** · 12 und 13 bleiben. Für **V09 und alles danach**
> bleibt nichts.
>
> Drei Wege, keiner davon jetzt zu entscheiden:
>
> 1. **Belegte Anker wiederverwenden.** Die Formel erlaubt es ausdrücklich —
>    §1: „Ein bewährter Anker ist wiederverwendbar; die Streuung liegt
>    woanders." B #4 und B #7 tragen denselben Anker, und **#7 war der
>    166K-Durchbruch**. Das ist der einzige der drei Wege mit Beleg.
> 2. **Die 7 ungeprüften aus der Liste unten einsetzen.** Kostet je einen
>    belegten Anker und ist genau der Fall, den Gate 1.3 als SOLL-Abweichung
>    führt.
> 3. **Eigene Anker aus Kanaldaten ableiten**, sobald genug Videos mit CTR
>    laufen. Gate 2 sieht dafür bereits vor, §10 „um eine eigene Spalte zu
>    ergänzen" — braucht aber Fallzahlen, die es vor V09 nicht gibt.
>
> Zu entscheiden vor dem Titelbau für V09, nicht früher.

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
