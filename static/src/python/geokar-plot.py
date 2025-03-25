#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy

# Vnos podatkov, branje podatkov iz datoteke

dat = open(sys.argv[1], "r")

n = int(dat.readline())
tocke = []
for i in range(n):
    besede = dat.readline().split()
    tocka = [float(besede[0]), float(besede[1])]
    tocke.append(tocka)

dat.close()

# Narisi poligon
poligon = plt.Polygon(tocke, fill=None, edgecolor='r')
plt.gca().add_patch(poligon)

# Določi min in max vrednosti
min_x, min_y = numpy.min(numpy.array(tocke)[...,0]), numpy.min(numpy.array(tocke)[...,1])
max_x, max_y = numpy.max(numpy.array(tocke)[...,0]), numpy.max(numpy.array(tocke)[...,1])

# Določi koordinatne osi
plt.xlim(min_x-(max_x-min_x)/10, max_x+(max_x-min_x)/10)
plt.ylim(min_y-(max_y-min_y)/10, max_y+(max_y-min_y)/10)
plt.axes().set_aspect('equal', 'datalim')

# Prikaži sliko
plt.show()

# Shrani sliko na disk (png)
plt.savefig(sys.argv[1] + ".png")
