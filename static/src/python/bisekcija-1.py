#! /usr/bin/env python
# -*- coding: utf-8 -*-

iter = 1
a = 0.0
b = 10.0
eps = 0.0001

while b - a > eps:
    c = (a + b) / 2
    fa = 2 * a - 3
    fc = 2 * c - 3
    print("iter: {:d} fa: {:.3f}, fc: {:.3f}".format(iter, fa, fc))
    if fa * fc <= 0:
         b = c
    else:
        a = c

    iter += 1

print()
print("ničla funkcije: {:.3f}".format(c))
print("število iteracij: {:d}".format(iter))
