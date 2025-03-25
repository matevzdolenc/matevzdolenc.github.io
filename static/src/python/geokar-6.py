#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Funkcije za izračun geometrijskih karakteristik

def Ax(n, x, y):
    v = 0.0
    for i in range(n):
        v = v + (x[i+1] + x[i]) * (y[i+1] - y[i])

    return 0.5 * v

def Sx(n, x, y):
    v = 0.0
    for i in range(n):
        v = v + (x[i+1] - x[i]) * (y[i+1]**2 + y[i] * y[i+1] + y[i]**2)

    return -1. / 6. * v

def Sy(n, x, y):
    v = 0.0
    for i in range(n):
        v = v + (y[i+1] - y[i]) * (x[i+1]**2 + x[i] * x[i+1] + x[i]**2)

    return 1. / 6. * v

def Ix(n, x, y):
    v = 0.0
    for i in range(n):
        v = v + (x[i+1] - x[i]) * (y[i+1]**3 +  y[i+1]**2 * y[i] + y[i+1] * y[i]**2 + y[i]**3)

    return -1. / 12. * v

def Iy(n, x, y):
    v = 0.0
    for i in range(n):
        v = v + (y[i+1] - y[i]) * (x[i+1]**3 +  x[i+1]**2 * x[i] + x[i+1] * x[i]**2 + x[i]**3)

    return 1. / 12. * v

def Ixy(n, x, y):
    v = 0.0
    for i in range(n):
        v = v + (y[i+1] - y[i]) * (y[i+1] * (3* x[i+1]**2 + 2 * x[i] * x[i+1] + x[i]**2) + y[i] * (3 * x[i]**2 + 2 * x[i] * x[i+1] + x[i+1]**2))

    return -1. / 24. * v

def xt(n, x, y):
    return Sy(n, x, y) / Ax(n, x, y)
    
def yt(n, x, y):
    return Sx(n, x, y) / Ax(n, x, y)
    
def Ixt(n, x, y):
    return Ix(n, x, y) - yt(n, x, y)**2 * Ax(n, x, y)
    
def Iyt(n, x, y):
    return Iy(n, x, y) - xt(n, x, y)**2 * Ax(n, x, y)

def Ixyt(n, x, y):
    return Ixy(n, x, y) + xt(n, x, y) * yt(n, x, y) * Ax(n, x, y)


# Vnos podatkov, branje podatkov iz datoteke
    
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

# Izpis geometrijskih katakteristik na zaslon

print("{:6} {:10.3f}".format("Ax: ", Ax(n, x, y)))
print("{:6} {:10.3f}".format("Sx: ", Sx(n, x, y)))
print("{:6} {:10.3f}".format("Sy: ", Sy(n, x, y)))
print("{:6} {:10.3f}".format("Ix: ", Ix(n, x, y)))
print("{:6} {:10.3f}".format("Iy: ", Iy(n, x, y)))
print("{:6} {:10.3f}".format("Ixy: ", Ixy(n, x, y)))
print("{:6} {:10.3f}".format("xt: ", xt(n, x, y)))
print("{:6} {:10.3f}".format("yt: ", yt(n, x, y)))
print("{:6} {:10.3f}".format("Ixt: ", Ixt(n, x, y)))
print("{:6} {:10.3f}".format("Iyt: ", Iyt(n, x, y)))
print("{:6} {:10.3f}".format("Ixyt: ", Ixyt(n, x, y)))
