#! /usr/bin/env python
# -*- coding: utf-8 -*-

from time import process_time

import numpy as np
import scipy as sp
import scipy.io as spio
import scipy.sparse as sparse
import scipy.sparse.linalg as splinalg
import scipy.linalg as linalg

A = spio.mmread("fidapm37.mtx")
b = spio.mmread("fidapm37_rhs1.mtx")

print("x = sparse.linalg.spsolve(A, b) -->")
t_start = process_time()
x = sparse.linalg.spsolve(A, b)
t_end = process_time()
print("Execution time:  {:.2f}".format(t_end - t_start))
print(x)

print()
print("x = linalg.solve(A.todense(), b) -->")
AA = A.todense()
t_start = process_time()
x = linalg.solve(AA, b)
t_end = process_time()
print("Execution time:  {:.2f}".format(t_end - t_start))
print(x)

print()
print("x = AA.I * b -->")
AA = A.todense()
t_start = process_time()
x = AA.I * b
t_end = process_time()
print("Execution time:  {:.2f}".format(t_end - t_start))
print(x)
