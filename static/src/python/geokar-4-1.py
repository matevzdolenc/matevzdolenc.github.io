#! /usr/bin/env python
# -*- coding: utf-8 -*-

dat = open("geokar-podatki.txt", "r")

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

A = 0.0
for i in range(n):
    A = A + (x[i+1] + x[i]) * (y[i+1] - y[i])

A = 0.5 * A

# Izpis na zaslon
print("A: {:.3}".format(A))

# Izpis v datoteko
dat = open("geokar-rezultati.txt", "w")

dat.write("A: {:.3}\n".format(A))

dat.close()
