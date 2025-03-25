#! /usr/bin/env python
# -*- coding: utf-8 -*-

n = int(input("Podaj št. točk: "))

x = []
y = []
for i in range(n):
    kx = float(input("Podaj x: "))
    ky = float(input("Podaj y: "))

    x.append(kx)
    y.append(ky)

x.append(x[0])
y.append(y[0])

A = 0.0
for i in range(n):
    A = A + (x[i+1] + x[i]) * (y[i+1] - y[i])

A = 0.5 * A

print("A: {:.3}".format(A))
