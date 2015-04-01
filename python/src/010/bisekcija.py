#!/usr/bin/env python

# Poiščimo ničlo funkcije po metodi Bisekcije
# f(x) = 2x - 2

a = -5.0
b = 10.0
e = 0.001
iter = 0

while (b - a) > e:
    iter += 1
    c = (a + b) / 2
    print("{:10} {:10.4f} {:10.4f}".format(iter, c, b - a))
    if (2 * a - 2) * (2 * c - 2) > 0:
        a = c
    else:
        b = c

print()
print("Ničla funkcije: {:.4f}".format(c))
print("Število iteracij:", iter)
