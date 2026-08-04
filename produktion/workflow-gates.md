# Workflow-Gates

Zwei Haltepunkte im Produktionsablauf. Gate 1 vor jedem Rendering, Gate 2
einmalig nach Video 4. Sie fassen zusammen, was ohnehin in
`produktion/pipeline/` geprüft wird — hier steht es an einer Stelle und mit
Begründung, damit kein Lauf startet, dessen Ergebnis danach ohnehin
verworfen werden müsste.

Bindende Quellen: [`formel/video-formel.md`](../formel/video-formel.md) ·
[`regeln/erfolgsregeln.md`](../regeln/erfolgsregeln.md) ·
[`formel/thumbnail-checkliste.md`](../formel/thumbnail-checkliste.md)

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
| 1.2 | **Titelähnlichkeit** | < 50 % gemeinsame inhaltstragende Wörter mit **jedem** Gewinnertitel | Formel §1: Kanal F kopierte wörtlich → 18 Views | `produktion/titel_pruefung.py` |
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

**1.1 und 1.11 sind Sonderfälle:** Die Korpuslänge lässt sich erst nach dem
Textbau prüfen (Schritt 1), der Pegelabstand erst nach der Mischung
(Schritt 3). Beide liegen aber **vor** dem teuren Teil — TTS und Montage —
und beide brechen die Pipeline hart ab, wenn sie reißen.

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
| **Traffic-Quellen** | Reichweite | Vorgeschlagene Videos vs. Suche vs. Startseite — entscheidet, ob Titel-Keywords oder Thumbnail wichtiger sind. |
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

### Was danach passiert

- Jede Korrektur wird **in die Dokumente geschrieben**, mit eigener Fallzahl
  und Datum, und markiert, welcher Fremdbefund sie ersetzt.
- Erst danach werden Videos 5–8 gerendert. Vier Videos sind die kleinste
  Menge, aus der sich überhaupt ein Vergleich ziehen lässt — und n=4 bleibt
  eine schwache Grundlage. Was nicht deutlich ist, bleibt unverändert.
