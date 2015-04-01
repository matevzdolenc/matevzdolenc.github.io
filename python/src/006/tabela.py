#!/usr/bin/env python

import math

radiji = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for r in radiji:
    pl = math.pi * r**2
    print("{:3d} {:.3f}".format(r, pl))
