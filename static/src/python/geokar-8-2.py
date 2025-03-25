#! /usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as et

# Vnos podatkov, branje podatkov iz datoteke

dat_txt = "geokar-podatki.txt"
dat_xml = dat_txt + ".xml"

dat = open(dat_txt, "r")

n = int(dat.readline())

x = []
y = []
for i in range(n):
    vrstica = dat.readline()
    besede = vrstica.split()

    x.append(float(besede[0]))
    y.append(float(besede[1]))

x.append(x[0])
y.append(y[0])

dat.close()

# Zapis podatkov v XML datoteko

xml_prerez = et.Element("prerez")

xml_naslov = et.SubElement(xml_prerez, "naslov")
xml_naslov.text = dat_xml

xml_tocke = et.SubElement(xml_prerez, "tocke")

for i in range(n):
    xml_tocka = et.SubElement(xml_tocke, "tocka")
    xml_tocka.set("id", str(i + 1))
    
    xml_x = et.SubElement(xml_tocka, "x")
    xml_x.text = str(x[i])
    xml_y = et.SubElement(xml_tocka, "y")
    xml_y.text = str(y[i])
    
xml_tree = et.ElementTree(xml_prerez)
xml_tree.write(dat_xml, encoding='utf-8', xml_declaration=True)
