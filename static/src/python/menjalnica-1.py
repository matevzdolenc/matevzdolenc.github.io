#! /usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as et

# Vnos podatkov, branje podatkov iz datoteke
xml_tree = et.parse("dtecbs.xml")
xml_root = xml_tree.getroot()
xml_tecajnica = xml_root.find("tecajnica")
xml_tecaj_seznam = xml_tecajnica.findall("tecaj")
oznake = []
vrednosti = []
for xml_tecaj in xml_tecaj_seznam:
    oznake.append(xml_tecaj.get("oznaka"))
    vrednosti.append(float(xml_tecaj.text))

vnos = input("Vnesi znesek in valuto (npr. 12 EUR): ")

besede = vnos.split()
znesek = float(besede[0])
valuta = besede[1]
    
if valuta.lower() == "eur":
    # Izpis vrednosti zneska v vseh ostalih valutah
    for i in range(len(oznake)):
        print("{:.4f} {}".format(vrednosti[i] * znesek, oznake[i]))
else:
    # Izpis vrednosti v EUR
    for i in range(len(oznake)):
        if oznake[i].lower() == valuta.lower():
            print("{} {} --> {:.4f} {}".format(znesek, valuta.upper(), znesek / vrednosti[i], "EUR"))
