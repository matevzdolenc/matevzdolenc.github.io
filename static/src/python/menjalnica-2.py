#! /usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as et
from urllib.request import urlopen

# Vnos podatkov, branje podatkov iz datoteke
xml_tree = et.ElementTree(file=urlopen('http://www.bsi.si/_data/tecajnice/dtecbs.xml'))
xml_root = xml_tree.getroot()
xml_tecajnica = xml_root.find("{http://www.bsi.si}tecajnica")
xml_tecaj_seznam = xml_tecajnica.findall("{http://www.bsi.si}tecaj")
tecaji = []
for xml_tecaj in xml_tecaj_seznam:
    tecaj = [xml_tecaj.get("oznaka"), xml_tecaj.get("sifra"), float(xml_tecaj.text)]
    tecaji.append(tecaj)

# Preberi

while 1:
    vnos = input("Vnesi znesek in valuto (npr. 12 EUR): ")
    
    # Če imamo prazno vrstico, končaj s programom
    if vnos == "":
        break
    
    b = vnos.split()
    znesek = float(b[0])
    valuta = b[1]

    if valuta.lower() == "eur":
        # Izpis vrednosti zneska v vseh ostalih valutah
        for tecaj in tecaji:
            print("{:.4f} {}".format(tecaj[2] * znesek, tecaj[0]))
    else:
        # Izpis vrednosti v EUR
        for tecaj in tecaji:
            if tecaj[0].lower() == valuta.lower():
                print("{} {} --> {:.4f} {}".format(znesek, valuta.upper(),znesek / tecaj[2], "EUR"))
