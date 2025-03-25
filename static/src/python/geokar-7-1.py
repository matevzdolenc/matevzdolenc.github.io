#! /usr/bin/env python
# -*- coding: utf-8 -*-

import geometrijske_karakteristike as geokar
import sys

# Vnos podatkov, branje podatkov iz datoteke

dat = open(sys.argv[1], "r")

n = int(dat.readline())

x = []
y = []
for i in range(n):
    vrstica = dat.readline()
    besede = vrstica.split()

    x.append(float(besede[0]))
    y.append(float(besede[1]))

x.append(x[0])
y.append(y[0])

dat.close()

# Izpis geometrijskih katakteristik na zaslon

print("{:6} {:10.3f}".format("Ax: ", geokar.Ax(n, x, y)))
print("{:6} {:10.3f}".format("Sx: ", geokar.Sx(n, x, y)))
print("{:6} {:10.3f}".format("Sy: ", geokar.Sy(n, x, y)))
print("{:6} {:10.3f}".format("Ix: ", geokar.Ix(n, x, y)))
print("{:6} {:10.3f}".format("Iy: ", geokar.Iy(n, x, y)))
print("{:6} {:10.3f}".format("Ixy: ", geokar.Ixy(n, x, y)))
print("{:6} {:10.3f}".format("xt: ", geokar.xt(n, x, y)))
print("{:6} {:10.3f}".format("yt: ", geokar.yt(n, x, y)))
print("{:6} {:10.3f}".format("Ixt: ", geokar.Ixt(n, x, y)))
print("{:6} {:10.3f}".format("Iyt: ", geokar.Iyt(n, x, y)))
print("{:6} {:10.3f}".format("Ixyt: ", geokar.Ixyt(n, x, y)))
