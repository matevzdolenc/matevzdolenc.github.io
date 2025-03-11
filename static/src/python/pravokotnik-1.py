#! /usr/bin/env python

import math

print("Izračun osnovnih katakteristik pravokotnika")
print()

# Vnos podatkov
print("Podaj stranici pravokotnika ...")
a = float(input("a? "))
b = float(input("b? "))

# Izpis podatkov
print()
print("Izpis podatkov", "-" * 20)
print()
print(f"a = {a}")
print(f"b = {b}")

# Izračun
pl = a * b
ob = 2 * a + 2 * b
d = math.sqrt(a**2 + b**2)
alfa = math.degrees(math.asin(b / d))

# Izpis rezultatov
print()
print("Izpis rezultatov", "-" * 20)
print()
print(f" Ploščina: {pl:.3f}")
print(f"    Obseg: {ob:.3f}")
print(f"Diagonala: {d:.3f}")
print(f"     Alfa: {alfa:.3f}")
print()
