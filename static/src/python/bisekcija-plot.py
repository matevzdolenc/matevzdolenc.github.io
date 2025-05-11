#! /usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 2 * x - 3

def main():
    iter = 1
    iters = []
    a = 0.0
    b = 10.0
    eps = 0.0001

    dat = open("bisekcija.txt", "w")

    while b - a > eps:
        c = (a + b) / 2
        fa = f(a)
        fc = f(c)
        iters.append(c)
        print("iter: {:d} fa: {:.3f}, fc: {:.3f}".format(iter, fa, fc))
        dat.write("{}\n".format(c))
        if fa * fc <= 0:
             b = c
        else:
            a = c

        iter += 1

    dat.close()

    print()
    print("ničla funkcije: {:.3f}".format(c))
    print("število iteracij: {:d}".format(iter))

    plt.plot(iters)

    plt.title('Bisekcija - f(x) = 2x - 3')
    plt.ylabel('Približek ničle funkcije')
    plt.xlabel('Iteracija')
    plt.savefig('bisekcija-plot.png')
    plt.show()

if __name__ == "__main__":
    main()
