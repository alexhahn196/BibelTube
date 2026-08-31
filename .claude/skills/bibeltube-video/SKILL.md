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

Drei der üblich genannten Pfade stimmen nicht. Nachgeprüft am 2026-08-31:

| gemeint | tatsächlich |
|---|---|
| `plan.json` | **`produktion/korpus/plan.json`** |
| `produktion/videos-06.md` | **existiert nicht.** V06 ist der Block `# Video 06` in `produktion/videos-01-08.md`. Die V06-Vorarbeit liegt in `produktion/v06-korpus.md` und `produktion/v06-titel.md` — **auf einem unvereinigten Branch**, siehe unten. |
| `config.md` | **`produktion/config.md`** |

### Der unvereinigte V06-Branch

`origin/claude/bibeltube-v06-korpus-m8-rz2oce` (3 Commits, weder in `main` noch
in einem anderen Branch) trägt Werkzeuge, die dieser Ablauf braucht und die auf
`main`/HEAD **fehlen**:

| Datei | Zweck |
|---|---|
| `produktion/erzaehlanteil.py` | misst den Erzählanteil eines Korpus |
| `produktion/kopisten_titel.json` | **45** Kopisten-Titel (C: 35, F: 10) — die dritte Vergleichsliste |
| `produktion/titel_pruefung.py` (neuere Fassung) | misst gegen **drei** Listen statt einer, Kandidatengrenze 45 % |
| `produktion/v06-korpus.md`, `v06-titel.md` | die ausgeführte V06-Runde als Vorbild |
| `produktion/korpus/wpm_gemessen.json` | gemessenes Tempo je Video |
| `produktion/korpus/eigene_videos_erzaehlanteil.json` | Erzählanteil V01–V05 |
| `produktion/korpus/plan.json` (Fassung mit `_meta`) | Laufzeiten auf gemessenem Tempo |

**Bis der Branch vereinigt ist:** lies daraus mit
`git show origin/claude/bibeltube-v06-korpus-m8-rz2oce:PFAD` und führe Skripte
über eine Kopie im Scratchpad aus. **Vereinige nichts eigenmächtig** — der
Branch überschneidet sich in 9 Dateien mit HEAD, das ist ein eigener Auftrag.
Melde es einmal im Freigabepunkt, dann arbeite weiter.

---

## Schritt 0 — Vorprüfung

**Nichts vorschreiben, was sich ausrechnen lässt.**

1. `git fetch --all`, Arbeitsbaum sauber, Branch geprüft.
2. **Freie Bücher ausrechnen, nicht fortschreiben.** Aus
   `produktion/korpus/plan.json` alle `refs` aller **bereits ausgelieferten**
   Videos einsammeln, gegen `produktion/korpus/kapitel.json` und
   `produktion/korpus/wortzahlen.json` halten, Rest = frei. Der Absatz „Nicht
   verplant und für Video 09+ frei" in `videos-01-08.md` ist eine **Momentaufnahme
   von 2026-08-23** und darf nicht als Bestand gelesen werden.
3. **WPM aus `produktion/config.md` lesen** (`wpm_erwartet`). Nie hart
   eintragen, nie aus einem Bericht übernehmen, nie aus `plan.json` —
   die dortigen `stunden` sind auf HEAD mit einem **älteren** Tempo gerechnet.
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
eine nachgebaute Formel. Gegenprobe, die stimmen muss: V05 mit 29.988
Korpuswörtern und 36 Kapiteln → 3,40 h; gerendert wurden **3,404 h**
(`produktion/video-05/qa.json`).

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
2. **Nebenstoff frei.** Was neben dem dominanten Buch steht, darf
   Spruchsammlung, Brief oder Prophetie sein — Rahmen, nicht Hauptsache.
3. **Kanonische Lesereihenfolge.** Rut → 1 Samuel → Ester, nicht nach Länge
   oder Wirkung sortiert.
4. **Ganze Bücher bevorzugen.** Teilung nur an einer **Erzählnaht**
   (Genesis 1–42 ist eine, Jesaja 1–25 + 40–66 ist keine).
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
Aussage, „81,7 %" allein ist es nicht.

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

`produktion/erzaehlanteil.py` ist dabei **auf V06 zugeschnitten**, nicht
allgemein: es hat die drei V06-Varianten fest im Code und schreibt
`v06_varianten.json`. Als fertiges Werkzeug für ein anderes Video taugt es
nicht — als Vorlage für Zählmethode und Config-Anbindung schon (es liest
`wpm_erwartet` aus `config.md`, genau richtig).

**Liegt ein Buch in keiner der beiden Dateien, ist sein feiner Erzählanteil nicht
gemessen.** Markus, Römer und Offenbarung — der ganze V07-Plan — fehlen in
beiden. Dann nur den groben Wert melden und ihn so nennen.

### Ausgabe je Variante

Bücher · Kapitelzahl · Wörter · Laufzeit bei aktuellem WPM · dominantes Buch mit
Prozentanteil · Erzählanteil · Nachttauglichkeit (Einschätzung) · was die Variante
kostet (welche Bücher sie für spätere Videos verbraucht).

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
| `titel_pruefung.py` | Rückgabewert **0** | — |

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

> **Zwei Mängel im Prüfer auf HEAD — vor dem Lauf nachbessern oder von Hand
> gegenprüfen:**
>
> 1. `titel_kandidaten.py` hat die Kopisten-Liste **fest im Code: zwei Titel**
>    (`produktion/titel_kandidaten.py:74`). Die eingecheckte Liste hat **45**.
>    Sie steht nur auf dem V06-Branch — bis der vereinigt ist, gegen
>    `git show …:produktion/kopisten_titel.json` von Hand gegenprüfen.
> 2. Als „eigene veröffentlichte" Titel sind **`("V1","V2","V3","V4")` fest
>    verdrahtet** (Zeile 82). **V05 ist ausgeliefert und fehlt.** Ein Kandidat
>    könnte direkt neben V05 liegen, ohne dass der Prüfer etwas meldet — prüf
>    ihn zusätzlich von Hand gegen den V05-Titel.

> **45 % gilt für Kandidaten, 50 % für den Bestand.** `titel_pruefung.py` auf HEAD
> misst gegen **eine** Liste mit Grenze 50 %; die Fassung auf dem V06-Branch misst
> gegen **drei** mit 45 % für Neues. Nimm die strengere. Am Bestand gemessen liegen
> **V01, V07 und V08 bei exakt 50,0 %** und würden die 45 reißen — sie hielten die
> 50, unter der sie freigegeben wurden. Nicht nachträglich anfassen.
>
> *Nachgemessen am 2026-08-31, weil ein Bericht etwas anderes sagte:*
> `produktion/v06-titel.md` (V06-Branch) führt an dieser Stelle **„V01, V05, V07
> und V08"**. Der Prüflauf gibt für **V05 27,3 %** aus — der niedrigste Wert des
> ganzen Bestands. V05 gehört dort nicht hin. Belege im Repo sind selbst prüfbar;
> lauf den Prüfer, statt die Tabelle abzuschreiben.

### VERBOTEN als Bauform

> **Anker + reiner Buchname als zweite Hälfte.**
> `If You're Anxious, Rest to the Gospel of John` — Kanal F ist mit dieser
> Bauform auf **18 Aufrufe** gestorben, die **einzige belegte Todesursache im
> ganzen Datensatz** (§1: „Titel von Konkurrenten wörtlich übernehmen").
>
> Die zweite Hälfte muss eine **eigene Zusage** sein, in der der Eigenname
> vorkommt: `…First Samuel Runs All the Way to Morning`, `…Let Saul and David
> Take the Night Shift`. Ebenfalls ausgeschlossen: `the Book of X`, `the Story of
> X` — dieselbe Bauform.

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
Vorbild für Ton und Tiefe: `produktion/v06-titel.md` (V06-Branch) — Kandidatentabelle,
je Kandidat „was ihn trägt / woran er scheitert", dann eine Empfehlung mit dem
Satz *„Das ist eine Empfehlung, keine Entscheidung. Du entscheidest."*

### Eigennamen-Deckung prüfen, bevor du einen Namen setzt

Rechne aus, wieviel Prozent des Korpus der Name wirklich abdeckt. Vorbild V06:
`David` deckt 39,6 %, `First Samuel` deckt 75,1 %, `David and Goliath` deckt
**5,2 %** — grober Etikettenschwindel, ausgeschlossen. Ein Name, der unter der
Hälfte deckt, überverkauft; sag das dazu.

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

Alles wird in den Block `# Video 0N` in **`produktion/videos-01-08.md`**
geschrieben — das ist die Vorlagendatei, die `produktion/pipeline/vorlage.py`
parst. `vorlage.pruefe()` verlangt **alle** diese Felder, sonst bricht Schritt 1
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

> **Zwei Prüfungen brechen NICHT ab, obwohl das Dokument es behauptet.**
> `workflow-gates.md` schreibt zu 1.1 und 1.11: *„beide brechen die Pipeline
> hart ab, wenn sie reißen."* Im Code tun sie das nicht.
> `schritt1_text.py` druckt nur `„UNTER der harten Untergrenze 3,0 h"` und gibt
> **0** zurück; `schritt3_bett.py` druckt nur `„REISST"` und gibt **0** zurück.
> Der Lauf geht danach durch TTS und Montage weiter.
>
> **Folge für diesen Ablauf:** Nach Schritt 1 und nach Schritt 3 **selbst
> hinsehen** — Zielband-Zeile und die beiden `abstand_eingehalten_*`-Zeilen —
> und von Hand anhalten. Verlass dich nicht darauf, dass die Pipeline es tut.

> **Grenzen nie aufweichen, um durchzukommen.** Wenn eine Grenze wiederholt
> gegen gemessene Werte verliert, gehört **die Grenze überprüft, nicht das
> Ergebnis** — und das ist eine Entscheidung des Kanalinhabers, kein Schritt in
> diesem Ablauf. Vorbild: der bewusst stehen gelassene 1.15-Verstoß bei V05
> (73 statt 70 Zeichen), dokumentiert samt Folgeregel.

---

## Wo Dokument und Praxis auseinandergehen

Acht Stellen. Im Ablauf oben steht jeweils die **Praxis**.

| # | Dokument sagt | Praxis zeigt | im Skill festgeschrieben |
|---|---|---|---|
| 1 | Gate 1.13: **Erzählanteil ≥ 80 %** | **zwei eingecheckte Messungen widersprechen sich** — V05 grob 81,7 % (besteht), fein 47,6 % (fällt durch). Der einzige Erfolg V03 fällt in beiden (62,3 / 38,2 %). | Erzählanteil **messen und ausweisen, mit dem Namen der Messung**, nicht darüber abbrechen. Das belegte Kriterium ist die Struktur (M8), nicht die Zahl. |
| 2 | §3: Eingangsgebet **~400 Wörter** | acht Gebete, **153–195 Wörter** | **150–200 W** |
| 3 | Gate 1.2: Ähnlichkeit **< 50 %** gegen die Gewinner | V06-Runde misst gegen **drei** Listen mit **45 %** für Kandidaten | **45 % gegen alle drei Listen** für Neues; 50 % bleibt für den Bestand |
| 4 | Gate 1.14: Eigenname (Buch- oder Evangelienname) in **jedem** Titel | V02 („God's Wisdom") und V04 („Words of Jesus") tragen keinen | Gate 1.14 gilt laut `workflow-gates.md` **ab V05**. Für neue Videos: Pflicht. |
| 5 | `plan.json` führt `stunden` je Video | auf HEAD mit **älterem WPM** gerechnet (V05: 3,56 h dort, 3,404 h gerendert) | **Laufzeit immer neu rechnen** mit `wpm_erwartet` aus `config.md` |
| 6 | `korpus_pruefung.py`: `RAHMEN_W = 232` | an **einem** Video gemessen (V05); V01–V04 wiesen 354–561 aus (inkl. Kapitelansagen) | 232 als Planwert, tatsächliche Rahmenwortzahl nach Schritt 3 melden |
| 7 | Gate 1.1 und 1.11 „brechen die Pipeline hart ab" | beide geben **0** zurück und drucken nur eine Warnung | nach Schritt 1 und 3 **von Hand** prüfen und anhalten |
| 8 | `v06-titel.md`: „V01, **V05**, V07 und V08 bei exakt 50,0 %" | Prüflauf gibt für V05 **27,3 %** aus | V01, V07, V08 — V05 gehört nicht dazu |

Dazu zwei Altlasten, die **kein** Vorbild sind:
`produktion/video-03/beschreibung.txt` trägt eine deutsche Überschrift `Kapitel:`
statt `Chapters:` und einen liegengebliebenen Formel-§7-Kommentar mitten im
Auslieferungstext. Beides nicht nachbauen.

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
   Zum Vergleich: V08 Genesis 1–42 ist 100 % dominant und landet bei
   **3,400 h** — genau auf der Kante des Bands.
3. **V06 auf HEAD ist noch Jesaja** (89,8 % dominant, aber prophetische Rede —
   nach M8 als Hauptkorpus ausgeschlossen; grober Erzählanteil 10,2 %). Der
   Ersatz steht nur auf dem unvereinigten Branch.
4. **Die drei Erklärungen für V03's Impressionen** (Titel-CTR / kontextliche
   Zuordnung / Retention) sind nicht getrennt. Getrennt würden sie erst durch ein
   Erzählvideo **ohne** Eigennamen im Titel — eine Variable pro Runde, das steht
   hinter dem Korpuswechsel an.
5. **Ob die Gebete überhaupt etwas bewirken** — weder für Reichweite noch für
   YPP gibt es einen Beleg.
