#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from scipy import linalg

# A x = b

# 1. način, za manjše matrike
# x = A(-1) b

A = np.asmatrix('3 1 4; 1 5 9; 2 6 5')
b = np.asmatrix('1; 2; 3')
x = A.I * b
print ("1. način ->")
print(x)

# 2. način
x = linalg.solve(A, b)
print ("2. način ->")
print(x)

