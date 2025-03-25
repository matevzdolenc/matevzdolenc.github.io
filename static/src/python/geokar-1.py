#! /usr/bin/env python
# -*- coding: utf-8 -*-

n = 4

x = [0, 1, 1, 0, 0]
y = [0, 0, 1, 1, 0]

A = 0.0
for i in range(n):
    A = A + (x[i+1] + x[i]) * (y[i+1] - y[i])

A = 0.5 * A

print("A: {:.3}".format(A))
