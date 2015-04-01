#! /usr/bin/env python

# Število točk prereza
n = 4

# Koordinate točk prereza.
# Zadnja točka (n + 1) je enaka prvi točki
tocke = [[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]]

# Izračun ploščine prereza
Ax = 0.0
for i in range(n):
    Ax = Ax + (tocke[i+1][0] + tocke[i][0]) * (tocke[i+1][1] - tocke[i][1])

Ax = 0.5 * Ax

# Izpis rezultatov
print("Ax = {:.3f}".format(Ax))
