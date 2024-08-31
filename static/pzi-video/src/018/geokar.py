#! /usr/bin/env python

import geometrijske_karakteristike as gk
import sys
import collections

def izpisi_vrednost(naslov, vrednost):
    return "{:>5} = {:.3f}\n".format(naslov, vrednost)


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
    n, x, y = vnos_podatkov()

    # Izračun količin
    print("Izračun ...")
    vrednosti = izracun(n, x, y)

    # Izpis rezultatov
    print("Izpis ...")
    izpis(vrednosti)


if __name__ == "__main__": main()
