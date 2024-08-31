#! /usr/bin/env python

# Vnos podatkov
print("Vnos podatkov ...")
n = int(input("Podaj število točk: "))

x = []
y = []
for i in range(n):
    # 1. primer: vsaka koordinata posebej
    # xi = float(input("x({}): ".format(i + 1)))
    # yi = float(input("y({}): ".format(i + 1)))
    # x.append(xi)
    # y.append(yi)

    # 2. primer: podajanje x in y koordinate točke skupaj
    vrstica = input("Točka {}: ".format(i+1))
    besede = vrstica.split()
    x.append(float(besede[0]))
    y.append(float(besede[1]))

x.append(x[0])
y.append(y[0])

# Izračun ploščine prereza
print()
print("Izračun ...")
Ax = 0.0
for i in range(n):
    Ax = Ax + (x[i+1] + x[i]) * (y[i+1] - y[i])

Ax = 0.5 * Ax

# Izpis rezultatov
print()
print("Izpis ...")
print("Ax = {:.3f}".format(Ax))
