#! /usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as et
import sys

# Vnos podatkov, branje podatkov iz datoteke

kraji = []
kraji_x = []
kraji_y = []

dat = open(sys.argv[1], "r")

# Preberi podatke o središču
vrstica = dat.readline()
besede = vrstica.split()
center = besede[0]
center_x = besede[1]
center_y = besede[2]

# Preberi število podatkov
n = int(dat.readline())

# Preberi podatke o podanih krajih
for i in range(n):
    vrstica = dat.readline()
    besede = vrstica.split()
    kraji.append(besede[0])
    kraji_x.append(besede[1])
    kraji_y.append(besede[2])
    
dat.close()

# Izpiši podatke na zaslon

print("Ime središča: {}".format(center))
print("           x: {}".format(center_x))
print("           y: {}".format(center_y))
print()

print("{:30} {:20} {:20}".format("Kraj", "x", "y"))
print("-" * 80)
for i in range(n):
    print("{:30} {:20} {:20}".format(kraji[i], kraji_x[i], kraji_y[i]))

# Izpis v KML datoteko

kml = et.Element("kml")
kml.set("xmlns", "http://www.opengis.net/kml/2.2")
kml.set("xmlns:gx", "http://www.google.com/kml/ext/2.2")
kml.set("xmlns:kml", "http://www.opengis.net/kml/2.2")
kml.set("xmlns:atom", "http://www.w3.org/2005/Atom")

document = et.SubElement(kml, "Document")

document_name = et.SubElement(document, "name")
document_name.text = sys.argv[1]

folder = et.SubElement(document, "Folder")
folder_name = et.SubElement(folder, "name")
folder_name.text = "Vse poti vodijo v/na {}".format(center)

for i in range(n):
    placemark = et.SubElement(folder, "Placemark")
    placemark_name = et.SubElement(placemark, "name")
    placemark_name.text = kraji[i]
    
    linestring = et.SubElement(placemark, "LineString")
    
    coordinates = et.SubElement(linestring, "coordinates")
    coordinates.text = "{},{},0 {},{},0".format(kraji_y[i], kraji_x[i], center_y, center_x)

xml_tree = et.ElementTree(kml)

xml_tree.write(sys.argv[1]+".kml", encoding='utf-8', xml_declaration=True)