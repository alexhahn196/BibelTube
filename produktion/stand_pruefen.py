#!/usr/bin/env python3
"""Prueft die Invarianten des zusammengefuehrten Stands.

Am 2026-09-02 sind zwei Zweige vereinigt worden. Vorher fuehrten fuenfzehn
Dateien zwei Inhalte, und dieselbe Groesse hatte an zwei Stellen zwei Werte:
zwei Sprechtempi, zwei Bandrechnungen, zwei Fassungen von Gate 1.13, zwei
Klangbetten unter einem Dateinamen. Dieses Skript haelt fest, dass es dabei
bleibt, dass es EINEN Stand gibt.

Es prueft keine Regel und aendert nichts. Es prueft, ob zwei Werkzeuge, die
dieselbe Groesse berechnen, dasselbe herausbekommen.

Rueckgabewert 0 = alle Invarianten halten. Jeder andere Wert heisst, dass der
Stand wieder auseinanderlaeuft.

Aufruf:  python3 produktion/stand_pruefen.py
"""
import importlib.util
import json
import os
import subprocess
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
sys.path.insert(0, os.path.join(HIER, "pipeline"))


def _laden(name, datei):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HIER, datei))
    modul = importlib.util.module_from_spec(spec)
    sys.modules[name] = modul
    spec.loader.exec_module(modul)
    return modul


def main():
    from gemeinsam import config
    import soundfile as sf

    cfg = config()
    kp = _laden("korpus_pruefung", "korpus_pruefung.py")
    ea = _laden("erzaehlanteil", "erzaehlanteil.py")

    fehler = []

    def pruef(name, bedingung, info=""):
        print(("  OK    " if bedingung else "  FEHLT ") + name + ("   " + info if info else ""))
        if not bedingung:
            fehler.append(name)

    print("Invarianten des Stands\n")
    print(" Sprechtempo und Bandrechnung")
    pruef("beide Werkzeuge lesen dasselbe WPM", kp.WPM == ea.WPM, "%s / %s" % (kp.WPM, ea.WPM))
    pruef("Zielband identisch", kp.band_fuer(45, False) == ea.band(False),
          "%s / %s" % (kp.band_fuer(45, False), ea.band(False)))
    pruef("tieferes Band identisch", kp.band_fuer(45, True) == ea.band(True),
          "%s / %s" % (kp.band_fuer(45, True), ea.band(True)))
    pruef("Band haengt nicht an der Kapitelzahl", kp.band_fuer(30) == kp.band_fuer(80))

    print("\n Gate-1.13-Schwellen - eine Quelle (config.md)")
    pruef("Dominanz", kp.DOMINANZ_MIN == ea.GATE_DOMINANZ == float(cfg["gate_dominanz_min"]))
    pruef("Erzaehlwerk", kp.ERZAEHLWERK_MIN == ea.GATE_ERZAEHLEND == float(cfg["gate_erzaehlanteil_min"]))
    pruef("Abstand", kp.ABSTAND_MIN == ea.GATE_ABSTAND == float(cfg["gate_abstand_min"]))

    print("\n Gate 1.13 - beide Werkzeuge urteilen gleich")
    kapstd = json.load(open(os.path.join(HIER, "korpus", "kapitel.json"), encoding="utf-8"))
    feinstd = kp.fein_lesen()
    moegl = json.load(open(os.path.join(HIER, "korpus", "v07_v08_moeglichkeiten.json"),
                           encoding="utf-8"))
    planstd = json.load(open(os.path.join(HIER, "korpus", "plan.json"), encoding="utf-8"))
    for video, pf in sorted(moegl["planfassungen"].items()):
        kapitel = [(r.rsplit(" ", 1)[0], int(r.rsplit(" ", 1)[1]))
                   for r in planstd[video]["refs"]]
        teile = []
        for buch in dict.fromkeys(b for b, _ in kapitel):
            ii = sorted(i for b, i in kapitel if b == buch)
            voll = kp.buchlaenge(kapstd, buch)
            teile.append({"spec": buch, "buch": buch, "von": ii[0], "bis": ii[-1],
                          "kapitel_gelesen": ii, "ganzes_buch": ii == list(range(1, voll + 1)),
                          "woerter": sum(kapstd["%s %d" % (buch, i)]["w"] for i in ii),
                          "erzaehlung": 0})
        r = kp.zusammenfassen(teile, kapitel, kapstd, feinstd)
        zweiter = r["zweiter"]
        werte = (round(r["groesster"]["woerter"] / r["woerter"], 4),
                 round(r["erz_anteil_dominant"], 4),
                 r["groesster"]["ganzes_buch"],
                 round((r["groesster"]["woerter"] - (zweiter["woerter"] if zweiter else 0))
                       / r["woerter"], 4))
        soll = (pf["dominanz"], pf["vollwerk"]["erzaehlanteil_des_buches"],
                pf["vollwerk"]["volle_laenge"], pf["abstand"])
        pruef("%s: Dominanz, Erzaehlwerk, Vollstaendigkeit, Abstand" % video,
              werte == soll, "%s / %s" % (werte, soll))

    print("\n Erzaehlanteil - eine Zahl aus einer Datei")
    kap = json.load(open(os.path.join(HIER, "korpus", "kapitel.json"), encoding="utf-8"))
    fein = kp.fein_lesen()
    plan = json.load(open(os.path.join(HIER, "korpus", "plan.json"), encoding="utf-8"))
    refs = [(r.rsplit(" ", 1)[0], int(r.rsplit(" ", 1)[1])) for r in plan["V6"]["refs"]]
    aus_kp, _ = kp.fein_anteil(refs, kap, fein)
    varianten = json.load(open(os.path.join(HIER, "korpus", "v06_varianten.json"), encoding="utf-8"))
    aus_ea = [v for v in varianten["varianten"] if v["kuerzel"] == "V06-A"][0]["erzaehlanteil"] * 100
    pruef("V06 in beiden Werkzeugen gleich", round(aus_kp, 1) == round(aus_ea, 1),
          "%.1f %% / %.1f %%" % (aus_kp, aus_ea))

    print("\n Klangbett - ein Bett, ein Name")
    bett, _ = sf.read(os.path.join(HIER, "..", cfg["bett_datei"]))
    pruef("Produktionsbett ist einkanalig", bett.ndim == 1, str(bett.shape))
    verworfen = os.path.join(HIER, "klang", "verworfen_bett_mono_variante_e.flac")
    pruef("verworfene Variante liegt unter eigenem Namen", os.path.exists(verworfen))
    # --exclude: dieses Skript nennt das Muster selbst und wuerde sich sonst finden.
    treffer = subprocess.run(
        ["grep", "-rn", "sf.write.*bett_mono_feuer_leise", "--include=*.py",
         "--exclude=stand_pruefen.py", "."],
        capture_output=True, text=True, cwd=os.path.join(HIER, "..")).stdout
    pruef("kein Skript schreibt das Produktionsbett", treffer == "", treffer.strip()[:80])

    print("\n Titel - Dokument und Auslieferung stimmen ueberein")
    titel = {t["nr"]: t["titel"] for t in json.load(
        open(os.path.join(HIER, "eigene_titel.json"), encoding="utf-8"))}
    for nr in sorted(titel):
        datei = os.path.join(HIER, "video-%02d" % int(nr[1:]), "titel.txt")
        if not os.path.exists(datei):
            continue
        geliefert = open(datei, encoding="utf-8").read().strip()
        pruef("%s wie ausgeliefert" % nr, titel[nr] == geliefert, geliefert[:44])

    print("\n%s" % ("Ein Stand." if not fehler
                    else "AUSEINANDERGELAUFEN: " + ", ".join(fehler)))
    return 1 if fehler else 0


if __name__ == "__main__":
    raise SystemExit(main())
