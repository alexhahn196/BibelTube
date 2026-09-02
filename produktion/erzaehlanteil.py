#!/usr/bin/env python3
"""Stuft den verfuegbaren WEBBE-Erzaehlstoff kapitelweise ein und rechnet die
drei V06-Korpusvarianten gegen Regel M8 durch.

Erzeugt:
  produktion/korpus/erzaehlanteil.json   Einstufung je Kapitel
  produktion/korpus/v06_varianten.json   die drei Varianten mit allen Zahlen

Rueckgabewert 0 bedeutet: alle drei Varianten bestehen Zielband, Erzaehlanteil
und Dominanz. Jeder andere Wert heisst, dass mindestens eine reisst.

Sprechtempo, Zielband und die beiden Gate-Schwellen kommen vollstaendig aus
produktion/config.md (wpm_erwartet, laufzeit_ziel_von_h[_vollwerk],
laufzeit_ziel_bis_h, gate_erzaehlanteil_min, gate_dominanz_min). In dieser Datei
steht keine Schwelle als Literal. Das Sprechtempo ist in
produktion/korpus/wpm_gemessen.json gemessen; bis 2026-08-30 stand hier fest
148,1 WPM aus der V06-Vorgabe, ein unbelegter Wert.

Der Rueckgabewert ist seit 2026-08-30 eine 1: Variante V06-C liegt mit 33.460 W
ueber der oberen Bandgrenze. Das ist der erwartete Stand, kein Defekt - gewaehlt
und gebaut ist Variante A.

Gate 1.13 ist seit dem 2026-09-02 die STRUKTURFASSUNG (Entscheidung des
Kanalinhabers bei der Zusammenfuehrung der beiden Zweige). Geprueft wird:

    dominantes Buch >= gate_dominanz_min der Woerter
    UND dieses Buch ist selbst Erzaehlwerk (>= gate_erzaehlanteil_min,
        kapitelweise gemessen)
    UND es steht in voller Laenge im Korpus
    UND es liegt >= gate_abstand_min vor dem zweitgroessten Buch

Der Erzaehlanteil des GESAMTEN Korpus wird weiter kapitelweise gemessen und in
jedem Ergebnis GEMELDET - er gatet nicht mehr. Grund: die 80 % sind von keiner
eigenen Messung beruehrt (V01-V05 liegen bei 0,0-47,6 %), und V03, das einzige
Video des Kanals, das funktioniert hat, faellt in jeder Koernung durch. Belegt
ist die Struktur, nicht der Prozentwert. Ausfuehrlich in
produktion/workflow-gates.md.

Ebenfalls am 2026-09-02: Dominanz von 60 auf 50 % gesenkt, untere Bandgrenze von
3,4 auf 3,0 h fuer den Fall, dass das dominante Buch selbst Erzaehlwerk ist und
in voller Laenge im Korpus steht (vollwerk_pruefen), und der Mindestabstand zum
zweitgroessten Buch neu eingefuehrt.

Wortzahlen kommen aus derselben Quelle und mit derselben Zaehlmethode wie
produktion/wortzahlen.py (bible-api.com, translation=webbe, Verstexte mit
Leerzeichen verbunden, dann str.split()), damit die Zahlen mit V01-V05
vergleichbar bleiben. Ganze Kapitel werden aus produktion/korpus/kapitel.json
wiederverwendet; Versbereiche geteilter Kapitel werden einmal geholt und in
produktion/korpus/kapitel_verse.json zwischengespeichert.
"""
import json, os, re, sys, time, urllib.parse, urllib.request

KAPITEL = "produktion/korpus/kapitel.json"
VERSE = "produktion/korpus/kapitel_verse.json"
AUS_EINSTUFUNG = "produktion/korpus/erzaehlanteil.json"
AUS_VARIANTEN = "produktion/korpus/v06_varianten.json"

def _config():
    """Sprechtempo und Zielband aus produktion/config.md - dort steht der einzige Wert."""
    text = open("produktion/config.md", encoding="utf-8").read()
    werte = {}
    for zeile in "\n".join(re.findall(r"```ini\n(.*?)```", text, re.S)).splitlines():
        zeile = zeile.split("#", 1)[0].strip()
        if "=" in zeile:
            k, v = zeile.split("=", 1)
            werte[k.strip()] = v.strip()
    gebraucht = ("wpm_erwartet", "laufzeit_ziel_von_h", "laufzeit_ziel_bis_h",
                 "laufzeit_ziel_von_h_vollwerk", "gate_erzaehlanteil_min",
                 "gate_dominanz_min", "gate_abstand_min")
    fehlt = [k for k in gebraucht if k not in werte]
    if fehlt:
        raise SystemExit("produktion/config.md: fehlende Werte %s" % fehlt)
    return tuple(float(werte[k]) for k in gebraucht)


# Alle sieben Zahlen kommen aus produktion/config.md. Hier steht keine einzige
# Schwelle als Literal - wer eine aendern will, aendert sie dort.
(WPM, ZIEL_VON_H, ZIEL_BIS_H, ZIEL_VON_H_VOLLWERK,
 GATE_ERZAEHLEND, GATE_DOMINANZ, GATE_ABSTAND) = _config()


def band(vollwerk=False):
    """Zielband in Woertern. Ist das dominante Buch ein Erzaehlwerk in voller
    Laenge, gilt die tiefere untere Grenze (laufzeit_ziel_von_h_vollwerk)."""
    von = ZIEL_VON_H_VOLLWERK if vollwerk else ZIEL_VON_H
    return (round(von * 60 * WPM), round(ZIEL_BIS_H * 60 * WPM))


BAND = band()                    # Regelfall 3,4-3,8 h
BAND_VOLLWERK = band(True)       # dominantes Buch ganz und Erzaehlwerk

REGEL = (
    "Erzaehlend = fortlaufende Handlung mit Akteuren, Ortswechsel und Zeitverlauf. "
    "Nicht erzaehlend = Gesetzestexte, Kult- und Bauvorschriften, Genealogien, "
    "eingelegte Lieder und Gebete, prophetische Rede, apokalyptische Vision, "
    "Briefe und Lehrreden. Direkte Rede innerhalb einer laufenden Szene (Dialog, "
    "Befehl, Botenwort) bleibt erzaehlend. Ein Kapitel, dessen Wortmehrheit aus "
    "zusammenhaengender Rede ohne Handlungsfortschritt besteht, ist nicht "
    "erzaehlend, es sei denn, der Bruch laesst sich sauber an Versgrenzen ziehen; "
    "dann werden beide Teile gemessen. Reine Regierungs- und Rahmenformeln mit "
    "Quellenverweis gelten als Chroniknotiz, nicht als Erzaehlung. "
    "Im Zweifel gegen den Erzaehlanteil."
)

# Einstufung je Kapitel: (erzaehlend, teilung, begruendung)
#   erzaehlend                -> bei geteilten Kapiteln nur ein Etikett und auf die
#                                gemessene Mehrheit gesetzt; gezaehlt werden die Bereiche
#   teilung = None            -> das ganze Kapitel zaehlt nach dem ersten Feld
#   teilung = (erz, nicht)    -> Listen von Versbereichen; gemessen wird, nicht
#                                geschaetzt. Deckt die Teilung das Kapitel nicht
#                                luecken- und ueberlappungsfrei ab (Probe: Summe
#                                der Teile == Kapitelwortzahl UND Summe der Verse
#                                == Kapitelverszahl), wird sie verworfen und das
#                                Kapitel konservativ als nicht erzaehlend gezaehlt.
def _gleichfoermig(von, bis, erzaehlend, begruendung):
    """Kapitelfolge mit einer einzigen Einstufung - fuer Buecher, die als Gattung
    durchgehend sind (Brief, apokalyptische Vision, Prophetenrede). Kein
    Ermessensspielraum je Kapitel: die Regel nennt diese Gattungen woertlich."""
    return {n: (erzaehlend, None, begruendung) for n in range(von, bis + 1)}


EINSTUFUNG = {
    "acts": {
        1: (True, (["1-23", "26"], ["24-25"]),
            "Nur V.24-25 (43 W., nachgezaehlt) faellt: woertlich eingelegtes Gebet, nach Regel 3 ohne "
            "Ermessen nicht erzaehlend und wie acts 4,24-30 zu behandeln; Petrus' Rede V.16-22 bleibt "
            "erzaehlend, weil sie als Beschlussrede die Loswahl V.23-26 unmittelbar ausloest, und der "
            "Prolog V.1-2 ist mit V.3 eine Satzperiode mit Handlungsreferat, keine reine "
            "Rahmenformel."),
        2: (False, (["1-13", "37-47"], ["14-36"]),
            "Pfingstereignis (V.1-13) und Taufe der Dreitausend (V.37-47) sind Handlung, aber Petrus' "
            "Pfingstpredigt V.14-36 traegt mit 533 von 972 Woertern die Mehrheit; sauber an "
            "Versgrenzen geteilt."),
        3: (False, (["1-11"], ["12-26"]),
            "Heilung des Lahmen am Tor Schoen (V.1-11, 241 Woerter) ist Handlung, Petrus' "
            "Tempelpredigt in Salomos Halle V.12-26 (381 Woerter) ist zusammenhaengende Rede und "
            "ueberwiegt."),
        4: (True, (["1-23", "31-37"], ["24-30"]),
            "Verhaftung und Verhoer vor dem Hohen Rat (V.1-23) sowie Guetergemeinschaft/Barnabas "
            "(V.31-37) sind Handlung; nur das eingelegte Gemeindegebet V.24-30 ist herausgeloest."),
        5: (True, None,
            "Hananias und Saphira, Zeichen der Apostel, Gefaengnisbefreiung und Verhoer; Gamaliels "
            "Rat (V.33-39, 193 von 965 Woertern) ist Wechselrede in der Ratssitzung und fuehrt zur "
            "Freilassung."),
        6: (True, None,
            "Streit der Hellenisten, Wahl der sieben Armenpfleger und Verhaftung des Stephanus - "
            "durchgehend Handlung mit Akteuren."),
        7: (False, (["54-60"], ["1-53"]),
            "V.1 ist nur die Redeeroeffnung des Hohepriesters ohne Handlung und gehoert zum "
            "Redeblock; die Stephanusrede V.1-53 (1215 von 1371 Woertern) dominiert, nur die "
            "Steinigung V.54-60 ist Szene."),
        8: (True, (["1-31", "34-40"], ["32-33"]),
            "V.32-33 (56 W., nachgezaehlt) sind ausdruecklich als gelesene Schriftstelle "
            "eingefuehrter Jesaja-Text - prophetische Rede ohne Akteur und Handlungsschritt, sauber "
            "an Versgrenzen, wie eingelegte Dokumente sonst auch herausgeloest."),
        9: (True, None,
            "Bekehrung des Saulus vor Damaskus, Ananias, Flucht im Korb, Heilung des Aeneas und "
            "Auferweckung der Tabitha - reine Szenenfolge."),
        10: (True, (["1-33", "44-48"], ["34-43"]),
            "Kornelius-Vision, Petrus' Tuchvision und Reise nach Caesarea (V.1-33) plus "
            "Geistausgiessung und Taufe (V.44-48) tragen 839 von 1058 Woertern; Petrus' Predigt "
            "V.34-43 ist abgetrennt."),
        11: (True, (["1-4", "18-30"], ["5-17"]),
            "V.4 ist noch Erzaehlerrahmen ('Petrus begann und legte es ihnen der Reihe nach dar'), "
            "die Rede setzt erst V.5 ein; Rahmen V.1-4 und Antiochia/Barnabas/Saulus/Agabus V.18-30 "
            "tragen 354 von 635 Woertern gegen 281 der Wiedererzaehlung V.5-17."),
        12: (True, None,
            "Hinrichtung des Jakobus, Petrus' Befreiung durch den Engel, Szene an Rhodes Tuer und Tod "
            "des Herodes - durchgehende Handlung."),
        13: (True, (["1-15", "42-52"], ["16-41"]),
            "Aussendung von Barnabas und Saulus, Elymas auf Zypern und Reisen (V.1-15) sowie Reaktion "
            "und Vertreibung aus Antiochia (V.42-52) ergeben 625 von 1190 Woertern gegen die "
            "Synagogenpredigt V.16-41."),
        14: (True, None,
            "Ikonion, Heilung des Lahmen in Lystra mit dem Zeus-Opfer, Steinigung des Paulus und "
            "Rueckreise; der Zuruf an die Menge (V.15-17) ist kurz und in der Szene."),
        15: (True, (["1-22", "30-41"], ["23-29"]),
            "Apostelkonzil als Versammlungsszene mit Wechselrede und Beschluss (V.1-22) und Trennung "
            "von Paulus und Barnabas (V.30-41) ueberwiegen deutlich; nur der Aposteldekret-Brief "
            "V.23-29 ist Briefe-Text."),
        16: (True, None,
            "Timotheus, der mazedonische Ruf, Lydia, die Wahrsagerin und das Erdbeben im Gefaengnis "
            "von Philippi - lauter Handlung mit Ortswechseln."),
        17: (True, (["1-21", "32-34"], ["22-31"]),
            "Thessalonich, Beroea und Ankunft in Athen (V.1-21) plus Reaktion der Hoerer (V.32-34) "
            "ergeben 553 von 824 Woertern; die Areopagrede V.22-31 ist abgetrennt."),
        18: (True, None,
            "Paulus bei Aquila und Priscilla in Korinth, Prozess vor Gallio, Reise nach Ephesus und "
            "Apollos - fortlaufende Handlung."),
        19: (True, None,
            "Johannesjuenger in Ephesus, Skevas' Soehne, Buecherverbrennung und Demetrius-Aufruhr; "
            "die Rede des Stadtschreibers (V.35-41, 164 von 926 Woertern) beendet den Auflauf "
            "innerhalb der Szene."),
        20: (True, (["1-17", "36-38"], ["18-35"]),
            "Reise durch Mazedonien, Eutychus in Troas und Fahrt nach Milet (V.1-17) plus Abschied am "
            "Strand (V.36-38) ergeben 447 von 852 Woertern gegen die Abschiedsrede an die Aeltesten "
            "V.18-35."),
        21: (True, None,
            "Seereise nach Tyrus und Caesarea, Agabus' Zeichenhandlung, Nasiraeergeluebde im Tempel "
            "und Verhaftung des Paulus - durchgehend Handlung."),
        22: (False, (["22-30"], ["1-21"]),
            "Paulus' Verteidigungsrede auf der Freitreppe mit dem Damaskusbericht (V.1-21) macht 485 "
            "von 729 Woertern aus; nur Tumult, Geisselung und Buergerrecht (V.22-30) sind Handlung."),
        23: (True, (["1-25", "31-35"], ["26-30"]),
            "Verhoer vor dem Synedrium, Spaltung von Pharisaeern und Sadduzaeern, Mordkomplott und "
            "Nachttransport nach Caesarea tragen das Kapitel; nur der Brief des Claudius Lysias "
            "V.26-30 ist herausgeloest."),
        24: (False, (["1", "9", "22-27"], ["2-8", "10-21"]),
            "V.1 (Ankunft nach fuenf Tagen) und V.9 (Zustimmung der Juden) sind echte "
            "Handlungsnotizen; Tertullus' Anklage V.2-8 (119 W.) und Paulus' Verteidigung V.10-21 "
            "(269 W.) machen 388 von 593 Woertern aus, Handlung nur V.1, 9, 22-27."),
        25: (True, (["1-13", "22-23"], ["14-21", "24-27"]),
            "Festus' Fallbericht an Agrippa V.14-21 (210 W.) wiederholt nur V.1-12 ohne "
            "Handlungsfortschritt, seine Eroeffnungsansprache V.24-27 (119 W.) ebenso; Handlung "
            "V.1-13 und V.22-23 traegt mit 389 von 718 Woertern die Mehrheit, Naht sauber an "
            "Versgrenzen."),
        26: (False, (["1", "24-32"], ["2-23"]),
            "V.1 ist Szene (Redeerlaubnis Agrippas, Paulus streckt die Hand aus), die "
            "Verteidigungsrede V.2-23 umfasst 542 von 751 Woertern; nur Wortwechsel mit "
            "Festus/Agrippa und Aufbruch V.24-32 sind Handlung."),
        27: (True, None,
            "Seefahrt nach Rom mit Sturm Euroklydon, Leichtern des Schiffes und Strandung vor Malta - "
            "reiner Reisebericht mit Zeitverlauf."),
        28: (True, (["1-25", "29-31"], ["26-28"]),
            "Malta, Heilungen, Fahrt nach Rom und Gespraech mit den Judenaeltesten sind durchlaufende "
            "Handlung (V.1-25, V.29-31); das Jesaja-Orakel samt Schlusswort V.26-28 (91 W.) ist "
            "prophetische Rede und wird nach Regel 3 sauber an Versgrenzen abgetrennt."),
    },
    "exodus": {
        1: (True, None,
            "Unterdrueckung Israels in Aegypten, Fronarbeit und die Szene mit den Hebammen Schiphra "
            "und Pua vor Pharao."),
        2: (True, None,
            "Geburt und Aussetzung des Mose, Totschlag des Aegypters, Flucht nach Midian und Heirat "
            "mit Zippora."),
        3: (True, None,
            "Szene am brennenden Dornbusch am Horeb mit Wechselrede zwischen Gott und Mose (Berufung, "
            "Namensoffenbarung)."),
        4: (True, None,
            "Zeichen mit Stab und aussaetziger Hand, Einsetzung Aarons, Rueckreise nach Aegypten und "
            "Zippora am Nachtlager."),
        5: (True, None,
            "Erste Audienz bei Pharao, Verschaerfung der Ziegelfron und Klage der israelitischen "
            "Aufseher."),
        6: (False, (["9-13", "28-30"], ["1-8", "14-27"]),
            "V.1-8 sind 237 Woerter geschlossene Gottesrede (Ankuendigung + Namensoffenbarung 'Ich "
            "bin JHWH') ohne Handlungsvollzug, V.14-27 sind 311 Woerter Geschlechterregister "
            "Ruben/Simeon/Levi; erzaehlend bleiben nur V.9-13 (Mose redet zum Volk, es hoert nicht, "
            "Sendung zu Pharao, Einwand) und die kurze Wiederaufnahmeszene V.28-30, zusammen 162 von "
            "710 Woertern."),
        7: (True, None,
            "Stab-Schlangen-Zeichen vor Pharao und die erste Plage, das Blutwasser des Nils, als "
            "fortlaufende Handlung."),
        8: (True, None,
            "Frosch-, Stechmuecken- und Fliegenplage mit Pharaos wiederholten Verhandlungen und "
            "Wortbruch."),
        9: (True, None,
            "Viehpest, Geschwuere und Hagelplage; Botenwort und Pharaos Suendenbekenntnis stehen in "
            "laufender Szene."),
        10: (True, None,
            "Heuschreckenplage und Finsternis, dazu die Verhandlungen mit Pharao bis zum Bruch mit "
            "Mose."),
        11: (True, None,
            "Ankuendigung der Erstgeburtsplage als Botenwort in der Konfrontationsszene, mit Moses "
            "zornigem Abgang von Pharao."),
        12: (False, (["28-41", "50-51"], ["1-27", "42-49"]),
            "Passa- und Mazzotvorschriften V.1-27 (831 W.) plus Passaordnung fuer Fremde V.42-49 (200 "
            "W., dabei ist V.42 selbst kultische Merkformel ohne Handlung) ueberwiegen klar; "
            "erzaehlend nur Erstgeburtsschlag, Vertreibung und Auszug V.28-41 sowie die Ausfuehrungs- "
            "und Auszugsnotiz V.50-51, zusammen 393 von 1424 Woertern."),
        13: (False, (["17-22"], ["1-16"]),
            "Erstgeburts- und Mazzotgebot samt Sohnesbelehrung (V. 1-16) traegt die Mehrheit; erst V. "
            "17-22 erzaehlt Aufbruch, Josefsgebeine und Wolken-/Feuersaeule."),
        14: (True, None,
            "Verfolgung durch Pharaos Streitwagen, Durchzug durchs Schilfmeer und Untergang des "
            "aegyptischen Heeres."),
        15: (False, (["19-27"], ["1-18"]),
            "Das eingelegte Meerlied des Mose (V. 1-18) ueberwiegt; erzaehlend sind Mirjams Reigen "
            "und der Zug nach Mara und Elim (V. 19-27)."),
        16: (True, None,
            "Murren in der Wueste Sin, Wachteln und Manna, Sabbatprobe am sechsten Tag - durchgehend "
            "Handlung mit Ortswechsel."),
        17: (True, None,
            "Wasser aus dem Felsen bei Massa und Meriba und die Schlacht gegen Amalek mit Moses "
            "erhobenen Haenden."),
        18: (True, None,
            "Besuch Jitros im Lager am Gottesberg, Opfermahl und die Einsetzung der Richter samt "
            "Ausfuehrung und Abschied."),
        19: (True, None,
            "Ankunft am Sinai, Heiligung des Volkes und die Theophanie mit Donner, Rauch und "
            "Posaunenschall."),
        20: (False, (["18-21"], ["1-17", "22-26"]),
            "Dekalog (V. 1-17) und Altargesetz (V. 22-26) ueberwiegen; erzaehlend ist nur die "
            "Furchtszene des Volkes am Berg (V. 18-21)."),
        21: (False, None,
            "Bundesbuch: Sklavenrecht, Koerperverletzung, Toetungsfaelle und Ersatzrecht fuer "
            "stoessige Rinder - reiner Gesetzestext."),
        22: (False, None,
            "Bundesbuch: Diebstahl-, Schadens-, Darlehens- und Sozialrecht sowie Erstlingsgaben - "
            "reiner Gesetzestext."),
        23: (False, None,
            "Bundesbuch: Rechtspflege, Sabbatjahr, drei Wallfahrtsfeste und die Verheissung des "
            "vorausziehenden Engels - Gesetzes- und Verheissungsrede."),
        24: (True, None,
            "Bundesschluss am Sinai: Altarbau, Blutbesprengung, Mahl der Aeltesten vor Gott und Moses "
            "Aufstieg in die Wolke."),
        25: (False, None,
            "Bauvorschriften fuer Lade, Schaubrottisch und Leuchter mit genauen Massangaben."),
        26: (False, None,
            "Bauvorschriften fuer Zeltbahnen, Decken, Bretter, Riegel und den Vorhang der "
            "Stiftshuette."),
        27: (False, None,
            "Bauvorschriften fuer Brandopferaltar, Vorhof und das Oel fuer den Leuchter."),
        28: (False, None,
            "Kultvorschrift fuer die Priesterkleider Aarons: Efod, Brustschild mit zwoelf Steinen, "
            "Oberkleid, Stirnblech und Beinkleider."),
        29: (False, None,
            "Ritualvorschrift fuer die siebentaegige Priesterweihe Aarons und seiner Soehne samt "
            "taeglichem Brandopfer."),
        30: (False, None,
            "Vorschriften fuer Raeucheraltar, Halbschekel-Abgabe, Becken, Salboel und Raeucherwerk."),
        31: (False, None,
            "Beauftragung Bezalels und Oholiabs als Gottesrede, Sabbatgebot als ewiges Zeichen, nur "
            "die Schlussnotiz zu den Tafeln ist Handlung."),
        32: (True, None,
            "Goldenes Kalb: Aarons Guss, Moses Fuerbitte, Zerbrechen der Tafeln, Strafgericht der "
            "Leviten und Plage."),
        33: (True, None,
            "Trauer des Volkes ueber die Schmuckablegung, Zelt der Begegnung mit Wolkensaeule und "
            "Moses Wechselrede um Gottes Mitgehen und Herrlichkeit."),
        34: (True, (["1-9", "27-35"], ["10-26"]),
            "Neue Tafeln, Gottes Vorueberzug und Moses strahlendes Gesicht rahmen den eingeschobenen "
            "Gesetzesblock des Bundesprivilegrechts (V. 10-26)."),
        35: (False, None,
            "Sabbatgebot, Materialliste fuer die Stiftshuette, Aufzaehlung der Gaben und die Rede "
            "ueber Bezalel und Oholiab - Kultanweisung und Listen ohne Handlungsfortschritt."),
        36: (False, (["2-7"], ["1", "8-38"]),
            "Der Baubericht zu Zeltbahnen, Brettern und Vorhang (V. 8-38) ueberwiegt klar; nur die "
            "Szene um die zu reichlichen Gaben und Moses Halt-Befehl (V. 2-7) ist Handlung."),
        37: (False, None,
            "Ausfuehrungsbericht zur Anfertigung von Lade, Tisch, Leuchter und Raeucheraltar mit "
            "Massangaben."),
        38: (False, None,
            "Ausfuehrungsbericht zu Brandopferaltar, Becken und Vorhof samt Abrechnung ueber Gold, "
            "Silber und Bronze."),
        39: (False, None,
            "Anfertigung der Priesterkleider und abschliessendes Inventarverzeichnis aller "
            "Werkstuecke vor Mose."),
        40: (False, None,
            "Aufrichtungsbefehl und der listenfoermige Vollzugsbericht zur Stiftshuette (V. 1-33) "
            "beherrschen das Kapitel; nur der Schluss ueber Wolke und Herrlichkeit ist szenisch."),
    },
    "joshua": {
        1: (False, (["10-18"], ["1-9"]),
            "Nachgelesen: Vv1-9 sind eine zusammenhaengende Gottesrede (Beauftragung, Zusage, "
            "Gesetzesmahnung 'dies Buch des Gesetzes soll nicht von deinem Munde weichen') ohne "
            "Ortswechsel oder Handlungsfortschritt; ab V10 ('Then Joshua commanded the officers') "
            "laeuft eine Szene mit Marschbefehl, Anrede an die Ostjordanstaemme und deren Antwort. "
            "Naht liegt sauber an Versgrenze 9/10, daher Teilung; gemessen 285 Woerter Redeblock "
            "gegen 264 Woerter Szene, also Etikett nicht erzaehlend."),
        2: (True, None,
            "Die Kundschafter bei Rahab in Jericho: Verstecken auf dem Dach, Flucht am Seil, roter "
            "Faden, Rueckkehr zu Josua - durchgehende Handlung mit Ortswechsel."),
        3: (True, None,
            "Der Zug ueber den Jordan: Aufbruch von Schittim, Marschbefehle an die Priester, das "
            "Wasser staut sich, das Volk zieht trockenen Fusses hinueber."),
        4: (True, None,
            "Die zwoelf Gedenksteine aus dem Jordanbett werden geholt und in Gilgal aufgerichtet, die "
            "Priester steigen herauf, das Wasser kehrt zurueck."),
        5: (True, None,
            "Beschneidung in Gibeat-Haaralot, Passafeier in den Ebenen von Jericho, Ende des Manna "
            "und die Begegnung mit dem Fuersten des Heeres JHWHs."),
        6: (True, None,
            "Der Fall Jerichos: sieben Tage Umzug mit Widderhoernern, Kriegsgeschrei, Einsturz der "
            "Mauer, Rettung Rahabs und Verbrennung der Stadt."),
        7: (True, None,
            "Achans Diebstahl am Banngut: Niederlage vor Ai, Josuas Klage, Losverfahren, Gestaendnis "
            "und Steinigung im Tal Achor."),
        8: (True, None,
            "Eroberung Ais durch den Hinterhalt, Hinrichtung des Koenigs, danach Altarbau auf dem "
            "Ebal und Verlesung des Gesetzes - durchweg ausgefuehrte Handlung."),
        9: (True, None,
            "Die List der Gibeoniter mit altem Brot und zerrissenen Schlaeuchen, der erschlichene "
            "Bundesschluss und ihre Verurteilung zu Holzhauern und Wassertraegern."),
        10: (True, None,
            "Schlacht bei Gibeon gegen die fuenf Amoriterkoenige, Hagelsteine, Sonnenstillstand, die "
            "Koenige in der Hoehle von Makkeda und der Feldzug im Sueden."),
        11: (True, None,
            "Feldzug gegen Jabin von Hazor am Wasser von Merom, Laehmung der Pferde, Verbrennung "
            "Hazors und Vertilgung der Anakiter."),
        12: (False, None,
            "Reines Verzeichnis der besiegten Koenige - Sihon und Og im Ostjordanland, dann die "
            "Aufzaehlung 'der Koenig von Jericho, einer; der Koenig von Ai, einer' bis 31."),
        13: (False, None,
            "Aufzaehlung des noch nicht eroberten Landes und Grenz- und Staedtelisten des "
            "ostjordanischen Erbteils von Ruben, Gad und Halb-Manasse."),
        14: (True, (["6-15"], ["1-5"]),
            "Nach der Verwaltungsnotiz zur Landverteilung (1-5) folgt die ausgefuehrte Szene, in der "
            "Kaleb in Gilgal vor Josua tritt und Hebron erhaelt (6-15)."),
        15: (False, (["13-19"], ["1-12", "20-63"]),
            "Grenzbeschreibung und lange Staedtelisten Judas, darin als klar abgegrenzte Episode "
            "Kalebs Eroberung von Debir und Achsas Bitte um die Wasserquellen (13-19)."),
        16: (False, None,
            "Reine Grenzbeschreibung des Erbteils der Josefsoehne bzw. Ephraims von Jericho ueber "
            "Bet-Horon bis zum Meer."),
        17: (False, None,
            "Erbteil Manasses mit Sippenregister, Zelofhads Toechtern und Grenzliste; die angehaengte "
            "Wechselrede der Josefsoehne mit Josua bleibt in der Minderheit."),
        18: (False, (["1-10"], ["11-28"]),
            "Versammlung in Silo, Aussendung der Landvermesser und Losentscheid (1-10) laufen als "
            "Handlung, danach folgt die Grenz- und Staedteliste Benjamins (11-28)."),
        19: (False, None,
            "Loszuteilungen fuer Simeon, Sebulon, Issachar, Asser, Naftali und Dan als reine Grenz- "
            "und Staedtelisten mit Schlussnotiz zu Josuas Erbteil."),
        20: (False, None,
            "Rechtsvorschrift ueber die Asylstaedte fuer den Totschlaeger samt der Aufzaehlung der "
            "sechs Zufluchtsstaedte."),
        21: (False, None,
            "Verzeichnis der 48 Levitenstaedte mit Weideland, nach Kehatitern, Gerschonitern und "
            "Merariten geordnet."),
        22: (True, None,
            "Heimkehr der Ostjordanstaemme, Bau des grossen Altars am Jordan, drohender Buergerkrieg "
            "und die Gesandtschaft des Pinhas - Anklage und Antwort sind Wechselrede in einer sich "
            "aufloesenden Szene."),
        23: (False, None,
            "Josuas Abschiedsrede an die Aeltesten: Mahnung zum Gesetz, Warnung vor Mischehen und vor "
            "dem Verlust des Landes - fast der ganze Kapiteltext ist Rede ohne Handlung."),
        24: (True, (["1", "14-33"], ["2-13"]),
            "Die Gottesrede mit dem Geschichtsrueckblick von Terach bis zur Landgabe (2-13) ist "
            "Predigt, waehrend Versammlung, Wechselrede 'wir wollen dem HERRN dienen', Bundesschluss, "
            "Gedenkstein und die Begraebnisse Josuas, Josefs und Eleasars Handlung sind."),
    },
    "judges": {
        1: (True, (["1-26"], ["27-36"]),
            "Eroberungszuege nach Josuas Tod (Adoni-Besek, Kaleb/Achsa, Bethel-Kundschafter) als "
            "Handlung, ab V.27 nur noch Liste der Staemme, die ihre Landesteile nicht einnahmen."),
        2: (False, (["1-10"], ["11-23"]),
            "Szene des Engels in Bochim und Josuas Tod/Begraebnis laufen als Handlung, V.11-23 ist "
            "theologische Rahmensumme des Richterzyklus mit Gottesrede."),
        3: (True, (["7-31"], ["1-6"]),
            "V.1-6 Liste der zur Pruefung belassenen Voelker, ab V.7 durchlaufende Handlung um Otniel "
            "und vor allem Ehuds Attentat auf Eglon."),
        4: (True, None,
            "Debora, Barak, Schlacht am Kischon gegen Sisera und Jaels Zeltpflock -- fortlaufende "
            "Szenen mit Ortswechseln."),
        5: (False, None,
            "Das Debora-Lied fuellt praktisch das ganze Kapitel (V.2-31) als eingelegtes Siegeslied, "
            "nur V.1 ist Erzaehlrahmen."),
        6: (True, None,
            "Midianiternot, Berufung Gideons am Terebinth, Zerstoerung des Baalsaltars und Wollvlies- "
            "Probe als zusammenhaengende Handlung."),
        7: (True, None,
            "Auslese der 300 Mann am Wasser, Traumdeutung im Midianiterlager und Ueberfall mit "
            "Kruegen und Fackeln."),
        8: (True, None,
            "Gideons Streit mit Ephraim, Verfolgung von Sebach und Zalmunna, Strafe an Sukkot und "
            "Pnuel, Ephod und Gideons Tod."),
        9: (True, (["1-7", "21-57"], ["8-20"]),
            "Handlung (Putsch, Brudermord, Gaal-Aufstand, Tebez/Muehlstein) traegt 1240 von 1581 "
            "Woertern; nur V.8-20 ist Jotams Baeumefabel samt Anwendung als eingelegte Rede ohne "
            "Handlungsfortschritt, V.7 bleibt Szene (Aufstieg auf den Garizim), Naht bei 7/8 und "
            "20/21 sauber."),
        10: (True, (["6-18"], ["1-5"]),
            "V.1-5 blosse Richternotizen zu Tola und Jair, ab V.6 Ammoniterbedraengnis, Zwiegespraech "
            "mit JHWH und Aufmarsch nach Mizpa."),
        11: (True, (["1-14", "28-40"], ["15-27"]),
            "V15-27 ist Jeftas langes geschichtlich-juristisches Botenschreiben an den "
            "Ammoniterkoenig (402 Woerter, reine Argumentation ohne Handlung), waehrend V1-14 "
            "(Vertreibung, Berufung, Botenwechsel) und V28-40 (Geluebde, Feldzug, Tochter) mit 773 "
            "Woertern die Mehrheit tragen; Nahtstellen bei V14/15 und V27/28 liegen exakt auf "
            "Versgrenzen."),
        12: (True, (["1-6"], ["7-15"]),
            "V.7 ist bereits reine Richter-Rahmenformel (regierte sechs Jahre, starb, wurde begraben) "
            "und gehoert zu den Amtsnotizen ab V.8, nicht zur Szene; V.1-6 (Ephraimkrieg, Schibbolet- "
            "Probe an den Jordanfurten, 235 Woerter) uebertrifft die Notizenliste (144 Woerter)."),
        13: (True, None,
            "Erscheinung des Gottesboten bei Manoach und seiner Frau, Opfer auf dem Felsen und Geburt "
            "Simsons."),
        14: (True, None,
            "Simsons Hochzeit in Timna, Loewe und Honig, Raetsel und Erschlagen der Aschkeloniter -- "
            "Dialog innerhalb der Handlung."),
        15: (True, None,
            "Fuechse mit Fackeln in den Kornfeldern, Auslieferung am Felsen Etam und Eselskinnbacken "
            "-- der Spottvers ist nur eine Zeile."),
        16: (True, None,
            "Simson in Gaza, Delila und das Haargeheimnis, Blendung und Einsturz des Dagontempels."),
        17: (True, None,
            "Michas gestohlenes Silber, das Gussbild im Hausheiligtum und die Anstellung des "
            "wandernden Leviten."),
        18: (True, None,
            "Danitische Kundschafter, Raub von Michas Kultbild und Priester, Eroberung von "
            "Lajisch/Dan."),
        19: (True, None,
            "Der Levit holt seine Nebenfrau aus Bethlehem, Nachtlager in Gibea, Schandtat und "
            "Zerstueckelung."),
        20: (True, None,
            "Stammesversammlung in Mizpa und die drei Feldzuege gegen Benjamin mit Hinterhalt bei "
            "Gibea."),
        21: (True, None,
            "Frauenbeschaffung fuer Benjamin: Strafzug gegen Jabesch-Gilead und Maedchenraub beim "
            "Fest in Schilo."),
    },
    "ruth": {
        1: (True, None,
            "Elimelechs Auswanderung nach Moab, Tod der Maenner, Naomis Rueckkehr mit Ruth nach "
            "Bethlehem - durchgehend Handlung mit Ortswechsel und Szenendialog."),
        2: (True, None,
            "Ruth liest Aehren auf Boas' Feld, Begegnung und Gespraech mit Boas, Rueckkehr zu Naomi "
            "am Abend - fortlaufende Szene."),
        3: (True, None,
            "Durchgehende Nachtszene: Naomis Anweisung, Ruths Gang zur Tenne, Boas erwacht um "
            "Mitternacht, Zusage der Loeserpflicht, Rueckkehr mit sechs Mass Gerste - alle Rede ist "
            "Dialog innerhalb fortlaufender Handlung mit Ortswechsel und Zeitverlauf, kein Redeblock, "
            "daher keine Teilung noetig."),
        4: (True, (["1-6", "8-17"], ["7", "18-22"]),
            "V. 7 ist am WEBBE-Wortlaut nachgeprueft eine antiquarische Erzaehler-Erklaerung des "
            "Loese-/Sandalenbrauchs ohne Akteur und Handlungsfortschritt (Brauch-/Rechtstext), und "
            "die Naht liegt sauber an Versgrenzen zwischen der Rede in V. 6 und der "
            "Handlungsfortsetzung in V. 8 (41 von 640 Woertern; Erzaehlanteil 527/640)."),
    },
    "1 samuel": {
        1: (True, None,
            "Elkanas Wallfahrt nach Schilo, Hannas Geluebde, Samuels Geburt und Uebergabe an Eli - "
            "durchlaufende Handlung mit Ortswechsel und Zeitverlauf."),
        2: (False, (["11-12", "18-26"], ["1-10", "13-17", "27-36"]),
            "V.13-17 ist am Wortlaut nachgeprueft iterative Kultbrauch-Beschreibung ('The custom of "
            "the priests...', 'They did this to all the Israelites...', Konditionalrede 'If the man "
            "said... then he would say') samt bewertender Schlussnotiz V.17; erst V.18 ('But Samuel "
            "ministered') setzt die Szene wieder ein, der Bruch liegt sauber an Versgrenzen."),
        3: (True, None,
            "Naechtliche Berufung Samuels in Schilo mit Wechselrede zwischen Samuel und Eli und dem "
            "Bericht am Morgen."),
        4: (True, None,
            "Schlacht bei Eben-Eser, Raub der Bundeslade, Tod der Soehne Elis, Elis Sturz und die "
            "Geburt Ikabods - fortlaufende Handlung."),
        5: (True, None,
            "Die Lade bei den Philistern: Dagon stuerzt in Aschdod, Beulenplage, Weitertransport nach "
            "Gat und Ekron - Ortswechsel und Zeitverlauf."),
        6: (True, (["1-16", "19-21"], ["17-18"]),
            "V.17-18 ist nachgeprueft Inventarkatalog nach Staedten plus 'to this day'-Aetiologie (86 "
            "W.) und damit Liste statt Szene, waehrend V.3-9 Rede in laufender Szene bleibt (Frage "
            "V.2, Rat, Ausfuehrung V.10 'The men did so') und daher erzaehlend zaehlt."),
        7: (True, (["1-14"], ["15-17"]),
            "V.15-17 ist reine Richter-Rahmenformel nach Praezisierung 4 ('all the days of his life', "
            "'from year to year in a circuit'), waehrend V.13-14 noch das Ergebnis der erzaehlten "
            "Schlacht berichtet und deshalb erzaehlend bleibt."),
        8: (True, (["1-10", "19-22"], ["11-18"]),
            "Nachgezaehlt am WEBBE-Wortlaut: Rahmen 1-10 (228 W.) und 19-22 (93 W.) sind Handlung mit "
            "Ortswechsel nach Rama und Dialog, dazwischen steht als geschlossener Rechts-/Lehrblock "
            "das 'Recht des Koenigs' 11-18 (204 W., kein Handlungsfortschritt); die Naht liegt sauber "
            "an Versgrenzen (Redeeinleitung V.11, Redeschluss V.18), Erzaehlteil traegt die Mehrheit."),
        9: (True, None,
            "Saul sucht die Eselinnen, trifft den Seher Samuel in der Stadt und wird zum Opfermahl "
            "geladen - Reise mit Ortswechsel."),
        10: (True, (["1", "9-27"], ["2-8"]),
            "V.2-8 (275 W. nachgezaehlt) sind durchgaengig Futur-Ankuendigung dreier Zeichen plus "
            "Gilgal-Auftrag ohne jeden Handlungsfortschritt zwischen der Salbung V.1 und dem Aufbruch "
            "V.9 - prophetische Rede und damit nicht erzaehlend, Bruch sauber an Versgrenzen."),
        11: (True, None,
            "Nahasch belagert Jabesch-Gilead, Saul zerstueckelt das Rindergespann, Feldzug und "
            "Koenigserneuerung in Gilgal."),
        12: (False, None,
            "Samuels Abschiedsrede an ganz Israel (Rechenschaft, Geschichtsrueckblick, Mahnung); nur "
            "die Donnerszene (18-19) ist Handlung, zu klein fuer eine saubere Teilung."),
        13: (True, (["2-18", "23"], ["1", "19-22"]),
            "V.1 ist reine Regierungsformel (Praezisierung 4) und V.19-22 ein iterativer "
            "Zustandsexkurs zur Schmiedenot mit Gebuehrentarif ('The price was one payim each'), "
            "waehrend V.23 die Handlung wieder aufnimmt."),
        14: (True, (["1-46"], ["47-52"]),
            "V.47-52 (170 W. nachgezaehlt) ist geschlossener Regierungssummar, Genealogie- und "
            "Beamtenliste plus Dauerformel 'all the days of Saul'; die Szene endet sauber mit V.46."),
        15: (True, None,
            "Feldzug gegen Amalek, Sauls Schonung Agags, Streitgespraech mit Samuel und die "
            "Hinrichtung Agags in Gilgal."),
        16: (True, None,
            "Samuel salbt David in Bethlehem, danach kommt David als Harfenspieler an Sauls Hof."),
        17: (True, None,
            "Goliats Herausforderung im Terebinthental, Davids Kampf und Sieg; alle Reden stehen in "
            "der laufenden Szene."),
        18: (True, None,
            "Jonatans Freundschaftsbund, Sauls Neid nach dem Frauenlied, Speerwurf und Michals "
            "Brautpreis von hundert Vorhaeuten."),
        19: (True, None,
            "Sauls Nachstellungen: Michals Fluchtlist mit dem Hausgoetzen, Davids Flucht zu Samuel "
            "nach Rama und die Prophetenekstase der Boten."),
        20: (True, None,
            "Davids Bund mit Jonatan, das Neumondmahl mit Sauls Zorn und das Pfeilzeichen auf dem "
            "Feld."),
        21: (True, None,
            "David holt die Schaubrote und Goliats Schwert bei Ahimelech in Nob und stellt sich bei "
            "Achisch in Gat wahnsinnig."),
        22: (True, None,
            "David in der Hoehle Adullam und in Moab, Dogs Anzeige und das Priestermorden zu Nob mit "
            "Abjatars Flucht."),
        23: (True, None,
            "Befreiung Kelas, Efod-Orakel, Verrat der Siphiter und Sauls Abbruch der Verfolgung am "
            "Felsen der Trennung."),
        24: (True, None,
            "David schneidet Saul in der Hoehle bei En-Gedi den Mantelzipfel ab und ruft ihm nach - "
            "Dialog innerhalb der Szene."),
        25: (True, None,
            "Nabals Weigerung, Abigajils Ritt mit Proviant und Bittrede, Nabals Tod und Abigajils "
            "Heirat mit David."),
        26: (True, None,
            "David nimmt dem schlafenden Saul im Lager auf Hachila Speer und Wasserkrug und ruft "
            "Abner vom Gegenhang aus an."),
        27: (True, None,
            "David siedelt bei Achisch in Ziklag und fuehrt Raubzuege gegen Geschuriter und "
            "Amalekiter mit Taeuschungsberichten."),
        28: (True, None,
            "Saul geht nachts verkleidet zur Totenbeschwoererin von En-Dor; die Samuel-Erscheinung "
            "ist Rede in laufender Szene mit Sauls Zusammenbruch."),
        29: (True, None,
            "Die Philisterfuersten in Afek weisen David ab, Achisch schickt ihn am Morgen zurueck."),
        30: (True, (["1-24", "26"], ["25", "27-31"]),
            "V.25 ist aetiologische Rechtssetzung ('a statute and an ordinance for Israel to this "
            "day') und V.27-31 ein reiner Ortsnamenkatalog ohne Akteur und Zeitverlauf, waehrend V.26 "
            "mit Davids Ankunft in Ziklag und Botenwort Handlung bleibt."),
        31: (True, None,
            "Schlacht auf dem Gilboa, Sauls Tod im Schwert, Schaendung der Leichen und Bergung durch "
            "die Maenner von Jabesch."),
    },
    "2 samuel": {
        1: (True, (["1-16"], ["17-27"]),
            "V.17-18 sind Ueberschrift des Klagelieds plus Quellenverweis ('written in the book of "
            "Jashar'), enden im WEBBE mit Doppelpunkt und gehoeren nach Regel 3/4 zum eingelegten "
            "Lied - parallel zu 22,1; erzaehlend bleiben nachgezaehlt 423 von 665 Woertern."),
        2: (True, (["1-9", "12-32"], ["10-11"]),
            "V.10-11 (nachgezaehlt 45 Woerter) sind reine Regierungsformeln wie 5,4-5, die dort "
            "bereits ausgeschieden wurden; Regel 4 greift, der Bruch liegt sauber zwischen V.9 (Abner "
            "macht Ischboschet zum Koenig) und V.12 (Aufbruch nach Gibeon)."),
        3: (True, (["1", "6-32", "35-39"], ["2-5", "33-34"]),
            "Abners Uebertritt zu David, Michals Rueckgabe und Abners Ermordung durch Joab; "
            "herausgeloest sind die Sohnesliste aus Hebron (V.2-5) und Davids Klagelied ueber Abner "
            "(V.33-34)."),
        4: (True, None,
            "Rechab und Baana ermorden Ischboschet und werden von David dafuer hingerichtet - reine "
            "Szenenfolge."),
        5: (True, (["1-3", "6-13", "17-25"], ["4-5", "14-16"]),
            "Salbung, Einnahme Zions und zwei Philisterschlachten sind Handlung; V.4-5 ist reine "
            "Regierungsformel (Chroniknotiz) und V.14-16 die Namensliste, waehrend V.13 noch "
            "erzaehlende Notiz mit Akteur ist."),
        6: (True, None,
            "Ueberfuehrung der Lade, Usas Tod, Aufenthalt bei Obed-Edom, Davids Tanz und der Streit "
            "mit Michal - fortlaufende Handlung mit Ortswechsel."),
        7: (False, (["1-3"], ["4-29"]),
            "Nur V.1-3 sind Szene (David/Nathan); V.4-17 Gottesrede mit Dynastieverheissung und "
            "V.18-29 Davids Dankgebet tragen die klare Wortmehrheit - die Naht liegt sauber bei "
            "V.3/4, deshalb geteilt, aber das Kapitel zaehlt als nicht erzaehlend."),
        8: (True, (["1-14"], ["15-18"]),
            "V.1-14 annalistischer Feldzugsbericht mit Akteuren, Ortswechsel und Zeitverlauf; V.15 "
            "ist bereits allgemeine Regierungsformel ('David reigned over all Israel... executed "
            "justice') und leitet das Beamtenregister V.16-18 ein."),
        9: (True, None,
            "David sucht ueber Ziba den lahmen Mephiboschet und holt ihn an seinen Tisch - "
            "durchgehende Szene mit Dialog."),
        10: (True, None,
            "Schmaehung von Davids Gesandten durch Hanun und der daraus folgende Ammoniter-Aramaeer- "
            "Krieg unter Joab - fortlaufende Handlung."),
        11: (True, None,
            "Davids Ehebruch mit Batseba und die Beseitigung Urijas vor Rabba - reine Erzaehlhandlung "
            "mit Zeitverlauf."),
        12: (True, (["1-6", "13-31"], ["7-12"]),
            "V.7-12 ist ein geschlossener JHWH-Gerichtsspruch mit doppelter Botenformel (V.7 und "
            "V.11) ohne Handlungsfortschritt - dieselbe prophetische Redeform wie 7,4-17, die dort "
            "ausgeschieden wurde; der Mischvers 7 faellt nach 'im Zweifel gegen den Erzaehlanteil' "
            "auf die nicht erzaehlende Seite, erzaehlend bleiben 749 von 962 Woertern."),
        13: (True, None,
            "Amnons Vergewaltigung Tamars und Absaloms Rachemord beim Schafschur in Baal-Hazor, dann "
            "Flucht nach Geschur."),
        14: (True, (["1-24", "28-33"], ["25-27"]),
            "V.25-27 (nachgezaehlt 102 Woerter) ist Beschreibungs- und Kinderlisten-Exkurs "
            "(Schoenheit, iterative Haarnotiz 'at every year's end', 'Three sons were born to "
            "Absalom') ohne Handlung; die Szene laeuft von V.24 sauber nach V.28 weiter, gleiche "
            "Textsorte wie die ausgeschiedenen Listen 3,2-5 und 5,14-16."),
        15: (True, None,
            "Absaloms Verschwoerung in Hebron und Davids Flucht ueber den Kidron zum Oelberg mit "
            "Zadok und Huschai - staendiger Ortswechsel."),
        16: (True, None,
            "Ziba mit den Vorraeten, Schimis Fluch in Bahurim und Absaloms Einzug in Jerusalem mit "
            "Ahitofels Rat - fortlaufende Handlung."),
        17: (True, None,
            "Der Ratschlag Ahitofels gegen den Huschais, die Botenkette ueber En-Rogel und Ahitofels "
            "Selbstmord - Reden dienen der Handlung."),
        18: (True, None,
            "Schlacht im Wald Ephraim, Absaloms Tod an der Eiche durch Joab und die Botenlaeufer zu "
            "David - durchgehende Handlung."),
        19: (True, None,
            "Joab stellt den trauernden David zur Rede, dann Rueckkehr ueber den Jordan mit Schimi, "
            "Mephiboschet und Barsillai - Szenenfolge mit Ortswechsel."),
        20: (True, (["1-22"], ["23-26"]),
            "Schebas Aufstand, Amasas Ermordung und die Belagerung von Abel-Bet-Maacha; abgetrennt "
            "die abschliessende Beamtenliste (V.23-26)."),
        21: (True, (["1-17"], ["18-22"]),
            "V.18-22 (nachgezaehlt 132 Woerter) ist ein formelhafter Heldenkatalog mit dreifach "
            "gleicher Einleitung und abschliessender Summenformel 'These four were born to the giant "
            "in Gath' - derselbe Registertyp wie 23,8-39 (0 %); die echte Szene endet sauber mit "
            "V.17."),
        22: (False, None,
            "Das gesamte Kapitel ist Davids Danklied nach der Errettung (Parallele zu Psalm 18), nur "
            "V.1 ist Ueberschrift."),
        23: (False, None,
            "Letzte Worte Davids als Gottesspruch (V.1-7) plus Heldenkatalog der Dreissig mit "
            "Namensliste (V.8-39) - Spruch und Register ueberwiegen."),
        24: (True, None,
            "Volkszaehlung durch Joab, Gads Strafangebot, Pest und Altarbau auf der Tenne Araunas - "
            "fortlaufende Handlung."),
    },
    "1 kings": {
        1: (True, None,
            "Adonijas Thronanmassung, Natans und Batsebas Intervention und Salomos Salbung am Gihon - "
            "durchgehende Szenenfolge mit Ortswechsel."),
        2: (True, (["1", "10-46"], ["2-9"]),
            "V.2-9 sind Davids Abschiedsrede/Testament ohne Handlungsfortschritt (336 W.), der "
            "Erzaehlrahmen V.1 und die geschlossene Handlungskette Tod Davids, Adonija, Abjatar, "
            "Joab, Schimi (1074 W. = 76%) tragen klar; Naht liegt sauber an Versgrenzen."),
        3: (True, None,
            "Traumoffenbarung in Gibeon als Wechselrede und das Salomonische Urteil ueber die beiden "
            "Frauen - fortlaufende Handlung."),
        4: (False, None,
            "Beamtenliste Salomos, zwoelf Versorgungsbezirke, Hofbedarfszahlen und Weisheitsnotiz - "
            "reine Register und Summarien ohne Handlung."),
        5: (False, None,
            "Rund die Haelfte der Woerter (248 von 508) sind die schriftlichen Botenworte Salomos und "
            "Hirams ueber den Tempelbau, dazu 132 W. Fronarbeiter- und Materialstatistik; nur ca. 128 "
            "W. Rahmennotizen (Vertrag, Lieferung) ohne Szene, Ortswechsel oder Zeitverlauf - Brief "
            "plus Verwaltungsnotiz, keine saubere Teilung moeglich."),
        6: (False, None,
            "Massangaben des Tempelbaus: Hallen, Seitenkammern, Zedernverkleidung, Cherubim und "
            "Tueren - Baubeschreibung."),
        7: (False, None,
            "Palastbau und Hirams Bronzearbeiten: Saeulen Jachin und Boas, ehernes Meer, Kesselwagen "
            "und Tempelgeraet - Bau- und Inventarbeschreibung."),
        8: (False, (["1-11", "62-66"], ["12-61"]),
            "Ladeueberfuehrung und Opferfest sind Handlung, doch Salomos Weihgebet und die beiden "
            "Segensreden tragen die Wortmehrheit; Naht an V. 11/12 und 61/62 sauber."),
        9: (False, None,
            "Zweite Gotteserscheinung als laengere Warnrede, danach Staedteabtretung an Hiram, "
            "Fronliste und Bauzusammenfassung - kein Handlungsfaden."),
        10: (False, (["1-13"], ["14-29"]),
            "Besuch der Koenigin von Saba ist eine Szene mit Anreise und Dialog, ab V. 14 folgt der "
            "Reichtumskatalog (Gold, Schilde, Elfenbeinthron, Pferdehandel); Naht bei V. 13/14 "
            "sauber."),
        11: (True, (["1-10", "14-30", "40"], ["11-13", "31-39", "41-43"]),
            "Salomos Abfall, Hadad, Reson und Jerobeams Flucht sind Handlung (737 W. = 61%); die "
            "Gottesrede V.11-13, Ahijas Orakel V.31-39 und die Schlussformel V.41-43 sind Rede bzw. "
            "Chroniknotiz - Teilung deckt V.1-43 lueckenlos ab."),
        12: (True, None,
            "Reichsteilung in Sichem: Rehabeams Beratung, harte Antwort, Steinigung Adorams und "
            "Jerobeams Stierbilder in Bethel und Dan."),
        13: (True, None,
            "Der Gottesmann aus Juda am Altar von Bethel, verdorrte Hand des Koenigs, Verfuehrung "
            "durch den alten Propheten und Tod durch den Loewen."),
        14: (False, (["1-6", "17-18", "25-28"], ["7-16", "19-24", "29-31"]),
            "Der Verkleidungsgang der Frau Jerobeams (1-6), der Tod des Kindes (17-18) und der "
            "Schischak-Ueberfall mit den Bronzeschilden (25-28) sind ausgefuehrte Szenen, bleiben "
            "aber mit 333 W. gegen 597 W. Gerichtsorakel und Regierungsformeln in der Minderheit; "
            "B-Teilung ist praeziser als A und deckt V.1-31 exakt ab."),
        15: (False, (["17-22"], ["1-16", "23-34"]),
            "Regierungsformeln fuer Abijam, Asa, Nadab und Bascha; nur Asas Buendnis mit Ben-Hadad "
            "und der Abbruch von Rama ist eine ausgefuehrte Szene."),
        16: (False, (["9-12", "15-18"], ["1-8", "13-14", "19-34"]),
            "Jehu-Orakel und dichte Chronik- und Quellenformeln dominieren (ca. 780 W.); nur Simris "
            "Mord an Ela in Arzas Haus (9-12) und Omris Erhebung samt Belagerung von Tirza und Simris "
            "Selbstverbrennung (15-18) sind ausgefuehrte Szenen - A's Teilung war unsauber (V.19-20 "
            "sind Formeln), hier korrigiert, Abdeckung V.1-34 lueckenlos."),
        17: (True, None,
            "Elija am Bach Krit von Raben gespeist, bei der Witwe in Sarepta, Mehl und Oel und die "
            "Erweckung ihres Sohnes."),
        18: (True, None,
            "Obadja, Begegnung mit Ahab und das Gottesurteil auf dem Karmel mit anschliessendem Regen "
            "und Elijas Lauf nach Jesreel."),
        19: (True, None,
            "Elijas Flucht vor Isebel, Engel unter dem Ginster, Gotteserscheinung am Horeb und "
            "Berufung Elischas beim Pfluegen."),
        20: (True, None,
            "Ben-Hadads Belagerung Samarias, zwei Feldzuege, der Vertrag mit Ahab und das Gleichnis "
            "des verkleideten Propheten - fortlaufende Kriegshandlung."),
        21: (True, None,
            "Nabots Weinberg: Isebels Briefintrige, Steinigung Nabots und Elijas Auftritt im Weinberg "
            "mit Ahabs Busse."),
        22: (True, (["1-38"], ["39-53"]),
            "Micha ben Jimla vor Ahab und Joschafat, Zug nach Ramot-Gilead und Ahabs Tod bis zum "
            "Blutlecken der Hunde (V.1-38, 1034 W. = 73%) sind Handlung; V.39-40 sind bereits reine "
            "Quellen- und Sterbeformel fuer Ahab, daher gehoert der Schnitt vor V.39 - Abdeckung "
            "V.1-53 lueckenlos."),
    },
    "2 kings": {
        1: (True, (["1-16"], ["17-18"]),
            "V.18 ist reine Quellenformel (25 W.) und V.17 besteht zu 25 von 37 nachgezaehlten "
            "Woertern aus Thronbesteigungs-/Synchronismusformel, deren Bruch mitten im Vers liegt - "
            "also nach Praezisierung 4 und der konservativen Regel beide Verse nicht erzaehlend; die "
            "Szene endet mit dem Botenwort V.16."),
        2: (True, None,
            "Elijas Himmelfahrt im Feuerwagen, Weg Gilgal-Bethel-Jericho-Jordan, Elischas Mantel, "
            "Heilung der Quelle und die Baeren bei Bethel."),
        3: (True, (["4-27"], ["1-3"]),
            "V.1-3 (26+32+24 = 82 von 811 nachgezaehlten Woertern) sind vollstaendiger "
            "deuteronomistischer Koenigsrahmen ohne Akteursszene, Ortswechsel oder Zeitverlauf; die "
            "Handlung setzt erst mit Mescha in V.4 ein, die Naht liegt sauber an der Versgrenze 3/4."),
        4: (True, None,
            "Elischa-Wunderreihe: Oelkrug der Witwe, Sohn der Schunemiterin, Tod im Topf und Speisung "
            "der Hundert - lauter ausgefuehrte Szenen."),
        5: (True, None,
            "Naamans Aussatzheilung im Jordan und Gehasis Betrug - durchgehende Handlung von Damaskus "
            "nach Samaria und zurueck."),
        6: (True, None,
            "Schwimmendes Eisen, Blendung des syrischen Heeres bei Dotan und Beginn der Hungersnot in "
            "der belagerten Stadt Samaria."),
        7: (True, (["1-17"], ["18-20"]),
            "V.18-20 (40+41+18 = 99 W., davon 81 woertlich wiederholtes Prophetenwort aus V.1-2) sind "
            "rueckblickende Erfuellungsnotiz ohne neuen Akteur, Ortswechsel oder Zeitfortschritt - "
            "auch V.20 wiederholt nur die schon in V.17 erzaehlte Zertrampelung, daher der "
            "einheitliche Schnitt an der Versgrenze 17/18."),
        8: (True, (["1-15"], ["16-29"]),
            "V.1-15 Schunemiterin vor dem Koenig und Hasaels Mord an Benhadad als Szene; ab V.16 nur "
            "noch Regierungsformeln zu Joram und Ahasja mit Quellenverweis."),
        9: (True, None,
            "Jehus Salbung durch den Prophetenjuenger, die Fahrt nach Jesreel, Toetung Jorams und "
            "Ahasjas und Isebels Sturz aus dem Fenster."),
        10: (True, None,
            "Jehu laesst die siebzig Ahabsoehne koepfen, trifft Ahasjas Brueder und Jonadab und "
            "schlachtet die Baalsdiener im Tempel - fortlaufende Handlung."),
        11: (True, None,
            "Ataljas Gewaltherrschaft, Verstecken des Joasch im Tempel, Jojadas Wachplan, Kroenung "
            "und Ataljas Toetung - geschlossene Szenenfolge."),
        12: (True, (["4-18", "20-21"], ["1-3", "19"]),
            "V4-18 und V20-21 sind ausgefuehrte Handlung (Joaschs Anweisung an die Priester, Jojadas "
            "angebohrte Truhe, Geldzaehlung und Auszahlung, Hasaels Zug gegen Gath, Tribut, Ermordung "
            "des Koenigs); V1-3 Regierungsformel und V19 Quellenverweis sind Chroniknotiz, Naht liegt "
            "sauber an Versgrenzen."),
        13: (False, (["14-21"], ["1-13", "22-25"]),
            "Rahmenformeln zu Joahas und Joasch (V.1-13) und Schlussnotizen zu Hasael (V.22-25) "
            "ueberwiegen; nur V.14-21 sind die ausgefuehrte Szene von Elischas Pfeilorakel, Tod und "
            "Totenerweckung am Grab."),
        14: (False, (["5-14"], ["1-4", "15-29"]),
            "Ausgefuehrt ist nur V.5-14 (Amazjas Rache, Distelfabel des Joasch, Schlacht bei Beth- "
            "Schemesch); Rest sind Regierungs- und Quellenformeln zu Amazja, Asarja und Jerobeam."),
        15: (False, None,
            "Reine Koenigsliste von Asarja bis Jotam mit Thronbesteigungs-, Bewertungs- und "
            "Quellenformeln; die Umsturznotizen (Schallum, Menahem, Pekach) bleiben Chronikvermerke "
            "ohne ausgefuehrte Szene."),
        16: (True, (["5-18"], ["1-4", "19-20"]),
            "V5-18 tragen als Handlungsfolge (Belagerung durch Rezin und Pekah, Hilferuf und Tribut "
            "an Tiglat-Pileser, Reise nach Damaskus, Urijas Altarbau, Ahas' Umbauten); der "
            "Altarbefehl V15 ist Rede in laufender Szene, V1-4 und V19-20 sind reine Regierungs- und "
            "Sterbeformel."),
        17: (False, (["1-6", "24-28"], ["7-23", "29-41"]),
            "Nur V.1-6 (Hoscheas Verrat, Fall Samarias) und V.24-28 (Ansiedlung der Fremdvoelker, "
            "Loewenplage, Rueckkehr des Priesters) sind Handlung; V.7-23 ist die grosse Schuldpredigt "
            "und V.29-41 Goetzenkatalog samt Bundesmahnrede."),
        18: (True, None,
            "Hiskias Reform, Sanheribs Feldzug und die Verhandlungsszene am Wasserleitungsgraben: "
            "Rabschakes Reden sind Botenwort im laufenden Belagerungsgespraech mit Antwort, Schweigen "
            "und Rueckkehr der Beamten."),
        19: (False, (["1-9", "14", "35-37"], ["10-13", "15-34"]),
            "Nachgelesen: Sanheribs Schreiben V10-13 ist ausdruecklich ein Brief (V14 'empfing den "
            "Brief'), Hiskias Tempelgebet V15-19 und Jesajas Spottorakel V20-34 sind Gebet und "
            "Prophetenrede; nur Botengang V1-9, Briefempfang V14 und Engelschlag V35-37 sind "
            "Handlung, 363 gegen 702 Woerter."),
        20: (True, None,
            "Hiskias Krankheit und Heilung durch den Feigenkuchen, das Schattenzeichen an der "
            "Sonnenuhr und der Besuch der babylonischen Gesandten - durchgehender Szenenverlauf."),
        21: (False, None,
            "Suendenkatalog Manasses und Amons in Rahmen- und Bewertungsformeln, dazu das "
            "prophetische Unheilsorakel V.10-15; keine ausgefuehrte Szene."),
        22: (True, (["3-14"], ["1-2", "15-20"]),
            "V3-14 sind Handlung mit Ortswechsel (Schafans Gang zum Tempel, Hilkijas Fund des "
            "Gesetzbuches, Vorlesen vor Josia, Botengang zur Prophetin Hulda); V1-2 ist "
            "Regierungsformel, V15-20 ein geschlossenes Gottesorakel, Erzaehlteil traegt mit 381 "
            "gegen 273 Woerter die Mehrheit."),
        23: (True, None,
            "Joschijas Bundesschluss und Reformzug: er verbrennt, zerbricht und entweiht Kultstaetten "
            "von Jerusalem bis Bethel, feiert Passa und faellt bei Megiddo - lauter Handlungen mit "
            "Ortswechsel."),
        24: (False, (["10-17"], ["1-9", "18-20"]),
            "Nachgezaehlt: nur V10-17 (Belagerung, Jojachins Kapitulation, Wegfuehrung nach Babel) "
            "sind ausgefuehrte Szene mit 234 Woertern; V1-9 und V18-20 sind Chronik-, Quellen- und "
            "Regierungsformeln samt Deutungsnotiz zu Manasses Schuld mit 317 Woertern, also Mehrheit "
            "nicht erzaehlend."),
        25: (True, (["1-12", "18-30"], ["13-17"]),
            "V1-12 und V18-30 sind durchlaufende Handlung (Belagerung, Zedekias Flucht und Blendung, "
            "Tempelbrand, Hinrichtungen in Ribla, Gedaljas Ermordung, Jojachins Begnadigung); V13-17 "
            "ist reines Bronzeinventar mit Saeulenmassen, sauber an Versgrenzen abtrennbar."),
    },
    "esther": {
        1: (True, (["1-5", "9-22"], ["6-8"]),
            "V.6 ist reine statische Ausstattungsbeschreibung ohne Akteur, V.7 Gefaess-Inventar, V.8 "
            "ausdrueckliche Rechts-/Brauchnotiz ('In accordance with the law, the drinking was not "
            "compulsory') - kein Zeitverlauf, und der Bruch liegt sauber zwischen der Handlung V.5 "
            "und V.9 (92 von 666 Woertern nachgezaehlt)."),
        2: (True, (["1-11", "15-23"], ["12-14"]),
            "V.12-14 ist durchgehend iterative Harems-Verfahrensregel ('Each young woman's turn came "
            "... The young woman then came to the king like this ... She came in to the king no more, "
            "unless') ohne benannten Akteur und ohne einmalige Szene; die Handlung setzt sauber erst "
            "V.15 wieder ein (122 von 757 Woertern nachgezaehlt)."),
        3: (True, None,
            "Hamans Aufstieg, Mordechais verweigerter Kniefall, das Losen des Pur und der erwirkte "
            "Vernichtungserlass - erzaehlter Handlungsverlauf mit kurzen Dialogen."),
        4: (True, None,
            "Mordechais Trauer im Sack, der Botenverkehr durch Hatach und Esthers Entschluss zum "
            "Fastenaufruf - Wechselrede innerhalb laufender Handlung."),
        5: (True, None,
            "Esthers Gang in den Innenhof, das erste Gastmahl und Hamans Prahlerei mit dem Bau des "
            "Galgens - reine Szenenhandlung."),
        6: (True, None,
            "Schlaflose Nacht des Koenigs, Verlesung der Chronik und Hamans erzwungene Ehrung "
            "Mordechais auf dem Pferd - dichte Handlung mit Ortswechsel."),
        7: (True, None,
            "Zweites Gastmahl, Esthers Anklage, Hamans Sturz am Polster und seine Hinrichtung am "
            "Galgen - durchgehende Szene."),
        8: (True, None,
            "Durchgehend Handlung: Siegelring an Mordechai, Esthers Fussfall und Zepterszene mit "
            "Dialog innerhalb der Szene, Abfassung und Aussendung des Gegenerlasses als erzaehlter "
            "Vorgang (Briefinhalt nur referiert, nicht zitiert), Mordechais Auszug im Koenigsgewand - "
            "keine Teilung noetig."),
        9: (True, (["1-18"], ["19-32"]),
            "V.1-18 Kampf, Toetung der zehn Hamansoehne, Esthers zweite Bitte und der zweite Tag als "
            "fortlaufende Handlung (507 Woerter); ab V.19 aetiologische Brauchnotiz im Praesens und "
            "dann Mordechais/Esthers Purim-Briefe mit Festverordnung, also Gesetzes- und Brieftext - "
            "Naht liegt sauber vor V.19, Abdeckung 1-18 + 19-32 = alle 32 Verse."),
        10: (False, None,
            "Nur Rahmennotiz ueber Ahasveros' Tribut, Quellenverweis auf die Chronik der Koenige von "
            "Medien und Persien und Schlusslob auf Mordechai - keine Szene."),
    },
    "jonah": {
        1: (True, None,
            "Jonas Flucht nach Tarsis, Sturm, Losentscheid und Wurf ins Meer mit Seeleuten als "
            "Akteuren, Ortswechsel Joppe-Schiff und Zeitverlauf; die Reden sind Szenendialog."),
        2: (False, (["1", "10"], ["2-9"]),
            "Nur V.1 (Jona betet im Fischbauch) und V.10 (der Fisch speit ihn aus) sind Handlung, "
            "V.2-9 ist Jonas eingelegter Dankpsalm und traegt die Wortmehrheit."),
        3: (True, None,
            "Zweiter Auftrag, Jonas Gang durch Ninive, Busse der Stadt und des Koenigs bis zu Gottes "
            "Umkehr; das Fastenedikt V.7-9 ist ein Befehl innerhalb der weiterlaufenden Szene und "
            "bleibt in der Minderheit."),
        4: (True, None,
            "Jonas Zorn vor der Stadt, die Laubhuette, Rizinus, Wurm und Ostwind als fortlaufende "
            "Handlung mit Tagesverlauf; die Gottesrede V.10-11 ist nur der kurze Schlussdialog."),
    },
    "daniel": {
        4: (False, (["4-9", "18-19", "28-33", "36"], ["1-3", "10-17", "20-27", "34-35", "37"]),
            "Nachgezaehlt 773 von 1252 Woertern (61,7 %) sind Briefformel und Doxologie (V.1-3), "
            "Traumvision mit Waechter-Dekret (V.10-17), Daniels Deutungs- und Mahnrede (V.20-27) "
            "sowie Schlusslobpreis (V.34-35.37); erzaehlend bleiben Traumbericht an den anwesenden "
            "Daniel, Wahnsinn und Wiedereinsetzung, der Bruch liegt sauber an Versgrenzen."),
        5: (True, None,
            "Belsazars Gastmahl mit der Schrift an der Wand, Danielis Deutung von Mene Tekel und noch "
            "in derselben Nacht Belsazars Tod und Darius' Machtuebernahme."),
        6: (True, (["1-24", "28"], ["25-27"]),
            "V25-27 ist ein zitierter Rundbrief mit derselben Formel wie Dan 4,1 plus eingelegter "
            "Doxologie ohne Akteur, Ort oder Zeitverlauf (93 von 890 Woertern, Bruch sauber an 24/25 "
            "und 27/28); V28 bleibt als erzaehlender Ausgang ueber Daniels weiteres Ergehen stehen, "
            "da es keine reine Regierungsformel mit Quellenverweis ist."),
        7: (False, None,
            "Danielis Nachtgesicht von den vier Tieren, dem Alten der Tage und dem Menschensohn samt "
            "Deutung -- apokalyptische Vision, nur der Datumsvermerk in V.1 ist Rahmen."),
        8: (False, None,
            "Die Vision von Widder und Ziegenbock in Susa mit Gabriels Deutung ueber das kleine Horn "
            "und die 2300 Abende -- reiner Visions- und Deutungstext."),
        9: (False, None,
            "Danielis langes Buss- und Suendenbekenntnisgebet und darauf Gabriels Offenbarung der "
            "siebzig Jahrwochen -- eingelegtes Gebet plus Orakel, keine Handlung."),
        10: (False, None,
            "Danielis dreiwoechiges Fasten und die Erscheinung des Mannes in Leinen am Tigris als "
            "Eroeffnung der Schlussvision -- Epiphanie- und Redeszene innerhalb der Vision, die ohne "
            "Bruch in die Prophetie von Kap. 11 uebergeht."),
        11: (False, None,
            "Die durchgehende Engelrede ueber die Perserkoenige, den Griechenkoenig und die Kriege "
            "der Koenige des Nordens und des Suedens -- Prophetenorakel ohne Szenenhandlung."),
        12: (False, None,
            "Fortsetzung der Engelrede ueber Michael, Auferstehung, Versiegeln des Buches und die "
            "Zeitangaben von 1290 und 1335 Tagen -- eschatologische Rede."),
    },
    "genesis": {
        1: (True, None,
            "Sechs Schoepfungstage mit einem handelnden Akteur und Zeitverlauf. Bericht, nicht "
            "Szene: die Einstufung stuetzt sich auf Handlung und Zeitverlauf, nicht auf "
            "Ortswechsel, und faellt unter keinen Ausschluss der Regel."),
        2: (True, None,
            "Ruhetag, Bildung des Menschen, Pflanzung des Gartens, Benennung der Tiere und "
            "Bildung der Frau - fortlaufende Handlung; die Stromnotiz V.10-14 bleibt Minderheit."),
        3: (True, None,
            "Schlange, Uebertretung, Verhoer und Vertreibung - durchgehende Szene; die "
            "Fluchsprueche stehen als Rede innerhalb der laufenden Handlung."),
        4: (True, (["1-16", "25-26"], ["17-24"]),
            "Kain und Abel (V.1-16) und die Geburt Sets (V.25-26) sind Handlung; V.17-24 ist "
            "Kains Geschlechterliste mit Lamechs Schwertlied - Naht an V.17 und V.25 sauber."),
        5: (False, None,
            "Toledot Adams: zehn Generationen als reine Geschlechterliste mit Lebensaltern; nur "
            "die Henoch-Notiz V.24 ragt heraus und traegt keine Wortmehrheit."),
        6: (True, (["1-13", "17-22"], ["14-16"]),
            "Menschensoehne, Verderben der Erde, Noahs Auftrag und seine Ausfuehrung sind "
            "Handlung; V.14-16 sind Bauvorschriften der Arche mit Massangaben."),
        7: (True, None,
            "Einzug in die Arche, Beginn der Flut und das Steigen des Wassers ueber 150 Tage - "
            "Handlung mit ausdruecklichem Zeitverlauf."),
        8: (True, None,
            "Fallen des Wassers, Rabe und Taube, Verlassen der Arche und Altarbau - fortlaufende "
            "Handlung mit Datumsangaben."),
        9: (True, (["18-29"], ["1-17"]),
            "V.1-17 ist Segens- und Bundesrede mit Blutverbot und Toetungsverbot, also "
            "Gesetzestext; erzaehlend sind Noahs Weinberg, die Trunkenheitsszene, der "
            "Kanaan-Spruch und die Sterbenotiz ab V.18."),
        10: (False, None,
            "Voelkertafel: Nachkommen Japhets, Hams und Sems als Geschlechter- und "
            "Voelkerliste; die Nimrod-Notiz V.8-12 traegt keine Mehrheit."),
        11: (True, (["1-9", "31-32"], ["10-30"]),
            "Turmbau zu Babel (V.1-9) und Terachs Aufbruch nach Haran (V.31-32) sind Handlung; "
            "V.10-30 ist die Sem-Genealogie bis Abram."),
        12: (True, None,
            "Ruf Abrams, Zug nach Kanaan, Altarbauten und der Aufenthalt in Aegypten mit der "
            "Schwesterluege - Handlung mit mehrfachem Ortswechsel."),
        13: (True, None,
            "Rueckkehr aus Aegypten, Streit der Hirten, Trennung von Lot und Zug nach Mamre."),
        14: (True, None,
            "Vierkoenigskrieg, Lots Gefangennahme, Abrams Befreiungszug und die Begegnung mit "
            "Melchisedek - Feldzug mit Ortswechsel und Zeitverlauf."),
        15: (True, None,
            "Naechtliche Szene: Abrams Einwand, der Blick auf die Sterne, das zerteilte Getier, "
            "die Raubvoegel und der Feuerofen zwischen den Stuecken - Handlung mit Wechselrede."),
        16: (True, None,
            "Hagar und Sarai, Flucht zur Quelle, Begegnung mit dem Engel und Ismaels Geburt."),
        17: (True, (["23-27"], ["1-22"]),
            "V.1-22 ist Bundesrede mit der Beschneidungsvorschrift - Kultvorschrift, keine "
            "Handlung; erzaehlend ist nur die Ausfuehrung an Ismael und dem Haus (V.23-27)."),
        18: (True, None,
            "Die drei Maenner bei Mamre, Saras Lachen und Abrahams Fuerbitte fuer Sodom - "
            "Szene mit Bewirtung, Ortswechsel und Wechselrede."),
        19: (True, None,
            "Sodom: die Engel bei Lot, der Auflauf vor dem Haus, Flucht nach Zoar, Salzsaeule "
            "und die Hoehlenszene mit Lots Toechtern - durchgehende Handlung."),
        20: (True, None,
            "Abimelech nimmt Sara, Traumwarnung, Rueckgabe und Suehnegabe - Szene mit Dialog."),
        21: (True, None,
            "Isaaks Geburt, Vertreibung Hagars und Ismaels, Rettung an der Quelle und der "
            "Brunnenvertrag mit Abimelech in Beerscheba."),
        22: (True, (["1-19"], ["20-24"]),
            "Die Bindung Isaaks mit Aufbruch, Dreitagesweg, Altar, Widder und Rueckkehr ist "
            "Handlung; V.20-24 ist die angehaengte Nachor-Genealogie."),
        23: (True, None,
            "Saras Tod in Hebron und der Kauf der Hoehle Machpela - Verhandlungsszene vor den "
            "Hethitern mit Abschluss am Stadttor."),
        24: (True, None,
            "Brautwerbung fuer Isaak: Schwur, Reise nach Nahor, Zeichen am Brunnen, Verhandlung "
            "im Haus Labans und Heimkehr mit Rebekka - laengste durchlaufende Reiseerzaehlung."),
        25: (True, (["7-11", "19-34"], ["1-6", "12-18"]),
            "Abrahams Tod und Begraebnis (V.7-11) sowie Geburt und Linsengericht der Zwillinge "
            "(V.19-34) sind Handlung; V.1-6 (Keturas Soehne) und V.12-18 (Ismaels Geschlechter) "
            "sind Listen."),
        26: (True, None,
            "Isaak in Gerar: Hungersnot, Schwesterluege, Streit um die Brunnen, Zug nach "
            "Beerscheba und Vertrag mit Abimelech."),
        27: (True, None,
            "Der erschlichene Segen: Rebekkas Anstiftung, das Ziegenfell, Isaaks Taeuschung, "
            "Esaus Schrei und Jakobs Flucht - Szene mit Wechselrede und Zeitdruck."),
        28: (True, None,
            "Jakobs Aufbruch nach Haran, der Traum von der Leiter in Bethel und das Geluebde am "
            "aufgerichteten Stein."),
        29: (True, None,
            "Ankunft am Brunnen, Rahel und Lea, die vertauschte Hochzeitsnacht und die "
            "vierzehn Dienstjahre - Handlung mit langem Zeitverlauf."),
        30: (True, None,
            "Der Kinderwettstreit von Lea und Rahel, die Alraunen und Jakobs Zuchtlist mit den "
            "geschaelten Staeben."),
        31: (True, None,
            "Heimliche Flucht vor Laban, die gestohlenen Hausgoetter, Labans Verfolgung und "
            "Durchsuchung und der Steinhaufen als Vertrag."),
        32: (True, None,
            "Boten an Esau, Teilung des Lagers, das Geschenk vor dem Zug und der Ringkampf am "
            "Jabbok - Nachtszene mit Ortswechsel."),
        33: (True, None,
            "Begegnung mit Esau, Verbeugung der Familie, Annahme des Geschenks und Jakobs Zug "
            "nach Sukkot und Sichem."),
        34: (True, None,
            "Dina und Sichem, die Beschneidungsforderung als Kriegslist und das Blutbad der "
            "Soehne Jakobs - durchgehende Handlung."),
        35: (True, None,
            "Zug nach Bethel, Vergraben der fremden Goetter, Rahels Tod bei Bethlehem und "
            "Isaaks Begraebnis; die Soehneliste V.23-26 bleibt Minderheit der Woerter."),
        36: (False, None,
            "Toledot Esaus: Frauen, Soehne, Fuersten und die Koenigsliste Edoms - reine "
            "Geschlechter- und Regentenliste."),
        37: (True, None,
            "Josephs Traeume, der Rock, der Wurf in die Zisterne, der Verkauf an die Ismaeliter "
            "und Jakobs Trauer - Handlung mit Ortswechsel."),
        38: (True, None,
            "Juda und Tamar: Er, Onan, das Versprechen an Schela, die Szene am Weg nach Timna "
            "und das Urteil ueber die Schwangere."),
        39: (True, None,
            "Joseph bei Potifar, die Nachstellung der Herrin, das zurueckgelassene Kleid und "
            "das Gefaengnis."),
        40: (True, None,
            "Muendschenk und Baecker im Gefaengnis: Traeume, Deutung und der Vollzug am dritten "
            "Tag - Szene mit Zeitverlauf."),
        41: (True, None,
            "Pharaos Traeume, Josephs Deutung und Einsetzung, die sieben fetten und sieben "
            "mageren Jahre - Handlung ueber vierzehn Jahre."),
        42: (True, None,
            "Erste Reise der Brueder nach Aegypten, Spionagevorwurf, Simeons Zuruecklassung und "
            "die Rueckkehr mit dem Geld in den Saecken."),
        43: (True, None,
            "Zweite Reise der Brueder nach Aegypten mit Benjamin, Israels Einwilligung und das Mahl "
            "in Josephs Haus - durchgehende Handlung mit Ortswechsel."),
        44: (True, None,
            "Der Silberbecher in Benjamins Sack, Verfolgung, Durchsuchung und Judas Fuerbitte vor "
            "Joseph - Szene mit Wechselrede, die Rede (V.18-34) bleibt Minderheit der Woerter."),
        45: (True, None,
            "Joseph gibt sich den Bruedern zu erkennen, Pharaos Einladung und die Rueckreise nach "
            "Kanaan zu Jakob - fortlaufende Handlung."),
        46: (True, (["1-7", "28-34"], ["8-27"]),
            "Erzaehlter Aufbruch nach Beerscheba und Wiedersehen in Goschen umrahmen die Namensliste "
            "der 70 Seelen, die nach Aegypten zogen - saubere Naht an V.8 und V.28."),
        47: (True, None,
            "Jakob und die Brueder vor dem Pharao, Josephs Hungersnot-Verwaltung (Land- und Viehkauf) "
            "und Jakobs Begraebniseid - Handlung mit Zeitverlauf."),
        48: (True, None,
            "Krankenbettszene: Jakob adoptiert Ephraim und Manasse und kreuzt die Haende, Joseph "
            "widerspricht - Handlung mit Dialog, Segensspruch nur eingebettet."),
        49: (False, (["28-33"], ["1-27"]),
            "Jakobs Stammesspruch-Gedicht ueber die zwoelf Soehne (V.1-27, rund 570 Woerter) "
            "ueberwiegt klar; nur die Begraebnisanweisung und Jakobs Tod ab V.28 sind Handlung."),
        50: (True, None,
            "Einbalsamierung und Trauerzug zur Hoehle Machpela, Versoehnung mit den Bruedern und "
            "Josephs Tod - durchgehende Handlung mit Ortswechsel."),
    },
    # Markus, Roemer und Offenbarung stehen als Planfassung fuer V07 im Bestand;
    # Jesaja war der gestrichene V06-Korpus. Alle vier sind hier eingestuft, damit
    # produktion/v07_v08_moeglichkeiten.py gegen gemessene statt vermutete Werte
    # rechnet.
    "mark": {
        1: (True, None,
            "Taeufer, Taufe, Wueste, Berufung der ersten Juenger und der Tag in Kafarnaum bis "
            "zum Aussaetzigen - dichte Handlungsfolge mit Ortswechseln."),
        2: (True, None,
            "Der Gelaehmte durchs Dach, Berufung des Levi, Mahl mit den Zoellnern, Fastenfrage "
            "und Aehrenraufen - fuenf Szenen, die Streitworte stehen jeweils in der Handlung."),
        3: (True, None,
            "Heilung der verdorrten Hand am Sabbat, Andrang am See, Einsetzung der Zwoelf, "
            "Beelzebul-Vorwurf und die Mutter mit den Bruedern vor dem Haus."),
        4: (False, (["35-41"], ["1-34"]),
            "V.1-34 ist der Gleichniszyklus vom Saemann bis zum Senfkorn - zusammenhaengende "
            "Lehrrede ohne Handlungsfortschritt und klare Wortmehrheit; erzaehlend ist nur die "
            "Sturmstillung V.35-41."),
        5: (True, None,
            "Der Besessene von Gerasa mit der Schweineherde, die blutfluessige Frau und die "
            "Auferweckung der Tochter des Jairus - drei Szenen mit Ortswechsel."),
        6: (True, None,
            "Ablehnung in Nazaret, Aussendung der Zwoelf, Tod des Taeufers, Speisung der "
            "Fuenftausend und der Gang auf dem See."),
        7: (True, (["24-37"], ["1-23"]),
            "V.1-23 ist das Streitgespraech um Reinheit samt anschliessender Belehrung im Haus - "
            "zusammenhaengende Rede; erzaehlend sind die Syrophoenizierin und der Taubstumme "
            "ab V.24."),
        8: (True, None,
            "Speisung der Viertausend, Zeichenforderung, der Blinde von Betsaida, das Bekenntnis "
            "bei Caesarea Philippi und die erste Leidensankuendigung."),
        9: (True, None,
            "Verklaerung, der besessene Knabe, zweite Leidensankuendigung und der Rangstreit in "
            "Kafarnaum; die Mahnworte V.38-50 bleiben Minderheit der Woerter."),
        10: (True, None,
            "Ehefrage, Kindersegnung, der reiche Mann, dritte Leidensankuendigung, die Bitte der "
            "Zebedaeussoehne und Bartimaeus - Szenen mit wechselnden Gegenuebern und Wegstrecke."),
        11: (True, None,
            "Einzug in Jerusalem, verfluchter Feigenbaum, Tempelreinigung und die Frage nach der "
            "Vollmacht - Handlung ueber drei Tage."),
        12: (False, None,
            "Winzergleichnis und die Reihe der Streitgespraeche (Steuer, Auferstehung, hoechstes "
            "Gebot, Davidssohn) tragen die Wortmehrheit als zusammenhaengende Rede; nur das "
            "Scherflein der Witwe V.41-44 ist Szene. Im Zweifel gegen den Erzaehlanteil."),
        13: (False, None,
            "Endzeitrede auf dem Oelberg - durchgehende apokalyptische Rede ohne "
            "Handlungsfortschritt."),
        14: (True, None,
            "Salbung in Betanien, Verrat des Judas, Passamahl, Gethsemane, Gefangennahme, "
            "Verhoer vor dem Hohen Rat und Petrus' Verleugnung."),
        15: (True, None,
            "Prozess vor Pilatus, Barabbas, Verspottung, Kreuzigung, Tod und Grablegung."),
        16: (True, None,
            "Die Frauen am leeren Grab, die Erscheinungen und die Himmelfahrt - Handlung mit "
            "Ortswechsel."),
    },
    # Jesaja, Roemer und Offenbarung sind Gattung, nicht Grenzfall: Prophetenrede,
    # Brief und apokalyptische Vision stehen woertlich im Ausschluss der Regel.
    # Sie sind ganzkapitelweise eingestuft, ohne Teilung - Ausnahme ist der
    # Hiskija-Einschub Jesaja 36-39.
    "isaiah": dict(
        list(_gleichfoermig(1, 35, False,
            "Prophetische Rede: Gerichts-, Droh- und Heilsworte ueber Juda und die Voelker, "
            "dazu die Visionsberichte; keine fortlaufende Handlung.").items())
        + [(36, (True, None,
            "Sanheribs Feldzug: der Rabschake vor der Mauer Jerusalems, Botenwechsel und die "
            "Antwort der Gesandten - Szene mit Akteuren und Ort.")),
           (37, (True, None,
            "Hiskijas Gang zum Tempel, Jesajas Botenwort, der zweite Brief und der Abzug des "
            "Heeres bis zu Sanheribs Ermordung - Handlung mit Zeitverlauf.")),
           (38, (False, None,
            "Krankheit und Genesung Hiskijas rahmen sein aufgeschriebenes Danklied (V.9-20), "
            "das die Wortmehrheit traegt. Konservativ ganz nicht erzaehlend - die Naht liesse "
            "sich ziehen, sie ist hier nicht gemessen.")),
           (39, (True, None,
            "Die Gesandtschaft aus Babel, Hiskijas Vorfuehrung des Schatzhauses und Jesajas "
            "Ansage - kurze, geschlossene Szene."))]
        + list(_gleichfoermig(40, 66, False,
            "Trostbuch und Gottesknechtlieder: durchgehend prophetische Rede, Klage und "
            "Verheissung ohne Handlungstraeger.").items())
    ),
    "romans": _gleichfoermig(1, 16, False,
        "Brief des Paulus an die Roemer - Lehrschreiben mit Grussliste, ohne Handlung."),
    "revelation": _gleichfoermig(1, 22, False,
        "Apokalyptische Vision: Sendschreiben, Siegel, Posaunen, Schalen und Schlussbilder - "
        "steht woertlich im Ausschluss der Regel."),
}

# Die drei Varianten. Struktur bewusst verschieden: Anthologie ganzer Buecher,
# ein durchlaufender Lebensbogen ueber die Buchgrenze, ein AT/NT-Mischkorpus.
VARIANTEN = {
    "V06-A": {
        "name": "1 Samuel + Rut + Ester",
        "bauart": "Anthologie",
        "korpus": [("1 samuel", 1, 31), ("ruth", 1, 4), ("esther", 1, 10)],
        "eigenname": "Samuel",
        "nachttauglichkeit":
            "EINSCHAETZUNG, KEINE MESSUNG. Rut 1-4 ist der ruhigste Erzaehlstoff im ganzen "
            "Pool. Kritisch: 1 Sam 15 (Bann an Amalek, Agag zerhauen), 1 Sam 17 (Enthauptung "
            "Goliats), 1 Sam 18,25-27 (zweihundert Vorhaeute als Brautpreis), 1 Sam 22 "
            "(Priestermord in Nob, 85 Erschlagene), 1 Sam 28 (Totenbeschwoererin von En-Dor, "
            "unheimlich statt beruhigend), 1 Sam 31 (Sauls Selbstmord und Leichenschaendung), "
            "Ester 9 (75.000 Erschlagene, zehn Soehne aufgehaengt). Rund ein Sechstel der "
            "Laufzeit liegt in solchen Passagen, alle im Mittelteil.",
        "staerke":
            "Hoechster Erzaehlanteil der drei und drei vollstaendige Buecher ohne einen "
            "einzigen Schnitt, also kein Torso fuer spaeter. Drei abgeschlossene Geschichten "
            "mit je eigenem Ende geben dem Nachthoerer drei Ruhepunkte statt eines.",
        "risiko":
            "Der Eigenname 'Samuel' traegt den Titel schwaecher als 'David' oder 'Esther', "
            "und die drei Buecher haben ausser der Richterzeit keine gemeinsame Klammer. "
            "1 Samuel ist der gewalttaetigste der drei Korpora im Mittelteil.",
        "rest_fuer_v07":
            "170.132 W. Apostelgeschichte bleibt vollstaendig frei - das einzige noch "
            "unverplante NT-Buch. Dazu 2 Samuel, beide Koenigsbuecher, Josua, Richter, "
            "Exodus, Jona, Daniel 4-12 und Genesis 43-50, alle ungeschnitten.",
    },
    "V06-B": {
        "name": "1 Samuel 16-31 + 2 Samuel (Davids Leben)",
        "bauart": "Lebensbogen",
        "korpus": [("1 samuel", 16, 31), ("2 samuel", 1, 24)],
        "eigenname": "David",
        "nachttauglichkeit":
            "EINSCHAETZUNG, KEINE MESSUNG. Die schwerste Passage im gesamten Pool: 2 Sam 13 "
            "(Amnons Vergewaltigung Tamars) ist um 2 Uhr nachts nicht zumutbar. Dazu 2 Sam 11 "
            "(Ehebruch und Auftragsmord), 2 Sam 12 (Tod des Kindes), 2 Sam 4 (abgeschlagener "
            "Kopf Ischboschets), 2 Sam 18 (Absaloms Tod an der Eiche), 2 Sam 21 (sieben Soehne "
            "Sauls aufgehaengt, Rizpas Totenwache) und aus dem ersten Teil 1 Sam 17, 22, 28, 31. "
            "Der Stoff wird nach hinten duesterer statt ruhiger - genau die falsche Richtung "
            "fuer ein Einschlafvideo.",
        "staerke":
            "Ein einziger durchlaufender Erzaehlbogen von der Salbung bis zum Tod, ohne "
            "Themenwechsel - das ist formal am naechsten an V03 (Johannes), dem Video, aus dem "
            "Regel M8 stammt. 'David' ist der staerkste Eigenname im ganzen verfuegbaren Pool.",
        "risiko":
            "Dominantes Buch ist 2 Samuel mit nur 60,9 % - die knappste Dominanz der drei, und "
            "der Buchname 'Second Samuel' taugt nicht als Titelwort, der Korpus laeuft "
            "faktisch unter 'David'. Ausserdem bleibt 1 Samuel 1-15 als Torso zurueck.",
        "rest_fuer_v07":
            "169.685 W, aber davon 1 Samuel 1-15 (11.156 W) als Torso: Eli, Samuels Berufung "
            "und Sauls Aufstieg ohne Fortsetzung, allein zu kurz fuer ein Video. "
            "Apostelgeschichte, beide Koenigsbuecher, Josua, Richter, Exodus, Rut, Ester, "
            "Jona, Daniel 4-12 und Genesis 43-50 bleiben frei.",
    },
    "V06-C": {
        "name": "Apostelgeschichte 1-12 + 1 Samuel",
        "bauart": "AT + NT",
        "korpus": [("acts", 1, 12), ("1 samuel", 1, 31)],
        "eigenname": "Samuel",
        "nachttauglichkeit":
            "EINSCHAETZUNG, KEINE MESSUNG. Apg 1-12 ist der ruhigste NT-Erzaehlstoff im Pool; "
            "kritisch dort nur Apg 5 (Hananias und Saphira fallen tot um), Apg 7,54-60 "
            "(Steinigung des Stephanus) und Apg 12 (Jakobus enthauptet, Herodes von Wuermern "
            "gefressen). Der 1-Samuel-Teil bringt dieselben Stellen wie Variante A mit "
            "(1 Sam 15, 17, 18, 22, 28, 31).",
        "staerke":
            "Die einzige Variante mit NT-Anteil, die das Gate haelt, und mit 33.460 W die "
            "laengste - naeher an den 3,8 h, wo die bisherigen Videos ihre Zuschauer "
            "am laengsten halten. Apg 1-12 endet mit einer echten Schlusskadenz "
            "(Tod des Herodes, 'das Wort Gottes wuchs'), ist also kein abgeschnittener Torso.",
        "risiko":
            "Mit 83,6 % der niedrigste Erzaehlanteil der drei; Apg 1-12 traegt selbst nur "
            "70,6 %, weil Pfingstpredigt, Tempelrede und Stephanusrede darin liegen. Der "
            "Sprung zwischen Jerusalem und der Richterzeit hat keine erzaehlerische Bruecke, "
            "und Apg 13-28 bleibt als Torso zurueck.",
        "rest_fuer_v07":
            "168.154 W, davon Apostelgeschichte 13-28 (13.321 W) als Torso: die Paulusreisen "
            "ohne Anfang. 2 Samuel, beide Koenigsbuecher, Josua, Richter, Exodus, Rut, Ester, "
            "Jona, Daniel 4-12 und Genesis 43-50 bleiben ungeschnitten.",
    },
}


def _hole(ref, cache):
    """Holt einen Versbereich mit der Zaehlmethode aus wortzahlen.py."""
    if ref in cache:
        return cache[ref]
    url = "https://bible-api.com/%s?translation=webbe" % urllib.parse.quote(ref)
    fehler = None
    for versuch in range(6):
        try:
            with urllib.request.urlopen(url, timeout=60) as antwort:
                daten = json.load(antwort)
            text = " ".join(re.sub(r"\s+", " ", v["text"]).strip() for v in daten["verses"])
            cache[ref] = {"w": len(text.split()), "v": len(daten["verses"])}
            return cache[ref]
        except Exception as e:                      # noqa: BLE001
            fehler = e
            time.sleep(3 * (versuch + 1))
    raise SystemExit("Abruf gescheitert fuer %s: %s" % (ref, fehler))


def einstufung_rechnen():
    """Baut die Kapiteltabelle und misst alle Teilungen nach."""
    kapitel = json.load(open(KAPITEL))
    cache = json.load(open(VERSE)) if os.path.exists(VERSE) else {}
    vorher = len(cache)
    tabelle, verworfen = {}, []
    for buch, kapitel_map in EINSTUFUNG.items():
        for nummer, (erzaehlend, teilung, begruendung) in sorted(kapitel_map.items()):
            ref = "%s %d" % (buch, nummer)
            if ref not in kapitel:
                raise SystemExit("%s fehlt in %s - erst produktion/wortzahlen.py laufen lassen" % (ref, KAPITEL))
            woerter, verse = kapitel[ref]["w"], kapitel[ref]["v"]
            eintrag = {
                "buch": buch,
                "kapitel": nummer,
                "woerter": woerter,
                "erzaehlend": erzaehlend,
                "begruendung": begruendung,
            }
            if teilung is None:
                eintrag["erzaehlend_woerter"] = woerter if erzaehlend else 0
            else:
                erz_bereiche, nicht_bereiche = teilung
                teile = {g: [_hole("%s:%s" % (ref, b), cache) for b in bs]
                         for g, bs in (("e", erz_bereiche), ("n", nicht_bereiche))}
                summe_w = sum(t["w"] for gs in teile.values() for t in gs)
                summe_v = sum(t["v"] for gs in teile.values() for t in gs)
                if summe_w != woerter or summe_v != verse:
                    # Teilung deckt das Kapitel nicht sauber ab -> konservativ verwerfen
                    verworfen.append("%s (Teile %d W/%d V gegen Kapitel %d W/%d V)"
                                     % (ref, summe_w, summe_v, woerter, verse))
                    eintrag["erzaehlend"] = False
                    eintrag["erzaehlend_woerter"] = 0
                    eintrag["begruendung"] = begruendung + " [Teilung verworfen, konservativ nicht erzaehlend]"
                else:
                    eintrag["erzaehlend_woerter"] = sum(t["w"] for t in teile["e"])
                    eintrag["teilung"] = {"erzaehlend": erz_bereiche, "nicht_erzaehlend": nicht_bereiche}
            eintrag["erzaehlanteil"] = round(eintrag["erzaehlend_woerter"] / woerter, 4)
            tabelle[ref] = eintrag
    if len(cache) != vorher:
        json.dump(cache, open(VERSE, "w"), indent=0, sort_keys=True)
    return tabelle, verworfen


def spanne(tabelle, buch, von, bis):
    refs = ["%s %d" % (buch, i) for i in range(von, bis + 1)]
    return (sum(tabelle[r]["woerter"] for r in refs),
            sum(tabelle[r]["erzaehlend_woerter"] for r in refs))


def buchlaenge(buch):
    """Kapitelzahl des Buches nach produktion/korpus/kapitel.json."""
    kapitel = json.load(open(KAPITEL))
    praefix = buch + " "
    return sum(1 for ref in kapitel if ref.startswith(praefix)
               and ref[len(praefix):].isdigit())


def vollwerk_pruefen(tabelle, buch, teile):
    """Ist das dominante Buch ein Erzaehlwerk in voller Laenge? Zwei Bedingungen,
    beide gemessen, keine Einschaetzung:

      1. volle Laenge - alle Kapitel des Buches stehen im Korpus,
      2. Erzaehlwerk  - das Buch selbst haelt gate_erzaehlanteil_min, kapitelweise
                        gemessen wie der Korpus auch.

    Nur wenn beides zutrifft, gilt das tiefere Band (siehe band()). Ein
    beschnittenes Buch qualifiziert nicht: sonst liesse sich jede Laufzeit durch
    Wegschneiden von Kapiteln passend machen."""
    im_korpus = sorted({k for t in teile if t["buch"] == buch
                        for k in range(t["von"], t["bis"] + 1)})
    ganz = im_korpus == list(range(1, buchlaenge(buch) + 1))
    refs = ["%s %d" % (buch, k) for k in im_korpus]
    w = sum(tabelle[r]["woerter"] for r in refs)
    e = sum(tabelle[r]["erzaehlend_woerter"] for r in refs)
    anteil = e / w if w else 0.0
    return {
        "volle_laenge": ganz,
        "kapitel_im_korpus": len(im_korpus),
        "kapitel_des_buches": buchlaenge(buch),
        "erzaehlanteil_des_buches": round(anteil, 4),
        "ist_erzaehlwerk": anteil >= GATE_ERZAEHLEND,
        "erfuellt": ganz and anteil >= GATE_ERZAEHLEND,
    }


def variante_rechnen(tabelle, kuerzel, v):
    teile = []
    for buch, von, bis in v["korpus"]:
        w, e = spanne(tabelle, buch, von, bis)
        teile.append({"buch": buch, "von": von, "bis": bis, "kapitel": bis - von + 1,
                      "woerter": w, "erzaehlend_woerter": e})
    woerter = sum(t["woerter"] for t in teile)
    erz = sum(t["erzaehlend_woerter"] for t in teile)
    pro_buch = {}
    for t in teile:
        pro_buch[t["buch"]] = pro_buch.get(t["buch"], 0) + t["woerter"]
    dominant, dom_w = max(pro_buch.items(), key=lambda x: x[1])
    ergebnis = {
        "kuerzel": kuerzel,
        "name": v["name"],
        "bauart": v["bauart"],
        "teile": teile,
        "woerter": woerter,
        "erzaehlend_woerter": erz,
        "erzaehlanteil": round(erz / woerter, 4),
        "laufzeit_h": round(woerter / WPM / 60, 3),
        "laufzeit": "%d:%02d h" % (int(woerter / WPM / 60), round((woerter / WPM / 60 % 1) * 60)),
        "dominantes_buch": dominant,
        "dominanz": round(dom_w / woerter, 4),
        "eigenname": v["eigenname"],
        "nachttauglichkeit": v["nachttauglichkeit"],
        "staerke": v["staerke"],
        "risiko": v["risiko"],
        "rest_fuer_v07": v["rest_fuer_v07"],
    }
    vw = vollwerk_pruefen(tabelle, dominant, teile)
    grenzen = band(vw["erfuellt"])
    zweit = sorted(pro_buch.values(), reverse=True)
    ergebnis["vollwerk"] = vw
    ergebnis["abstand"] = round((dom_w - (zweit[1] if len(zweit) > 1 else 0)) / woerter, 4)
    ergebnis["zielband_woerter"] = list(grenzen)
    # Gate 1.13, Strukturfassung (entschieden 2026-09-02). Der Erzaehlanteil des
    # Gesamtkorpus steht als "erzaehlanteil" im Ergebnis und wird gemeldet - er
    # ist KEINE Pruefung mehr. Begruendung in produktion/workflow-gates.md.
    ergebnis["pruefungen"] = {
        "band": grenzen[0] <= woerter <= grenzen[1],
        "dominanz": ergebnis["dominanz"] >= GATE_DOMINANZ,
        "erzaehlwerk": vw["ist_erzaehlwerk"],
        "volle_laenge": vw["volle_laenge"],
        "abstand": ergebnis["abstand"] >= GATE_ABSTAND,
    }
    ergebnis["bestanden"] = all(ergebnis["pruefungen"].values())
    return ergebnis


def main():
    tabelle, verworfen = einstufung_rechnen()
    json.dump({"regel": REGEL, "quelle": "bible-api.com, translation=webbe",
               "zaehlmethode": "Verstexte mit Leerzeichen verbunden, dann str.split()",
               "hinweis_flagge": ("Bei geteilten Kapiteln ist 'erzaehlend' nur ein Etikett "
                                  "nach der gemessenen Wortmehrheit; massgeblich ist "
                                  "'erzaehlend_woerter' aus den gemessenen Versbereichen."),
               "kapitel": tabelle},
              open(AUS_EINSTUFUNG, "w"), ensure_ascii=False, indent=1)
    if verworfen:
        print("Verworfene Teilungen (konservativ als nicht erzaehlend gezaehlt):")
        for z in verworfen:
            print("  " + z)
        print()

    varianten = [variante_rechnen(tabelle, k, v) for k, v in VARIANTEN.items()]
    json.dump({"wpm": WPM,
               "zielband_woerter": list(BAND),
               "zielband_woerter_vollwerk": list(BAND_VOLLWERK),
               "gate_erzaehlanteil": GATE_ERZAEHLEND, "gate_dominanz": GATE_DOMINANZ,
               "gate_abstand": GATE_ABSTAND,
               "gate_fassung": ("Struktur - dominantes Buch >= gate_dominanz_min, selbst "
                                "Erzaehlwerk, in voller Laenge, >= gate_abstand_min vor dem "
                                "zweitgroessten Buch. Der Erzaehlanteil des Gesamtkorpus wird "
                                "gemeldet und gatet nicht."),
               "schwellen_quelle": "produktion/config.md",
               "varianten": varianten},
              open(AUS_VARIANTEN, "w"), ensure_ascii=False, indent=1)

    print("Kapitel eingestuft: %d  |  davon erzaehlend gezaehlt: %d"
          % (len(tabelle), sum(1 for e in tabelle.values() if e["erzaehlend_woerter"] > 0)))
    gesamt_w = sum(e["woerter"] for e in tabelle.values())
    gesamt_e = sum(e["erzaehlend_woerter"] for e in tabelle.values())
    print("Wortmasse gesamt: %d W, davon erzaehlend %d W (%.1f %%)\n"
          % (gesamt_w, gesamt_e, gesamt_e / gesamt_w * 100))

    print("%-6s %-12s %8s %9s %9s %-11s %s" % ("", "Bauart", "Woerter", "erzaehl.", "Laufzeit", "dominant", "Gates"))
    alle_ok = True
    for v in varianten:
        marken = "".join(("+" if v["pruefungen"][p] else "-")
                         for p in ("band", "dominanz", "erzaehlwerk", "volle_laenge", "abstand"))
        print("%-6s %-12s %8s %8.2f%% %9s %-11s %s %s"
              % (v["kuerzel"], v["bauart"], "{:,}".format(v["woerter"]),
                 v["erzaehlanteil"] * 100, v["laufzeit"], v["dominantes_buch"],
                 marken, "BESTANDEN" if v["bestanden"] else "GERISSEN"))
        alle_ok = alle_ok and v["bestanden"]
    print("\n(Gate 1.13, Strukturfassung - Marken in dieser Reihenfolge:")
    print(" Zielband | Dominanz >= %g %% | dominantes Buch ist Erzaehlwerk (>= %g %%) |"
          % (GATE_DOMINANZ * 100, GATE_ERZAEHLEND * 100))
    print(" in voller Laenge gelesen | Abstand zum zweitgroessten Buch >= %g Punkte)"
          % (GATE_ABSTAND * 100))
    print("(Der Erzaehlanteil des Gesamtkorpus wird gemeldet, gatet aber NICHT.)")
    print("(Zielband %d-%d W; ist das dominante Buch Erzaehlwerk in voller Laenge: %d-%d W)"
          % (BAND[0], BAND[1], BAND_VOLLWERK[0], BAND_VOLLWERK[1]))
    print("(Alle Schwellen stehen in produktion/config.md, nirgends sonst.)")
    for v in varianten:
        print("\n%s - %s" % (v["kuerzel"], v["name"]))
        for t in v["teile"]:
            print("   %-10s %2d-%-2d  %6s W  erzaehlend %6s W (%4.0f %%)"
                  % (t["buch"], t["von"], t["bis"], "{:,}".format(t["woerter"]),
                     "{:,}".format(t["erzaehlend_woerter"]),
                     t["erzaehlend_woerter"] / t["woerter"] * 100))
        print("   Summe %s W, erzaehlend %s W (%.1f %%), %s, dominant %s mit %.0f %%"
              % ("{:,}".format(v["woerter"]), "{:,}".format(v["erzaehlend_woerter"]),
                 v["erzaehlanteil"] * 100, v["laufzeit"], v["dominantes_buch"], v["dominanz"] * 100))
    if not alle_ok:
        print("\nMindestens eine Variante reisst ein Gate.")
        return 1
    print("\nAlle drei Varianten bestehen Zielband, 80-%-Gate und Dominanz.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
