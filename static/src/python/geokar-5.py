#! /usr/bin/env python
# -*- coding: utf-8 -*-


def A(n, x, y):
    A = 0.0
    for i in range(n):
        A = A + (x[i+1] + x[i]) * (y[i+1] - y[i])

    return 0.5 * A

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

print("A: {:.3}".format(A(n, x, y)))
