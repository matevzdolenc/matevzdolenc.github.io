#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Vnos podatkov, branje podatkov iz datoteke

dat_txt = "geokar-podatki.txt"
dat_xml = dat_txt + ".xml"

dat = open(dat_txt, "r")

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

# Zapis podatkov v XML datoteko

dat = open(dat_xml, "w")

s = "<?xml version=\"1.0\" ?>"
s = s + "<prerez>"
s = s + "<naslov>" + dat_xml + "</naslov>"
s = s + "<tocke>"

for i in range(n):
    s = s + "<tocka id=\"{}\">".format(i+1)
    s = s + "<x>" + str(x[i]) + "</x>"
    s = s + "<y>" + str(y[i]) + "</y>"
    s = s + "</tocka>"

s = s + "</tocke>"
s = s + "</prerez>"

dat.write(s)

dat.close()