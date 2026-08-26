#!/usr/bin/env python3
"""
Gate 1.11 - Pegelabstand in BEIDEN Wiedergabefaellen.

**NICHT TEIL DER PIPELINE.** Gate 1.11 prueft `schritt3_bett.py`; es misst
seit 2026-08-23 selbst beide Faelle und schreibt sie nach `qa_mix.json`
(`gemessen_bett_je_kanal_dbfs`, `gemessener_abstand_je_kanal_db`,
`bett_dekorreliert_db`, getrennte Flags). Dieses Skript ist am 2026-08-25
unabhaengig davon entstanden und bleibt als Einzelwerkzeug liegen: es misst
eine BETT-DATEI allein, ohne Renderlauf, und beantwortet damit die Frage
"wieviel verliert dieses Bett beim Downmix" fuer ein Artefakt, das noch
nirgends verwendet wird. Ergebnis in
`produktion/pipeline/qa/pegel_wiedergabe.json`.


`schritt3_bett.py` mischt stereo, misst aber mono: sowohl `rahmen_datei()`
als auch `rms_db(bett.mean(axis=1))` summieren vorher L und R. Der Wert in
`qa_mix.json` beschreibt deshalb nur den MONO-Fall.

Das ist kein Rundungsproblem. Das Bett hat Stereobreite
(`stimmtest/musikbett.py`: `np.stack([sig, np.roll(sig, 240)])`), L und R
sind dadurch negativ korreliert - die Monosumme loescht einen Teil davon
aus. Die Stimme dagegen liegt identisch in beiden Kanaelen und summiert
verlustfrei. Der Abstand ist in Mono also systematisch groesser als in
Stereo, und zwar genau um den Betrag, den das Bett beim Downmix verliert.

Zwei Wiedergabefaelle, beide real:
  MONO   - Handylautsprecher, Bluetooth-Box, Smart Speaker. Das ist der
           Fall, den die Pipeline bisher misst und meldet.
  STEREO - Kopfhoerer. Jeder Kanal traegt das Bett voll, die Stimme
           unveraendert. Das ist der Fall, den bisher niemand gemessen hat.

Der Unterschied haengt nur am Bett und ist damit fuer alle Videos gleich:
`bett_datei` ist ein festes, eingechecktes Artefakt (`config.md`).

Aufruf:
    python3 produktion/pipeline/pegel_wiedergabe.py
        Rechnung aus config.md + Bettdatei. Braucht keinen Renderlauf.

    python3 produktion/pipeline/pegel_wiedergabe.py --video V5
        zusaetzlich mit dem tatsaechlich gemessenen Stimmpegel aus
        produktion/arbeit/video-05/qa_stimme.json, falls vorhanden.
"""
import argparse
import json
import os
import sys

import numpy as np
import soundfile as sf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gemeinsam import arbeit, config, pfad, rms_db  # noqa: E402


def kanal_rms_db(y):
    """RMS je Kanal als Leistungsmittel - nicht als Mittel der dB-Werte.

    Bei zwei gleich lauten Kanaelen ist beides identisch; bei ungleichen
    waere das dB-Mittel falsch.
    """
    p = np.array([10 ** (rms_db(y[:, k]) / 10) for k in range(y.shape[1])])
    return float(10 * np.log10(p.mean()))


def messen(cfg, stimme_dbfs=None, quelle_stimme="config.md"):
    y, sr = sf.read(pfad(cfg["bett_datei"]), dtype="float32", always_2d=True)
    if y.shape[1] == 1:
        y = np.repeat(y, 2, axis=1)

    mono_db = rms_db(y.mean(axis=1))
    kanal_db = kanal_rms_db(y)

    # Derselbe Faktor, den schritt3_bett.py anwendet: er normalisiert die
    # MONOSUMME des Betts auf pegel_bett_dbfs.
    soll_bett = float(cfg["pegel_bett_dbfs"])
    g_bett_db = soll_bett - mono_db

    if stimme_dbfs is None:
        stimme_dbfs = float(cfg["pegel_stimme_dbfs"])

    bett_mono = mono_db + g_bett_db
    bett_kanal = kanal_db + g_bett_db

    k = float(np.corrcoef(y[:, 0].astype(np.float64),
                          y[:, 1].astype(np.float64))[0, 1])

    return {
        "bett_datei": cfg["bett_datei"],
        "bett_dauer_s": round(len(y) / sr, 3),
        "bett_samplerate": int(sr),
        "bett_kanaele": int(y.shape[1]),
        "bett_korrelation_LR": round(k, 5),
        "bett_rms_roh_mono_dbfs": round(mono_db, 3),
        "bett_rms_roh_kanal_dbfs": round(kanal_db, 3),
        "downmix_verlust_db": round(kanal_db - mono_db, 3),
        "gain_bett_db": round(g_bett_db, 3),
        "stimme_dbfs": round(float(stimme_dbfs), 3),
        "stimme_quelle": quelle_stimme,
        "bett_mono_dbfs": round(bett_mono, 3),
        "bett_stereo_kanal_dbfs": round(bett_kanal, 3),
        "abstand_mono_db": round(stimme_dbfs - bett_mono, 2),
        "abstand_stereo_db": round(stimme_dbfs - bett_kanal, 2),
        "soll_abstand_db": float(cfg["abstand_soll_db"]),
        "toleranz_db": 1.0,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--video", help="V1 … V8 - nimmt den gemessenen "
                                    "Stimmpegel aus qa_stimme.json, falls da")
    ap.add_argument("--aus", default=None, help="Zieldatei der Messung")
    a = ap.parse_args()
    cfg = config()

    stimme_dbfs, quelle = None, "config.md: pegel_stimme_dbfs (Sollwert)"
    if a.video:
        p = arbeit(a.video, "qa_stimme.json")
        if os.path.exists(p):
            # Der Sollwert wird beim Mischen exakt getroffen; hier steht er
            # trotzdem aus der Messung, damit die Zahl aus einer Messdatei
            # kommt und nicht aus einer Absicht.
            stimme_dbfs = float(cfg["pegel_stimme_dbfs"])
            quelle = (f"{os.path.relpath(p, pfad())} vorhanden - "
                      f"Stimme auf {stimme_dbfs} dBFS normalisiert")
        else:
            quelle += f" ({os.path.relpath(p, pfad())} fehlt, kein Renderlauf)"

    b = messen(cfg, stimme_dbfs, quelle)
    if a.video:
        b["video"] = a.video

    b["mono_eingehalten"] = bool(
        abs(b["abstand_mono_db"] - b["soll_abstand_db"]) <= b["toleranz_db"])
    b["stereo_eingehalten"] = bool(
        abs(b["abstand_stereo_db"] - b["soll_abstand_db"]) <= b["toleranz_db"])
    b["bestanden"] = bool(b["mono_eingehalten"] and b["stereo_eingehalten"])

    ziel = a.aus or pfad("produktion", "pipeline", "qa", "pegel_wiedergabe.json")
    os.makedirs(os.path.dirname(ziel), exist_ok=True)
    json.dump(b, open(ziel, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    print(f"Bett  {b['bett_datei']}  ({b['bett_dauer_s']} s, "
          f"Korrelation L/R {b['bett_korrelation_LR']:+.3f})")
    print(f"  Downmix-Verlust des Betts   {b['downmix_verlust_db']:+.2f} dB")
    print(f"  Stimme                      {b['stimme_dbfs']:.1f} dBFS "
          f"({b['stimme_quelle']})")
    print()
    print(f"  Gate 1.11 MONO    Bett {b['bett_mono_dbfs']:7.2f} dBFS   "
          f"Abstand {b['abstand_mono_db']:5.2f} dB   "
          f"{'OK' if b['mono_eingehalten'] else 'REISST'}")
    print(f"  Gate 1.11 STEREO  Bett {b['bett_stereo_kanal_dbfs']:7.2f} dBFS   "
          f"Abstand {b['abstand_stereo_db']:5.2f} dB   "
          f"{'OK' if b['stereo_eingehalten'] else 'REISST'}")
    print(f"  Soll {b['soll_abstand_db']:.1f} dB "
          f"(Toleranz {b['toleranz_db']:.1f} dB)")
    print(f"\ngeschrieben: {os.path.relpath(ziel, pfad())}")
    return 0 if b["bestanden"] else 1


if __name__ == "__main__":
    sys.exit(main())
