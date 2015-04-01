#! /usr/bin/env python

import geometrijske_karakteristike as gk
import sys
import sqlite3

def izpisi_vrednost(n, v):
    return "{:>5} = {:.3f}\n".format(n, v)


def vnos_podatkov():
    db = sqlite3.connect(sys.argv[1])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tocke")
    tocke = cursor.fetchall()

    db.close()

    n = len(tocke)
    x = []
    y = []

    for tocka in tocke:
        x.append(float(tocka[1]))
        y.append(float(tocka[2]))

    x.append(x[0])
    y.append(y[0])

    return n, x, y


def izracun(n, x, y):
    vrednosti = {}
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
    for key in vrednosti:
        s = s + izpisi_vrednost(key, vrednosti[key])

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
    n, x, y = vnos_podatkov()

    # Izračun ploščine prereza
    print("Izračun ...")
    vrednosti = izracun(n, x, y)

    # Izpis rezultatov
    print("Izpis ...")
    izpis(vrednosti)


if __name__ == "__main__": main()
