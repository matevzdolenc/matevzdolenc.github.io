#! /usr/bin/env python

import sys
import xml.etree.cElementTree as et

def vnos_podatkov():
    # Vnos podatkov
    dat = open(sys.argv[1], "r")

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

    return n, x, y

def izpis_v_xml_datoteko(n, x, y):
    xml_prerez = et.Element("prerez")

    xml_tocke = et.SubElement(xml_prerez, "tocke")

    for i in range(n):
        xml_tocka = et.SubElement(xml_tocke, "tocka")
        xml_tocka.set("id", str(i + 1))

        xml_x = et.SubElement(xml_tocka, "x")
        xml_x.text = str(x[i])
        xml_y = et.SubElement(xml_tocka, "y")
        xml_y.text = str(y[i])

    xml_tree = et.ElementTree(xml_prerez)
    xml_tree.write(sys.argv[2], encoding='utf-8', xml_declaration=True)


def main():
    # Vnos podatkov
    print("Vnos podatkov ...")
    n, x, y = vnos_podatkov()

    # Izpis podatkov v XML datoteko
    print("Izpis v XML ...")
    izpis_v_xml_datoteko(n, x, y)


if __name__ == "__main__": main()
