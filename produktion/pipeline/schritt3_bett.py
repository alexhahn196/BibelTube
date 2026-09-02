#!/usr/bin/env python3
"""
Schritt 3 - Klangbett unterlegen.

Die einzige harte Abmischregel, die die Daten hergeben (Formel §5b):
**die Stimme sitzt klar ueber dem Bett, in 6 von 6 vermessenen
Konkurrenzvideos.** Umgesetzt als 12 dB Abstand, Stimme -19 dBFS RMS,
Bett -31 dBFS RMS.

Der Stimmpegel wird ueber die SPRACHABSCHNITTE gemessen, nicht ueber die
ganze Datei: bei 3,4 Stunden Lesung mit Pausen zwischen den Versen wuerde
ein Gesamt-RMS die Stimme systematisch zu leise melden.

**Kein Ducking.** Bei den Gewinnern ist keines hoerbar, und ein atmendes
Bett zieht Aufmerksamkeit - das Gegenteil des Zwecks.

Vorlauf: Formel §3 verlangt Sprachbeginn in Sekunde 0-3 (n=11,
regeln/daten/skript_anatomie.json - die frueher zitierten n=24 aus der
teardown-Matrix belegen die Regel nicht, siehe config.md bei vorlauf_s). Das Bett
laeuft also nur kurz allein an, nicht die 4 s aus stimmtest/musik-prompt.md.

Aufruf:
    python3 produktion/pipeline/schritt3_bett.py V1
"""
import argparse
import json
import os
import sys

import numpy as np
import soundfile as sf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gemeinsam import (SR, Gates, arbeit, config, gate_abschluss,  # noqa: E402
                       hms, pfad, rms_db, sprach_rms_db)

BLOCK = 1 << 20


def bett_laden(cfg):
    y, sr = sf.read(pfad(cfg["bett_datei"]), dtype="float32", always_2d=True)
    if sr != SR:
        raise SystemExit(f"Bett hat {sr} Hz statt {SR}")
    if y.shape[1] == 1:
        y = np.repeat(y, 2, axis=1)
    return y


def _bett_block(bett, start, laenge):
    """Geloopter Ausschnitt des Betts ab Sample `start`."""
    n = len(bett)
    idx = (np.arange(start, start + laenge) % n)
    return bett[idx]


def mischen(video, cfg, nur_messen=False, skalierung=1.0):
    quelle = arbeit(video, "stimme.wav")
    ziel = arbeit(video, "mix.wav")
    qa = json.load(open(arbeit(video, "qa_stimme.json"), encoding="utf-8"))

    bett = bett_laden(cfg)
    g_stimme = 10 ** (float(cfg["pegel_stimme_dbfs"]) / 20) / \
        10 ** (qa["sprach_rms_db"] / 20)
    g_bett = 10 ** (float(cfg["pegel_bett_dbfs"]) / 20) / \
        10 ** (rms_db(bett.mean(axis=1)) / 20)

    vor = int(float(cfg["vorlauf_s"]) * SR)
    nach = int(float(cfg["nachlauf_s"]) * SR)
    ein = int(float(cfg["einblende_s"]) * SR)
    aus = int(float(cfg["ausblende_s"]) * SR)

    info = sf.info(quelle)
    gesamt = info.frames + vor + nach

    schreiber = None
    if not nur_messen:
        schreiber = sf.SoundFile(ziel, "w", samplerate=SR, channels=2,
                                 subtype="PCM_16")
    spitze = 0.0
    pos = 0
    with sf.SoundFile(quelle) as f:
        while pos < gesamt:
            n = min(BLOCK, gesamt - pos)
            mix = _bett_block(bett, pos, n) * g_bett

            # Ein- und Ausblende des Betts
            if pos < ein:
                k = min(n, ein - pos)
                r = np.linspace(pos / ein, (pos + k) / ein, k, endpoint=False)
                mix[:k] *= r[:, None]
            if pos + n > gesamt - aus:
                a0 = max(0, gesamt - aus - pos)
                k = n - a0
                r = np.linspace((pos + a0 - (gesamt - aus)) / aus,
                                (pos + n - (gesamt - aus)) / aus, k, endpoint=False)
                mix[a0:] *= (1 - r)[:, None]

            # Stimme einsetzen
            v_von, v_bis = max(pos, vor), min(pos + n, vor + info.frames)
            if v_bis > v_von:
                f.seek(v_von - vor)
                v = f.read(v_bis - v_von, dtype="float32", always_2d=True).mean(axis=1)
                v = v * g_stimme
                mix[v_von - pos:v_bis - pos, 0] += v
                mix[v_von - pos:v_bis - pos, 1] += v

            mix *= skalierung
            spitze = max(spitze, float(np.abs(mix).max()))
            if schreiber is not None:
                schreiber.write(mix)
            pos += n
    if schreiber is not None:
        schreiber.close()
    return spitze, gesamt, g_stimme, g_bett


def pruefen(video, cfg, gs, gb):
    """Pegelabstand bestimmen - ueber die VOLLE Laenge beider Signale.

    Ein kurzes Fenster taugt hier nicht: das Bett schwillt sehr langsam an
    und ab, ein 3-s-Ausschnitt weicht leicht um 2-3 dB vom Mittel der
    56-s-Schleife ab. Gemessen wird deshalb
      - die Stimme ueber alle Sprachrahmen der vollen 3,5 Stunden,
      - das Bett ueber die komplette Schleife,
    beides mit dem tatsaechlich angewandten Faktor.

    Zusaetzlich eine Stichprobe am fertigen Mix: der freiliegende Abschnitt
    im Nachlauf wird gegen denselben Abschnitt der Quelle gehalten. Weicht
    er ab, stimmt etwas am Schreibweg nicht - das faengt Rechenfehler, die
    eine reine Sollwert-Rechnung nicht sehen wuerde.

    ZWEI WIEDERGABEFAELLE, seit 2026-08-23. Das Bett wird an der Mono-Summe
    (L+R)/2 normiert, die Stimme aber identisch in beide Kanaele addiert.
    Ist das Bett zwischen den Kanaelen dekorreliert, verliert es beim
    Mono-Downmix Pegel und die Stimme nicht - der gemessene Abstand haengt
    dann davon ab, WORAN man misst. Beim alten Bett (R = L um 240 Samples
    versetzt) waren das 12,0 dB in Mono und 6,8 dB je Kanal. Gemeldet wurde
    nur der erste Wert. Seitdem werden beide gemessen und beide geprueft.
    """
    from gemeinsam import rahmen_datei, sprach_maske_env

    env, rmsf, sr, w, _ = rahmen_datei(arbeit(video, "stimme.wav"))
    m = sprach_maske_env(env)
    stimme_db = float(20 * np.log10(
        np.sqrt((rmsf[m].astype(np.float64) ** 2).mean()) + 1e-12)) + 20 * np.log10(gs)

    bett = bett_laden(cfg)
    bett_db = rms_db(bett.mean(axis=1)) + 20 * np.log10(gb)
    # je Kanal: das hoert ein Kopfhoerer, und es kann lauter sein als die
    # Mono-Summe, wenn die Kanaele dekorreliert sind
    bett_db_kanal = max(rms_db(bett[:, 0]), rms_db(bett[:, 1])) + 20 * np.log10(gb)

    # Stichprobe: Bett allein im Nachlauf gegen die Quelle an derselben Stelle
    nach, aus = float(cfg["nachlauf_s"]), float(cfg["ausblende_s"])
    plateau = max(0.5, nach - aus)
    with sf.SoundFile(arbeit(video, "mix.wav")) as f:
        n = f.frames
        start = n - int((nach - 0.05) * SR)
        f.seek(max(0, start))
        ist = f.read(int(plateau * SR), dtype="float32", always_2d=True).mean(axis=1)
    soll = _bett_block(bett, start, len(ist)).mean(axis=1) * gb
    abweichung = rms_db(ist) - rms_db(soll)
    return stimme_db, bett_db, bett_db_kanal, abweichung


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("--nur-messen", action="store_true",
                    help="vorhandene mix.wav nur nachmessen, nicht neu bauen")
    ap.add_argument("--force", action="store_true",
                    help="Gate-Verstoesse melden, aber nicht abbrechen")
    a = ap.parse_args()
    cfg = config()

    if a.nur_messen:
        # Faktoren neu herleiten statt aus einem frueheren Bericht lesen:
        # eine abgebrochene Messung darf die naechste nicht vergiften.
        from gemeinsam import rahmen_datei
        qa = json.load(open(arbeit(a.video, "qa_stimme.json"), encoding="utf-8"))
        gs = 10 ** (float(cfg["pegel_stimme_dbfs"]) / 20) / 10 ** (qa["sprach_rms_db"] / 20)
        gb = 10 ** (float(cfg["pegel_bett_dbfs"]) / 20) / \
            10 ** (rms_db(bett_laden(cfg).mean(axis=1)) / 20)
        gesamt = sf.info(arbeit(a.video, "mix.wav")).frames
        spitze2 = rahmen_datei(arbeit(a.video, "mix.wav"))[4]
    else:
        # Erster Durchlauf nur zum Messen der Spitze, damit anschliessend
        # ohne Limiter linear skaliert werden kann.
        spitze, gesamt, gs, gb = mischen(a.video, cfg, nur_messen=True)
        ziel_peak = 10 ** (float(cfg["peak_max_dbfs"]) / 20)
        skal = min(1.0, ziel_peak / spitze) if spitze > 0 else 1.0
        print(f"  Spitze vor Skalierung {20*np.log10(spitze):.2f} dBFS "
              f"→ Faktor {skal:.4f}")
        spitze2, _, _, _ = mischen(a.video, cfg, nur_messen=False, skalierung=skal)
        gs, gb = gs * skal, gb * skal
    st_db, bett_db, bett_db_kanal, stichprobe = pruefen(a.video, cfg, gs, gb)

    b = {
        "dauer_s": round(gesamt / SR, 1),
        "dauer_hms": hms(gesamt / SR),
        "dauer_h": round(gesamt / SR / 3600, 3),
        "vorlauf_s": float(cfg["vorlauf_s"]),
        "nachlauf_s": float(cfg["nachlauf_s"]),
        "gain_stimme_db": round(float(20 * np.log10(gs)), 2),
        "gain_bett_db": round(float(20 * np.log10(gb)), 2),
        "gemessen_stimme_dbfs": round(st_db, 2),
        "gemessen_bett_allein_dbfs": round(bett_db, 2),
        "gemessen_bett_je_kanal_dbfs": round(bett_db_kanal, 2),
        "gemessener_abstand_db": round(st_db - bett_db, 2),
        "gemessener_abstand_je_kanal_db": round(st_db - bett_db_kanal, 2),
        "bett_dekorreliert_db": round(bett_db_kanal - bett_db, 2),
        "soll_abstand_db": float(cfg["abstand_soll_db"]),
        "peak_dbfs": round(float(20 * np.log10(spitze2)), 2),
        "stichprobe_schreibweg_db": round(float(stichprobe), 2),
        "ducking": bool(cfg.get("ducking", False)),
    }
    # Beide Wiedergabefaelle muessen den Sollabstand erreichen. 0,1 dB
    # Rechentoleranz, damit ein exakt getroffener Wert nicht an der
    # Gleitkommadarstellung scheitert.
    soll = b["soll_abstand_db"]
    b["abstand_eingehalten_mono"] = bool(b["gemessener_abstand_db"] >= soll - 0.1)
    b["abstand_eingehalten_je_kanal"] = bool(b["gemessener_abstand_je_kanal_db"] >= soll - 0.1)
    b["abstand_eingehalten"] = bool(
        b["abstand_eingehalten_mono"] and b["abstand_eingehalten_je_kanal"])
    # Ein Bett, das viel zu leise sitzt, ist genauso falsch wie eines, das
    # zu laut sitzt - nur nicht gefaehrlich. Deshalb getrennt gemeldet.
    b["bett_auffaellig_leise"] = bool(
        min(b["gemessener_abstand_db"], b["gemessener_abstand_je_kanal_db"]) > soll + 3.0)
    json.dump(b, open(arbeit(a.video, "qa_mix.json"), "w"), indent=1)

    print(f"\nMISCHUNG {a.video}")
    print(f"  Gesamtlaufzeit        {b['dauer_hms']}  ({b['dauer_h']:.2f} h)")
    print(f"  Stimme (alle Sprachrahmen) {b['gemessen_stimme_dbfs']} dBFS RMS")
    print(f"  Bett Mono-Summe            {b['gemessen_bett_allein_dbfs']} dBFS RMS")
    print(f"  Bett je Kanal              {b['gemessen_bett_je_kanal_dbfs']} dBFS RMS "
          f"({b['bett_dekorreliert_db']:+.2f} dB gegen die Mono-Summe)")
    print(f"  Abstand Mono-Summe    {b['gemessener_abstand_db']} dB → "
          f"{'eingehalten' if b['abstand_eingehalten_mono'] else 'REISST'}")
    print(f"  Abstand je Kanal      {b['gemessener_abstand_je_kanal_db']} dB → "
          f"{'eingehalten' if b['abstand_eingehalten_je_kanal'] else 'REISST'}")
    print(f"  Soll {b['soll_abstand_db']} dB in BEIDEN Faellen → "
          f"{'eingehalten' if b['abstand_eingehalten'] else 'ABWEICHUNG'}")
    if b["bett_auffaellig_leise"]:
        print("  HINWEIS: Bett liegt mehr als 3 dB unter dem Soll - vermutlich unhoerbar")
    print(f"  Peak                  {b['peak_dbfs']} dBFS "
          f"(Grenze {cfg['peak_max_dbfs']} → "
          f"{'eingehalten' if b['peak_dbfs'] <= float(cfg['peak_max_dbfs']) else 'ÜBERSCHRITTEN'})")
    print(f"  Stichprobe Schreibweg {b['stichprobe_schreibweg_db']:+.2f} dB "
          f"(Bett im Nachlauf gegen die Quelle — 0,00 = fehlerfrei geschrieben)")
    print(f"  Ducking               {'ja' if b['ducking'] else 'nein'}")

    # Gate 1.11. Beide Wiedergabefaelle muessen halten, nicht nur die
    # Mono-Summe: qa_mix.json mass bis 2026-08-23 nur den Downmix und meldete
    # 12,0 dB, wo am Kopfhoerer 6,8 dB standen (V01-V04). Ein dekorreliertes
    # Bett verliert im Downmix Pegel und sieht dadurch besser aus, als es ist.
    g = Gates(a.force)
    g.pruefen("1.11", "Pegelabstand (Mono-Summe)", b["abstand_eingehalten_mono"],
              f"{b['gemessener_abstand_db']} dB statt {b['soll_abstand_db']} dB")
    g.pruefen("1.11", "Pegelabstand (je Kanal)", b["abstand_eingehalten_je_kanal"],
              f"{b['gemessener_abstand_je_kanal_db']} dB statt "
              f"{b['soll_abstand_db']} dB — am Kopfhoerer hoerbar, "
              f"in der Mono-Summe nicht")
    g.pruefen("", "Peak", b["peak_dbfs"] <= float(cfg["peak_max_dbfs"]),
              f"{b['peak_dbfs']} dBFS ueber der Grenze {cfg['peak_max_dbfs']} dBFS")
    return gate_abschluss(g, "Schritt 3 (Klangbett)")


if __name__ == "__main__":
    sys.exit(main())
