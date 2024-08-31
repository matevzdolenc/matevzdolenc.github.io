#! /usr/bin/env python

# Število točk prereza
n = 4

# Koordinate točk prereza.
# Zadnja točka (n + 1) je enaka prvi točki
x = [0, 1, 1, 0, 0]
y = [0, 0, 1, 1, 0]

# Izračun ploščine prereza
Ax = 0.0
for i in range(n):
    Ax = Ax + (x[i+1] + x[i]) * (y[i+1] - y[i])

Ax = 0.5 * Ax

# Izpis rezultatov
print("Ax = {:.3f}".format(Ax))
