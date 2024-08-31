#!/usr/bin/env python

import math

radiji = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

s = "{:>6} | {:>10} | {:>10}".format("Radij", "Ploščina", "Obseg")
print(s)
print("-" * len(s))
for r in radiji:
    pl = math.pi * r**2
    ob = 2 * math.pi * r
    print("{:6d} | {:10.3f} | {:10.3f}".format(r, pl, ob))
