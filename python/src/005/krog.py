#!/usr/bin/env python

import math

# Vnos podatkov
r = float(input("Podaj radij kroga: "))

# Izračun
pl = math.pi * r**2

# Izpis
print("Ploščina kroga je", pl)
print("Ploščina kroga je {:.3f}".format(pl))
print("Ploščina kroga pri radiju {:.2f} je {:.3f}".format(r, pl))

