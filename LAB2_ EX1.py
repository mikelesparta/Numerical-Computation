# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 16:12:50 2021

@author: mikel
"""
#%%
import numpy as np
#%%

def horner(p,x0):
    quotient = np.zeros_like(p)
    quotient[0] = p[0]
    for i in range(1, len(p)):
        quotient[i] = p[i] + quotient[i -1]*x0
    remainder = quotient[len(p) -1]
    quotient = quotient[:-1]
    return quotient, remainder

p0 = np.array([1.,2,1])
x0 = 1.
a, b = horner(p0, x0)

p1 = np.array([1., -1, 2, -3,  5, -2])
x1 = 1.
c, d = horner(p1, x1)

p2 = np.array([1., -1, -1, 1, -1, 0, -1, 1])
x2 = -1.
e, f = horner(p2, x2)

print('Coeficients of p0 = ', a)
print('P0(1) = ', b)

print('Coeficients of p1 = ', c)
print('P1(1) = ', d)

print('Coeficients of p2 = ', e)
print('P2(-1) = ', f)

