# -*- coding: utf-8 -*-

# String: String
# product id, product description
dict_titles = {
    
    # RADOLAN (online) base products:
    'EY': "Europäische quantitative Radardaten, qualitätskorrigiert",
    'EZ': "Europäische quantitative Radardaten, nicht qualitätskorrigiert",
    'RH': "(qualitätsgeprüfte) Radardaten nach Abschattungskorrektur und nach Anwendung der verfeinerten Z-R-Beziehung in Niederschlagshöhen umgerechnet und auf eine Stunde aufsummiert",
    'RB': "Radardaten, vorangeeicht mit einem Faktor, Stundensumme",
    'RW': "Radardaten nach Aneichung mit der gewichteten Mittelung aus zwei Standardverfahren, Stundensumme",
    'RO': "Radardaten nach Anwendung der Standard-Z-R-Beziehung in Niederschlagshöhen umgerechnet",
    'RY': "Qualitätsgeprüfte Radardaten nach Abschattungskorrektur und nach Anwendung der verfeinerten Z-R-Beziehung in Niederschlagshöhen umgerechnet",
    'RZ': "Radardaten nach Abschattungskorrektur und nach Anwendung der verfeinerten Z-R-Beziehung in Niederschlagshöhen umgerechnet",
    
    # hourly/daily sums:
    'S2': "2h-Niederschlagssumme",
    'S3': "3h-Niederschlagssumme",
    'SH': "12h-Niederschlagssumme",
    'SF': "24h-Niederschlagssumme",
    'D2': "48h-Niederschlagssumme",
    'D3': "72h-Niederschlagssumme",
    
    "DC": "Anzahl Stunden (h) am Tag mit Clutter-Kennung",
    "DF": "Anzahl Stunden (h) am Tag mit Fehlwert",
    "DI": "Tagesniederschlagssumme aus REGNIE",
    "DK": u"Tagesniederschlagssumme aus RW. Fehlwerte werden, wenn verfügbar, mit Werten aus REGNIE aufgefüllt.",
    "DM": "Max. 1h-Niederschlagssumme des Tages",
    "DR": u"Anzahl Stunden (h) am Tag mit Niederschlag ausschließlich aus Bodenmessung",
    "DS": "Anzahl Stunden (h) am Tag mit Niederschlag ≥ 0.1 mm",
    "DU": u"Anzahl Stunden (h) am Tag an denen der Bemessungsniederschlag (T > 1a) überschritten wird",
    "DW": "Tagesniederschlagssumme",
    "GA": "Skalierte Gesamtzeitraumsniederschlagssumme",
    "GC": "Anzahl Stunden (h) im Gesamtzeitraum mit Clutter-Kennung",
    "GF": "Anzahl Stunden (h) im Gesamtzeitraum mit Fehlwert",
    "GI": "Gesamtzeitraumsniederschlagssumme aus REGNIE",
    "GK": u"Gesamtzeitraumsniederschlagssumme aus DW. Fehlwerte werden, wenn verfügbar, mit Werten aus REGNIE aufgefüllt.",
    "GM": "Max. 1h-Niederschlagssumme des Gesamtzeitraums",
    "GS": "Anzahl Stunden (h) im Gesamtzeitraum mit Niederschlag ≥ 0.1 mm",
    "GU": u"Anzahl Stunden (h) im Gesamtzeitraum an denen der Bemessungsniederschlag (T > 1a) überschritten wird",
    "GW": "Gesamtzeitraumsniederschlagssumme",
    "HA": "Skalierte Halbjahresniederschlagssumme",
    "HC": "Anzahl Stunden (h) im Halbjahr mit Clutter-Kennung",
    "HF": "Anzahl Stunden (h) im Halbjahr mit Fehlwert",
    "HI": "Halbjahresniederschlagssumme aus REGNIE",
    "HK": u"Halbjahresniederschlagssumme aus DW. Fehlwerte werden, wenn verfügbar, mit Werten aus REGNIE aufgefüllt.",
    "HM": "Max. 1h-Niederschlagssumme der Jahreszeit",
    "HS": "Anzahl Stunden (h) im Halbjahr mit Niederschlag ≥ 0.1 mm",
    "HU": u"Anzahl Stunden (h) im Halbjahr an denen der Bemessungsniederschlag (T > 1a) überschritten wird",
    "HW": "Halbjahresniederschlagssumme",
    "JA": "Skalierte Jahresniederschlagssumme",
    "JC": "Anzahl Stunden (h) im Jahr mit Clutter-Kennung",
    "JF": "Anzahl Stunden (h) im Jahr mit Fehlwert",
    "JI": "Jahresniederschlagssumme aus REGNIE",
    "JK": u"Jahresniederschlagssumme aus DW. Fehlwerte werden, wenn verfügbar, mit Werten aus REGNIE aufgefüllt.",
    "JM": "Max. 1h-Niederschlagssumme des Jahres",
    "JS": "Anzahl Stunden (h) im Jahr mit Niederschlag ≥ 0.1 mm",
    "JU": u"Anzahl Stunden (h) im Jahr an denen der Bemessungsniederschlag (T > 1a) überschritten wird",
    "JW": "Jahresniederschlagssumme",
    "MA": "Skalierte Monatsniederschlagssumme",
    "MC": "Anzahl Stunden (h) im Monat mit Clutter-Kennung",
    "MF": "Anzahl Stunden (h) im Monat mit Fehlwert",
    "MI": "Monatsniederschlagssumme aus REGNIE",
    "MK": "Monatsniederschlagssumme aus DW. Fehlwerte werden, wenn verfügbar, mit Werten aus REGNIE aufgefüllt.",
    "MM": "Max. 1h-Niederschlagssumme des Monats",
    "MS": "Anzahl Stunden (h) im Monat mit Niederschlag ≥ 0.1 mm",
    "MU": u"Anzahl Stunden (h) im Monat an denen der Bemessungsniederschlag (T > 1a) überschritten wird",
    "MW": "Monatsniederschlagssumme",
    "QA": "Skalierte Jahreszeitenniederschlagssumme",
    "QC": "Anzahl Stunden (h) in der Jahreszeit mit Clutter-Kennung",
    "QF": "Anzahl Stunden (h) in der Jahreszeit mit Fehlwert",
    "QI": "Jahreszeitenniederschlagssumme aus REGNIE",
    "QK": u"Jahreszeitenniederschlagssumme aus DW. Fehlwerte werden, wenn verfügbar, mit Werten aus REGNIE aufgefüllt.",
    "QM": "Max. 1h-Niederschlagssumme der Jahreszeit",
    "QS": "Anzahl Stunden (h) in der Jahreszeit mit Niederschlag ≥ 0.1 mm",
    "QU": u"Anzahl Stunden (h) in der Jahreszeit an denen der Bemessungsniederschlag (T > 1a) überschritten wird",
    "QW": "Jahreszeitenniederschlagssumme",
    "SJ": "Niederschlagssumme seit Jahresbeginn",
    "SM": "Niederschlagssumme seit Monatsbeginn",
    "SQ": "6h-Niederschlagssumme",
    "SY": "Niederschlagssumme für das hydrologische Jahr (Beginn November)",
    "UA": u"Anzahl Stunden (h) am Tag mit Überschreitung der Starkregen-Warnstufe 2 (markantes Wetter)",
    "UB": u"Anzahl Stunden (h) am Tag mit Überschreitung der Starkregen-Warnstufe 3 (Unwetter)",
    "UC": u"Anzahl Stunden (h) am Tag mit Überschreitung der Starkregen-Warnstufe 4 (extremes Unwetter)",
    "UD": u"Anzahl Stunden (h) am Tag mit Überschreitung der Dauerregen-Warnstufe 2 (markantes Wetter)",
    "UE": u"Anzahl Stunden (h) am Tag mit Überschreitung der Dauerregen-Warnstufe 3 (Unwetter)",
    "UF": u"Anzahl Stunden (h) am Tag mit Überschreitung der Dauerregen-Warnstufe 4 (extremes Unwetter)",
    "W1": "7d-Niederschlagssumme basierend auf RW-Produkt",
    "W2": "14d-Niederschlagssumme basierend auf RW-Produkt",
    "W3": "21d-Niederschlagssumme basierend auf RW-Produkt",
    "W4": "30d-Niederschlagssumme basierend auf RW-Produkt",
    'YW': "quasi-angeeichte 5-Minuten-Niederschlagsraten (RY nach Skalierung mit dem Quasianeichungsfaktor berechnet aus Verhältnis RW zu RH)",
    
    # X-products - in RVP6 units:
    'RX': "Radardaten ohne Korrektur (in RVP6-Units)",
    'WX': "Qualitätsgeprüfte Radardaten (in RVP6-Units)",
    'EX': "Europäische Radardaten (in RVP6-Units)",
    
    # B = R-factor products:
    "BR": "Ereignisbasierter R-Faktor nach DIN19708 [kJm2*mm/h]",
    "BD": "Dauer des Ereignisses in Stunden ([h])",
    "BK": "Kinetische Energie des Ereignisses [kJ/m2]",
    "BI": "Maximale 30-Minuten-Intensität [mm/h]",
    "BJ": "Mittlerer Jahres-R-Faktor [kJm2*mm/h]",
    "BQ": "Mittlerer Jahreszeit-R-Faktor [kJm2*mm/h]",
    "BM": "Mittlerer Monats-R-Faktor [kJm2*mm/h]",
    "BY": "R-Faktor (Jahressumme) [kJm2*mm/h]",

    # Not RADOLAN:
    "HG": "Deutschlandkomposit der Niederschlagsart in 2m Höhe über Grund",
    "WN": "Deutschlandkomposit der Reflektivität",
}
