#!/usr/bin/env python

import math
import sys

prvi = int(input("Podaj začetno vrednost: "))
zadnji = int(input("Podaj končno vrednost: "))

if prvi < 0 or zadnji < 0:
    print("Napaka. Vrednosti morata biti večji od 0.")
    sys.exit(1)

if prvi < zadnji:
    korak = 1
    zadnji = zadnji + 1
else:
    korak = -1
    zadnji = zadnji - 1

s = "{:>6} | {:>10} | {:>10}".format("Radij", "Ploščina", "Obseg")
print(s)
print("-" * len(s))
for r in range(prvi, zadnji, korak):
    pl = math.pi * r**2
    ob = 2 * math.pi * r
    print("{:6d} | {:10.3f} | {:10.3f}".format(r, pl, ob))
