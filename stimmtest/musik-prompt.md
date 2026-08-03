# Musikbett — Prompt und Spezifikation

Das Bett ist die Konstante des Kanals: Es läuft unter **jedem** Video und trägt die
Wiedererkennung mit, genau wie die Thumbnail-Serie. Einmal festlegen, dann nie wieder ändern.

## Woher die Vorgaben kommen

Gemessen an 6 Konkurrenzvideos (`regeln/daten/stimm_stichprobe.json`):

| Merkmal | Befund | Konsequenz |
|---|---|---|
| Ambient-Synth-Pad | 3/3 Gewinner — aber auch 3/3 Verlierer | Pflicht, aber kein Unterscheider |
| Knisterndes Lagerfeuer | 2/3 Gewinner, 1/3 Verlierer | drin, passt zum Bildmotiv |
| Grillen | 0/3 Gewinner, 2/3 Verlierer | **weglassen** |
| Stimme über dem Bett | 6/6 | einzige harte Abmischregel |
| Klavier | nur bei einem Verlierer | nicht verwenden |

„Delta-Wellen" und „Klavier+Regen" aus dem ursprünglichen Briefing waren in keinem
Gewinner hörbar zu bestätigen.

## Der Prompt

Für Suno, Udio, ElevenLabs Sound Effects oder jeden anderen Generator:

```
Continuous ambient sleep drone for a Christian bedtime Bible reading.
Deep sustained synth pad in a low register, built only on a root note,
its fifth and its octave — no third, so it reads neither major nor minor.
Very slow, barely perceptible swells. Underneath, a soft low-frequency
drone. A faint layer of distant crackling campfire.

Absolutely no melody, no chord progression, no rhythm, no percussion,
no vocals, no bells, no piano, no crickets. Nothing that resolves,
builds, or draws attention. Dark, warm, nocturnal, reverent.

Must sit far behind a spoken voice and stay perfectly even in level
from start to finish. Seamlessly loopable.
```

**Negativer Prompt** (wo unterstützt):
`melody, chords, progression, drums, percussion, beat, vocals, choir, piano, bells, chimes, crickets, birds, rain, swells, crescendo, build-up, fade, key change`

## Technische Vorgaben

| Größe | Zielwert | Grund |
|---|---|---|
| Pegel Bett | **−31 dBFS RMS** | 12 dB unter der Stimme |
| Pegel Stimme | **−19 dBFS RMS**, über Sprachabschnitte gemessen | Pausen würden den Wert verfälschen |
| Abstand Stimme zu Bett | **12 dB** | „Stimme klar obenauf" in 6/6 gemessenen Videos |
| Ducking | **keins** | bei den Gewinnern nicht hörbar; ein atmendes Bett zieht Aufmerksamkeit |
| Vorlauf | 4 s Bett allein, 3 s Einblende | Einstieg ohne harten Sprung |
| Nachlauf | 6 s, 3 s Ausblende | |
| Loop | exakt, mit übergeblendeter Naht | bei 3–4 h Laufzeit sonst hörbare Stöße |
| Peak gesamt | unter −0,3 dBFS | Reserve für die MP3-Kodierung |

## Was hier mitgeliefert wird

`musikbett.py` erzeugt das Bett selbst — Grundton 55 Hz (A1) plus Quinte, Oktave und
Duodezime, zwei leicht verstimmte Schichten je Ton für Breite, sehr langsame und
unregelmäßige Amplitudenbewegung, Höhen ab 1,8 kHz abgesenkt. Dazu optional das
Feuerknistern aus gefilterten Rauschimpulsen.

Zwei Fassungen in `musik/`:
- `bett_pad.wav` — nur Pad
- `bett_pad_feuer.wav` — Pad plus Feuer *(in den Hörproben verwendet)*

Beide 56 s lang und exakt loopbar (gemessener Samplesprung an der Naht: 0,00017 —
unhörbar). Selbst erzeugt, also ohne Lizenzfrage dauerhaft nutzbar — bei einem Kanal,
der dasselbe Bett unter Hunderte Stunden Material legt, ist das kein Nebenaspekt.

Wenn dir der Klang nicht zusagt, nimm den Prompt oben für einen externen Generator.
Die technischen Vorgaben bleiben in beiden Fällen gleich.
