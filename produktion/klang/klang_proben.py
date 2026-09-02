#!/usr/bin/env python3
"""
klang_proben.py - Hoerproben des Klangbetts zur Entscheidung ueber Feuerschicht
UND Stereoaufbau.

WARUM NICHT NEU ERZEUGT: config.md fuehrt produktion/klang/bett_pad_feuer.flac
ausdruecklich als ARTEFAKT - stimmtest/musikbett.py zieht die Luftschicht des
Pads aus einem ungeseedeten np.random.randn, ein zweiter Lauf ergaebe ein
anderes Bett. Die Proben werden deshalb AUS dem vorhandenen Bett gebaut. Das
Pad, das man in allen Proben hoert, ist das Pad des Kanals.

SCHICHTTRENNUNG: harmonisch/perkussiv nach Fitzgerald 2010 - im Spektrogramm
ueber die Zeit medianfiltern haelt stehende Toene (Pad), ueber die Frequenz
medianfiltern haelt Klick-Transienten (Feuer). Die Masken addieren sich zu 1,
die Rekonstruktion ist verlustfrei. Dreifach gekachelt analysiert, damit die
Fensterung an den Dateiraendern die Loop-Naht nicht zerstoert.

DER STEREOAUFBAU IST DER EIGENTLICHE BEFUND (2026-08-23):
Das Bett ist kein echtes Stereo, sondern L mit R = L um 240 Samples versetzt.
240 Samples sind 5,442 ms. Wer das zu Mono summiert - und 68 % des Publikums
hoert ueber Handy, 12 % ueber TV -, bekommt einen Kammfilter mit Kerben bei
91,9 Hz und dann alle 183,8 Hz. Das trifft ausgerechnet die Quinte des Pads
(82,5 Hz, -15,9 dB) und die Oktave (110 Hz, -10,3 dB). In Mono steht damit ein
anderer Akkord als der, der im Hoertest ausgewaehlt wurde.
Die Stimme ist NICHT betroffen: schritt3_bett.py addiert sie identisch in
beide Kanaele, sie wird nicht kammgefiltert.

Jede Variante wird als Stereodatei UND als Mono-Summe geschrieben und in
beiden Faellen vermessen.

Aufruf: python3 produktion/klang/klang_proben.py
"""
import argparse
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
STEREO_VERSATZ = 240
NPERSEG, NOVERLAP, MEDIAN = 4096, 3072, 31
FEUER_DB = -6.0
FEUER_TIEFPASS_HZ = 1100.0
PEGEL_BETT_DBFS = -31.0        # config.md, gemessen an der Mono-Summe
PEGEL_STIMME_DBFS = -19.0
LAUFZEIT_H = 3.5
ROOT = 55.0                    # stimmtest/musikbett.py
TEILTOENE = [(ROOT, 0.55, "Grundton A1"), (ROOT * 1.5, 0.30, "Quinte E2"),
             (ROOT * 2, 0.30, "Oktave A2"), (ROOT * 3, 0.14, "Duodezime E3"),
             (ROOT * 4, 0.08, "Doppeloktave A3")]


def rms_db(x):
    x = np.asarray(x, dtype=float)
    return float(20 * np.log10(np.sqrt((x ** 2).mean()) + 1e-12))


def hpss_geloopt(x):
    n = len(x)
    _, _, Z = stft(np.tile(x, 3), fs=SR, nperseg=NPERSEG, noverlap=NOVERLAP, window="hann")
    S = np.abs(Z)
    h2 = median_filter(S, size=(1, MEDIAN), mode="wrap") ** 2
    p2 = median_filter(S, size=(MEDIAN, 1), mode="nearest") ** 2
    nrm = h2 + p2 + 1e-12
    _, xh = istft(Z * (h2 / nrm), fs=SR, nperseg=NPERSEG, noverlap=NOVERLAP, window="hann")
    _, xp = istft(Z * (p2 / nrm), fs=SR, nperseg=NPERSEG, noverlap=NOVERLAP, window="hann")
    return xh[n:2 * n], xp[n:2 * n]


def tiefpass_geloopt(x, fg_hz, ordnung=4):
    """Dreifach gekachelt, sonst bricht sosfiltfilt die Loop-Naht auf."""
    n = len(x)
    sos = butter(ordnung, fg_hz / (SR / 2), btype="low", output="sos")
    return sosfiltfilt(sos, np.tile(x, 3))[n:2 * n]


def hochpass_geloopt(x, fg_hz, ordnung=4):
    n = len(x)
    sos = butter(ordnung, fg_hz / (SR / 2), btype="high", output="sos")
    return sosfiltfilt(sos, np.tile(x, 3))[n:2 * n]


def kreuzblende_loop(x, fade_s):
    f = int(fade_s * SR)
    y = x.copy()
    r = np.linspace(0, 1, f, endpoint=False)
    y[:f] = x[:f] * np.sin(r * np.pi / 2) ** 2 + x[-f:] * np.cos(r * np.pi / 2) ** 2
    return y[:-f]


def probe(mono, naht_bei_s=NAHT_BEI_S, dauer_s=PROBE_S):
    n = len(mono)
    ziel, naht = int(dauer_s * SR), int(naht_bei_s * SR)
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
    return {"nahtsprung": round(sprung, 6),
            "nahtsprung_perzentil": round(float((dif < sprung).mean() * 100), 1),
            "nulldurchgang_ms": round(1000 * d / SR, 3) if d is not None else None}


# Jeder Teilton besteht aus ZWEI Schichten, um +-0,12 Hz verstimmt
# (stimmtest/musikbett.py, "det"). Bei 60 s Probe sind das +-7,2 FFT-Bins.
# Ein schmales Suchfenster misst deshalb an den Schichten vorbei - mit
# +-4 Bins kam die Oktave 5,7 dB zu leise heraus. Das Fenster muss die
# Verstimmung und die LFO-Seitenbaender (1/23 und 1/37 Hz) einschliessen.
TEILTON_FENSTER_HZ = 0.3


def akkordbalance(sig_stereo):
    """Pegel der fuenf Pad-Teiltoene relativ zum Grundton, in der Mono-Summe."""
    m = sig_stereo.mean(axis=1)
    n = len(m)
    F = np.abs(np.fft.rfft(m * np.hanning(n)))
    f = np.fft.rfftfreq(n, 1 / SR)
    def pegel(fz):
        s = (f >= fz - TEILTON_FENSTER_HZ) & (f <= fz + TEILTON_FENSTER_HZ)
        return float(np.sqrt((F[s] ** 2).sum()))
    g0 = pegel(ROOT)
    return {nm: round(float(20 * np.log10(pegel(fz) / (g0 + 1e-18) + 1e-18)), 2)
            for fz, _, nm in TEILTOENE}


def kammkerben(sig_stereo):
    """Wie tief liegt die Mono-Summe an den Kammfilter-Kerben unter einem Kanal?"""
    L = sig_stereo[:, 0]
    m = sig_stereo.mean(axis=1)
    n = len(L)
    w = np.hanning(n)
    FL = np.abs(np.fft.rfft(L * w))
    FM = np.abs(np.fft.rfft(m * w))
    f = np.fft.rfftfreq(n, 1 / SR)
    T = STEREO_VERSATZ / SR
    out = {}
    for k in range(4):
        fz = (2 * k + 1) / (2 * T)
        i = np.argmin(np.abs(f - fz))
        sl = slice(max(0, i - 3), i + 4)
        out[f"{fz:.0f} Hz"] = round(float(20 * np.log10(
            (FM[sl].max() + 1e-15) / (FL[sl].max() + 1e-15))), 1)
    return out


def mixpegel(feuerspur, g, schleife_s):
    huelle = np.abs(hilbert(feuerspur)) * g
    ueber = huelle > 10 ** (PEGEL_STIMME_DBFS / 20)
    ereignisse = int(np.sum(np.diff(ueber.astype(int)) == 1))
    return {"rms_dbfs": round(rms_db(feuerspur * g), 1),
            "spitze_dbfs": round(float(20 * np.log10(huelle.max() + 1e-12)), 1),
            "ueber_stimmen_rms_je_schleife": ereignisse,
            "ueber_stimmen_rms_je_video": int(ereignisse * round(LAUFZEIT_H * 3600 / schleife_s)),
            "spitze_gegen_stimmen_rms_db": round(
                float(20 * np.log10(huelle.max() + 1e-12)) - PEGEL_STIMME_DBFS, 1)}


#: Das Produktionsbett. Dieses Skript schreibt NICHT hierher - siehe
#: produktionsbett().
PRODUKTIONSBETT = "produktion/klang/bett_mono_feuer_leise.flac"
#: Wohin Variante (e) geht. Eigener Name, damit nie wieder zwei verschiedene
#: Betten denselben Dateinamen tragen.
VARIANTE_E = "produktion/klang/verworfen_bett_mono_variante_e.flac"


def produktionsbett(pad, feuer_leise, ziel_mono_rms):
    """Schreibt Variante (e): Pad ohne Stereoversatz, Feuerschicht 6 dB tiefer
    mit Tiefpass bei 1,1 kHz.

    VERWORFEN AM 2026-09-02. Das Produktionsbett ist seither der LINKE KANAL des
    Stereo-Artefakts, unveraendert bis auf -6 dB Pegel (nachgemessen:
    Korrelation 1,000000 zum linken Kanal, Restfehler -69 dB). Diese Funktion
    schreibt deshalb nach VARIANTE_E und NICHT mehr nach PRODUKTIONSBETT -
    die beiden Betten lagen auf zwei Zweigen unter demselben Dateinamen, und
    genau das soll nicht wieder passieren.

    Das Pad ist in beiden Faellen bitgleich das Pad des alten Betts: es wird
    nicht neu erzeugt, sondern aus dem Artefakt herausgetrennt. Der Unterschied
    zwischen den beiden Kandidaten ist kleiner, als die Namen vermuten lassen -
    Variante (e) korreliert mit 0,9929 mit dem linken Kanal. Entschieden wurde
    also nicht "mono gegen stereo", sondern ob die Feuerschicht leiser und
    tiefpassgefiltert laufen soll. Sie soll nicht.
    """
    mono = pad + feuer_leise
    g = 10 ** (ziel_mono_rms / 20) / 10 ** (rms_db(mono) / 20)
    st = np.stack([mono * g, mono * g], axis=1)
    ziel = VARIANTE_E
    if os.path.abspath(ziel) == os.path.abspath(PRODUKTIONSBETT):
        raise SystemExit("Variante (e) darf das Produktionsbett nicht ueberschreiben.")
    sf.write(ziel, st, SR, subtype="PCM_16")
    print(f"\n{ziel}")
    print(f"  {len(mono)/SR:.1f} s, {SR} Hz, L = R (kein Versatz)")
    print(f"  RMS je Kanal {rms_db(st[:,0]):.2f} dBFS = RMS der Mono-Summe "
          f"{rms_db(st.mean(axis=1)):.2f} dBFS")
    print(f"  Peak {20*np.log10(np.abs(st).max()):.2f} dBFS")
    n = naht_kennzahlen(np.concatenate([mono, mono]), len(mono))
    print(f"  Loop-Naht: Sprung {n['nahtsprung']:.6f} = {n['nahtsprung_perzentil']:.1f}. "
          f"Perzentil, Nulldurchgang {n['nulldurchgang_ms']} ms")
    bal = akkordbalance(st)
    print("  Akkord in der Mono-Summe (Soll: -5,26 / -5,26 / -11,88 / -16,75):")
    print("    " + " · ".join(f"{k.split()[0]} {v:+.2f}" for k, v in bal.items() if k != "Grundton A1"))
    return ziel


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--produktionsbett", action="store_true",
                    help="statt der Proben das neue Kanalbett schreiben (Variante e)")
    args = ap.parse_args()
    os.makedirs(ZIEL, exist_ok=True)
    y, sr = sf.read(BETT, dtype="float64", always_2d=True)
    if sr != SR:
        raise SystemExit(f"Bett hat {sr} Hz statt {SR}")
    L = y[:, 0]
    versatz_ok = bool(np.allclose(y[:, 1], np.roll(L, STEREO_VERSATZ), atol=1e-4))
    ziel_mono_rms = rms_db(y.mean(axis=1))

    T = STEREO_VERSATZ / SR
    print(f"Bett {len(L)/SR:.1f} s, {sr} Hz | Stereo = versetztes Mono: {versatz_ok} "
          f"({STEREO_VERSATZ} Samples = {1000*T:.3f} ms)")
    print(f"Kammfilter-Kerben in der Mono-Summe: {1/(2*T):.1f} Hz, dann alle {1/T:.1f} Hz")
    print(f"Mono-Summe des Betts: {ziel_mono_rms:.2f} dBFS, ein Kanal: {rms_db(L):.2f} dBFS "
          f"({rms_db(L)-ziel_mono_rms:.2f} dB Verlust)\n")

    print("Trenne Pad und Feuer ...")
    pad, feuer = hpss_geloopt(L)
    print(f"  Pad {rms_db(pad):.2f} | Feuer {rms_db(feuer):.2f} dBFS | "
          f"Rekonstruktionsfehler {rms_db(L-(pad+feuer)):.2f} dBFS\n")
    feuer_leise = 10 ** (FEUER_DB / 20) * tiefpass_geloopt(feuer, FEUER_TIEFPASS_HZ)

    if args.produktionsbett:
        produktionsbett(pad, feuer_leise, ziel_mono_rms)
        return

    def versetzt(mono):
        return np.stack([mono, np.roll(mono, STEREO_VERSATZ)], axis=1)

    def echt_mono(mono):
        return np.stack([mono, mono], axis=1)

    # Zusatzvariante f: nur die Feuerschicht versetzen, das Pad echt mono.
    # Das Pad traegt 93 % seiner Energie unter 120 Hz - genau dort sitzt die
    # erste Kerbe. Das Feuer sitzt oberhalb, wo der Kamm feiner und harmloser ist.
    def pad_mono_feuer_breit(pad_s, feuer_s):
        return np.stack([pad_s + feuer_s,
                         pad_s + np.roll(feuer_s, STEREO_VERSATZ)], axis=1)

    varianten = [
        ("probe_a_feuer_kreuzblende", lambda: versetzt(kreuzblende_loop(pad + feuer, KREUZBLENDE_S)),
         "Feuer unveraendert, Naht kreuzgeblendet, Stereo versetzt (Ist-Zustand)", feuer, True),
        ("probe_b_feuer_leiser_tiefpass", lambda: versetzt(pad + feuer_leise),
         f"Feuer {FEUER_DB:.0f} dB + Tiefpass {FEUER_TIEFPASS_HZ/1000:.1f} kHz, Stereo versetzt",
         feuer_leise, False),
        ("probe_c_ohne_feuer", lambda: versetzt(pad),
         "nur Pad, Stereo versetzt", None, False),
        ("probe_d_echt_mono_feuer", lambda: echt_mono(pad + feuer),
         "Feuer unveraendert, ECHT MONO (L = R, kein Versatz)", feuer, False),
        ("probe_e_echt_mono_feuer_leiser", lambda: echt_mono(pad + feuer_leise),
         f"Feuer {FEUER_DB:.0f} dB + Tiefpass {FEUER_TIEFPASS_HZ/1000:.1f} kHz, ECHT MONO",
         feuer_leise, False),
        ("probe_f_pad_mono_feuer_breit", lambda: pad_mono_feuer_breit(pad, feuer_leise),
         f"Pad echt mono, nur die Feuerschicht versetzt ({FEUER_DB:.0f} dB + Tiefpass)",
         feuer_leise, False),
    ]

    g_mix = 10 ** ((PEGEL_BETT_DBFS - ziel_mono_rms) / 20)
    bericht = {
        "erzeugt_am": "2026-08-23",
        "quelle": BETT,
        "stereoaufbau": {
            "ist_versetztes_mono": versatz_ok,
            "versatz_samples": STEREO_VERSATZ,
            "versatz_ms": round(1000 * T, 3),
            "erste_kerbe_hz": round(1 / (2 * T), 1),
            "kerbabstand_hz": round(1 / T, 1),
            "stimme_betroffen": False,
            "hinweis": "schritt3_bett.py addiert die Stimme identisch in beide Kanaele "
                       "(Zeilen 102/103) - sie wird nicht kammgefiltert. Nur das Bett.",
        },
        "publikum": {"mobil_pct": 68, "tv_pct": 12, "tablet_pct": 11, "desktop_pct": 7,
                     "hinweis": "80 % hoeren ueber Handy- oder TV-Lautsprecher, also mono "
                                "oder nahezu mono - der Mono-Fall ist der Regelfall."},
        "trennung": {"pad_dbfs": round(rms_db(pad), 2), "feuer_dbfs": round(rms_db(feuer), 2),
                     "rekonstruktionsfehler_dbfs": round(rms_db(L - (pad + feuer)), 2)},
        "proben": {},
    }

    print(f"{'Variante':34s} {'Kanal':>8s} {'Mono':>8s} {'Verlust':>8s} {'Quinte/Grundton':>16s}")
    for name, bauen, beschreibung, feuerspur, _ in varianten:
        st = bauen()
        sig, naht = probe(st[:, 0])
        st2, _ = probe(st[:, 1])
        st = np.stack([sig, st2], axis=1)
        # Alle Varianten auf denselben MONO-Pegel bringen: das ist der Fall,
        # den 68 % des Publikums hoeren, und die Pipeline normiert ebenfalls
        # an der Mono-Summe.
        g = 10 ** (ziel_mono_rms / 20) / 10 ** (rms_db(st.mean(axis=1)) / 20)
        st = st * g
        mono = st.mean(axis=1)

        sf.write(f"{ZIEL}/{name}.flac", st, SR, subtype="PCM_16")
        sf.write(f"{ZIEL}/{name}_mono.flac",
                 np.stack([mono, mono], axis=1), SR, subtype="PCM_16")

        bal = akkordbalance(st)
        p = {"beschreibung": beschreibung,
             "rms_kanal_dbfs": round(rms_db(st[:, 0]), 2),
             "rms_mono_dbfs": round(rms_db(mono), 2),
             "mono_verlust_db": round(rms_db(st[:, 0]) - rms_db(mono), 2),
             "peak_dbfs": round(float(20 * np.log10(np.abs(st).max() + 1e-12)), 2),
             "akkordbalance_mono_db": bal,
             "kammkerben_mono_db": kammkerben(st),
             "naht": naht_kennzahlen(sig, naht),
             "im_fertigen_mix": {
                 "bett_je_kanal_dbfs": round(PEGEL_BETT_DBFS + rms_db(st[:, 0]) - rms_db(mono), 2),
                 "bett_mono_dbfs": PEGEL_BETT_DBFS,
                 "abstand_je_kanal_db": round(
                     PEGEL_STIMME_DBFS - (PEGEL_BETT_DBFS + rms_db(st[:, 0]) - rms_db(mono)), 2),
                 "abstand_mono_db": PEGEL_STIMME_DBFS - PEGEL_BETT_DBFS,
             }}
        if feuerspur is not None:
            p["feuer_im_fertigen_mix"] = mixpegel(feuerspur, g_mix, len(L) / SR)
        bericht["proben"][name] = p
        print(f"{name:34s} {p['rms_kanal_dbfs']:7.2f} {p['rms_mono_dbfs']:8.2f} "
              f"{p['mono_verlust_db']:8.2f} {bal['Quinte E2']:15.2f}")

    json.dump(bericht, open(f"{ZIEL}/proben_messung.json", "w"), indent=1, ensure_ascii=False)
    print(f"\nSollwert der Quinte nach Bauplan: "
          f"{20*np.log10(TEILTOENE[1][1]/TEILTOENE[0][1]):.2f} dB unter dem Grundton")
    print(f"Bericht: {ZIEL}/proben_messung.json")


if __name__ == "__main__":
    main()
