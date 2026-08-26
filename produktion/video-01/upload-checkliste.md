# Upload-Checkliste — Video 01

**Titel:** `I Know You're Tired… Let These Psalms Carry You Through the Night`
**Korpus:** Psalmen 1–89 + 1. Petrus + Jakobus (WEBBE) · **3:34:57**

> Alles hier wird beim Upload **von Hand** eingetragen. Der Upload läuft
> bewusst nicht automatisch — unter anderem wegen der KI-Kennzeichnung.

## Pflichtschritte

- [ ] **KI-Kennzeichnung setzen.** Unter *Altered content* → „Yes" bei
      **Realistic audio** (die Stimme ist synthetisch) und bei
      **Realistic video** (die Bildspur ist KI-generiert).
      Formel §7/§8: Compliance-Entscheidung, kein Datenbeleg in beide
      Richtungen — aber beides trifft hier zu.
- [ ] **Thumbnail wählen und hochladen:** `thumbnail-a.png`
      („SO TIRED TONIGHT", so im Achterplan vorgesehen) **oder**
      `thumbnail-b.png` („LET THESE PSALMS"). Beide bestehen die
      Checkliste; A ist die geplante Variante.
- [ ] **Untertitel hochladen:** `untertitel.srt`, Sprache **Englisch**.
      0 von 19 Gewinner-Videos hat eine — die einzige unbesetzte Lücke
      (Formel §7).
- [ ] **Beschreibung** aus `beschreibung.txt` übernehmen — enthält die
      100 Kapitelmarken bereits. `[Spendenlink]` durch die echte URL
      ersetzen.
- [ ] **Tags** aus `tags.txt`. Formel §7: A hat auf allen 8 Videos
      **0 Tags**, B's drei gemessene Treffer ebenfalls 0. Kosten nichts,
      erwarte nichts.
- [ ] **Sichtbarkeit/Zeitplan** nach `produktion/videos-01-08.md`
      (5 Tage Abstand zum nächsten Upload).
- [ ] Sprache des Videos: Englisch. Kategorie: *People & Blogs* oder
      *Education* — nicht belegt, freie Wahl.
- [ ] Nicht für Kinder gemacht.

## Dateien im Paket

| Datei | Inhalt |
|---|---|
| `video-01.mp4` | 3:34:57 · 2,52 GB · 1920×1080 @ 24 fps |
| `thumbnail-a.png` / `thumbnail-b.png` | zwei Varianten, je + `_160x90.png` und `_messung.json` |
| `untertitel.srt` | 3.300 Kacheln |
| `titel.txt`, `beschreibung.txt`, `tags.txt` | Metadaten zum Kopieren |

## Messwerte dieses Renderlaufs

> **Diese Tabelle ist nicht belegbar (Vermerk 2026-08-26).** Die Werte stammen
> aus den QA-Dateien des Renderlaufs in `produktion/arbeit/` — und das
> Verzeichnis steht in `.gitignore`. Die Quelle existiert nicht mehr. Nach der
> Regel in `produktion/workflow-gates.md` („Prozessbefund — was als gemessen
> gilt") gelten diese Zahlen damit **nicht als gemessen**: sie sind maschinell
> erzeugt, aber im Repository nicht nachprüfbar.
>
> Ab Video 05 schreibt `schritt7_paket.py` die Messwerte als `qa.json` neben
> `upload.md`, mit Commit und Config-Prüfsumme. **Nicht rückwirkend** — für
> V01–V04 ist die Lücke nicht mehr zu schließen.


| Größe | Wert | Vorgabe | |
|---|---|---|---|
| Laufzeit | 3:34:57 (3,58 h) | ≥ 3,0 h, Ziel 3,4–3,8 h (§2) | ✓ |
| Sprechbeginn | 1,5 s | Sekunde 0–3 (§3, n=24) | ✓ |
| Ton-Versatz | 0,0 s (kreuzkorreliert bei t = 1:47:36) | 0 | ✓ |
| Streamlängen | Video 12.896,79 s / Audio 12.896,70 s | Differenz < 1 Frame | ✓ |
| Abstand Stimme zu Bett | 12,0 dB (Stimme −19,0 / Bett −31,0 dBFS) | 12 dB (§5b) | ✓ |
| Peak | −1,61 dBFS | < −0,3 dBFS | ✓ |
| Tempo | 140,4 WPM über 30.155 Wörter | 120–160 WPM (§5b) | ✓ |
| längste Pause | 1,42 s | < 20 s (§3) | ✓ |
| CTA | 2, beide bis Sekunde 38,5 | höchstens 2, erste 60 s (§3) | ✓ |
| Sprachanteil | 95,6 % (Lücken < 1 s zugerechnet) | ≥ 97 % (§3) | **knapp darunter** |
| Thumbnail A/B Versalhöhe | 125 px = 11,57 % | ≥ 11,5 % / ≥ 125 px | ✓ |
| Thumbnail A/B Kontrast p95 | 14,0 : 1 / 14,1 : 1 | ≥ 10 : 1 | ✓ |

**Zum Sprachanteil:** Der Benchmark 97–100 % stammt aus Untertitel-Zeitstempeln
der Konkurrenz, die kurze Atempausen mitüberdecken. Mit derselben Konvention
(Lücken unter 1 s als Sprache) kommt dieses Video auf 95,6 % — 1,4 Punkte
darunter. Die Originalmethode ist nicht exakt rekonstruierbar; die längste
Pause liegt mit 1,42 s weit unter der 20-s-Grenze, es gibt also keine
hörbare Lücke. Kein Blocker, aber der einzige Wert, der die Vorgabe nicht
klar erreicht.

## Was am Paket bewusst fehlt

- **Eingebrannte Untertitel** (6 von 11 Stichproben) und **Kanal-Wasserzeichen**
  (6 von 11): in Formel §5 als belegtes Muster geführt, nicht als PFLICHT.
  Ein Burn-in vervielfacht die Bildbitrate und muss je Video neu gerendert
  werden — bewusste Entscheidung, nachrüstbar.
- **Motiv-Detailvariation.** Der Achterplan sieht für Video 01
  „Sternenhimmel besonders weit, Mond hoch links, Feuer klein" vor. Gerendert
  ist das Serienmotiv V3 (großes Feuer, Baum) — es existieren nur für V3
  KI-Clips. Die Variation je Video braucht je eigene Clips (~72 Credits).
