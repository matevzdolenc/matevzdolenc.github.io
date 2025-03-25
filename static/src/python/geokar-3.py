#! /usr/bin/env python
# -*- coding: utf-8 -*-

n = int(input("Podaj št. točk: "))

x = []
y = []
for i in range(n):
    vrstica = input("Točka {}: ".format(i + 1))
    besede = vrstica.split()

    x.append(float(besede[0]))
    y.append(float(besede[1]))

x.append(x[0])
y.append(y[0])

A = 0.0
for i in range(n):
    A = A + (x[i+1] + x[i]) * (y[i+1] - y[i])

A = 0.5 * A

print("A: {:.3}".format(A))
