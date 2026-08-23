#!/usr/bin/env python3
"""
klang_proben.py - drei Hoerproben des Klangbetts zur Entscheidung ueber die
Feuerschicht.

WARUM NICHT NEU ERZEUGT: config.md fuehrt produktion/klang/bett_pad_feuer.flac
ausdruecklich als ARTEFAKT - stimmtest/musikbett.py zieht die Luftschicht des
Pads aus einem ungeseedeten np.random.randn, ein zweiter Lauf ergaebe ein
anderes Bett. Die Proben werden deshalb AUS dem vorhandenen Bett gebaut, nicht
neben ihm. Das Pad, das man in allen drei Proben hoert, ist das Pad des Kanals;
nur die Feuerschicht unterscheidet sich.

WIE DIE SCHICHTEN GETRENNT WERDEN: harmonisch/perkussive Trennung nach
Fitzgerald 2010 - im Spektrogramm ueber die Zeit medianfiltern haelt stehende
Toene (Pad), ueber die Frequenz medianfiltern haelt Klick-Transienten (Feuer).
Die Masken addieren sich zu 1, die Rekonstruktion ist verlustfrei.

Das Bett wird dafuer DREIFACH GEKACHELT analysiert und die mittlere Kachel
entnommen. Ohne das erzeugt die Fensterung an Dateianfang und -ende einen
Fehler, der die Loop-Naht der getrennten Spuren um Faktor 10 verschlechtert -
gemessen und der Grund fuer diese Umstaendlichkeit.

Die Proben sind 60 s lang und legen die Loop-Naht bewusst auf Sekunde 30,
damit sie beim Hoeren Kontext auf beiden Seiten hat.

Aufruf: python3 produktion/klang/klang_proben.py
"""
import json
import os

import numpy as np
import soundfile as sf
from scipy.ndimage import median_filter
from scipy.signal import butter, hilbert, istft, sosfiltfilt, stft

SR = 44100
BETT = "produktion/klang/bett_pad_feuer.flac"
ZIEL = "produktion/klang/proben"
PROBE_S = 60.0
NAHT_BEI_S = 30.0
KREUZBLENDE_S = 0.75
STEREO_VERSATZ = 240          # wie in stimmtest/musikbett.py
NPERSEG, NOVERLAP, MEDIAN = 4096, 3072, 31
FEUER_DB = -6.0               # Variante B
FEUER_TIEFPASS_HZ = 1100.0    # Variante B
# aus produktion/config.md, fuer die Hochrechnung auf den fertigen Mix
PEGEL_BETT_DBFS = -31.0
PEGEL_STIMME_DBFS = -19.0
LAUFZEIT_H = 3.5


def rms_db(x):
    x = np.asarray(x, dtype=float)
    return float(20 * np.log10(np.sqrt((x ** 2).mean()) + 1e-12))


def hpss_geloopt(x):
    """Pad und Feuer trennen, ohne die Loop-Eigenschaft zu zerstoeren."""
    n = len(x)
    kachel = np.tile(x, 3)
    _, _, Z = stft(kachel, fs=SR, nperseg=NPERSEG, noverlap=NOVERLAP, window="hann")
    S = np.abs(Z)
    H = median_filter(S, size=(1, MEDIAN), mode="wrap")      # ueber die Zeit
    P = median_filter(S, size=(MEDIAN, 1), mode="nearest")   # ueber die Frequenz
    h2, p2 = H ** 2, P ** 2
    nrm = h2 + p2 + 1e-12
    _, xh = istft(Z * (h2 / nrm), fs=SR, nperseg=NPERSEG, noverlap=NOVERLAP, window="hann")
    _, xp = istft(Z * (p2 / nrm), fs=SR, nperseg=NPERSEG, noverlap=NOVERLAP, window="hann")
    return xh[n:2 * n], xp[n:2 * n]


def tiefpass_geloopt(x, fg_hz, ordnung=4):
    """Tiefpass, der die Loop-Eigenschaft nicht zerstoert.

    sosfiltfilt polstert die Raender kuenstlich auf; auf einem 56-s-Block
    angewandt bricht das die Naht auf. Deshalb dreifach kacheln und die
    mittlere Kachel entnehmen - gemessen: Nahtsprung faellt dadurch von
    0,0024 auf den Wert des unbearbeiteten Signals zurueck.
    """
    n = len(x)
    sos = butter(ordnung, fg_hz / (SR / 2), btype="low", output="sos")
    return sosfiltfilt(sos, np.tile(x, 3))[n:2 * n]


def kreuzblende_loop(x, fade_s):
    """Verkuerzt die Schleife um fade_s und blendet das Ende ueber den Anfang.

    Dasselbe Verfahren wie loopbar() in stimmtest/musikbett.py, nur mit
    gleichleistungs- statt linearer Rampe. Ergebnis: eine Schleife, deren
    Umbruch keinen Sprung mehr traegt - um den Preis, dass 0,75 s Material
    entfallen und die letzten 0,75 s eine Mischung zweier Stellen sind.
    """
    f = int(fade_s * SR)
    y = x.copy()
    r = np.linspace(0, 1, f, endpoint=False)
    ein, aus = np.sin(r * np.pi / 2) ** 2, np.cos(r * np.pi / 2) ** 2
    y[:f] = x[:f] * ein + x[-f:] * aus
    return y[:-f]


def probe(mono, naht_bei_s=NAHT_BEI_S, dauer_s=PROBE_S):
    """dauer_s Sekunden aus der Schleife, Umbruch genau bei naht_bei_s.

    Der Umbruch selbst ist hart - genau wie _bett_block() in
    schritt3_bett.py ihn in der Produktion macht.
    """
    n = len(mono)
    ziel = int(dauer_s * SR)
    naht = int(naht_bei_s * SR)
    start = (n - naht) % n
    return mono[(np.arange(start, start + ziel) % n)].copy(), naht


def naht_kennzahlen(x, i):
    sprung = float(abs(x[i] - x[i - 1]))
    s = np.sign(x)
    d = None
    for k in range(8000):
        for j in (i - k, i + k):
            if 1 <= j < len(x) and s[j - 1] != s[j] and s[j] != 0:
                d = k
                break
        if d is not None:
            break
    dif = np.abs(np.diff(x))
    innen = float(dif.max())
    # Die eigentlich aussagekraeftige Zahl: wie gewoehnlich ist dieser Sprung
    # im Vergleich zu einem beliebigen Schritt von Sample zu Sample?
    perzentil = float((dif < sprung).mean() * 100)
    return {"nahtsprung": round(sprung, 6),
            "groesster_sprung_innerhalb": round(innen, 6),
            "faktor_innen_zu_naht": round(innen / max(sprung, 1e-12), 1),
            "nahtsprung_perzentil": round(perzentil, 1),
            "nulldurchgang_samples": d,
            "nulldurchgang_ms": round(1000 * d / SR, 3) if d is not None else None}


def stereo(mono):
    return np.stack([mono, np.roll(mono, STEREO_VERSATZ)], axis=1)


def mixpegel(feuerspur, g, schleife_s):
    """Was aus der Feuerschicht im fertigen Mix wird - je Kanal.

    schritt3_bett.py normiert das Bett auf PEGEL_BETT_DBFS, gemessen am
    Mono-Downmix (L+R)/2, und addiert die Stimme identisch in beide Kanaele.
    Ein Kopfhoerer hoert aber die Kanaele einzeln. Deshalb hier je Kanal.
    """
    huelle = np.abs(hilbert(feuerspur)) * g
    schwelle = 10 ** (PEGEL_STIMME_DBFS / 20)
    ueber = huelle > schwelle
    ereignisse = int(np.sum(np.diff(ueber.astype(int)) == 1))
    def db(v):
        return round(float(20 * np.log10(v + 1e-12)), 1)
    return {
        "rms_dbfs": round(rms_db(feuerspur * g), 1),
        "spitze_dbfs": db(huelle.max()),
        "perzentil_99_9_dbfs": db(np.percentile(huelle, 99.9)),
        "ueber_stimmen_rms_je_schleife": ereignisse,
        "ueber_stimmen_rms_je_video": int(ereignisse * round(LAUFZEIT_H * 3600 / schleife_s)),
        "spitze_gegen_stimmen_rms_db": round(db(huelle.max()) - PEGEL_STIMME_DBFS, 1),
    }


def main():
    os.makedirs(ZIEL, exist_ok=True)
    y, sr = sf.read(BETT, dtype="float64", always_2d=True)
    if sr != SR:
        raise SystemExit(f"Bett hat {sr} Hz statt {SR}")
    L, R = y[:, 0], y[:, 1]
    versatz_ok = bool(np.allclose(R, np.roll(L, STEREO_VERSATZ), atol=1e-4))
    ziel_rms = rms_db(y.mean(axis=1))     # Mass, das schritt3_bett.py verwendet

    print(f"Bett: {len(L)/SR:.1f} s, {sr} Hz, Mono-RMS {ziel_rms:.2f} dBFS, "
          f"Stereo = versetztes Mono: {versatz_ok}")
    print("Trenne Pad und Feuer (dreifach gekachelte HPSS) ...")
    pad, feuer = hpss_geloopt(L)
    rekon = rms_db(L - (pad + feuer))
    print(f"  Pad {rms_db(pad):.2f} dBFS | Feuer {rms_db(feuer):.2f} dBFS "
          f"({rms_db(pad)-rms_db(feuer):.1f} dB darunter) | "
          f"Rekonstruktionsfehler {rekon:.2f} dBFS\n")

    # --- Was daraus im fertigen Mix wird -----------------------------
    g_mix = 10 ** ((PEGEL_BETT_DBFS - ziel_rms) / 20)
    kanal_gegen_mono = rms_db(L) - ziel_rms
    print("Hochrechnung auf den fertigen Mix (config.md: Bett -31, Stimme -19 dBFS):")
    print(f"  Das Bett wird am Mono-Downmix (L+R)/2 normiert. Der 240-Sample-Versatz")
    print(f"  der Stereobreite macht diesen Downmix {kanal_gegen_mono:.2f} dB leiser als")
    print(f"  ein einzelner Kanal. Die Stimme wird identisch in beide Kanaele addiert,")
    print(f"  verliert im Downmix also nichts.")
    print(f"    Abstand Stimme/Bett im Mono-Downmix : "
          f"{PEGEL_STIMME_DBFS - PEGEL_BETT_DBFS:+.2f} dB  <- das meldet qa_mix.json")
    print(f"    Abstand Stimme/Bett je Kanal        : "
          f"{PEGEL_STIMME_DBFS - (PEGEL_BETT_DBFS + kanal_gegen_mono):+.2f} dB  "
          f"<- das hoert ein Kopfhoerer\n")

    feuer_leise = 10 ** (FEUER_DB / 20) * tiefpass_geloopt(feuer, FEUER_TIEFPASS_HZ)

    varianten = [
        ("probe_a_feuer_kreuzblende", pad + feuer, True,
         "Feuer unveraendert, Loop-Naht zusaetzlich kreuzgeblendet (0,75 s)"),
        ("probe_b_feuer_leiser_tiefpass", pad + feuer_leise, False,
         f"Feuer {FEUER_DB:.0f} dB und Tiefpass {FEUER_TIEFPASS_HZ/1000:.1f} kHz, "
         f"Naht hart wie in der Produktion"),
        ("probe_c_ohne_feuer", pad, False,
         "nur Pad, Feuerschicht entfernt, Naht hart wie in der Produktion"),
    ]

    bericht = {
        "erzeugt_am": "2026-08-23",
        "mixhochrechnung": {
            "pegel_bett_dbfs": PEGEL_BETT_DBFS,
            "pegel_stimme_dbfs": PEGEL_STIMME_DBFS,
            "kanal_lauter_als_mono_downmix_db": round(rms_db(L) - ziel_rms, 2),
            "abstand_mono_db": PEGEL_STIMME_DBFS - PEGEL_BETT_DBFS,
            "abstand_je_kanal_db": round(
                PEGEL_STIMME_DBFS - (PEGEL_BETT_DBFS + rms_db(L) - ziel_rms), 2),
            "hinweis": "qa_mix.json misst den Mono-Downmix. Je Kanal - also am "
                       "Kopfhoerer - liegt das Bett um den Kammfilterbetrag lauter.",
        },
        "quelle": BETT,
        "quelle_dauer_s": round(len(L) / SR, 3),
        "quelle_rms_mono_dbfs": round(ziel_rms, 2),
        "quelle_naht": naht_kennzahlen(np.concatenate([L, L]), len(L)),
        "stereo_ist_versetztes_mono": versatz_ok,
        "trennung": {
            "verfahren": "HPSS (Fitzgerald 2010), Medianfilter 31, STFT 4096/3072, "
                         "dreifach gekachelt und mittlere Kachel entnommen",
            "pad_dbfs": round(rms_db(pad), 2),
            "feuer_dbfs": round(rms_db(feuer), 2),
            "feuer_unter_pad_db": round(rms_db(pad) - rms_db(feuer), 2),
            "rekonstruktionsfehler_dbfs": round(rekon, 2),
            "pad_naht": naht_kennzahlen(np.concatenate([pad, pad]), len(pad)),
            "feuer_naht": naht_kennzahlen(np.concatenate([feuer, feuer]), len(feuer)),
        },
        "probe_dauer_s": PROBE_S,
        "naht_bei_s": NAHT_BEI_S,
        "kreuzblende_s": KREUZBLENDE_S,
        "proben": {},
    }

    for name, mono_v, kb, beschreibung in varianten:
        schleife = kreuzblende_loop(mono_v, KREUZBLENDE_S) if kb else mono_v
        sig, naht = probe(schleife)
        st = stereo(sig)
        g = 10 ** (ziel_rms / 20) / 10 ** (rms_db(st.mean(axis=1)) / 20)
        st = st * g
        spitze = float(np.abs(st).max())
        sf.write(f"{ZIEL}/{name}.flac", st, SR, subtype="PCM_16")

        # Vergleichswert: dieselbe Variante OHNE Kreuzblende
        roh, naht_roh = probe(mono_v)
        p = {
            "beschreibung": beschreibung,
            "kreuzblende": kb,
            "schleifenlaenge_s": round(len(schleife) / SR, 3),
            "pegelangleich_db": round(float(20 * np.log10(g)), 2),
            "rms_mono_dbfs": round(rms_db(st.mean(axis=1)), 2),
            "peak_dbfs": round(float(20 * np.log10(spitze)), 2),
            "naht_in_der_probe": naht_kennzahlen(sig, naht),
            "naht_ohne_kreuzblende": naht_kennzahlen(roh, naht_roh),
        }
        if kb or "ohne_feuer" not in name:
            spur = {"probe_a_feuer_kreuzblende": feuer,
                    "probe_b_feuer_leiser_tiefpass": feuer_leise}.get(name)
            if spur is not None:
                p["feuer_im_fertigen_mix"] = mixpegel(spur, g_mix, len(L) / SR)
        bericht["proben"][name] = p
        print(f"{name}.flac  ({len(sig)/SR:.0f} s)")
        print(f"   {beschreibung}")
        print(f"   RMS {p['rms_mono_dbfs']} dBFS  Peak {p['peak_dbfs']} dBFS  "
              f"Pegelangleich {p['pegelangleich_db']:+.2f} dB")
        n1, n0 = p["naht_in_der_probe"], p["naht_ohne_kreuzblende"]
        print(f"   Naht in der Probe:      Sprung {n1['nahtsprung']:.6f}  = "
              f"{n1['nahtsprung_perzentil']:.1f}. Perzentil aller Sample-Schritte, "
              f"Nulldurchgang {n1['nulldurchgang_ms']} ms entfernt")
        print(f"   dieselbe Variante hart: Sprung {n0['nahtsprung']:.6f}  = "
              f"{n0['nahtsprung_perzentil']:.1f}. Perzentil, "
              f"Nulldurchgang {n0['nulldurchgang_ms']} ms")
        fm = p.get("feuer_im_fertigen_mix")
        if fm:
            print(f"   Feuer im fertigen Mix (je Kanal): RMS {fm['rms_dbfs']} dBFS, "
                  f"lauteste Spitze {fm['spitze_dbfs']} dBFS "
                  f"({fm['spitze_gegen_stimmen_rms_db']:+.1f} dB gegen den Stimmen-RMS)")
            print(f"   Transienten ueber dem Stimmen-RMS: "
                  f"{fm['ueber_stimmen_rms_je_schleife']} je Schleife = "
                  f"{fm['ueber_stimmen_rms_je_video']:,} je Video")
        print()

    json.dump(bericht, open(f"{ZIEL}/proben_messung.json", "w"), indent=1, ensure_ascii=False)
    print(f"Bericht: {ZIEL}/proben_messung.json")


if __name__ == "__main__":
    main()
