#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import statistics

# Zahtevana marka betona
MB = float(input("Vnesi zahtevano marko betona: "))

# Returns a DataFrame
df = pd.read_excel('mb_primer-2.xlsx', sheet_name=0)

# Podatki o preiskušancih
x = df['x']

# srednja vrednost
mn = sum(x) / len(x) 
print("mn = {:.2f}".format(mn))

# standardni odklon
sn = statistics.stdev(x)
print("sn = {:.4f}".format(sn))

# 1. kriterij
if mn > MB + 1.3 * sn:
	print("mn > MB + 1.3 * sn ... kriterij je izpolnjen")
else:
	print("mn < MB + 1.3 * sn ... kriterij NI izpolnjen")

# 2. kriterij
if min(x) > MB - 4:
	print("xmin > MB - 4 ... kriterij je izpolnjen")
else:
	print("xmin > MB - 4 ... kriterij NI izpolnjen")
