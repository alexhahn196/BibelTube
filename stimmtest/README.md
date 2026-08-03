# Stimmtest Fish Audio S2.1 Pro

Blindtest dreier männlicher Stimmen an 30 Minuten Bibellesung, um vor
Produktionsbeginn zu entscheiden, ob Fish Audio als TTS trägt.

## Hörtest

Die drei Dateien liegen in `hoertest/` als `01.mp3`, `02.mp3`, `03.mp3` —
Reihenfolge zufällig, keine Stimmnamen in Dateinamen oder Metadaten.
**`aufloesung.txt` erst nach dem Hören öffnen.**

## Text

World English Bible **British Edition** (WEBBE), Johannes 1–5.
Quelle: `bible-api.com?translation=webbe`, gemeinfrei.

WEBBE statt WEB, weil die reguläre WEB den Gottesnamen als „Yahweh"
überträgt — empirisch geprüft an Psalm 23,1:

| Fassung | Wortlaut |
|---|---|
| WEB | „**Yahweh** is my shepherd" |
| WEBBE | „**The LORD** is my shepherd" |

Johannes 1–4 ergab nur 3.257 Wörter; Kapitel 5 wurde ergänzt, um die
Zielmenge von 4.000–4.500 Wörtern zu erreichen (jetzt 4.237).

## Pipeline

```
gen_par.py        Text -> 13 Chunks an Satzenden -> Fish Audio -> WAV je Chunk
assemble_qa.py    WAV sample-exakt fügen -> einmal MP3 kodieren -> Prüfung
namen_vergleich.py Aussprache der Eigennamen über alle drei Stimmen kreuzprüfen
verblinden.py     zufällige Reihenfolge, Metadaten entfernen, aufloesung.txt
```

Chunks werden als **WAV** geholt und erst nach dem Zusammenfügen **einmal**
nach MP3 kodiert. Würde man MP3-Chunks aneinanderhängen, entstünden an jeder
Naht Encoder-Lücken und Knackser.

## Modell und Kosten

`s2.1-pro` verlangt bezahltes API-Guthaben (HTTP 402). Verwendet wurde
**`s2.1-pro-free`**, der kostenlose Entwickler-Tier — funktioniert ohne
Guthaben. Der Antwort-Header meldet
`ratelimit-limit-concurrency: 4294967295`, also praktisch keine
Parallelitätsgrenze; 9 gleichzeitige Anfragen liefen fehlerfrei.

## Grenzen der automatischen Prüfung

Die Aussprachekontrolle läuft über Spracherkennung (faster-whisper `base.en`).
Sie erkennt **grobe** Fehlbetonungen, unterscheidet aber nicht zwischen
Schreibvariante und Fehlaussprache: „Nathanael" wird regelmäßig als
„Nathaniel" verschriftet, obwohl das Lautbild korrekt ist. Deshalb der
Kreuzvergleich in `namen_vergleich.py` — nur wenn **eine** Stimme von den
beiden anderen abweicht, liegt es an der Stimme.

Ein abschließendes Urteil über Klangfarbe und Angenehmheit kann nur der
Hörtest liefern.
