# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 15:30:42 2021

@author: mikel
"""
#%%
import numpy as np
#%%

def triangular(A, b):
    At = np.copy(A)
    bt = np.copy(b)
    f = 0
    for i in range(0, len(A) - 1, 1):
        f = A[i+1][i] / A[i][i]
        At[i+1][i] = A[i+1][i] - f * A[i][i]
        At[i+1][i+1] = A[i+1][i+1] - f * A[i][i+1]
        bt[i+1] = b[i+1] - f * b[i]
    return At, bt

n = 7 

A1 = np.diag(np.ones(n))*3
A2 = np.diag(np.ones(n-1),1) 
A = A1 + A2 + A2.T 

b = np.arange(n,2*n)*1.

result1, result2 = triangular(A, b)
np.set_printoptions(precision = 2)
print('TRIANGULAR SYSTEM \n At')
print(result1)
print('bt')
print(result2)

n = 8 

np.random.seed(3)
A1 = np.diag(np.random.rand(n))
A2 = np.diag(np.random.rand(n-1),1)
A = A1 + A2 + A2.T 

b = np.random.rand(n)

result3, result4 = triangular(A, b)
print()
print('TRIANGULAR SYSTEM \n At')
print(result3)
print('bt')
print(result4)