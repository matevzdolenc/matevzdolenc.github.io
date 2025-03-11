#! /usr/bin/env python
# -*- coding: utf-8 -*-

def f(x):
    return 2 * x - 3

def main():
    iter = 1
    a = 0.0
    b = 10.0
    eps = 0.0001

    dat = open("bisekcija.txt", "w")

    while b - a > eps:
        c = (a + b) / 2
        fa = f(a)
        fc = f(c)
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

if __name__ == "__main__":
    main()
