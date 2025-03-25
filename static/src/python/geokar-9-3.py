#! /usr/bin/env python
# -*- coding: utf-8 -*-

import geometrijske_karakteristike as geokar
import xml.etree.cElementTree as et
import sys

# Vnos podatkov, branje podatkov iz datoteke

xml_tree = et.parse(sys.argv[1])

xml_prerez = xml_tree.getroot()
xml_naslov = xml_prerez.find("naslov")
xml_tocke = xml_prerez.find("tocke")
xml_tocke_seznam = xml_tocke.findall("tocka")

n = len(xml_tocke_seznam)
x = []
y = []

for xml_tocka in xml_tocke_seznam:
	id = xml_tocka.get("id")
	
	x.insert(int(id) - 1, float(xml_tocka.find("x").text))
	y.insert(int(id) - 1, float(xml_tocka.find("y").text))

x.append(x[0])
y.append(y[0])

# Izpis geometrijskih katakteristik na zaslon

print("{:6} {:10.3f}".format("Ax: ", geokar.Ax(n, x, y)))
print("{:6} {:10.3f}".format("Sx: ", geokar.Sx(n, x, y)))
print("{:6} {:10.3f}".format("Sy: ", geokar.Sy(n, x, y)))
print("{:6} {:10.3f}".format("Ix: ", geokar.Ix(n, x, y)))
print("{:6} {:10.3f}".format("Iy: ", geokar.Iy(n, x, y)))
print("{:6} {:10.3f}".format("Ixy: ", geokar.Ixy(n, x, y)))
print("{:6} {:10.3f}".format("xt: ", geokar.xt(n, x, y)))
print("{:6} {:10.3f}".format("yt: ", geokar.yt(n, x, y)))
print("{:6} {:10.3f}".format("Ixt: ", geokar.Ixt(n, x, y)))
print("{:6} {:10.3f}".format("Iyt: ", geokar.Iyt(n, x, y)))
print("{:6} {:10.3f}".format("Ixyt: ", geokar.Ixyt(n, x, y)))

# Zapis podatkov v XML datoteko

xml_prerez = et.Element("prerez")

xml_naslov = et.SubElement(xml_prerez, "naslov")
xml_naslov.text = sys.argv[1]

xml_tocke = et.SubElement(xml_prerez, "tocke")

for i in range(n):
    xml_tocka = et.SubElement(xml_tocke, "tocka")
    xml_tocka.set("id", str(i + 1))
    
    xml_x = et.SubElement(xml_tocka, "x")
    xml_x.text = str(x[i])
    xml_y = et.SubElement(xml_tocka, "y")
    xml_y.text = str(y[i])
    
xml_tree = et.ElementTree(xml_prerez)
xml_tree.write(sys.argv[1], encoding='utf-8', xml_declaration=True)
