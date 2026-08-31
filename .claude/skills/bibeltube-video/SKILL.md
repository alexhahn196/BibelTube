---
name: bibeltube-video
description: Produziert ein komplettes BibelTube-Video von der Korpuswahl bis zur Auslieferung. Auslösen, sobald der Kanalinhaber ein Video der Achterserie benennt oder bauen lässt — "Video 07", "V08 bauen", "das nächste Video", "mach Video 6 fertig", "neues Video" —, oder nach Korpus-, Titel- oder Thumbnail-Vorschlägen für ein solches Video fragt. Führt Schritt 0 bis 6 durch, hält genau einmal an (nach dem Titelvorschlag) und läuft danach ohne Rückfrage bis zum GoFile-Link durch.
---

# BibelTube-Video produzieren

Ein Lauf, sechs Schritte, **genau ein Freigabepunkt** — nach Schritt 2. Davor
wird nichts gerendert, danach nichts mehr gefragt.

Alles hier ist aus dem Repo abgeleitet. Wo Dokument und gelebte Praxis
auseinandergehen, steht die Praxis im Ablauf und die Abweichung im Abschnitt
[Wo Dokument und Praxis auseinandergehen](#wo-dokument-und-praxis-auseinandergehen).

## Die Regel über allen Regeln

> **Eine Kennzahl gilt erst als gemessen, wenn sie aus einer eingecheckten
> Messdatei stammt — nicht aus einem Bericht. Wenn ein Wert in einem Bericht
> steht, aber in keiner Messdatei, ist er eine Absicht, kein Ergebnis.**
> (`produktion/workflow-gates.md`, Prozessbefund 2026-08-25)

Praktisch für diesen Skill:

- Jede Zahl, die du meldest, bekommt die Datei dazu, aus der sie stammt.
- **Vor jeder Aussage „X gibt es nicht": `git fetch --all`, dann über *alle*
  Refs suchen** (`git log --all -S`, `git ls-tree -r --name-only <branch>`).
  Das Prüfverfahren gehört **vor** die Meldung, nicht in die Rückfrage.
  Dieser Fehler ist im Repo zweimal dokumentiert (129-px-Fall, 72-gegen-144-Fall).
- Ein Vorabpreis ist eine Absicht, die Abrechnung ist das Ergebnis.

---

## Wo die Quellen wirklich liegen

| gemeint | tatsächlich |
|---|---|
| `plan.json` | **`produktion/korpus/plan.json`** |
| `config.md` | **`produktion/config.md`** |
| `produktion/videos-NN.md` | Auf HEAD stehen **alle** Textebenen in `produktion/videos-01-08.md` als Blöcke `# Video 0N`. Auf dem V06-Branch ist `vorlage.py` so geändert, dass es **Einzeldateien** `produktion/videos-<nn>.md` findet; dort existiert `videos-06.md`, und der V06-Block in `videos-01-08.md` ist entfernt. **Sieh nach, welche der beiden Welten gerade gilt**, bevor du schreibst. |

### Der unvereinigte V06-Branch — größer und gefährlicher, als er aussieht

`origin/claude/bibeltube-v06-korpus-m8-rz2oce` trägt Werkzeuge, die dieser
Ablauf braucht und die auf `main`/HEAD **fehlen**:

| Datei | Zweck |
|---|---|
| `produktion/erzaehlanteil.py` | versgenaue Erzählanteil-Einstufung |
| `produktion/kopisten_titel.json` | **45** Kopisten-Titel (C: 35, F: 10) — die dritte Vergleichsliste |
| `produktion/titel_pruefung.py` (neuere Fassung) | misst gegen **drei** Listen statt einer, Kandidatengrenze 45 % |
| `produktion/korpus/erzaehlanteil.json` | 250 Kapitel einzeln eingestuft, mit Begründung |
| `produktion/korpus/eigene_videos_erzaehlanteil.json` | Erzählanteil V01–V05, versgenau |
| `produktion/korpus/wpm_gemessen.json` | gemessenes Tempo je Video |
| `produktion/wortzahlen.py` (30 Bücher statt 20) | siehe Schritt 0 |

> ### ⚠️ Nicht vereinigen, ohne das hier gelesen zu haben
>
> - **99 Dateien Unterschied**, +11.561 / −20.017 Zeilen — nicht 9.
> - **Der Branch löscht `produktion/video-05/` vollständig**, `qa.json`
>   eingeschlossen. Er ist **vor** der V05-Auslieferung abgezweigt. `qa.json` ist
>   die Quelle von `wpm_erwartet = 148.1`; eine naive Vereinigung setzt das
>   Projekt tempotechnisch auf V01–V04 zurück.
> - Er ändert das **Format** von `korpus/wortzahlen.json` (flach →
>   `{"wpm":…, "buecher":{…}}`). Alles, was die Datei liest, bricht über die
>   Vereinigung hinweg.
> - Er führt `wpm_erwartet = 143.7` statt 148,1 — siehe Schritt 0.
>
> **Vereinige nichts eigenmächtig.** Das ist ein eigener Auftrag mit
> Konfliktauflösung. Melde es einmal im Freigabepunkt, dann arbeite weiter.

**Bis dahin:** lies mit `git show <branch>:PFAD` und führe Skripte über eine
Kopie im Scratchpad aus — **nie über `main()`**, siehe Schritt 1.

> ### Der Branch bewegt sich
>
> Am 2026-08-31 stand er auf `f31ac14` (3 Commits, kein `videos-06.md`).
> Wenige Stunden später auf `9d7eedc` (4 Commits, **mit** `videos-06.md` und
> `produktion/video-06/`). Eine Aussage über seinen Inhalt ist **zum Zeitpunkt
> des Abrufs** wahr und danach nicht mehr.
>
> `git fetch --all` ist deshalb nicht Schritt 0 einer Sitzung, sondern
> **Schritt 0 jeder Aussage über einen Branch**. „Existiert nicht" heißt immer
> nur „existierte in dem Commit, den ich abgerufen hatte, nicht" — und gehört
> mit dem Commit-Hash gemeldet, nie ohne.

---

## Schritt 0 — Vorprüfung

**Nichts vorschreiben, was sich ausrechnen lässt.**

### Zuerst: die zwei Dinge, ohne die alles andere Zeitverschwendung ist

**Vor jeder anderen Prüfung, vor jedem Vorschlag:**

```bash
[ -n "$FISH_KEY" ] || echo "FISH_KEY fehlt"
ls produktion/motive/loops/ki-v<NN>/clip-*.mp4 2>/dev/null | wc -l   # muss 4 sein
grep -n "^ki_clip_ordner_V<N>" produktion/config.md                  # muss existieren
```

- **`FISH_KEY` nicht gesetzt → abbrechen und melden.** Ohne ihn scheitert
  Schritt 2, und zwar erst nach Textbau und Kapitelabruf. Der Schlüssel steht
  ausschließlich in der Umgebungsvariablen und nie im Repo.
- **KI-Clips nicht vorhanden → abbrechen und melden.** Vier `clip-*.mp4` im
  Ordner dieses Videos, plus der Eintrag `ki_clip_ordner_V<n>` in `config.md`.
  Fehlt der Eintrag, bricht Schritt 5 ab; fehlen die Clips, bricht er auch ab —
  aber erst nach TTS und Mischung, also nach dem teuren Teil.

Beides ist billig zu prüfen und teuer zu übersehen. **Melden, nicht selbst
beschaffen** — Clips kosten 72 Credits, und ob sie erzeugt werden, entscheidet
der Kanalinhaber am Freigabepunkt.

### Dann erst

1. `git fetch --all`, Arbeitsbaum sauber, Branch und Commit notiert.
2. **Freie Bücher ausrechnen, nicht fortschreiben.**

   | | was zählt |
   |---|---|
   | **verbraucht** | die `refs` der Videos, für die ein `produktion/video-0N/`-Paket existiert — derzeit **V01–V05** |
   | **reserviert** | die `refs` der geplanten Videos aus `plan.json` — derzeit **V06–V08**. Nicht anfassen. |
   | **frei** | alles Übrige aus `produktion/korpus/kapitel.json` |

   > **Grundgesamtheit ist `kapitel.json` (30 Bücher), nicht
   > `wortzahlen.json`.** Letzteres kennt auf HEAD nur **20** Bücher — und die
   > 10 fehlenden sind ausgerechnet die freien Erzählbücher: Rut, 1/2 Samuel,
   > 1/2 Könige, Josua, Richter, Ester, Exodus, Jona. `wortzahlen.py` auf HEAD
   > hat eine 20-Buch-Liste und kann sie nicht erzeugen; die Branch-Fassung hat
   > 30, aber ein anderes Ausgabeformat. **Wer `wortzahlen.json` als Bestand
   > liest, findet keinen einzigen freien Erzählstoff und meldet fälschlich
   > „es gibt nichts".**
   >
   > Der Absatz „Nicht verplant und für Video 09+ frei" in `videos-01-08.md`
   > nennt 5 Blöcke. Frei sind **13**. Momentaufnahme von 2026-08-23, kein
   > Bestand.

   Jede fertige Variante am Ende mit `--gegen V7 --gegen V8` gegenprüfen.

3. **WPM aus `produktion/config.md` auf HEAD lesen** (`wpm_erwartet`). Nie hart
   eintragen, nie aus einem Bericht, nie aus `plan.json` — die dortigen
   `stunden` sind auf HEAD mit einem älteren Tempo gerechnet.

   > **Es gibt zwei `config.md` mit zwei Tempi.** HEAD: **148,1** (aus
   > `video-05/qa.json`). V06-Branch: **143,7** (wortgewichtet über V01–V04,
   > `wpm_gemessen.json` — der Branch kennt V05 nicht). Der Unterschied
   > verschiebt das Wortband um rund **900 Wörter** und kippt Grenzfälle.
   >
   > **Falle:** Skripte vom Branch lesen `config.md` aus dem *Arbeitsverzeichnis*.
   > Wer sie gegen HEAD laufen lässt, bekommt 148,1 — auch dort, wo ihr eigener
   > Kommentar für 143,7 geschrieben ist. Maßgeblich ist HEAD. Den Konflikt
   > melden, nicht auflösen.

4. Zielband bestätigen aus derselben Datei: `laufzeit_ziel_von_h` /
   `laufzeit_ziel_bis_h` = **3,4–3,8 h**, harte Untergrenze
   `laufzeit_min_h` = 3,0 h.

### Die Laufzeitformel — genau so, nicht anders

`produktion/korpus_pruefung.py` rechnet:

```python
WPM      = float(_CFG["wpm_erwartet"])
RAHMEN_W = 232          # Hook + 2 CTA + Gebet
ANSAGE_W = 3            # "Luke chapter 1"
_RAND_S  = vorlauf_s + nachlauf_s          # 1,5 + 6,0 = 7,5 s

gesamt = korpus_w + ANSAGE_W * kapitel_n + RAHMEN_W
stunden = gesamt / WPM / 60 + _RAND_S / 3600
```

Rückwärts, für das Wortband bei *n* Kapiteln:

```python
w(h) = round((h - _RAND_S/3600) * 60 * WPM) - ANSAGE_W*kapitel_n - RAHMEN_W
```

Nutze **die Funktionen des Skripts** (`band_fuer(n)`, `_video_h(w, n)`), nicht
eine nachgebaute Formel.

**Gegenprobe, die stimmen muss** — sie steht als Kommentar in
`korpus_pruefung.py:49`:

```
V05:  29.880  +  3×36  +  232  =  30.220 Wörter
      ↑ plan.json         ↑ RAHMEN_W
      _video_h(29880, 36) = 3,403 h        gerendert: 3,404 h (video-05/qa.json)
```

> **Der Eingabewert ist `plan.json/woerter`, nicht `qa.json/woerter_korpus`.**
> `qa.json` führt 29.988 — das sind **29.880 + 108 Ansagewörter**, die schon
> drinstecken. Wer den einsetzt, addiert sie ein zweites Mal und landet bei
> 3,415 h. Die Gegenprobe scheitert dann, ohne dass etwas kaputt ist.

> **Zwei Wortbänder, 385 Wörter auseinander.** `korpus_pruefung.band_fuer(45)`
> ergibt **29.827–33.381** (Rahmen und Ansagen abgezogen).
> `erzaehlanteil.BAND` auf dem Branch ergibt **30.212–33.767**
> (`round(3,4 × 60 × WPM)`, ohne Rahmen). Ein Korpus mit 30.000 W besteht beim
> einen und reißt beim anderen.
> **Maßgeblich ist `band_fuer(n)`.** Von `erzaehlanteil.py` nur die
> Erzählanteile verwenden, sein Bandurteil ignorieren.

> **Das Band hängt an der Kapitelzahl, die erst mit dem Korpus feststeht.**
> Über den plausiblen Bereich n = 30…80 liegt es bei **29.722–33.426 W** —
> das ist die Spanne für die Suche. Sobald eine Variante steht, mit
> `band_fuer(n)` für ihr echtes *n* bestätigen.

> **`RAHMEN_W = 232` ist an genau einem Video gemessen** — V05
> (`produktion/arbeit/video-05/skript.json`: Hook 33 + CTA 13 + CTA 7 +
> Gebet 179). Für V01–V04 weist `wpm_gemessen.json` **354–561** Rahmenwörter
> aus, dort allerdings inklusive Kapitelansagen. Nimm 232 als Planwert und
> melde die tatsächliche Rahmenwortzahl nach Schritt 3.

---

## Schritt 1 — Korpus vorschlagen (2–3 Varianten)

### Die Kriterien, in dieser Reihenfolge

1. **Dominantes Buch ≥ 60 % der Wörter** — und dieses Buch ist selbst
   durchlaufendes Erzählwerk, **in voller Länge gelesen**.
   „Selbst Erzählwerk" ist in `korpus_pruefung.py:164` als Zahl hinterlegt:
   **der größte Block muss kapitelweise ≥ 80 % erzählend sein**
   (`groesster_ist_erzaehlung`). Ohne diese Schwelle ist Abbruchbedingung 3
   nicht überprüfbar. Beispiel, an dem sie greift: Exodus allein hält Band
   (30.926 W) und Dominanz (100 %) und fällt genau hier durch.
2. **Nebenstoff frei.** Was neben dem dominanten Buch steht, darf
   Spruchsammlung, Brief oder Prophetie sein — Rahmen, nicht Hauptsache.
3. **Kanonische Lesereihenfolge**, nicht nach Länge oder Wirkung sortiert.
   V05 liest Lukas vor Prediger, V04 Matthäus vor Epheser/Philipper/Daniel.
4. **Ganze Bücher bevorzugen.** Teilung nur an einer **Erzählnaht**.

   > **Es gibt dafür weder Liste noch Werkzeug — das ist Ermessen und gehört
   > begründet.** Der Bestand nutzt Genesis 1–42 / 43–50 als Naht, aber
   > Gen 42/43 liegt mitten in der Hungersnot-Sequenz; sauber ist das nicht.
   > Wenn du teilst: sag, an welchem Erzählschluss, und dass es dein Urteil ist.
5. **Laufzeit im Band 3,4–3,8 h**, gerechnet mit dem WPM aus `config.md`.

### Nachttauglichkeit — als Einschätzung kennzeichnen

Je Variante einen Absatz: Wieviel Gewalt, Verzweiflung, Fluchtext steckt drin?
1 Samuel trägt Schlachten, Ester trägt einen Galgen, Genesis trägt eine Sintflut.
Das arbeitet gegen den Zweck — jemanden beim Einschlafen zu begleiten.

> **Dies ist eine Einschätzung, keine Messung.** Es gibt im Repo keine Messdatei
> zur Nachttauglichkeit und keinen Retentionswert, der sie stützt. Schreib das
> Wort „Einschätzung" dazu, jedes Mal.

### Das Werkzeug für diesen Schritt

`produktion/korpus_pruefung.py` rechnet eine Variante komplett durch — auf HEAD,
ohne Branch:

```bash
python3 produktion/korpus_pruefung.py "Rut" "1 Samuel" "Ester"
python3 produktion/korpus_pruefung.py --plan V7          # den Planstand prüfen
python3 produktion/korpus_pruefung.py --gegen V8 --gegen V6 "Markus" "Exodus 1-20"
```

Es gibt je Baustein Wörter, Erzählanteil und „ganzes Buch ja/nein" aus, dazu
Summe, Laufzeit beim **aktuellen** WPM, Gate 1.1 (Wortfenster), Gate 1.13,
doppelte Kapitel und mit `--gegen` die Überschneidung mit schon verplanten
Videos. **Nutze es für jede Variante** — es ist die einzige Stelle, an der
Wortzahl, Erzählanteil und Laufzeit aus derselben Rechnung kommen.

### Erzählanteil messen und ausweisen — als Zahl, nicht als Gate

> **Es gibt zwei eingecheckte Messungen desselben Werts, und sie widersprechen
> sich.** Beide sind echte Messdateien, keine Berichte. Nachgerechnet 2026-08-31:
>
> | Video | **grob** — `korpus_pruefung.py`, buchweise | **fein** — `eigene_videos_erzaehlanteil.json`, kapitelweise |
> |---|---:|---:|
> | V01 Psalmen 1–89 | 0,0 % | 0,0 % |
> | V02 Psalmen 90–150 + Sprüche | 0,0 % | 0,0 % |
> | V03 Johannes + Hebräer + 1 Joh + Kol | 62,3 % | **38,2 %** |
> | V04 Matthäus + Eph + Phil + Dan 1–3 | **83,0 %** | 45,8 % |
> | V05 Lukas + Prediger | **81,7 %** | 47,6 % |
>
> Der Unterschied ist die Körnung: **grob** stuft ganze Bücher ein (Lukas =
> Erzählung, komplett), **fein** stuft Kapitel einzeln ein und zählt Lehrreden,
> Gleichniszyklen und eingelegte Gebete heraus — mit der ausdrücklichen Regel
> *„Im Zweifel gegen den Erzählanteil."*
>
> **Folge: Gate 1.13 („≥ 80 %") gibt je nach Messung das Gegenteil aus.** V05
> besteht grob mit 81,7 % („BESTANDEN") und fällt fein mit 47,6 %
> (`haelt_gate_m8: false`). Dasselbe Video, dieselbe Woche, zwei eingecheckte
> Dateien.

**Deshalb: messen, ausweisen, nicht darüber abbrechen.** Gib **beide** Werte an,
oder den einen mit dem Namen der Messung dazu — „81,7 % buchweise" ist eine
Aussage, „81,7 %" allein ist es nicht. Der Lauf von `korpus_pruefung.py`, den
Schritt 1 ohnehin verlangt, druckt den groben Wert direkt neben die Laufzeit;
wer daneben den feinen nennt, muss beide beschriften.

> **Die WPM-Regression hängt an der groben Spalte.** `config.md` leitet
> `wpm_erwartet` aus `WPM = 141,15 + 0,0769 × Erzählanteil%` her, gefittet auf
> V01–V05 mit den **buchweisen** Werten (0,0 / 0,0 / 62,3 / 83,0 / 81,7).
> Wer dort die versgenauen Werte einsetzt, bekommt ein anderes vorhergesagtes
> Tempo und damit ein anderes Wortband. **Die Regression nicht mit der feinen
> Messung füttern**, ohne sie neu zu fitten.

Was M8 in `regeln/erfolgsregeln.md` wirklich belegt, ist die **Struktur**:
*„Hauptkorpus ist durchlaufender Erzählstoff … Spruchsammlungen und prophetische
Rede nur als Beigabe."* V03 schlägt V02 in der Endretention um **Faktor 6** —
und V03 hält die 80 % in **keiner** der beiden Messungen (62,3 % / 38,2 %). Die
80 können also nicht die Größe sein, an der V03 gewonnen hat. Der Unterschied
ist Evangelium gegen Spruchsammlung, nicht 80 gegen 79.

**Was abbricht, ist Kriterium 1** — dominantes Buch unter 60 % oder kein
durchlaufendes Erzählwerk. Nicht der Prozentwert.

### Die feineren Quellen, wenn du sie brauchst

| Datei (V06-Branch) | Inhalt |
|---|---|
| `produktion/korpus/erzaehlanteil.json` | **250 Kapitel, 178 erzählend**, mit Begründung je Kapitel: `ruth` 4 · `1 samuel` 31 · `2 samuel` 24 · `1 kings` 22 · `2 kings` 25 · `joshua` 24 · `judges` 21 · `esther` 10 · `exodus` 40 · `genesis` 8 · `daniel` 9 · `jonah` 4 · `acts` 28 |
| `produktion/korpus/eigene_videos_erzaehlanteil.json` | die schon gelesenen Korpora je Video, mit `je_buch`-Aufschlüsselung |

> **`produktion/erzaehlanteil.py` NICHT über `main()` laufen lassen.** Es hat
> die V06-Varianten fest im Code und **schreibt beim Lauf zwei Dateien** —
> `korpus/erzaehlanteil.json` und `korpus/v06_varianten.json`. Eine CLI für
> einen eigenen Korpus hat es nicht. Nutzbar ist nur `einstufung_rechnen()`,
> importiert. Oder — einfacher — die eingecheckte `korpus/erzaehlanteil.json`
> direkt lesen: ein eigener Lauf ist mit ihr deckungsgleich (250 Kapitel,
> 0 Abweichungen).

**Liegt ein Buch in keiner der beiden Dateien, ist sein feiner Erzählanteil nicht
gemessen.** Markus, Römer und Offenbarung — der ganze V07-Plan — fehlen in
beiden. Dann nur den groben Wert melden und ihn so nennen.

### Was die Variante kostet — ausrechnen, nicht beschreiben

Der Restbestand ist groß und trotzdem knapp: **Rut (2.436 W), Ester (5.408 W)
und Jona (1.272 W) sind die einzigen kurzen Füllbücher.** Jedes große Erzählbuch
braucht eines davon, um ins Band zu kommen. Wer alle drei verbraucht, macht
spätere Videos unbaubar.

Je Variante ausrechnen:

- **Wieviele gültige Kombinationen bleiben danach übrig?** (Band + Dominanz
  ≥ 60 % + größter Block ≥ 80 % erzählend.)
- **Verbraucht sie einen Block, den ein späteres Video zur Rettung braucht?**
  Nachgerechnet am 2026-08-31:

  | | Laufzeit | |
  |---|---:|---|
  | V07 wie geplant (29.123 W, 43 Kap) | **3,320 h** | **reißt** |
  | V07 + Jona | 3,465 h | gerettet |
  | V07 + Rut | 3,596 h | gerettet |
  | V07 + Ester | 3,932 h | über dem Band |
  | V08 wie geplant (29.835 W, 42 Kap) | 3,400 h | **reißt 1.1 um genau 1 Wort** |
  | V08 + Jona | 3,544 h | gerettet |

  **Jona kann nur eines von beiden retten.** Eine V06-Variante, die Jona
  verbraucht, entscheidet damit still über V07 oder V08 mit. Das gehört in den
  Freigabepunkt.

### Ausgabe je Variante

Bücher (kanonisch) · Kapitelzahl · Wörter · Wortband bei diesem *n* ·
Laufzeit bei aktuellem WPM · dominantes Buch mit Prozentanteil · dessen eigener
Erzählanteil · Erzählanteil der Variante **mit dem Namen der Messung** ·
ganze Bücher ja/nein · Rückgabewert von `korpus_pruefung.py` ·
Überschneidung mit V07/V08 · Nachttauglichkeit (Einschätzung) ·
was sie kostet (Zahlen von oben).

---

## Schritt 2 — Titel vorschlagen (4–6 Kandidaten)

### Anker

Aus den **13 belegten** (`formel/video-formel.md` §10). Die Liste, mit Belegwert:

`If You're Anxious,` 245K · `I Know You're Tired…` 233K · `You're Tired, I Know…` 201K ·
`Lord, I Feel Tired` 184K · `No More Thinking Tonight…` 166K ·
`Stop Thinking For A Moment,` 96K · `You Need Rest…` 36K ·
`Fall Asleep Without Stress…` 35K · `Don't Go to Sleep Worried…` 32K ·
`If You're Overwhelmed,` 1,3K · `Rest Your Eyes…` 915 ·
`You Deserve Some Rest…` 559 · `God Knows You're Tired…` 140

Die letzten vier stammen aus Flops desselben Kanals — belegt als *verwendet*,
nicht als *wirksam*. Sag das dazu, wenn du einen davon vorschlägst.

**Wiederverwendung ist ausdrücklich erlaubt.** §1 führt das Wiederholungsverbot
als **gestrichen, widerlegt**: B #4 und B #7 tragen denselben Anker, und **#7 war
der 166K-Durchbruch**. Die Abgrenzung läuft über die **zweite Titelhälfte**,
nicht über den Anker.

> **Welche Anker frei sind, rechne selbst aus — die Buchhaltung in §10 stimmt
> nicht.** Dort steht „Acht sind im Achterplan vergeben: 5→V4 · 6→V2 · 8→V7 ·
> 9→V6 · 10→V3 · 11→V5 · 12 und 13 bleiben" — das sind **sechs** Zuordnungen,
> nicht acht, und V01 (#2) sowie V08 (#7) fehlen darin.
>
> Verlässlich ist `produktion/eigene_titel.json`: welcher der 13 Anker steht in
> welchem eigenen Titel. Auf HEAD sind **8** vergeben (#2, #5, #6, #7, #8, #9,
> #10, #11) und **5 frei**: #1 `If You're Anxious,` 245K · #3 `You're Tired,
> I Know…` 201K · #4 `Lord, I Feel Tired` 184K · #12 `You Deserve Some Rest…`
> 559 · #13 `God Knows You're Tired…` 140.
>
> Davon stehen #1, #3 und #4 zugleich in **A-Titeln** — brauchbar, aber näher
> am Feld. Wirklich unbelastet sind nur #12 und #13, und das sind zwei der vier
> Flop-Anker. **Die von §10 für V09 vorhergesagte Ankerknappheit ist schon
> jetzt da.** Bau die Liste bei jedem Lauf neu, statt §10 abzuschreiben.

### Eigenname

Ausgeschrieben und **eindeutig als Bibelbuch lesbar**: `First Samuel`, `the
Gospel of Mark`. Nicht `Samuel` allein (liest sich als Personen- oder Kanalname),
nicht `Mark` allein.

Pflicht in **jedem** Titel (Gate 1.14, §1) — aber als **billige Konvention, kein
belegter Hebel**: V03 trägt den Eigennamen und hat den **zweitschlechtesten CTR**
des Kanals. Ein Titel, der zieht, müsste sich zuerst im CTR zeigen. Tut er nicht.

### Grenzen

| Prüfung | Grenze | Art |
|---|---|---|
| Länge | **unter 70 Zeichen** | gesetzt (1.15, SOLL) |
| Eigenname beginnt | **vor Zeichen 60** | gesetzt (1.15, SOLL) |
| Ähnlichkeit gegen alle drei Listen | **unter 45 %** | gemessen |
| **Abstand zu den Kopisten** | **nicht näher an einem Kopisten-Titel als am nächsten Gewinner** | gemessen — zählt seit 2026-08-31 als Verstoß |
| `titel_kandidaten.py` | Rückgabewert **0** | — |

> **Die zweite Hälfte von Gate 1.2 zählt jetzt.** Wortlaut: *„… **und nicht
> näher an einem Kopisten-Titel als am nächsten Gewinner**."* Sie stammt aus dem
> einzigen dokumentierten Todesfall des Datensatzes (Kanal F, 18 Aufrufe) und
> stand in `titel_kandidaten.py` bis dahin nur als Warnung. Ein Kandidat, der
> beide Werte gleich hat, steht auf Gleichstand — kein Verstoß, aber null
> Reserve. Nenn es trotzdem.

Die drei Listen: `produktion/gewinner_titel.json` (**21**) ·
`produktion/eigene_titel.json` (**8**, V1–V8) ·
`produktion/kopisten_titel.json` (**45**: C 35, F 10 — **nur auf dem V06-Branch**).

Kandidaten prüfst du mit **`titel_kandidaten.py`**, den Bestand mit
`titel_pruefung.py` (der nimmt keine Argumente):

```bash
python3 produktion/titel_kandidaten.py \
  --grenze 0.45 --eigenname "First Samuel" --max-zeichen 70 --name-vor 60 \
  "Kandidat 1" "Kandidat 2" …
```

Es gibt Länge, Position des Eigennamens, den nächsten Treffer je Liste **und die
geteilten Wörter** aus.

> **Am 2026-08-31 bereinigt** — was der Prüfer jetzt tut, und was er vorher tat:
>
> | | vorher | jetzt |
> |---|---|---|
> | Kopisten-Titel | **2**, fest im Code | **45** aus `produktion/kopisten_titel.json` |
> | eigene veröffentlichte | `("V1","V2","V3","V4")` verdrahtet, **V05 fehlte** | abgeleitet aus den vorhandenen `produktion/video-0N/`-Ordnern |
> | geplante eigene Titel | gar nicht verglichen | zusätzlich gemessen und ausgewiesen |
> | Gate 1.2, zweite Hälfte | Warnung | **Verstoß** |
>
> Vergleichsmenge damit **21 + 5 + 45 = 71** Titel, plus die geplanten separat.
> `titel_pruefung.py` prüft weiter den **Bestand** (Grenze 50 %) und nimmt keine
> Argumente.

> **45 % gilt für Kandidaten, 50 % für den Bestand.** `titel_pruefung.py` auf HEAD
> misst gegen **eine** Liste mit Grenze 50 %; die Fassung auf dem V06-Branch misst
> gegen **drei** mit 45 % für Neues. Nimm die strengere. Am Bestand gemessen liegen
> **V01, V07 und V08 bei exakt 50,0 %** und würden die 45 reißen — sie hielten die
> 50, unter der sie freigegeben wurden. Nicht nachträglich anfassen.
>
> *Nachgemessen und berichtigt am 2026-08-31.* Die Tabelle in
> `videos-01-08.md` führte V05 mit 50,0 % — gemessen sind **27,3 %**, der
> niedrigste Wert des Bestands. **Ursache:** die Tabelle wurde gerechnet, als
> V05 noch seinen ersten Titel trug, und nach dem Titelwechsel am 2026-08-26
> nicht neu gefahren. `produktion/v06-titel.md` hat den falschen Wert von dort
> übernommen (die Datei liegt auf dem Branch und wird dort berichtigt).
> **Regel:** eine Tabelle gerechneter Werte gehört nach jeder Titeländerung neu
> gefahren — `titel_pruefung.py` dauert unter einer Sekunde.

### VERBOTEN als Bauform

> **Anker + reiner Buchname als zweite Hälfte.**
> `If You're Anxious, Rest to the Gospel of John` — Kanal F ist mit dieser
> Bauform auf **18 Aufrufe** gestorben, die **einzige belegte Todesursache im
> ganzen Datensatz** (§1: „Titel von Konkurrenten wörtlich übernehmen").
>
> Die zweite Hälfte muss eine **eigene Zusage** sein, in der der Eigenname
> vorkommt. Aus dem eigenen Bestand:
> `…Let the Gospel of John Quiet Your Mind` (V03),
> `…The Whole Gospel of Luke, Read Slowly Until Morning Comes` (V05).
> Ebenfalls ausgeschlossen: `the Book of X`, `the Story of X` — dieselbe
> Bauform, dazu bei zweiteiligen Büchern sachlich falsch.

### Je Kandidat auszuweisen

Anker mit Belegwert · Zeichenzahl · Position des Eigennamens · Ähnlichkeit gegen
**alle drei** Listen · **der schlechteste Einzeltreffer je Liste mit den geteilten
Wörtern** · Thumbnail-Text (≤ 4 Wörter) · Deckung des Eigennamens am Korpus in
Prozent.

> **Ähnlichkeit: die geteilten Wörter zählen, nicht der Prozentwert.**
> §10, Auflösungsgrenze: der Nenner liegt bei 3–11 Wörtern, ein einziges Wort
> wiegt **9,1 bis 33,3 Prozentpunkte, im Median 16,7**. Unterschiede unter etwa
> **10 Prozentpunkten sind kein Signal** — 27 % und 33 % sind gleich, nicht
> „der eine besser". Nachgewiesen am V05-Paar: ein inhaltsleeres Füllwort
> verbessert den Messwert, weil es nur den Nenner verdünnt. Das Maß lässt sich
> in diese Richtung beliebig schönen.

**Eigene Empfehlung mit Begründung, ausdrücklich als Empfehlung markiert.**
Vorbild für Ton und Tiefe ist die zuletzt gelaufene Titelrunde im Repo —
Kandidatentabelle, je Kandidat „was ihn trägt / woran er scheitert", dann eine
Empfehlung mit dem Satz *„Das ist eine Empfehlung, keine Entscheidung. Du
entscheidest."*

> **Nimm als Vorbild ein *abgeschlossenes* Video, nie das, das du gerade baust.**
> Wer die Beispiele aus der laufenden Runde zieht, schreibt die Antwort in die
> Aufgabe. (Genau das ist dieser Datei beim ersten Entwurf passiert: sie trug
> Korpus und Titel des nächsten Videos als Beispiele und machte einen
> unabhängigen Testlauf unmöglich.)

### Eigennamen-Deckung prüfen, bevor du einen Namen setzt

Rechne aus, wieviel Prozent des Korpus der Name wirklich abdeckt — aus
`kapitel.json`, buchweise. Im Bestand:

| | Deckung |
|---|---:|
| V05 `the Gospel of Luke` | **81,7 %** |
| V05 `Ecclesiastes` | 18,3 % |
| V03 `the Gospel of John` | **62,3 %** |
| V03 `Hebrews` | 22,9 % |

**Ein Name, der unter der Hälfte deckt, überverkauft.** Sag es dazu, oder nimm
ihn nicht. Der Sonderfall, vor dem zu warnen ist: der Name mit der größten
Wiedererkennung ist oft der mit der kleinsten Deckung — eine einzelne berühmte
Episode kann 5 % eines Korpus sein und trotzdem der erste Titelvorschlag.

### Zwei Dinge, die erst später wehtun, aber hier entschieden werden

1. **Der Thumbnail-Text hängt am Eigennamen.** `MAX_WOERTER = 4`.
   `THE ACTS OF THE APOSTLES` sind fünf Wörter und reißen — der Name
   entscheidet also über das Thumbnail mit, nicht erst Schritt 4. Führ den
   Thumbnail-Text je Kandidat gleich mit auf.
2. **Bei zwei Namen im Titel zählt für 1.15 der Name des dominanten Buchs.**
   Wenn ein Nebenbuch früher steht, ist die Prüfung trotzdem am dominanten zu
   messen — er trägt die kontextliche Zuordnung, auf der 1.14 beruht.

### Reihenfolge: der Titel braucht einen Korpus, der erst danach entschieden wird

Das ist eine echte Zirkularität dieses Ablaufs, und sie wird so aufgelöst:

- **4–6 Kandidaten für die von dir empfohlene Korpusvariante**, plus
  **je einen Rückfallkandidaten pro Alternative**.
- Wählt der Kanalinhaber eine andere Variante, wird **Schritt 2 für diese
  wiederholt**. Das ist **kein zweiter Freigabepunkt** — es ist derselbe, nur
  noch nicht abgeschlossen.

---

## 🛑 FREIGABEPUNKT — der einzige

**Hier anhalten.** Zeigen:

- die 2–3 Korpusvarianten mit allen Werten aus Schritt 1
- die 4–6 Titelkandidaten mit allen Werten aus Schritt 2
- die eigene Empfehlung für beides, als Empfehlung markiert
- alles, was auf dem Weg schiefstand oder fehlt (unvereinigter Branch,
  veraltete Planwerte, gerissene Grenzen)

**Auf die Entscheidung des Kanalinhabers warten. Danach durchlaufen bis zur
Auslieferung, ohne weitere Rückfrage.**

Grund, warum der Punkt genau hier liegt (`workflow-gates.md`, Gate-1-Kernregel):

> *„Kein Rendering, bevor Titel und Thumbnail stehen. Ein Renderlauf kostet rund
> 35 Minuten Rechenzeit und ~160.000 TTS-Zeichen. Titel und Thumbnail
> entscheiden, ob das Video überhaupt geklickt wird — sie sind der billigste
> Teil und müssen zuerst fertig sein. Wer erst rendert und dann den Titel sucht,
> hat den Anreiz, einen schlechten Titel zu behalten, weil das Video schon da
> ist."*

**Das Thumbnail bleibt trotzdem vor dem Render.** Der Freigabepunkt liegt auf
Korpus und Titel, nicht auf dem Bild — aber Schritt 4 kommt vor Schritt 5, und
die Gate-1-Kernregel ist damit gehalten. Wenn das Thumbnail seine Grenzwerte
nicht erreicht, ist das eine **Abbruchbedingung**, kein zweiter Freigabepunkt:
melden, nicht selbst entscheiden und nicht weiterrendern.

---

## Schritt 3 — Textebene

**Erst nachsehen, wohin `vorlage.py` schaut.** Auf HEAD parst es Blöcke
`# Video 0N` aus **`produktion/videos-01-08.md`**. Auf dem V06-Branch ist es so
geändert, dass es **Einzeldateien** `produktion/videos-<nn>.md` findet, und der
V06-Block in `videos-01-08.md` ist dort entfernt. Schreib in die Datei, die der
Parser im aktuellen Baum tatsächlich liest — nicht in beide, das ist genau der
doppelte Textstand, den `vorlage.py` verhindern soll.

`vorlage.pruefe()` verlangt **alle** diese Felder, sonst bricht Schritt 1
der Pipeline ab:

`titel` · `korpus_text` · `woerter_soll` · `beschreibung` · `thumb_motiv` ·
`thumb_text` · `gebet` · **`hook` a UND b** · genau **2** `cta` · ≥ 5 `tags`

> **Beide Hook-Varianten müssen ausformuliert dastehen**, auch wenn nur (a)
> läuft. Der Hook-Test ist auf V09+ verschoben, nicht gestrichen.

### Gebet — 150–200 Wörter

Gemessen an allen acht Blöcken: **153 / 161 / 166 / 166 / 179 / 182 / 183 / 195**
Wörter (V07 / V04 / V02 / V06 / V05 / V01 / V08 / V03).

Ton und Bauform, abgelesen an den fertigen Gebeten:

- **Anrede** — „Lord, …" oder „Father, …", erste Person Singular.
- **Zustand benennen, konkret und klein.** Nicht „ich bin müde", sondern
  *„Not one bad day — a run of them, close enough together that I've stopped
  counting."*
- **Nichts fordern.** *„I'm not asking you to explain the season I'm in."*
  Keine Dringlichkeit, kein Pathos, kein Ausrufezeichen.
- **Den Text übergeben** — eine Zeile, die den heutigen Korpus als Stimme im
  Raum einsetzt: *„So let Luke's account of your Son go past me slowly."*
- **Körper** — *„Take the ache out of my shoulders."*
- **Über sich hinaus** — ein Satz für die Mithörenden:
  *„And be gentle tonight with everyone else who has run out of ways to fix things."*
- **„Amen."** als eigener Absatz.

**Thematisch am dominanten Buch**, aber **ohne die Bibelstelle zu zitieren** —
das Gebet ist selbst geschriebener Text. Anspielung ja, Zitat nein: V05 sagt
*„Ecclesiastes says there is a time for everything"* und lässt die Stelle offen.

> §3 der Formel führt „~400 Wörter" — das ist **umetikettiert als
> Policy-Absicherung, kein Reichweitenelement**, und die gelebte Praxis liegt bei
> der Hälfte. 150–200 ist die Praxis.

### Hook — Variante (a), unter 110 s, Sprache ab Sekunde 0

Bauform, an V05 abgelesen (`produktion/video-05/video-05.srt`):

| | Sekunde | Text |
|---|---|---|
| Zustand | 1,5 | „You're tired — I know." |
| Erlaubnis | 4,2 | „This isn't something you have to listen to, it's just something to fall asleep in." |
| Ankündigung | 10,2 | „The whole Gospel of Luke, read slowly, and then Ecclesiastes." |
| Körperanweisung | 16,3 | „Close your eyes." |

Vier Sätze, 33 Wörter. Kein Musikintro, kein Logo, kein Vorspann
(Gate 1.9, §3 PFLICHT, n=11: Sprechbeginn 0,0–3,1 s).

**V05–V08 laufen alle mit (a)** — entschieden am 2026-08-23: eine Variable pro
Runde, und V03, das einzige funktionierende Video, lief mit (a).

### 2 CTAs, beide in den ersten 60 s

Gelebte Formulierung (V05, Sekunde 17,8 und 22,6):

1. *„If you'd like something carried in prayer tonight, leave it in the comments."*
2. *„Subscribe if these readings help you sleep."*

Höchstens 2 (Gate 1.10; Gewinner 0–2, tote Kanäle 4–7). Beide **vor** dem Gebet.

### Beschreibung — das Schema, an allen fünf abgelesen

```
<Titel, wörtlich wie titel.txt>

<Zustandssatz>. <Korpus in einem Satz, mit "read slowly" und
"without interruption" / "start to finish">.

<Freigabesatz: "Nothing to follow." o. ä.> Let it play, <Augen schließen>.

Focused on:
• <vier Punkte, immer genau vier>
• …
• …
• …

Read from the World English Bible (British Edition).

<Wunschsatz>. Subscribing helps you find the next reading.

[Chapters:  — nur bei Kapitelmarken-Videos]

#biblesleep #<korpusspezifisch> #christiansleep #bibleversesforsleep #<thema>
```

Konstant über alle fünf, **wörtlich zu übernehmen**:

- `Read from the World English Bible (British Edition).` — 5/5
- `Let it play` im Freigabesatz — 5/5
- `Subscribing helps you find the next reading.` — 3/5
  (2/5: `…find the next one.`)
- **genau vier** Bullets unter `Focused on:` — 5/5
- **genau fünf** Hashtags, darunter immer `#biblesleep`, `#christiansleep`,
  `#bibleversesforsleep` — 5/5

Die vier Bullets folgen der Reihe: *Zustand · was der Text tut · was der Hörer
loslassen darf · Schlaf.*

### Tags — 15, nicht mehr

Alle fünf produzierten Videos haben **exakt 15**. Sieben stehen in allen fünf:

`bible for sleep` · `christian sleep meditation` · `scripture for sleep` ·
`sleep with god's word` · `bible reading for sleep` · `bedtime bible` ·
`world english bible`

Dazu `peaceful bible reading` (4/5). Die restlichen sind korpusspezifisch.

> §7: A hat auf **allen 8** Videos 0 Tags, B's drei gemessene Treffer ebenfalls 0.
> Sie kosten nichts — erwarte aber nichts von ihnen.

### Kapitelmarken

**Ja** bei vielen kurzen, eigenständigen Einheiten, in die Hörer gezielt springen
(89 Psalmen, 52 Jesaja-Kapitel, 42 Genesis-Kapitel).
**Nein** bei durchlaufendem Erzählstrang — dort wären es 20–30 Zeilen ohne
erkennbaren Nutzen.

Eintragen in `kapitelmarken_videos` in `produktion/config.md`. §7: beide Muster
gewinnen, es ist eine **Nutzbarkeits- und keine Reichweitenfrage**.

---

## Schritt 4 — Thumbnail

### Serienmotiv (Pflicht, Gate 1.7 — trägt die Kanalidentität)

> **Erkennbare sitzende Jesus-Figur** (schlichtes Gewand, Bart), allein in weiter
> dunkler Nachtlandschaft, Augen geschlossen oder gesenkt, im Profil oder halb
> abgewandt — **kein Blickkontakt**. Genau **eine** warme Lichtquelle im Bild,
> darüber tiefblauer Sternenhimmel. Gemalter Stil, hoher Kontrast, dunkles
> Gesamtbild. Kein Innenraum, kein Lamm als Pflichtelement.

Beleg: in `GEW` (n=21) und `BEST` (n=39) kommt eine anonyme Figur ohne
erkennbaren Jesus **kein einziges Mal** vor; die einzigen zwei im 90er-Feld
liegen beide in `WORST`.

### Wie die Serie bisher variiert — an den fünf Thumbnails abgelesen

| | Landschaft | warme Lichtquelle | Figur | Besonderheit |
|---|---|---|---|---|
| V01 | Baum, Gras, Hügel | großes Lagerfeuer rechts | links der Mitte, roter Kapuzenmantel | hellstes Bild der Serie |
| V02 | offenes Feld, Hügelkette | kleineres Feuer rechts | Mitte-links | **aufgeschlagenes Buch** am Boden |
| V03 | See mit **Mondspiegelung** | kleines Feuer ganz rechts | rechts der Mitte | einziges Wasserbild |
| V04 | karge Ebene, Mondsichel | **erleuchtetes Hüttenfenster** — kein Feuer im Bild | links der Mitte | Lichtquelle ist kein Feuer |
| V05 | Fels und Geröll, Mondsichel | Feuer unten Mitte-rechts | Mitte, ockerfarbenes Gewand | dunkelstes Bild, kein roter Mantel |

**Konstant in allen fünf:** sitzende bärtige Figur im Profil, Kopf gesenkt, Hände
im Schoß, kein Blickkontakt · genau eine warme Lichtquelle · Nachthimmel, oberes
Drittel frei für den Text · gemalter Stil · **einzeilig, weiß, Versalien,
Serifenschrift, über die volle Breite**.

**Variabel:** Landschaftstyp, Lage und Art der Lichtquelle, Seite der Figur,
Gewandfarbe, Mond ja/nein, Helligkeit.

**Variation je Video selbst entwerfen, im Rahmen der Serie.** Nicht: neue
Bildwelt, zweite Lichtquelle, Blickkontakt, Innenraum.

### Was die Praxis bei den Zahlen zeigt

Alle sechs gemessenen Thumbnails (V01 hat zwei Varianten) tragen **genau 3
Wörter in einer Zeile**, `FreeSerifBold.ttf`, Fontgröße 184 px (V05: 190 px):

| | Text | Wörter | Versalhöhe | Textbreite | Kontrast (direkt p95) |
|---|---|---:|---|---:|---:|
| V01 a | `SO TIRED TONIGHT` | 3 | 125 px / 11,57 % | 1787 px | 14,0 |
| V01 b | `LET THESE PSALMS` | 3 | 125 px / 11,57 % | 1807 px | 14,1 |
| V02 | `QUIET YOUR MIND` | 3 | 125 px / 11,57 % | 1726 px | 18,0 |
| V03 | `GOSPEL OF JOHN` | 3 | 125 px / 11,57 % | 1609 px | 18,9 |
| V04 | `THINK NO MORE` | 3 | 125 px / 11,57 % | 1548 px | 17,7 |
| V05 | `GOSPEL OF LUKE` | 3 | **129 px / 11,94 %** | 1659 px | **12,2** |

> **Die 4-Wort-Grenze ist nie ausgereizt worden.** Sechsmal drei Wörter. Plan
> mit **drei**; vier ist der Spielraum, nicht das Ziel. Die Textbreite läuft bei
> 1548–1807 px gegen die 1840-px-Grenze — ein viertes Wort zwingt zu kleinerer
> Schrift, und genau das ist verboten.
>
> **V05 ist der Grenzfall der Serie:** direkter Kontrast 12,2 (niedrigster
> Wert), roher Kontrast **8,8** — der fällt unter 10. `kontrast_ok` misst den
> direkten Wert und ist deshalb `true`. Wenn dein Motiv unter V05 liegt, ist der
> Himmel hinter dem Text zu hell.

Praktisch heißt das: Text nur über den **dunkelsten** Teil des Himmels legen. Zieht
dort im Motiv eine helle Rauchfahne oder steht der Mond, ändere **das Motiv** —
nicht die Schriftgröße und nicht die Textfarbe.

### Text

**Ausgeschriebener Eigenname in Versalien, höchstens 4 Wörter.**
`GOSPEL OF MARK`, `FIRST SAMUEL`, `ALL OF FIRST SAMUEL`.

### Harte Werte (`produktion/pipeline/thumbnail.py`)

| | Wert | Konstante |
|---|---|---|
| Wörter | ≤ **4** | `MAX_WOERTER = 4` |
| Versalhöhe Prüfgrenze | ≥ **11,5 %** der Bildhöhe (125 px bei 1080p) | `CAP_MIN_PCT = 11.5` |
| Versalhöhe **Setzwert** | **11,9 %** (129 px bei 1080p) — B-Median | `CAP_ZIEL_PCT = 11.9` |
| Kontrast | ≥ **10 : 1** | `KONTRAST_MIN = 10.0` |
| Position | oberes Drittel | — |
| Farbe | weiß **nur über dem dunklen Himmel** — nie über Feuerschein oder Mond | — |

> **Die Wortgrenze 4 ist gesetzt, nicht gemessen.** Keine eingecheckte Messdatei
> enthält eine Wortzahl je Feld-Thumbnail. Beobachtet sind in
> `regeln/daten/thumbnail_forensik.json` nur **2- und 3-Wort-Zeilen**. Eine Zeile
> ist kein Bild: ein zweizeiliges Thumbnail mit 2 + 2 trägt vier Wörter und
> widerspricht der Beobachtung nicht. Aus einer Zeilenmessung eine Bildregel zu
> machen wäre derselbe Fehler in die andere Richtung.

> **Grenze und Zielwert sind nicht dasselbe.** Bis 2026-08-25 setzte
> `thumbnail.py` direkt auf der Grenze (125 px = 11,57 %, **0,8 px** Reserve) —
> eine Prüfung, die ihr eigenes Ergebnis gerade so besteht, prüft nichts. Seit
> V05: 129 px = 11,94 %, **4,8 px** Reserve. **V01–V04 bleiben bei 125 px.**

### Pflichtprüfung 160×90 (Gate 1.8)

Auf 160×90 verkleinern, ansehen. **Text in einer Sekunde lesbar? Lichtquelle
erkennbar?** Wenn nein: **Wörter streichen, nicht die Schrift verkleinern.**

---

## Schritt 5 — Render

### Feste Einstellungen — hier gibt es nichts zu entscheiden

| `produktion/config.md` | Wert | warum |
|---|---|---|
| `videoquelle` | **`ki_clips`** — **NIE `standbild`** | V01–V04 liefen alle mit KI-Clips. Standbild wäre eine zweite geänderte Variable neben dem Korpus, keine Konstante. |
| `ki_clip_ordner_V<n>` | eigener Ordner je Video | Clips gehören zum Standbild ihres Videos. Fehlt der Schlüssel, **bricht Schritt 5 ab** statt mit fremdem Motiv zu rendern. |
| `video_pixelformat` | **`yuv420p`** (8 Bit) — **NIE `yuv420p10le`** | 10 Bit ist H.264 High 10; die Datei spielte lokal nicht ab. Am 2026-08-26 zurückgestellt. |
| `bett_datei` | **`produktion/klang/bett_mono_feuer_leise.flac`**, echt mono | `bett_pad_feuer.flac` trug R = L um 240 Samples versetzt (5,442 ms) und verlor im Mono-Downmix 5,2 dB. Bit-identisch mono heißt: 12,00 dB in **beiden** Wiedergabefällen (V05: `bett_dekorreliert_db 0.0`, beide `abstand_eingehalten_*` true). `bett_datei_alt` ist der Altbestand — nicht zurückstellen. |
| Bild | 1920×1080, 24–30 fps, ein Standmotiv mit sanfter Bewegung, **kein Szenenschnitt** | §5, 11/11 Stichproben |
| Stimme | `MILO SOOTHING VOICE`, Fish Audio, `prosody_speed 0.88` | feste Kanalstimme |

### KI-Clips erzeugen

Vier Clips, Modell `seedance1_5`, **1080p, 12 s, 16:9, `generate_audio: false`**,
`start_image` = `end_image` = das Motiv-PNG (Loop-Trick: jeder Clip endet auf dem
Ausgangsbild, alle sind beliebig aneinanderfügbar). 4 × 12 s = **48-s-Zyklus**.

Gemessen am V05-Lauf (2026-08-26): **72 Credits** (4 × 18), **4 min 30 s**
Wanduhr für alle vier parallel, **5 min 38 s** für die Bildspur.

> Die Vorabpreisauskunft (`get_cost`) meldet **36** je Clip — doppelt so viel wie
> abgerechnet wird. Fünf Clipsätze, fünfmal 72. **Der Vorabpreis ist eine
> Absicht, das Transaktionsprotokoll das Ergebnis.**

Danach `python3 produktion/pipeline/ki_clip_pruefung.py <clips>` — Drift,
Naht-Sprung, Auflösung/fps/Dauer. Und **hinsehen**: Stil erhalten? Figur still?
Keine verformten Objekte? Rauch nicht kräftiger als bestellt?

### Nahtblende — fester Schritt, nicht optional

**Das Modell schließt die Schleife nicht von selbst, trotz
`start_image = end_image`.** Gemessen an allen vier Clipsätzen des Kanals
(`qa-ki-clips.json`):

| Satz | erster vs. letzter Frame | Sprung an der Naht | normaler Frameschritt |
|---|---|---|---|
| ki-v02 | 2,43–2,48 | 2,43–2,69 | 1,42–1,71 |
| ki-v03 | 1,92–2,36 | 1,92–3,12 | 0,78–0,96 |
| ki-v04 | 2,77–2,85 | 2,77–3,08 | 0,37–0,60 |
| ki-v05 | 3,03–3,15 | 3,03–3,22 | 1,15–1,27 |

**In keinem einzigen Clip landet der letzte Frame auf dem ersten.** Der Sprung
ist das 1,7- bis 5,6-fache eines normalen Frameschritts — bei einem Video, das
den 48-s-Zyklus über 3,4 Stunden **256-mal** durchläuft. Der Trick liefert die
*Nähe*, die den Schnitt überhaupt möglich macht; er liefert nicht die Identität.

Deshalb: **an jeder Clipgrenze eine kurze Blende**, bevor der Zyklus gebaut
wird. Eine halbe Sekunde reicht — der Zyklus wird ohnehin einmal neu kodiert
(CRF 28), die Blende kostet also keinen zusätzlichen Durchgang. Danach die
Kette erneut messen: der Nahtwert muss in die Größenordnung des normalen
Frameschritts fallen, sonst hat die Blende nicht gegriffen.

Ohne Blende ist der Schnitt alle 12 Sekunden ein sichtbares Zucken — in einem
Einschlafvideo genau der Blickfang, den das ganze Bildkonzept vermeiden soll.

### 1088 → 1080: bekannter Generatorfall

Seedance liefert die Höhe gelegentlich als **1088 px** statt 1080. Dann
**mittig beschneiden**, nicht skalieren:

```bash
ffmpeg -v error -i clip.mp4 -vf "crop=1920:1080:0:(ih-1080)/2" \
       -c:v libx264 -crf 18 -preset slow -pix_fmt yuv420p -an clip_1080.mp4
```

Mittig, weil oben der Himmel und unten das Feuer liegen — ein einseitiger
Schnitt verschiebt den Bildaufbau gegenüber dem Standbild und gegenüber den
anderen Clips. Skalieren wäre schlechter: es weicht das ganze Bild auf, um
8 Pixel zu retten.

> **Im Repo ist dieser Fall bisher nicht aufgetreten** — alle 20 vorhandenen
> Clips messen 1920×1080. Die Regel steht hier als Vorgabe des Kanalinhabers
> für den Fall, nicht als eigene Messung. `ki_clip_pruefung.py` meldet die
> Auflösung; **hinsehen, bevor der Zyklus gebaut wird**, denn ein 1088er Clip
> im Zyklus zwingt ffmpeg zu einer stillen Anpassung.

### Aussprache-QA **vor** dem Render — von Hand

**Alle Eigennamen des Korpus durchgehen**, bevor die TTS läuft. Zieh die
großgeschriebenen Nicht-Satzanfänge aus dem Korpustext und sieh dir die an, die
in V01–V05 noch nie vorkamen — 1 Samuel bringt Ebenezer, Achish, Jonathan,
Michal mit, Ester bringt Ahasuerus, Mordecai, Haman. Nach dem Render sind sie
160.000 TTS-Zeichen teuer.

Beleg (§5b PFLICHT): der einzige stimmseitige Mangel mit Trennschärfe war
**falsche Betonung** beim Verlierer C („so-LACE", „super-VISE").

> **`produktion/pipeline/qa_namen.py` ist die Gegenprobe *danach*, nicht davor.**
> Es vergleicht die Spracherkennung der fertigen Tonspur gegen das Skript und
> läuft in `render.py` automatisch **nach Schritt 6**. Es kann vor dem Render
> nichts prüfen — es gibt dann noch kein Audio. Und es entscheidet nichts:
> gemeldet wird, *was die Erkennung gehört hat*; ob das ein Fehler ist, klärt
> das Gegenhören („Nathanael" → „Nathaniel" war korrekt gesprochen).

### Lauf

```bash
python3 produktion/pipeline/render.py V7            # alle Schritte
python3 produktion/pipeline/render.py V7 --ab 4     # ab Schritt 4 weiter
python3 produktion/pipeline/schritt5_video.py V7 --neu-zyklus   # Zyklus neu kodieren
```

`--neu-zyklus` ist Pflicht, wenn `zyklus.mp4` aus einem früheren Lauf mit anderer
Quelle oder anderem Pixelformat stammt — sonst wird er stillschweigend
wiederverwendet.

**SRT erzeugen** (Schritt 6) und im Paket behalten.

---

## Schritt 6 — Messdatei und Auslieferung

### `produktion/korpus/v<NN>_render.json` — eingecheckt

```json
{
  "video": "V7",
  "herkunft": "gemessen",
  "dauer_s": 0.0,
  "dauer_quelle": "ffprobe auf produktion/video-07/video-07.mp4",
  "woerter_gesprochen": 0,
  "woerter_quelle": "produktion/arbeit/video-07/skript.json",
  "wpm_gemessen": 0.0,
  "wpm_formel": "woerter_gesprochen / (dauer_s - vorlauf_s) * 60",
  "commit": "",
  "config_sha256": ""
}
```

**`herkunft: "gemessen"` nur eintragen, wenn `dauer_s` wirklich aus `ffprobe`
auf die gerenderte Datei kommt** — nicht aus `qa.json`, nicht aus einem Bericht.
Das ist der ganze Zweck dieser Datei.

Wenn das neue WPM vom Planwert abweicht: melden, nicht stillschweigend
`config.md` ändern. Eine Tempoänderung verschiebt das Wortband aller künftigen
Videos.

### Auslieferung

**Die Tonspur als FLAC sichern — das macht die Pipeline nicht.** Schritt 7 legt
nur MP4, SRT und das Platzhalter-PNG ins Paket; `gofile_hochladen.sh` erwartet
zusätzlich `video-0N.flac` und überspringt die Rolle `ton` stillschweigend, wenn
sie fehlt:

```bash
ffmpeg -v error -i produktion/arbeit/video-07/mix.wav \
       -c:a flac produktion/video-07/video-07.flac
```

Der Sinn: eine spätere Neumontage (anderes Motiv, anderes Pixelformat) läuft
damit **ohne neue TTS-Kosten**. Genau so ist V05 zweimal neu gebaut worden.

```bash
produktion/pipeline/gofile_hochladen.sh V7
produktion/pipeline/gofile_hochladen.sh V7 --nur-pruefen   # nur Prüfsummen
```

Lädt MP4, FLAC und SRT hoch, prüft **byte-genau** die von GoFile gemeldete Größe,
rechnet `sha256` und hängt den Eintrag **append-only** an
`produktion/auslieferung/manifest.json`.

**MP4 und Tonspur gehören NICHT ins Repo** — `.gitignore` führt
`produktion/video-*/*.mp4`, `*.wav` und `*.flac`. Ins Repo kommt die
*Beschreibung* der Auslieferung, nicht die Auslieferung.

> **Token nie ins Repo, nie ins Manifest.** Ohne `GOFILE_TOKEN` legt das Skript
> ein Gastkonto an und gibt dessen Wegwerf-Token am Ende aus — nur damit sind die
> Dateien später zu verwalten. Er wird nirgends gespeichert. Gleiches gilt für
> `FISH_KEY`: ausschließlich Umgebungsvariable.

### Link ausgeben — mit Prüfsumme

Downloadseite je Datei plus `sha256` und Bytezahl. Eine Größe kann zufällig
stimmen, eine Prüfsumme nicht.

### Erinnerung an den Kanalinhaber (steht auch in `upload.md`)

- [ ] **KI-Kennzeichnung setzen** („Altered or synthetic content" / „Realistic
      audio") — die Stimme ist synthetisch.
- [ ] **SRT-Untertitelspur hochladen** (Sprache: Englisch). 0 von 19
      Gewinner-Videos hat eine — echte Lücke.
- [ ] **Thumbnail ersetzen** — im Paket liegt nur `PLATZHALTER_standbild.png`,
      das ist die Videospur, nicht das Thumbnail.
- [ ] Sichtbarkeit nach dem Upload-Plan (5 Tage Abstand, Band 4–7 Tage belegt).

---

## Abbruchbedingungen

**Anhalten und melden. Nicht selbst reparieren, nicht die Grenze aufweichen.**

1. **`titel_pruefung.py` meldet einen Verstoß** (Rückgabewert ≠ 0).
2. **Laufzeit außerhalb 3,4–3,8 h.**
3. **Kein Korpus hält dominantes Buch ≥ 60 % und Zielband gleichzeitig.**
4. **Grenzwerte des Thumbnails nicht erreichbar** — Versalhöhe, Kontrast oder
   160×90-Lesbarkeit lassen sich bei ≤ 4 Wörtern nicht halten.

### Was die Pipeline selbst abbricht — und was nicht

**Hart (`SystemExit`, der Lauf hält an):**

| Schritt | Abbruch bei |
|---|---|
| 1 Text | `Yahweh` im Text (klassische WEB statt WEBBE) · unvollständige Vorlage · Hook-Variante fehlt · Kapitel nicht abrufbar · Normalisierung ändert die Textlänge |
| 2 TTS | `FISH_KEY` nicht gesetzt · Chunk fehlgeschlagen · Satz über dem Chunk-Limit · falsche Samplerate · Anzeige- und TTS-Text unterschiedlich lang |
| 3 Klangbett | Bett hat die falsche Samplerate |
| 5 Video | Standbild fehlt · Mischung fehlt · **`ki_clip_ordner_V<n>` fehlt** · keine `clip-*.mp4` im Ordner |

**Gate-Abbrüche (seit 2026-08-31 — vorher wurden sie nur gedruckt):**

| Schritt | bricht ab bei |
|---|---|
| 1 Text | **1.1** Laufzeit unter `laufzeit_min_h` |
| 2 TTS | Sprachanteil unter `sprachanteil_min_pct` · längste Pause über `laengste_pause_max_s` |
| 3 Bett | **1.11** Pegelabstand Mono **oder** je Kanal · Peak über `peak_max_dbfs` |
| 5 Video | **1.1** Laufzeit der fertigen Datei · Ton-Versatz über 0,5 s |
| 6 SRT | **1.9** Sprechbeginn über `sprachstart_max_s` · überlappende Kacheln |

> **Das Zielband 3,4–3,8 h bricht NICHT ab** — es wird laut gewarnt. Es ist die
> Empfehlung aus dem Treffer-Median, keine Grenze, und V08 liegt mit **einem
> Wort** darunter. **Für diesen Ablauf bleibt es trotzdem Abbruchbedingung 2:**
> die Pipeline läuft weiter, du hältst an und meldest.

> **`--force` übergeht jeden Gate-Abbruch** — ausdrücklich zu setzen, schreibt
> eine Warnung ins Protokoll, und der Verstoß steht so oder so in der Messdatei.
> **Setz ihn nicht von dir aus.** Ein Verstoß, der bewusst in Kauf genommen
> wird, ist eine Entscheidung des Kanalinhabers, kein Schritt in diesem Ablauf.
> `render.py --force` reicht ihn an alle Gate-Schritte durch.

> **Grenzen nie aufweichen, um durchzukommen.** Wenn eine Grenze wiederholt
> gegen gemessene Werte verliert, gehört **die Grenze überprüft, nicht das
> Ergebnis** — und das ist eine Entscheidung des Kanalinhabers, kein Schritt in
> diesem Ablauf. Vorbild: der bewusst stehen gelassene 1.15-Verstoß bei V05
> (73 statt 70 Zeichen), dokumentiert samt Folgeregel.

---

## Wo Dokument und Praxis auseinandergehen

Dreizehn Stellen. Im Ablauf oben steht jeweils die **Praxis**.

| # | Dokument sagt | Praxis zeigt | im Skill festgeschrieben |
|---|---|---|---|
| 1 | ~~Gate 1.13: Erzählanteil ≥ 80 %~~ — **am 2026-08-31 gefallen** | zwei eingecheckte Messungen widersprachen sich: V05 buchweise 81,7 % (bestand), kapitelweise 47,6 % (fiel durch). Der einzige Erfolg V03 fiel in beiden (62,3 / 38,2 %). | **erledigt.** 1.13 prüft jetzt die Struktur: dominantes Buch ≥ 60 % **und** selbst Erzählwerk **und** in voller Länge. Der Erzählanteil wird kapitelweise gemessen und gemeldet, gatet nicht. |
| 2 | §3: Eingangsgebet **~400 Wörter** | acht Gebete, **153–195 Wörter** | **150–200 W** |
| 3 | Gate 1.2: Ähnlichkeit **< 50 %** gegen die Gewinner | V06-Runde misst gegen **drei** Listen mit **45 %** für Kandidaten | **45 % gegen alle drei Listen** für Neues; 50 % bleibt für den Bestand |
| 4 | Gate 1.14: Eigenname (Buch- oder Evangelienname) in **jedem** Titel | V02 („God's Wisdom") und V04 („Words of Jesus") tragen keinen | Gate 1.14 gilt laut `workflow-gates.md` **ab V05**. Für neue Videos: Pflicht. |
| 5 | `plan.json` führt `stunden` je Video | auf HEAD mit **älterem WPM** gerechnet (V05: 3,56 h dort, 3,404 h gerendert) | **Laufzeit immer neu rechnen** mit `wpm_erwartet` aus `config.md` |
| 6 | `korpus_pruefung.py`: `RAHMEN_W = 232` | an **einem** Video gemessen (V05); V01–V04 wiesen 354–561 aus (inkl. Kapitelansagen) | 232 als Planwert, tatsächliche Rahmenwortzahl nach Schritt 3 melden |
| 7 | ~~Gate 1.1 und 1.11 „brechen die Pipeline hart ab"~~ | beide gaben **0** zurück und druckten nur eine Warnung | **erledigt 2026-08-31.** Schritte 1, 2, 3, 5, 6 geben bei Verstoß **1** zurück; `--force` übergeht das ausdrücklich |
| 8 | ~~„V01, **V05**, V07 und V08 bei exakt 50,0 %"~~ | Prüflauf gibt für V05 **27,3 %** aus; die Tabelle stammte von vor dem V05-Titelwechsel | **erledigt 2026-08-31** in `videos-01-08.md` samt Ursache. Auf dem Branch steht der falsche Wert weiter |
| 9 | `videos-01-08.md`: „Nicht verplant und für Video 09+ frei" nennt **5 Blöcke** | frei sind **13** Blöcke; `wortzahlen.json` kennt 10 davon gar nicht | Bestand aus `kapitel.json` ausrechnen, nie aus `wortzahlen.json` oder aus dem Absatz |
| 10 | Gate 1.2 nennt eine zweite Bedingung (Abstand zu Kopisten) | **kein Skript prüft sie** | von Hand lesen und melden |
| 11 | §10 zählt „acht Anker im Achterplan vergeben" | es sind **sechs** genannte Zuordnungen, V01 und V08 fehlen darin | freie Anker aus `eigene_titel.json` neu ausrechnen |
| 12 | `plan.json` führt V08 mit 3,55 h (HEAD) bzw. 3,46 h (Branch) | `korpus_pruefung.py --plan V8` → **DURCHGEFALLEN**, 1.1 reißt um **1 Wort** | V08 gilt als offen, nicht als geplant |
| 13 | Skill-Entwurf: „Branch überschneidet sich in **9 Dateien**" | **99 Dateien**, und er **löscht `produktion/video-05/` samt `qa.json`** | nicht vereinigen ohne Konfliktauflösung |

Dazu zwei Altlasten, die **kein** Vorbild sind:
`produktion/video-03/beschreibung.txt` trägt eine deutsche Überschrift `Kapitel:`
statt `Chapters:` und einen liegengebliebenen Formel-§7-Kommentar mitten im
Auslieferungstext. Beides nicht nachbauen.

---

## Trockenlauf gegen V06 (2026-08-31) — was er ergeben hat

Der Ablauf wurde einmal blind gegen V06 gefahren: Schritt 0–2, ohne Zugriff auf
`v06-korpus.md`, `v06-titel.md` und die dortigen Kandidatendateien.

| | Ziel | Ergebnis |
|---|---|---|
| Korpus | Variante A (Rut + 1 Samuel + Ester) | **getroffen**, als Empfehlung von 26 gültigen Kombinationen |
| Titel | ein Kandidat der Bauform von K3 | **Bauform getroffen** — Anker aus den 13, Eigenname ausgeschrieben, zweite Hälfte als eigene Zusage, < 70 Zeichen, Name vor Zeichen 60. Empfohlen wurde ein anderer der sechs. |

> **Der Trockenlauf war nicht unabhängig, und das ist ein Befund über diese
> Datei.** Der erste Entwurf trug Korpus und Titelfragmente von V06 als
> Beispiele — der Lauf konnte die Lösung lesen, ohne eine gesperrte Datei zu
> öffnen. Zusätzlich druckt `git show <branch> --stat` die Commit-Nachricht mit,
> in der der freigegebene Titel wörtlich steht. Die Beispiele sind seither auf
> abgeschlossene Videos umgestellt; die Regel dazu steht in Schritt 2.

Aus dem Lauf sind **24 Mängel** an dieser Datei zurückgekommen; alle sind
eingearbeitet. Die schwersten waren die falsch gerechnete Gegenprobe in
Schritt 0, `wortzahlen.json` als Bestandsquelle, die zwei Wortbänder, die zwei
Erzählanteil-Messungen, die fehlende zweite Hälfte von Gate 1.2 und die um den
Faktor 11 zu klein angegebene Branch-Differenz.

---

## Offene Fragen — nicht in diesem Ablauf zu entscheiden

1. **Ab V09 ist kein belegter Anker mehr frei** (§10). Fünf stecken in A-Titeln,
   acht sind im Achterplan vergeben. Drei Wege — wiederverwenden (der einzige
   mit Beleg), die 7 ungeprüften einsetzen, eigene aus Kanaldaten ableiten.
   Zu entscheiden **vor** dem Titelbau für V09.
2. **Der V07-Plan reißt zwei Kriterien gleichzeitig** — nachgerechnet am
   2026-08-31 gegen `produktion/korpus/kapitel.json`:

   | | Wert | Kriterium |
   |---|---:|---|
   | Laufzeit bei 148,1 WPM | **3,32 h** | Zielband 3,4–3,8 h → **reißt** |
   | dominantes Buch Markus | **49,0 %** | ≥ 60 % → **reißt** |
   | Römer / Offenbarung | 32,4 % / 18,6 % | Brief + Apokalyptik als halber Korpus |

   Das ist kein Fehler im alten Plan, sondern die Folge des inzwischen
   **gemessenen** Tempos und der M8-Regel. Schritt 1 muss für V07 also
   **wirklich neu rechnen**, nicht fortschreiben.

   **V08 reißt ebenfalls — um genau ein Wort.** Genesis 1–42 ist 100 %
   dominant und 100 % erzählend, hat 29.835 W bei einer Untergrenze von
   **29.836 W**: `korpus_pruefung.py --plan V8` meldet
   `1.1 REISST — zu kurz` / `DURCHGEFALLEN`. Ein Skill, dessen oberste Regel
   die Messdatei über den Bericht stellt, nennt das **durchgefallen**, nicht
   „auf der Kante". Jona (1.272 W) würde es heilen — kann aber nur einmal
   vergeben werden, siehe Schritt 1.
3. **V06 auf HEAD ist noch Jesaja** (89,8 % dominant, aber prophetische Rede —
   nach M8 als Hauptkorpus ausgeschlossen; grober Erzählanteil 10,2 %). Der
   Ersatz steht nur auf dem unvereinigten Branch.
4. **Die drei Erklärungen für V03's Impressionen** (Titel-CTR / kontextliche
   Zuordnung / Retention) sind nicht getrennt. Getrennt würden sie erst durch ein
   Erzählvideo **ohne** Eigennamen im Titel — eine Variable pro Runde, das steht
   hinter dem Korpuswechsel an.
5. **Ob die Gebete überhaupt etwas bewirken** — weder für Reichweite noch für
   YPP gibt es einen Beleg.
