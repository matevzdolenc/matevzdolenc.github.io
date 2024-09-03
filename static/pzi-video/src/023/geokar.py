#! /usr/bin/env python

import geometrijske_karakteristike as gk
import sys
import collections
import xml.etree.cElementTree as et
import json
import sqlite3


def izpisi_vrednost(naslov, vrednost):
    return "{:>5} = {:.3f}\n".format(naslov, vrednost)


def vnos_podatkov_txt():
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


def vnos_podatkov_xml():
    # Vnos podatkov
    xml_tree = et.parse(sys.argv[1])

    xml_prerez = xml_tree.getroot()
    xml_tocke = xml_prerez.find("tocke")
    xml_tocke_seznam = xml_tocke.findall("tocka")

    n = len(xml_tocke_seznam)
    x = []
    y = []

    for xml_tocka in xml_tocke_seznam:
        tocka_id = int(xml_tocka.get("id"))
        tocka_x = float(xml_tocka.find("x").text)
        tocka_y = float(xml_tocka.find("y").text)
        x.insert(tocka_id - 1, tocka_x)
        y.insert(tocka_id - 1, tocka_y)

    x.append(x[0])
    y.append(y[0])

    return n, x, y


def vnos_podatkov_json():
    # Vnos podatkov
    with open(sys.argv[1], "r") as dat:
        data = json.load(dat)

    n = data["n"]
    x = data["x"]
    y = data["y"]

    x.append(x[0])
    y.append(y[0])

    return n, x, y


def vnos_podatkov_sqlite():
    db = sqlite3.connect(sys.argv[1])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tocke")
    tocke = cursor.fetchall()

    db.close()

    n = len(tocke)
    x = []
    y = []

    for tocka in tocke:
        x.insert(tocka[0] - 1, float(tocka[1]))
        y.insert(tocka[0] - 1, float(tocka[2]))

    x.append(x[0])
    y.append(y[0])

    return n, x, y


def izracun(n, x, y):
    vrednosti = collections.OrderedDict()
    vrednosti["Ax"] = gk.Ax(n, x, y)
    vrednosti["Sx"] = gk.Sx(n, x, y)
    vrednosti["Sy"] = gk.Sy(n, x, y)
    vrednosti["Iy"] = gk.Iy(n, x, y)
    vrednosti["Ixy"] = gk.Ixy(n, x, y)
    vrednosti["xt"] = gk.xt(n, x, y)
    vrednosti["yt"] = gk.yt(n, x, y)
    vrednosti["Ixt"] = gk.Ixt(n, x, y)
    vrednosti["Iyt"] = gk.Iyt(n, x, y)
    vrednosti["Ixyt"] = gk.Ixyt(n, x, y)
    return vrednosti

def izpis(vrednosti):
    s = ""
    for k in vrednosti:
        s = s + izpisi_vrednost(k, vrednosti[k])

    izpis_na_zaslon(s)
    izpis_v_datoteko(s)


def izpis_na_zaslon(s):
    print(s)


def izpis_v_datoteko(s):
    dat = open(sys.argv[2], "w")
    dat.write(s)
    dat.close()


def main():
    # Vnos podatkov
    print("Vnos podatkov ...")

    vnos = {"txt": vnos_podatkov_txt, "xml": vnos_podatkov_xml, "json": vnos_podatkov_json, "sqlite": vnos_podatkov_sqlite}
    fin = sys.argv[1]
    ext = fin[fin.rfind(".") + 1:]

    if ext not in vnos:
        print("Napaka: Neznan zapis podatkov")
        return

    n, x, y = vnos[ext]()

    # Izračun količin
    print("Izračun ...")
    vrednosti = izracun(n, x, y)

    # Izpis rezultatov
    print("Izpis ...")
    izpis(vrednosti)


if __name__ == "__main__": main()