#! /usr/bin/env python

import geometrijske_karakteristike as gk

def izpisi_vrednost(n, v):
    print("{:>5} = {:.3f}".format(n, v))

def main():
    # Vnos podatkov
    print("Vnos podatkov ...")
    n = int(input("Podaj število točk: "))

    x = []
    y = []
    for i in range(n):
        vrstica = input("Točka {}: ".format(i + 1))
        besede = vrstica.split()
        x.append(float(besede[0]))
        y.append(float(besede[1]))

    x.append(x[0])
    y.append(y[0])

    # Izračun ploščine prereza
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

if __name__ == "__main__": main()
