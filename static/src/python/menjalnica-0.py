#! /usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as et

# Vnos podatkov, branje podatkov iz datoteke
xml_tree = et.parse("dtecbs.xml")
xml_root = xml_tree.getroot()
xml_tecajnica = xml_root.find("tecajnica")
xml_tecaj_seznam = xml_tecajnica.findall("tecaj")

n = len(xml_tecaj_seznam)
oznake = []
vrednosti = []

for xml_tecaj in xml_tecaj_seznam:
    oznake.append(xml_tecaj.get("oznaka"))
    vrednosti.append(float(xml_tecaj.text))

znesek = float(input("Vnesi znesek v EUR: "))

for i in range(n):
    print("{:10.4f} {}".format(vrednosti[i] * znesek, oznake[i]))
