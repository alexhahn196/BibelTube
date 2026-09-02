#!/usr/bin/env python3
"""
gemeinsam.py - Konfiguration und Audio-Hilfen fuer alle Pipeline-Schritte.

Die Konfiguration kommt aus produktion/config.md. Bewusst aus einer
Markdown-Datei und nicht aus einer .py oder .json: die Werte sollen
lesbar und kommentiert an genau einer Stelle stehen. Der ini-Block darin
ist maschinenlesbar.
"""
import os
import re
import subprocess

import numpy as np

WURZEL = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CONFIG = os.path.join(WURZEL, "produktion", "config.md")
SR = 44100


def _wandeln(v):
    if v in ("ja", "true", "yes"):
        return True
    if v in ("nein", "false", "no"):
        return False
    try:
        return int(v)
    except ValueError:
        pass
    try:
        return float(v)
    except ValueError:
        return v


def config(pfad=CONFIG):
    """Liest den ```ini-Block aus config.md."""
    txt = open(pfad, encoding="utf-8").read()
    bloecke = re.findall(r"```ini\n(.*?)```", txt, re.S)
    if not bloecke:
        raise SystemExit(f"{pfad}: kein ```ini-Block gefunden")
    cfg = {}
    for zeile in "\n".join(bloecke).splitlines():
        zeile = zeile.split("#", 1)[0].strip()
        if not zeile or "=" not in zeile:
            continue
        k, v = zeile.split("=", 1)
        cfg[k.strip()] = _wandeln(v.strip())
    # Jeder Schluessel, dessen Fehlen das Ergebnis veraendert, MUSS hier stehen.
    # Sonst greift still ein Vorgabewert aus cfg.get() im jeweiligen Skript, und
    # der Lauf produziert etwas anderes als dokumentiert, ohne es zu melden.
    # Erweitert 2026-08-23 nach dem Audit der stillen Rueckfaelle: Anlass war
    # ki_clip_ordner_V5, das ohne Eintrag auf die Clips von V1 zurueckfiel.
    pflicht = ["stimme_id", "tts_modell", "prosody_speed", "pegel_stimme_dbfs",
               "pegel_bett_dbfs", "bett_datei", "fps", "breite", "hoehe",
               # Bild und Video
               "videoquelle", "video_crf", "video_preset", "video_pixelformat",
               "zoom_faktor",
               # Mischung
               "abstand_soll_db", "peak_max_dbfs", "vorlauf_s",
               # Text und Qualitaetsschwellen
               "chunk_max_zeichen", "laufzeit_min_h", "sprachanteil_min_pct"]
    fehlt = [k for k in pflicht if k not in cfg]
    if fehlt:
        raise SystemExit(f"{pfad}: fehlende Werte {fehlt}")
    return cfg


def pfad(*teile):
    return os.path.join(WURZEL, *teile)


def ordner(video):
    """Arbeitsordner eines Videos, z.B. produktion/video-01/."""
    p = pfad("produktion", f"video-{int(video[1:]):02d}")
    os.makedirs(p, exist_ok=True)
    return p


def arbeit(video, *teile):
    """Zwischenstaende, die nicht ins Repository gehoeren."""
    p = pfad("produktion", "arbeit", f"video-{int(video[1:]):02d}", *teile[:-1])
    os.makedirs(p, exist_ok=True)
    return os.path.join(p, teile[-1]) if teile else p


# ---------------------------------------------------------------- Audio

RAHMEN_S = 0.02          # 20-ms-Rahmen, nicht ueberlappend
SCHWELLE_FAKTOR = 0.15   # Anteil des 95. Perzentils der Huellkurve


def rms_db(x):
    x = np.asarray(x, dtype=np.float64)
    if x.size == 0:
        return -120.0
    return float(20 * np.log10(np.sqrt((x ** 2).mean()) + 1e-12))


def rahmen(x, sr, rahmen_s=RAHMEN_S):
    """Mittlerer Betrag und RMS je 20-ms-Rahmen eines Signalstuecks."""
    w = max(1, int(rahmen_s * sr))
    n = (len(x) // w) * w
    if n == 0:
        return np.zeros(0, np.float32), np.zeros(0, np.float32), w
    b = x[:n].reshape(-1, w).astype(np.float32)
    return np.abs(b).mean(axis=1), np.sqrt((b ** 2).mean(axis=1)), w


def rahmen_datei(datei, rahmen_s=RAHMEN_S, block=1 << 22):
    """Rahmenweise Huellkurve einer ganzen Datei, ohne sie zu laden.

    Bei 3,4 Stunden sind das 546 Millionen Samples - eine Faltung darueber
    ist nicht rechenbar. Deshalb nicht ueberlappende Rahmen und ein
    Blockleser: der Speicherbedarf bleibt konstant, die Kosten linear.
    """
    import soundfile as sf
    env, rmsf = [], []
    with sf.SoundFile(datei) as f:
        sr = f.samplerate
        w = max(1, int(rahmen_s * sr))
        blk = (block // w) * w
        peak = 0.0
        while True:
            y = f.read(blk, dtype="float32", always_2d=True)
            if len(y) == 0:
                break
            y = y.mean(axis=1)
            peak = max(peak, float(np.abs(y).max()))
            e, r, _ = rahmen(y, sr, rahmen_s)
            env.append(e)
            rmsf.append(r)
    return (np.concatenate(env) if env else np.zeros(0, np.float32),
            np.concatenate(rmsf) if rmsf else np.zeros(0, np.float32),
            sr, w, peak)


def sprach_maske_env(env, faktor=SCHWELLE_FAKTOR):
    return env > (faktor * np.percentile(env, 95))


def sprach_maske(x, sr, schwelle=SCHWELLE_FAKTOR, rahmen_s=RAHMEN_S):
    """Sprachmaske auf Samplerasterebene - nur fuer kurze Stuecke."""
    e, _, w = rahmen(x, sr, rahmen_s)
    if e.size == 0:
        return np.zeros(len(x), bool)
    m = np.repeat(sprach_maske_env(e, schwelle), w)
    return np.concatenate([m, np.zeros(len(x) - len(m), bool)])


def sprach_rms_db(x, sr):
    e, r, _ = rahmen(x, sr)
    if e.size == 0:
        return rms_db(x)
    m = sprach_maske_env(e)
    if m.sum() < 5:
        return rms_db(x)
    return float(20 * np.log10(np.sqrt((r[m].astype(np.float64) ** 2).mean()) + 1e-12))


def pausen_aus_maske(m, rahmen_s, min_s=0.25):
    """Startzeit und Laenge aller Pausen ab min_s, aus einer Rahmenmaske."""
    if m.size == 0:
        return []
    d = np.diff(np.concatenate([[True], m, [True]]).astype(np.int8))
    starts = np.flatnonzero(d == -1)
    enden = np.flatnonzero(d == 1)
    lang = (enden - starts) * rahmen_s >= min_s
    return [(float(s * rahmen_s), float((e - s) * rahmen_s))
            for s, e in zip(starts[lang], enden[lang])]


def pausen(x, sr, schwelle=SCHWELLE_FAKTOR, min_s=0.25):
    e, _, _ = rahmen(x, sr)
    return pausen_aus_maske(sprach_maske_env(e, schwelle), RAHMEN_S, min_s)


def ffprobe(datei, feld="format=duration"):
    r = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", feld,
         "-of", "default=nw=1:nk=1", datei],
        capture_output=True, text=True, check=True)
    return r.stdout.strip()


def dauer_s(datei):
    return float(ffprobe(datei))


def hms(sekunden):
    s = int(round(sekunden))
    return f"{s // 3600}:{(s % 3600) // 60:02d}:{s % 60:02d}"


# ----------------------------------------------------------------- Gates
#
# Bis 2026-08-31 haben die Pipeline-Schritte ihre Gate-Verstoesse GEDRUCKT
# und trotzdem 0 zurueckgegeben. workflow-gates.md behauptete zu 1.1 und
# 1.11 das Gegenteil ("beide brechen die Pipeline hart ab, wenn sie
# reissen") - der Lauf ging danach durch den bezahlten TTS-Schritt und die
# Montage weiter. Das war die teuerste Sorte Fehler: eine Pruefung, die
# nichts prueft, kostet mehr als gar keine, weil sich niemand mehr hinsetzt
# und selbst nachsieht.
#
# Seither sammelt jeder Schritt seine Gates hier ein und ruft am Ende
# gate_abschluss(). Rueckgabewert 1 bei Verstoss, 0 sonst.
#
# --force uebergeht den Abbruch. Bewusst umstaendlich: der Schalter muss
# ausdruecklich gesetzt werden, die Warnung steht trotzdem im Protokoll,
# und der Verstoss steht so oder so in der Messdatei des Schritts.

class Gates:
    """Sammelt Gate-Ergebnisse eines Schritts.

    pruefen() nimmt den ausgewerteten Wahrheitswert entgegen, nicht die
    Bedingung als Text - die Auswertung gehoert dorthin, wo die Zahlen
    liegen, und wird nicht ein zweites Mal formuliert.
    """

    def __init__(self, force=False):
        self.force = bool(force)
        self.verstoesse = []

    def pruefen(self, nummer, name, ok, meldung):
        """nummer: '1.1' oder '' fuer Pruefungen ohne Gate-Nummer."""
        if not ok:
            self.verstoesse.append((nummer, name, meldung))
        return bool(ok)

    def __bool__(self):
        return not self.verstoesse


def gate_abschluss(g, schritt):
    """Druckt das Ergebnis und liefert den Rueckgabewert des Schritts."""
    if not g.verstoesse:
        return 0
    print(f"\n{'=' * 66}")
    print(f"GATE-VERSTOSS in {schritt} — {len(g.verstoesse)} Pruefung(en) gerissen")
    print("=" * 66)
    for nummer, name, meldung in g.verstoesse:
        kopf = f"{nummer} {name}" if nummer else name
        print(f"  {kopf}: {meldung}")
    if g.force:
        print("\n  --force gesetzt: der Lauf geht WEITER, obwohl die Pruefung reisst.")
        print("  Der Verstoss steht in der Messdatei dieses Schritts und im Protokoll.")
        print("  Wer so ausliefert, liefert wissentlich gegen die eigene Regel aus.")
        return 0
    print("\n  Die Pipeline haelt hier an. Ursache beheben — oder, wenn der")
    print("  Verstoss bewusst in Kauf genommen wird, den Schritt mit --force")
    print("  erneut aufrufen. Grenzen werden nicht aufgeweicht, um durchzukommen.")
    return 1
