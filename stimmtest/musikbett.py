#!/usr/bin/env python3
"""
musikbett.py - erzeugt das Kanal-Musikbett.

Gebaut nach dem, was in den Konkurrenzkanaelen gemessen wurde
(regeln/daten/stimm_stichprobe.json):
  - Ambient-Synth-Pad bei 3/3 Gewinnern  -> Grundlage
  - knisterndes Lagerfeuer bei 2/3       -> als zuschaltbare Schicht
  - Grillen bei 0/3 Gewinnern            -> bewusst NICHT enthalten
  - Stimme in 6/6 Faellen klar obenauf   -> Bett wird leise gemischt

Bewusst ohne Melodie, ohne Rhythmus, ohne Akkordwechsel: nichts darf
Aufmerksamkeit ziehen. Nur Grundton, Quinte und Oktave (kein Terzton),
damit das Bett weder nach Dur noch nach Moll klingt und unter jedem Text
funktioniert.

Das Ergebnis ist exakt loopbar (gleitender Uebergang am Nahtpunkt) und
selbst erzeugt - also ohne Lizenzfragen dauerhaft nutzbar.
"""
import numpy as np
import soundfile as sf

SR = 44100
LOOP_S = 60.0          # Loop-Laenge; ganze Vielfache ergeben beliebige Dauer
ROOT = 55.0            # A1


def leiser_rausch(n, lowcut_rel):
    """Tiefpassgefiltertes Rauschen ueber FFT-Maske."""
    x = np.random.randn(n)
    X = np.fft.rfft(x)
    f = np.fft.rfftfreq(n, 1 / SR)
    X *= 1.0 / (1.0 + (f / lowcut_rel) ** 2)
    return np.fft.irfft(X, n)


def pad(dauer_s):
    n = int(dauer_s * SR)
    t = np.arange(n) / SR
    out = np.zeros(n)
    # Grundton, Quinte, Oktave, Duodezime - kein Terzton
    for f, amp in [(ROOT, 0.55), (ROOT * 1.5, 0.30), (ROOT * 2, 0.30),
                   (ROOT * 3, 0.14), (ROOT * 4, 0.08)]:
        # zwei leicht verstimmte Schichten pro Ton geben Breite ohne Schwebung im Takt
        for det in (-0.12, 0.12):
            # sehr langsame, unregelmaessige Amplitudenbewegung
            lfo = (0.72
                   + 0.16 * np.sin(2 * np.pi * t / 23.0 + f)
                   + 0.12 * np.sin(2 * np.pi * t / 37.0 + det))
            out += amp * lfo * np.sin(2 * np.pi * (f + det) * t)
    # Luftschicht: sehr leises, tief gefiltertes Rauschen
    out += 0.05 * leiser_rausch(n, 400)
    # weiche Hoehenabsenkung: nichts soll spitz werden
    X = np.fft.rfft(out)
    fr = np.fft.rfftfreq(n, 1 / SR)
    X *= 1.0 / (1.0 + (fr / 1800.0) ** 2)
    out = np.fft.irfft(X, n)
    return out


def feuer(dauer_s, dichte=9.0):
    """Knisterndes Lagerfeuer: kurze gefilterte Rauschimpulse, zufaellig verteilt."""
    n = int(dauer_s * SR)
    out = 0.06 * leiser_rausch(n, 900)          # Grundbrodeln
    rng = np.random.default_rng(7)
    for _ in range(int(dauer_s * dichte)):
        i = rng.integers(0, n - 2000)
        L = int(rng.integers(120, 900))
        huelle = np.exp(-np.linspace(0, 9, L))
        out[i:i + L] += rng.normal(0, 1, L) * huelle * rng.uniform(0.05, 0.22)
    X = np.fft.rfft(out)
    fr = np.fft.rfftfreq(n, 1 / SR)
    X *= 1.0 / (1.0 + (fr / 2600.0) ** 2)
    return np.fft.irfft(X, n)


def loopbar(x, fade_s=4.0):
    """Blendet das Ende ueber den Anfang, damit die Naht beim Loopen unhoerbar ist."""
    f = int(fade_s * SR)
    y = x.copy()
    rampe = np.linspace(0, 1, f)
    y[:f] = x[:f] * rampe + x[-f:] * (1 - rampe)
    return y[:-f]


def rms_db(x):
    return 20 * np.log10(np.sqrt((x ** 2).mean()) + 1e-12)


def normiere(x, ziel_db):
    return x * (10 ** (ziel_db / 20) / (10 ** (rms_db(x) / 20)))


def main():
    p = pad(LOOP_S)
    fu = feuer(LOOP_S)
    p = normiere(p, -26.0)
    fu = normiere(fu, -34.0)          # Feuer deutlich unter dem Pad

    nur_pad = loopbar(p)
    mit_feuer = loopbar(p + fu)

    for name, sig in [("bett_pad", nur_pad), ("bett_pad_feuer", mit_feuer)]:
        sig = normiere(sig, -26.0)
        sig = np.clip(sig, -0.98, 0.98)
        st = np.stack([sig, np.roll(sig, 240)], axis=1)   # leichte Stereobreite
        sf.write(f"musik/{name}.wav", st, SR)
        print(f"  {name}.wav  {len(sig)/SR:.1f}s loopbar, RMS {rms_db(sig):.1f} dBFS")


if __name__ == "__main__":
    import os
    os.makedirs("musik", exist_ok=True)
    main()
