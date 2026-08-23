# Workflow-Gates

Zwei Haltepunkte im Produktionsablauf. Gate 1 vor jedem Rendering, Gate 2
einmalig nach Video 4. Sie fassen zusammen, was ohnehin in
`produktion/pipeline/` geprüft wird — hier steht es an einer Stelle und mit
Begründung, damit kein Lauf startet, dessen Ergebnis danach ohnehin
verworfen werden müsste.

Bindende Quellen: [`formel/video-formel.md`](../formel/video-formel.md) (v2.2) ·
[`regeln/erfolgsregeln.md`](../regeln/erfolgsregeln.md) ·
[`formel/thumbnail-checkliste.md`](../formel/thumbnail-checkliste.md)

> **Stand 2026-08-23: Gate 2 ist gelaufen.** Die Ergebnisse stehen unten und sind in
> die drei bindenden Quellen eingearbeitet. **Gate 1 hat dadurch zwei neue Prüfungen
> bekommen (1.13 Korpusart, 1.14 Eigenname im Titel)** — beide gelten ab V05.

---

## Gate 1 — vor dem Rendern

> **Kernregel: Kein Rendering, bevor Titel und Thumbnail stehen.**
>
> Ein Renderlauf kostet rund 35 Minuten Rechenzeit und ~160.000 TTS-Zeichen.
> Titel und Thumbnail entscheiden, ob das Video überhaupt geklickt wird — sie
> sind der billigste Teil und müssen zuerst fertig sein. Wer erst rendert und
> dann den Titel sucht, hat den Anreiz, einen schlechten Titel zu behalten,
> weil das Video schon da ist.

| # | Prüfung | Grenze | Woher | Womit |
|---|---|---|---|---|
| 1.1 | **Korpuslänge** | ≥ 3,0 h; Ziel 3,4–3,8 h | Formel §2: kein Video unter 3 h je über 2.500 Views (n=6), alle 10 Treffer ≥ 3,2 h | `schritt1_text.py` meldet die erwartete Laufzeit |
| 1.2 | **Titelähnlichkeit** | < 50 % gemeinsame inhaltstragende Wörter mit **jedem** Gewinnertitel — **und nicht näher an einem Kopisten-Titel als am nächsten Gewinner** | Formel §1: Kanal F kopierte wörtlich → 18 Views; Kanal C baute Mashups → 17 Views | `produktion/titel_pruefung.py` (Bestand), `produktion/titel_kandidaten.py` (neue Titel, misst zusätzlich gegen Kopisten und den eigenen Katalog) |
| 1.3 | **Titelanker** | einer der 13 belegten Anker | Formel §10 („diese zuerst verwenden"); die 7 abgeleiteten sind ausdrücklich ungeprüft | von Hand gegen §10 |
| 1.4 | **Thumbnail: Wörter** | höchstens 4 | Checkliste | `thumbnail.py` |
| 1.5 | **Thumbnail: Versalhöhe** | ≥ 11,5 % der Bildhöhe (≥ 125 px bei 1080p) | Checkliste | `thumbnail.py` |
| 1.6 | **Thumbnail: Kontrast** | ≥ 10 : 1 zum direkten Hintergrund | Checkliste | `thumbnail.py` |
| 1.7 | **Thumbnail: Serienmotiv** | gleiches Motiv wie die letzten Uploads | Formel §5 (B: 13/13); trägt die Kanalidentität, nicht den Einzeltreffer | Sichtprüfung |
| 1.8 | **160×90-Kontrolle** | Text in einer Sekunde erfassbar, Lichtquelle erkennbar | Checkliste | Sichtprüfung am Handy |
| 1.9 | **Sprechbeginn** | Sekunde 0–3, kein Musikintro | Formel §3 PFLICHT (n=24; Gewinner 0,1–3,1 s) | `vorlauf_s` in `config.md`, nachgemessen in `schritt6_srt.py` (erste Kachel) |
| 1.10 | **CTA** | höchstens 2, beide in den ersten 60 s | Formel §3 (Gewinner 0–2, tote Kanäle 4–7) | `schritt1_text.py` zählt sie; Zeitpunkt aus der Rahmen-Wortzahl |
| 1.11 | **Pegelabstand** | Stimme 12 dB über dem Bett, über Sprachabschnitte gemessen | Formel §5b: „Stimme in 6/6 Fällen klar über dem Bett" — **qualitativ belegt, die Zahl 12 ist abgeleitet** | `schritt3_bett.py` |
| 1.12 | **Übersetzung** | WEBBE, kein „Yahweh" im Text | Formel §4 | `schritt1_text.py` bricht sonst ab |
| 1.13 | **Korpusart** | Erzählanteil ≥ 80 %, und der größte Block ist selbst Erzählung | **M8** (eigene Kanaldaten Gate 2, 2026-08-23: Endretention V3 14,4 % gegen V2 2,4 %, Faktor 6) | `produktion/korpus_pruefung.py` |
| 1.14 | **Eigenname im Titel** | Pflicht, in **jedem** Video (Buch- oder Evangelienname) | Formel §1. **Konvention, kein belegter Hebel** — der Wirkmechanismus ist ungeklärt, siehe §1 „die sparsamere Erklärung". Die Prüfung steht hier, weil sie nichts kostet und die Serie einheitlich hält. | von Hand gegen §1 |

**1.1 und 1.11 sind Sonderfälle:** Die Korpuslänge lässt sich erst nach dem
Textbau prüfen (Schritt 1), der Pegelabstand erst nach der Mischung
(Schritt 3). Beide liegen aber **vor** dem teuren Teil — TTS und Montage —
und beide brechen die Pipeline hart ab, wenn sie reißen.

**Die zweite Hälfte von 1.2 ist neu (2026-08-23) und stammt aus einem konkreten
Beinahe-Fehler.** Bei der Titelsuche für V05 lag der zunächst empfohlene Kandidat mit
33,3 % gegen den nächsten Gewinnertitel sauber unter der Grenze — aber mit **44,4 %
gegen C's totes Mashup** *„You're tired, I know… Rest to the Gospel of John"* (17 Views).
Er war der Kopie also ähnlicher als dem Original. Das ist genau die Bauform, vor der V3
warnt, und die Prüfung gegen die Gewinner allein sieht sie nicht: *„Zustand, ich weiß…"*
plus *„das Evangelium nach X"* **ist** C's Bauform. Wer nur gegen Gewinner misst,
kann den Kopisten nachbauen, ohne dass eine Zahl anschlägt.

**1.13 und 1.14 kommen vor allem anderen** — sie entscheiden über Korpus und Titel,
also über das, was Schritt 1 überhaupt baut. Sie sind seit 2026-08-23 die einzigen
Gate-1-Prüfungen aus **eigenen** Kanaldaten; alle übrigen stammen aus Fremdkanälen.

**Die 80-%-Schwelle in 1.13 ist gesetzt, nicht gemessen.** M8 trennt Erzählstoff von
Spruchsammlung, sagt aber nichts über die Grenze dazwischen — die eigenen Daten kennen
nur 81,7 % (V05, erfüllt) und 10,2 % (V06 alt, verletzt), dazwischen liegt nichts.
80 % ist die Zahl, die V05 gerade noch durchlässt; sie ist eine Arbeitsgrenze und wird
korrigiert, sobald ein Video dazwischen liegt. `korpus_pruefung.py` meldet immer den
tatsächlichen Prozentsatz mit, damit die Grenze nachvollziehbar bleibt.

**Die Gattungszuordnung steht im Skript, nicht im Kopf.** `korpus_pruefung.py` führt
kapitelweise, welches Material als Erzählung zählt — Jona 2 (Gebet), 2. Samuel 22
(Danklied), Josua 13–21 (Gebietslisten), Exodus 21–23/25–31/35–40 (Recht und
Stiftshütte), Daniel 7–12 (Visionen) zählen ausdrücklich nicht. Wer die Zuordnung für
falsch hält, ändert sie dort und sieht sofort, was das an den Prozentsätzen bewegt.

**Wenn eine Prüfung reißt:** anhalten und entscheiden, nicht umgehen. Die
einzige Prüfung mit Ermessensspielraum ist 1.3 (SOLL, nicht MUSS) — ein
ungeprüfter Anker ist erlaubt, kostet aber bewusst einen belegten.

---

## Gate 2 — Feedback-Schleife nach Video 4

**Auslöser:** Video 4 ist veröffentlicht **und** das älteste Video ist
mindestens **14 Tage** alt. Nicht früher: YouTube braucht Zeit, bis
Impressionen und CTR stabil sind, und die ersten Tage werden von der
Abo-Startverteilung verzerrt.

> **Kernregel: Eigene Daten schlagen Fremddaten.**
>
> Alles in `formel/video-formel.md` stammt aus 10 fremden Kanälen — mit
> allen Verzerrungen, die dabei entstehen: nur Views sichtbar, keine
> Impressionen, keine CTR, keine Retention, und die Treffer stammen aus
> genau 2 Kanälen. Sobald eigene Zahlen vorliegen, ersetzen sie die
> Fremdbefunde an jeder Stelle, wo sie sich widersprechen.

### Was gelesen wird (YouTube Studio, je Video)

| Kennzahl | Wo | Wofür |
|---|---|---|
| **Impressionen und Klickrate (CTR)** | Reichweite | Die Größe, die dem ganzen Fremddatensatz fehlt. Erst hier lässt sich Titel und Thumbnail überhaupt bewerten. |
| **Absprungstelle** (Zuschauerbindung) | Interaktion | Wo die Kurve zuerst kippt: in den ersten 30 s (Hook/Stimme) oder im Verlauf (Länge/Monotonie)? |
| **Durchschnittliche Wiedergabedauer** | Interaktion | Bei 3,5 h Laufzeit ist die absolute Minutenzahl aussagekräftiger als der Prozentwert. |
| **Traffic-Quellen** | Reichweite | Vorgeschlagene Videos vs. Suche vs. Startseite — entscheidet, ob Titel-Keywords oder Thumbnail wichtiger sind. **Vorsicht beim API-Label `SUBSCRIBER`: es bedeutet Startseite und Abo-Feed, NICHT Aufrufe durch Abonnenten.** |
| **Zuschauer nach Uhrzeit** | Publikum | Für den Upload-Zeitpunkt; im Fremddatensatz nicht ermittelbar. |

### Was daraus entschieden wird

1. **CTR-Vergleich der 4 Titel** — welcher Anker trägt bei *diesem* Kanal?
   Fremdbelegte Anker gegen die eigene CTR stellen. Bei klarem Unterschied:
   §10 um eine eigene Spalte ergänzen.
2. **Thumbnail A gegen B** — falls beide Varianten im Einsatz waren.
   Erst hier ist die offene Frage aus `thumbnail-motive.md` beantwortbar,
   ob das Motiv überhaupt CTR bewegt.
3. **Absprungstelle in den ersten 60 s** — testet Hook-Variante (a) gegen (b)
   und die Stimme. Formel §3 hält ausdrücklich fest, dass ein festes Schema
   **nicht** belegt ist; hier entstehen die ersten echten Daten dazu.
4. **Laufzeit** — bricht die Kurve regelmäßig weit vor Ende ab, ist das
   Zielband 3,4–3,8 h für diesen Kanal zu lang, und §2 wird korrigiert.

### Durchgeführt am 2026-08-23 — was herauskam

**Datengrundlage:** *The Nightly Word* (`UCai4rcN45WKqNvPdSJGADPg`), 25.07.–22.08.2026,
4 Videos, 151 Aufrufe, 69,4 Wiedergabestunden, 2 Abonnenten, 5.535 Impressionen,
CTR 2,71 %. Rohwerte: [`regeln/daten/gate2_eigene_kanaldaten.json`](../regeln/daten/gate2_eigene_kanaldaten.json).

Die vier geplanten Entscheidungen, der Reihe nach — und was tatsächlich entschieden
werden konnte:

| # | Geplant | Ergebnis |
|---|---|---|
| 1 | CTR-Vergleich der 4 Titel, ggf. eigene Spalte in §10 | **Keine eigene Spalte.** 5.535 Impressionen tragen keine CTR-Aussage. Der belastbare Teil ist ein Ausschluss: V3 hat den zweitschlechtesten CTR (1,82 %) **und** 3.130 der 5.535 Impressionen — ein Titel, der zieht, müsste sich zuerst im CTR zeigen, also zieht dieser nicht. Suche scheidet ebenfalls aus (0 Suchaufrufe). Der **Eigenname ist trotzdem Pflicht** in jedem Titel (§1), aber als billige Konvention; der Wirkmechanismus bleibt ungeklärt. |
| 2 | Thumbnail A gegen B | **Nicht durchführbar** — im Zeitraum lief je Video genau eine Variante. Bleibt offen. Neu ist die *Engpass*-Antwort: Thumbnails sind bei diesem Kanalstand **nicht** der Engpass (`formel/thumbnail-checkliste.md`, vorläufiges NEIN). |
| 3 | Absprungstelle in den ersten 60 s, Hook (a) gegen (b) | **Nicht auflösbar.** YouTubes Messpunkte sind 2-Minuten-Blöcke; der Abfall (V3 100 %→40 %, V2 100 %→29 % zwischen Minute 2 und 4) trifft Hook und Eingangsgebet gemeinsam. Als **Beobachtung** in Formel §9 aufgenommen, **nicht** als Regel. |
| 4 | Laufzeit — bricht die Kurve früh ab, ist §2 zu lang | **§2 bleibt unverändert.** Die Kurve bricht nicht wegen der Länge ab: V3 hält bei derselben Laufzeit 14,4 % Endretention, V2 nur 2,4 %. Nicht die 3,5 Stunden sind das Problem, sondern **womit sie gefüllt sind.** |

**Der eigentliche Befund stand nicht auf der Liste:** die **Korpusart**. Erzählstoff
schlägt Spruchsammlung um Faktor 6 in der Endretention, und V3 allein trägt 80 % der
Kanal-Wiedergabezeit. Daraus wurde **M8** in `regeln/erfolgsregeln.md` — die erste
Regel des Repos aus eigenen Daten — und Gate-1-Prüfung 1.13.
**M8 ist damit der einzige an eigenen Daten belegte Hebel dieser Auswertung.** Alles
andere, was Gate 2 hergegeben hat, sind Ausschlüsse (nicht die Suche, nicht die
Klickrate, nicht die Laufzeit) oder Konventionen (Eigenname). Wer nach der Auswertung
eine Sache anders macht, macht den Korpus anders.

**Zusätzlich entschieden:** Die **Kadenz bleibt bei 5 Tagen** (M1), obwohl eine
Fremdkohorte für häufigeres Hochladen spricht. Grund: V05–V08 sollen den
Korpuswechsel als einzige geänderte Variable testen.

**Nicht entschieden, obwohl an Gate 2 gebunden:** die Wahl zwischen den beiden
Kanalbannern (`produktion/motive/README.md`). Gate 2 liefert Video-Impressionen,
aber keine Kanalseiten-Conversion — und 2 Abonnenten sind keine Grundlage. Bleibt
offen.

### Was danach passiert

- Jede Korrektur wird **in die Dokumente geschrieben**, mit eigener Fallzahl
  und Datum, und markiert, welcher Fremdbefund sie ersetzt.
- Erst danach werden Videos 5–8 gerendert. Vier Videos sind die kleinste
  Menge, aus der sich überhaupt ein Vergleich ziehen lässt — und n=4 bleibt
  eine schwache Grundlage. Was nicht deutlich ist, bleibt unverändert.

**Nächster Messpunkt (festgelegt 2026-08-23):** nach V08, unter denselben
Auslösebedingungen wie Gate 2 (jüngstes Video veröffentlicht, ältestes ≥ 14 Tage alt).
Gemessen wird dann gegen das **Prüfkriterium von M8** — Endretention der vier
Erzählstoff-Videos gegen die 2,4 % von V02. Liegt sie nicht deutlich darüber, wird M8
gestrichen. Erst danach kommen die drei vertagten Fragen an die Reihe, einzeln und in
dieser Reihenfolge: **Kadenz** (M1) · **gekürzte Rahmung** (Formel §9) · **Hook-Variante
(a) gegen (b)** (`videos-01-08.md`). Eine Variable pro Runde.
