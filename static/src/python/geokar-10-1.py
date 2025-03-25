#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import geometrijske_karakteristike as geokar
import sys

# Odpri SQLite bazo
db = sqlite3.connect(sys.argv[1])
cursor = db.cursor()
cursor.execute("SELECT * FROM tocke")
tocke = cursor.fetchall()

db.close()

n = len(tocke)
x = []
y = []

for tocka in tocke:
    x.append(float(tocka[1]))
    y.append(float(tocka[2]))

x.append(x[0])
y.append(y[0])

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


