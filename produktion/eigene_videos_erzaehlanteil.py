#!/usr/bin/env python3
"""Rechnet den Erzaehlanteil der eigenen Videos V01-V05 nach - gegen die Korpora,
die in produktion/korpus/plan.json stehen.

Regel, Messmethode und die Selbstpruefung der Teilungen kommen unveraendert aus
produktion/erzaehlanteil.py; diese Datei importiert sie und liefert nur die
Kapiteltabelle fuer die Buecher, die V01-V05 verbrauchen und die im
V06-Vorrat nicht vorkommen. erzaehlanteil.py selbst wird nicht angefasst.

Ergebnis: produktion/korpus/eigene_videos_erzaehlanteil.json

Das ist eine Messung, keine Bewertung. Ob ein Video das 80-%-Gate aus Regel M8
haelt, wird ausgewiesen - die Regel wird daran nicht angepasst.
"""
import json, os, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
import erzaehlanteil as ea  # noqa: E402

PLAN = "produktion/korpus/plan.json"
AUS = "produktion/korpus/eigene_videos_erzaehlanteil.json"
# Gattungen, die die Regel ausdruecklich nennt: das ganze Buch faellt darunter,
# deshalb je Buch eine Begruendung statt einer je Kapitel.
KATEGORISCH = {
    "psalms": (150,
        "Lied und Gebet ueber das ganze Buch; auch die Geschichtspsalmen (78, 105, 106, 135, "
        "136) erzaehlen im Lied, nicht in Handlung."),
    "proverbs": (31,
        "Spruchweisheit und Lehrrede; kein Handlungstraeger, kein Ortswechsel."),
    "ecclesiastes": (12,
        "Lehrrede in der Ichform; der Rueckblick auf Bauten und Besitz (Kap. 1-2) ist Bilanz, "
        "keine fortlaufende Handlung."),
    "1 peter": (5,
        "Brief."),
    "james": (5,
        "Brief."),
    "hebrews": (13,
        "Brief; auch der Glaubenszeugen-Katalog Kap. 11 bleibt Aufzaehlung im Brief, keine "
        "Szene."),
    "1 john": (5,
        "Brief."),
    "colossians": (4,
        "Brief."),
    "ephesians": (6,
        "Brief."),
    "philippians": (4,
        "Brief."),
}

# Kapitelweise eingestuft: (erzaehlend, teilung, begruendung).
# teilung = (erzaehlende Versbereiche, nicht erzaehlende Versbereiche) oder None.
GEMISCHT = {
    "john": {
        1: (False, (["19-51"], ["1-18"]),
            "Der Prolog V.1-18 ist theologischer Hymnus ohne Akteur, Ort und Zeit; ab V.19 ('This "
            "is John's testimony') laeuft die Szene mit Gesandtschaft, Taufe und Juengerberufung."),
        2: (True, None,
            "Hochzeit zu Kana und Tempelreinigung - zwei Szenen mit Ortswechsel Kana/Jerusalem und "
            "Zeitverlauf."),
        3: (False, (["1-2", "22-30"], ["3-21", "31-36"]),
            "Nikodemus kommt bei Nacht (V.1-2) und der Taeufer-Abschnitt in Judaea (V.22-30) sind "
            "Szene; die Belehrung V.3-21 und das Zeugnis V.31-36 sind geschlossene Rede ohne "
            "Handlungsfortschritt und tragen die Wortmehrheit."),
        4: (True, None,
            "Reise Judaea-Samaria-Galilaea mit Brunnengespraech, Juengern, Samaritern und der "
            "Heilung des Beamtensohns - durchgehend Ortswechsel und Zeitverlauf."),
        5: (False, (["1-18"], ["19-47"]),
            "Heilung am Teich Bethesda und Sabbatkonflikt V.1-18 sind Szene; die Rede V.19-47 (602 "
            "von 980 Woertern) laeuft ohne Handlung weiter."),
        6: (True, (["1-25", "60-71"], ["26-59"]),
            "Speisung, Seewandel und Ueberfahrt V.1-25 sowie die Abkehr der Juenger und das "
            "Petrusbekenntnis V.60-71 sind Handlung; die Brotrede V.26-59 samt Ortsnotiz V.59 ist "
            "Lehrrede."),
        7: (True, (["1-15", "25-53"], ["16-24"]),
            "Laubhuettenfest als laufende Szene mit Bruedern, Suchen, ausgesandten Haeschern und "
            "Nikodemus; herausgeloest nur der Lehrblock V.16-24."),
        8: (False, (["1-11", "59"], ["12-58"]),
            "Die Ehebrecherin V.1-11 und der Steinigungsversuch V.59 sind Szene; der Streit V.12-58 "
            "ist Kontroversrede ohne Handlungsfortschritt und traegt die Mehrheit."),
        9: (True, None,
            "Blindgeborener: Heilung, dreifaches Verhoer, Ausschluss aus der Synagoge und "
            "Wiederbegegnung - fortlaufende Handlung mit Akteuren."),
        10: (False, (["19-42"], ["1-18"]),
            "Die Hirtenrede V.1-18 ist geschlossene Bildrede; ab V.19 ('a division arose again') "
            "laufen Spaltung, Tempelweihfest, Steinigungsversuch und Rueckzug an den Jordan."),
        11: (True, None,
            "Auferweckung des Lazarus: Botschaft, Reise nach Bethanien, Grabszene und der Beschluss "
            "des Hohen Rates."),
        12: (True, (["1-22"], ["23-50"]),
            "Salbung in Bethanien, Einzug in Jerusalem und die Griechen bei Philippus V.1-22 sind "
            "Handlung; ab V.23 Rede, Erzaehlerkommentar mit Jesaja-Zitaten und Schlussrede."),
        13: (True, (["1-30"], ["31-38"]),
            "Fusswaschung und Verraeteransage V.1-30 sind Szene mit Zeitverlauf; ab V.31 beginnt "
            "die Abschiedsrede."),
        14: (False, None,
            "Abschiedsrede in voller Laenge; kein Akteur ausser dem Sprechenden, kein Ortswechsel."),
        15: (False, None,
            "Abschiedsrede (Weinstock, Freundschaft, Hass der Welt) - 100 Prozent Rede."),
        16: (False, None,
            "Abschiedsrede ueber den Beistand und die Wiedersehensfreude."),
        17: (False, None,
            "Hohepriesterliches Gebet - eingelegtes Gebet ueber das ganze Kapitel."),
        18: (True, None,
            "Gefangennahme im Garten, Verhoer bei Hannas und Kaiaphas, Petrusverleugnung und "
            "Prozess vor Pilatus."),
        19: (True, None,
            "Geisselung, Kreuzigung, Tod und Grablegung - durchgehende Handlung mit Ortswechsel."),
        20: (True, None,
            "Leeres Grab, Maria Magdalena, die Juenger hinter verschlossenen Tueren und Thomas - "
            "Szenenfolge mit Zeitverlauf."),
        21: (True, None,
            "Fischzug am See Tiberias, Mahl am Kohlenfeuer und die Wiedereinsetzung des Petrus."),
    },
    "matthew": {
        1: (False, (["18-25"], ["1-17"]),
            "V.1-17 ist der Stammbaum von Abraham bis Josef; erst V.18 setzt mit Josefs Traum und "
            "der Geburt eine Szene ein."),
        2: (True, None,
            "Magier aus dem Osten, Flucht nach Aegypten, Kindermord und Rueckkehr nach Nazareth - "
            "Ortswechsel und Zeitverlauf."),
        3: (True, (["1-7", "13-17"], ["8-12"]),
            "Auftreten des Taeufers und die Taufe Jesu sind Szene; die Busspredigt V.8-12 (127 von "
            "377 Woertern) ist Verkuendigungsrede."),
        4: (True, None,
            "Versuchung in der Wueste mit dreifachem Ortswechsel, Rueckzug nach Kapernaum und "
            "Berufung der ersten Juenger."),
        5: (False, None,
            "Bergpredigt, erster Teil - 97 Prozent zusammenhaengende Rede."),
        6: (False, None,
            "Bergpredigt, zweiter Teil - 100 Prozent Rede."),
        7: (False, None,
            "Bergpredigt, Schluss; nur die Reaktionsnotiz V.28-29 waere Handlung, zu klein fuer "
            "eine eigene Naht."),
        8: (True, None,
            "Aussaetziger, Hauptmann von Kapernaum, Sturmstillung und die Gadarener - vier Szenen "
            "mit Ortswechsel."),
        9: (True, None,
            "Gelaehmter, Berufung des Matthaeus, Jairus, blutfluessige Frau, Blinde und Stummer - "
            "dichte Szenenfolge."),
        10: (False, None,
            "Aussendungsrede - 88 Prozent Rede, die Aussendung selbst nur zwei Verse."),
        11: (False, (["1-7", "20"], ["8-19", "21-30"]),
            "Nur die Anfrage des Taeufers V.1-7 und die Ueberleitung V.20 sind Szene; die Rede "
            "ueber Johannes V.8-19 und die Weherufe samt Heilandsruf V.21-30 tragen 486 von 642 "
            "Woertern."),
        12: (True, (["1-14", "46-50"], ["15-45"]),
            "Aehrenraufen, Heilung am Sabbat und der Beschluss der Pharisaeer V.1-14 sowie Mutter "
            "und Brueder V.46-50 sind Handlung; dazwischen Jesaja-Zitat und Beelzebul-Streitrede."),
        13: (False, (["53-58"], ["1-52"]),
            "Gleichnisrede vom Saemann bis zum Fischnetz; erst V.53-58 (Verwerfung in Nazareth) ist "
            "wieder Szene."),
        14: (True, None,
            "Tod des Taeufers, Speisung der Fuenftausend und der Seewandel - Handlung mit "
            "Ortswechsel."),
        15: (True, None,
            "Streit um die Ueberlieferung, die kanaanaeische Frau und die Speisung der Viertausend; "
            "die Rede bleibt Wechselrede in laufender Szene."),
        16: (True, None,
            "Zeichenforderung, Ueberfahrt, Petrusbekenntnis bei Caesarea Philippi und die erste "
            "Leidensansage mit Petrusschelte."),
        17: (True, None,
            "Verklaerung auf dem Berg, Heilung des fallsuechtigen Knaben und die Tempelsteuer im "
            "Fischmaul."),
        18: (False, None,
            "Gemeinderede ueber das Kind, das verlorene Schaf, die Zurechtweisung und den "
            "unbarmherzigen Knecht - 91 Prozent Rede."),
        19: (True, None,
            "Aufbruch nach Judaea, Streitgespraech ueber die Ehescheidung, Segnung der Kinder und "
            "der reiche Juengling, der weggeht."),
        20: (True, (["17-34"], ["1-16"]),
            "Das Gleichnis von den Arbeitern im Weinberg V.1-16 ist geschlossene Bildrede; ab V.17 "
            "laufen Aufstieg nach Jerusalem, Zebedaeussoehne und die Blinden von Jericho."),
        21: (True, (["1-27", "45-46"], ["28-44"]),
            "Einzug, Tempelreinigung, verdorrter Feigenbaum und Vollmachtsfrage V.1-27 sowie die "
            "Reaktion V.45-46 sind Handlung; die beiden Gleichnisse V.28-44 sind Rede."),
        22: (True, (["15-46"], ["1-14"]),
            "Das Gleichnis vom Hochzeitsmahl V.1-14 ist Bildrede; ab V.15 kommen Pharisaeer, "
            "Herodianer und Sadduzaeer nacheinander und werden abgewiesen."),
        23: (False, None,
            "Weherufe gegen Schriftgelehrte und Pharisaeer - 99 Prozent Rede."),
        24: (False, None,
            "Endzeitrede auf dem Oelberg - 90 Prozent Rede."),
        25: (False, None,
            "Gleichnisse von den Jungfrauen, den Talenten und dem Weltgericht - 100 Prozent Rede."),
        26: (True, None,
            "Salbung in Bethanien, Passamahl, Gethsemane, Gefangennahme, Verhoer und "
            "Petrusverleugnung."),
        27: (True, None,
            "Auslieferung an Pilatus, Judas' Ende, Kreuzigung, Tod und Grabwache."),
        28: (True, None,
            "Frauen am leeren Grab, Engel, Begegnung mit dem Auferstandenen und die Wache am Grab."),
    },
    "luke": {
        1: (True, (["5-45", "56-66", "80"], ["1-4", "46-55", "67-79"]),
            "Zacharias im Tempel, Verkuendigung und Heimsuchung sowie Geburt und Beschneidung des "
            "Taeufers sind Szene; herausgeloest Widmungsvorrede V.1-4, Magnificat V.46-55 und "
            "Benedictus V.67-79."),
        2: (True, (["1-28", "33-52"], ["29-32"]),
            "Schaetzung, Geburt, Hirten, Darstellung im Tempel und der zwoelfjaehrige Jesus sind "
            "durchgehend Handlung; nur der Lobgesang des Simeon V.29-32 ist eingelegtes Lied."),
        3: (False, (["1-2", "19-22"], ["3-18", "23-38"]),
            "Nur die Datierung V.1-2 sowie Herodes' Zugriff und die Taufe V.19-22 sind Szene; die "
            "Busspredigt V.3-18 ist Verkuendigung, V.23-38 der Stammbaum rueckwaerts bis Adam."),
        4: (True, None,
            "Versuchung, Verwerfung in Nazareth mit Fluchtversuch der Menge, Kapernaum und die "
            "Wanderung durch Judaea - Ortswechsel und Zeitverlauf."),
        5: (True, None,
            "Fischzug und Berufung, Aussaetziger, Gelaehmter durchs Dach, Berufung des Levi und die "
            "Fastenfrage."),
        6: (True, (["1-19"], ["20-49"]),
            "Aehrenraufen, Heilung der verdorrten Hand, Wahl der Zwoelf und der Zulauf V.1-19 sind "
            "Handlung; die Feldrede V.20-49 ist geschlossene Lehrrede."),
        7: (True, None,
            "Hauptmann von Kapernaum, Jungling zu Nain, die Anfrage des Taeufers und die Suenderin "
            "im Haus des Pharisaeers."),
        8: (True, (["1-4", "19-56"], ["5-18"]),
            "Die begleitenden Frauen V.1-4 und der Block Mutter/Brueder, Sturmstillung, Gerasener, "
            "Jairus V.19-56 sind Handlung; das Saemanngleichnis mit Deutung V.5-18 ist Rede."),
        9: (True, None,
            "Aussendung der Zwoelf, Speisung, Bekenntnis, Verklaerung, der fallsuechtige Knabe und "
            "der Aufbruch nach Jerusalem."),
        10: (False, (["1", "17-29", "37-42"], ["2-16", "30-36"]),
            "Aussendungsrede V.2-16 und das Samaritergleichnis V.30-36 sind Rede; Szene bleiben die "
            "Aussendung V.1, die Rueckkehr der Siebzig mit der Gesetzeslehrerfrage V.17-29 und "
            "Marta und Maria V.37-42."),
        11: (False, None,
            "Vaterunser, Beelzebulstreit, Zeichenforderung und Weherufe - 78 Prozent geschlossene "
            "Rede; die Szenenreste (V.14, V.37-38, V.53-54) liegen zu verstreut fuer eine saubere "
            "Naht."),
        12: (False, None,
            "Warnung vor Heuchelei, reicher Kornbauer, Sorgenrede, treuer Verwalter und Zeichen der "
            "Zeit - 88 Prozent Rede."),
        13: (False, (["10-17"], ["1-9", "18-35"]),
            "Nur die Heilung der gekruemmten Frau am Sabbat V.10-17 ist Szene; Bussruf und "
            "Feigenbaum V.1-9 sowie Senfkorn, enge Tuer und Herodeswort V.18-35 sind Rede."),
        14: (False, (["1-6"], ["7-35"]),
            "Nur die Sabbatheilung im Haus des Pharisaeers V.1-6 ist Szene; Ehrenplaetze, grosses "
            "Gastmahl und Nachfolgebedingungen V.7-35 sind Rede."),
        15: (False, None,
            "Verlorenes Schaf, verlorene Drachme und verlorener Sohn - 94 Prozent Gleichnisrede."),
        16: (False, None,
            "Ungerechter Verwalter und der reiche Mann mit Lazarus - 94 Prozent Rede."),
        17: (False, (["11-19"], ["1-10", "20-37"]),
            "Nur die zehn Aussaetzigen V.11-19 sind Szene mit Ortswechsel; Vergebungslehre V.1-10 "
            "und die Rede vom Kommen des Reiches V.20-37 sind Rede."),
        18: (True, (["15-43"], ["1-14"]),
            "Die Gleichnisse von der Witwe und vom Pharisaeer und Zoellner V.1-14 sind Rede; ab "
            "V.15 laufen Kindersegnung, reicher Oberer, Leidensansage und der Blinde von Jericho."),
        19: (True, (["1-11", "28-48"], ["12-27"]),
            "Zachaeus V.1-11 sowie Einzug, Weinen ueber Jerusalem und Tempelreinigung V.28-48 sind "
            "Handlung; das Mnengleichnis V.12-27 ist Bildrede."),
        20: (True, (["1-8", "19-47"], ["9-18"]),
            "Vollmachtsfrage V.1-8 und die Folge von Kundschaftern, Sadduzaeern und Davidsfrage "
            "V.19-47 sind Szene; das Winzergleichnis V.9-18 ist Bildrede."),
        21: (False, (["1-4", "37-38"], ["5-36"]),
            "Nur das Scherflein der Witwe V.1-4 und die Tagesordnungsnotiz V.37-38 sind Szene; die "
            "Endzeitrede V.5-36 traegt 606 von 764 Woertern."),
        22: (True, None,
            "Verrat des Judas, Passamahl, Oelberg, Gefangennahme, Petrusverleugnung und Verhoer vor "
            "dem Hohen Rat."),
        23: (True, None,
            "Prozess vor Pilatus und Herodes, Kreuzweg, Kreuzigung, Tod und Grablegung."),
        24: (True, None,
            "Frauen am Grab, Emmausgang mit Wiedererkennen beim Brotbrechen, Erscheinung vor den "
            "Elf und Abschied bei Bethanien."),
    },
    "daniel": {
        1: (True, None,
            "Wegfuehrung nach Babel, Auswahl der Knaben, die zehntaegige Probe mit Gemuese und der "
            "Dienstantritt vor dem Koenig - Zeitverlauf ueber drei Jahre."),
        2: (True, (["1-19", "24-26", "46-49"], ["20-23", "27-45"]),
            "Traum, Todesbefehl, Danielis Bitte, die naechtliche Offenbarung und die Erhoehung am "
            "Schluss sind Szene; herausgeloest der Lobpreis V.20-23 als eingelegtes Gebet und die "
            "Deutungsrede V.27-45 (583 Woerter)."),
        3: (True, None,
            "Goldbild in der Ebene Dura, Anklage, Feuerofen, die vierte Gestalt im Feuer und die "
            "Erhoehung der drei - fortlaufende Handlung; die Beamten- und Instrumentenlisten stehen "
            "im Erzaehlfluss."),
    },
}


def tabelle_bauen():
    """Kategorische Buecher ausrollen und mit den kapitelweise eingestuften mischen."""
    t = {}
    for buch, (n, grund) in KATEGORISCH.items():
        t[buch] = {i: (False, None, grund) for i in range(1, n + 1)}
    for buch, kapitel in GEMISCHT.items():
        t[buch] = dict(kapitel)
    return t


def main():
    # Regel und Messlogik aus erzaehlanteil.py, nur mit anderer Kapiteltabelle.
    ea.EINSTUFUNG = tabelle_bauen()
    kapitel, verworfen = ea.einstufung_rechnen()
    if verworfen:
        print("Verworfene Teilungen (konservativ als nicht erzaehlend gezaehlt):")
        for z in verworfen:
            print("  " + z)
        print()

    plan = json.load(open(PLAN))
    videos = []
    for kuerzel in ("V1", "V2", "V3", "V4", "V5"):
        v = plan[kuerzel]
        fehlend = [r for r in v["refs"] if r not in kapitel]
        if fehlend:
            raise SystemExit("nicht eingestuft: %s" % ", ".join(fehlend[:5]))
        woerter = sum(kapitel[r]["woerter"] for r in v["refs"])
        erz = sum(kapitel[r]["erzaehlend_woerter"] for r in v["refs"])
        pro_buch = {}
        for r in v["refs"]:
            b = kapitel[r]["buch"]
            pro_buch.setdefault(b, {"woerter": 0, "erzaehlend_woerter": 0, "kapitel": 0})
            pro_buch[b]["woerter"] += kapitel[r]["woerter"]
            pro_buch[b]["erzaehlend_woerter"] += kapitel[r]["erzaehlend_woerter"]
            pro_buch[b]["kapitel"] += 1
        for b in pro_buch:
            pro_buch[b]["erzaehlanteil"] = round(
                pro_buch[b]["erzaehlend_woerter"] / pro_buch[b]["woerter"], 4)
        videos.append({
            "video": kuerzel,
            "name": v["name"],
            "woerter_korpus": woerter,
            "erzaehlend_woerter": erz,
            "erzaehlanteil": round(erz / woerter, 4),
            "haelt_gate_m8": erz / woerter >= ea.GATE_ERZAEHLEND,
            "je_buch": pro_buch,
        })

    json.dump({
        "zweck": ("Nachrechnung des Erzaehlanteils der bereits geplanten und "
                  "teils gerenderten Videos V01-V05. Messung, keine Bewertung."),
        "regel": ea.REGEL,
        "quelle": "bible-api.com, translation=webbe",
        "zaehlmethode": "Verstexte mit Leerzeichen verbunden, dann str.split()",
        "hinweis_flagge": ("Bei geteilten Kapiteln ist 'erzaehlend' nur ein Etikett; "
                           "massgeblich ist 'erzaehlend_woerter' aus den gemessenen "
                           "Versbereichen."),
        "hinweis_korpus": ("Gezaehlt ist der Bibelkorpus aus plan.json. Eingangsgebet, "
                           "Hook und CTA sind nicht enthalten - sie stehen in keiner "
                           "der beiden Kategorien der Regel."),
        "gate_erzaehlanteil": ea.GATE_ERZAEHLEND,
        "videos": videos,
        "kapitel": kapitel,
    }, open(AUS, "w"), ensure_ascii=False, indent=1)

    print("%-4s %-46s %8s %9s %9s  %s" % ("", "Korpus", "Woerter", "erzaehl.", "Anteil", "Regel M8"))
    for v in videos:
        print("%-4s %-46s %8s %9s %8.1f%%  %s"
              % (v["video"], v["name"][:46], "{:,}".format(v["woerter_korpus"]),
                 "{:,}".format(v["erzaehlend_woerter"]), v["erzaehlanteil"] * 100,
                 "haelt" if v["haelt_gate_m8"] else "REISST"))
    print("\n(Gate: Erzaehlanteil >= %d %% der Woerter)" % (ea.GATE_ERZAEHLEND * 100))
    for v in videos:
        print("\n%s - %s" % (v["video"], v["name"]))
        for b, d in sorted(v["je_buch"].items(), key=lambda x: -x[1]["woerter"]):
            print("   %-14s %2d Kap %7s W  erzaehlend %6s W (%5.1f %%)"
                  % (b, d["kapitel"], "{:,}".format(d["woerter"]),
                     "{:,}".format(d["erzaehlend_woerter"]), d["erzaehlanteil"] * 100))
    return 0


if __name__ == "__main__":
    sys.exit(main())
