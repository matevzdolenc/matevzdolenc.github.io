#! /usr/bin/env python

import math

radiji = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for r in radiji:
	print("{0:3d} {1:10.3f}".format(r, math.pi * r**2))
