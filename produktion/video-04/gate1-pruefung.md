# Gate 1 — Video 04

**Renderlauf 2026-08-20.** Titel `No More Thinking Tonight… Let Tomorrow Wait
Until Morning`, Korpus Matthäus 1–28 + Epheser 1–6 + Philipper 1–4 +
Daniel 1–3 (41 Kapitel, WEBBE), **3:34:56**.

Gate 1 steht laut `produktion/workflow-gates.md` **vor** dem Rendern. 1.2 bis
1.8 waren vor dem Lauf erfüllt; 1.1, 1.9, 1.10 und 1.11 lassen sich
bauartbedingt erst nach Schritt 1, 3 und 6 messen und stehen deshalb hier mit
den Werten des fertigen Laufs.

| # | Prüfung | Grenze | Ist | |
|---|---|---|---:|---|
| 1.1 | Korpuslänge | ≥ 3,0 h; Ziel 3,4–3,8 | **3,58 h** | ✓ |
| 1.2 | Titelähnlichkeit | < 50 % | **37,5 %** | ✓ |
| 1.3 | Titelanker | einer der 13 belegten | `No More Thinking Tonight…` (166K) | ✓ |
| 1.4 | Thumbnail: Wörter | ≤ 4 | 3 — `THINK NO MORE` | ✓ |
| 1.5 | Thumbnail: Versalhöhe | ≥ 11,5 % | **11,94 %** (129 px) | ✓ |
| 1.6 | Thumbnail: Kontrast | ≥ 10 : 1 | 17,5–18,5 | ✓ |
| 1.7 | Thumbnail: Serienmotiv | gleich wie letzte Uploads | Sichtprüfung offen | **von Hand** |
| 1.8 | 160×90-Kontrolle | in einer Sekunde erfassbar | Sichtprüfung offen | **von Hand** |
| 1.9 | Sprechbeginn | Sekunde 0–3, kein Musikintro | **1,5 s** | ✓ |
| 1.10 | CTA | ≤ 2, beide in den ersten 60 s | 2, bei **19,9 s** und **29,6 s** | ✓ |
| 1.11 | Pegelabstand | 12 dB über dem Bett | **12,0 dB** | ✓ |
| 1.12 | Übersetzung | WEBBE, kein „Yahweh" | Schritt 1 lief durch | ✓ |

**10 von 12 maschinell bestanden, 0 Verstöße.** 1.7 und 1.8 sind
Sichtprüfungen und bleiben offen — sie gehören ans Handy, nicht in ein Skript.

**1.5 nachgebessert (2026-08-20).** Der erste Lauf lag mit 11,57 % gegen
11,50 % nur 0,07 Punkte über der Grenze — knapp 0,8 px, weil `thumbnail.py`
auf `ceil(1080 × 11,5 %)` = 125 px zielte, also exakt auf das Minimum. Das
Skript trennt jetzt Zielgröße und Grenze: `CAP_ZIEL_PCT` = 11,9 % (Median der
B-Serie) ergibt 129 px, `CAP_MIN_PCT` = 11,5 % bleibt die Prüfgrenze.
Neu gemessen: **129 px = 11,94 %**, Breite 1599 px, Rand 160 px je Seite,
Kontrast unverändert. Thumbnail neu gesetzt aus `motiv-video-04.png`.

## Aussprache-QA: zwei Beanstandungen, beide widerlegt

`qa_namen.py` hat `Jacob` und `Judah` als „WEIT ENTFERNT — gegenhören"
gemeldet (302 Namen, 1094 Vorkommen). Beides ist ein **Artefakt der
Spracherkennung, kein Tonfehler**:

- Die gemeldeten Fundstellen (4,7 s und 55,2 s) liegen im Hook und im Gebet.
  Dort kommen die Namen im Skript gar nicht vor — sie stehen im Stammbaum
  ab 2:04.
- `base.en` hat den dichten Stammbaum-Abschnitt übersprungen: die
  ASR-Wortliste springt von „Amen." (121,3 s) direkt auf „Hasran"/Hezron
  (131,7 s). `Jacob` und `Judah` tauchen darin **null mal** auf, worauf
  `qa_namen.py` auf den besten Zufallstreffer im Chunk zurückfällt —
  „be" aus *will be better* und „day" aus *the day its own troubles*.
- Gegengehört mit dem größeren Modell `small.en` über denselben Ausschnitt:
  „Isaac became the father of **Jacob**. **Jacob** became the father of
  **Judah** and his brothers." Beide Namen sitzen.

Die Untertitel sind davon nicht betroffen: `schritt6_srt.py` legt den
**Skripttext** auf die ASR-Zeiten, nicht den ASR-Text. Die Zuordnung meldet
für diesen Chunk 59,6 % — den schlechtesten Wert des Laufs, und genau die
Stelle, an der die ASR ausgelassen hat.

**Empfehlung für die nächsten Videos:** Chunk 0 ist mit 157 s ungewöhnlich
lang, weil Hook, beide CTA, das Gebet und der Textanfang hineinfallen. Je
länger der Chunk, desto eher findet die ungeortete Namenssuche in
`qa_namen.py` einen Zufallstreffer weit entfernt von der echten Stelle. Ein
Positionsfenster um die erwartete Zeit würde diese Fehlalarme abstellen.
