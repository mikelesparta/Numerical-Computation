# -*- coding: utf-8 -*-
"""
Exercise 1
"""
import numpy as np
#%%
x0 = -0.4
tol = 1.e-8
maxNumSum = 100

polynomial = 0.
factorial  = 1.
error = np.inf
i = 1

while (error > tol and i < maxNumSum):
    term = x0**i / factorial
    polynomial += term
    error=np.abs(term)
    factorial *= i+1
    i += 1

print('Function value in -0,4     = ', np.exp(x0))
print('Apporx value in -0,4     = ', np.exp(x0) - error)
print('Number of iterations     = ', i)
