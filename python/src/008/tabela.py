#!/usr/bin/env python

import math

prvi = int(input("Podaj začetno vrednost: "))
zadnji = int(input("Podaj končno vrednost: "))

s = "{:>6} | {:>10} | {:>10}".format("Radij", "Ploščina", "Obseg")
print(s)
print("-" * len(s))
for r in range(prvi, zadnji + 1):
    pl = math.pi * r**2
    ob = 2 * math.pi * r
    print("{:6d} | {:10.3f} | {:10.3f}".format(r, pl, ob))
