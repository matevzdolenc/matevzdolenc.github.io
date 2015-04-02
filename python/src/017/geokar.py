#! /usr/bin/env python

import geometrijske_karakteristike as gk
import sys

def izpisi_vrednost(naslov, vrednost):
    print("{:>5} = {:.3f}".format(naslov, vrednost))

def izpisi_vrednost_dat(naslov, vrednost, dat):
    dat.write("{:>5} = {:.3f}\n".format(naslov, vrednost))

def main():
    # Vnos podatkov
    dat = open(sys.argv[1], "r")

    print("Vnos podatkov ...")
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

    # Izračun količin
    print()
    print("Izračun ...")
    Ax = gk.Ax(n, x, y)
    Sx = gk.Sx(n, x, y)
    Sy = gk.Sy(n, x, y)
    Ix = gk.Ix(n, x, y)
    Iy = gk.Iy(n, x, y)
    Ixy = gk.Ixy(n, x, y)
    xt = gk.xt(n, x, y)
    yt = gk.yt(n, x, y)
    Ixt = gk.Ixt(n, x, y)
    Iyt = gk.Iyt(n, x, y)
    Ixyt = gk.Ixyt(n, x, y)

    # Izpis rezultatov
    print()
    print("Izpis ...")
    izpisi_vrednost("Ax", Ax)
    izpisi_vrednost("Sx", Sx)
    izpisi_vrednost("Sy", Sy)
    izpisi_vrednost("Ix", Ix)
    izpisi_vrednost("Iy", Iy)
    izpisi_vrednost("Ixy", Ixy)
    izpisi_vrednost("xt", xt)
    izpisi_vrednost("yt", yt)
    izpisi_vrednost("Ixt", Ixt)
    izpisi_vrednost("Iyt", Iyt)
    izpisi_vrednost("Ixyt", Ixyt)

    dat = open(sys.argv[2], "w")

    izpisi_vrednost_dat("Ax", Ax, dat)
    izpisi_vrednost_dat("Sx", Sx, dat)
    izpisi_vrednost_dat("Sy", Sy, dat)
    izpisi_vrednost_dat("Ix", Ix, dat)
    izpisi_vrednost_dat("Iy", Iy, dat)
    izpisi_vrednost_dat("Ixy", Ixy, dat)
    izpisi_vrednost_dat("xt", xt, dat)
    izpisi_vrednost_dat("yt", yt, dat)
    izpisi_vrednost_dat("Ixt", Ixt, dat)
    izpisi_vrednost_dat("Iyt", Iyt, dat)
    izpisi_vrednost_dat("Ixyt", Ixyt, dat)

    dat.close()

if __name__ == "__main__": main()
