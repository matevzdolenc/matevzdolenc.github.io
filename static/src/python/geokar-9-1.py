#! /usr/bin/env python
# -*- coding: utf-8 -*-

import geometrijske_karakteristike as geokar
import xml.etree.cElementTree as et

# Vnos podatkov, branje podatkov iz datoteke
    
xml_tree = et.parse("geokar-podatki.xml")
xml_prerez = xml_tree.getroot()
xml_naslov = xml_prerez.find("naslov")
xml_tocke = xml_prerez.find("tocke")
xml_tocke_seznam = xml_tocke.findall("tocka")

n = len(xml_tocke_seznam)
x = []
y = []

for xml_tocka in xml_tocke_seznam:
    x.append(float(xml_tocka.find("x").text))
    y.append(float(xml_tocka.find("y").text))

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
