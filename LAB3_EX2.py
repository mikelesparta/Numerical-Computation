# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 16:05:14 2021

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
        #A[i+1][i] = 0
        At[i+1][i+1] = At[i+1][i+1] - f * At[i][i+1]
        bt[i+1] = b[i+1] - f * b[i]
    return At, bt

def back_subs(At, bt):
    x = np.copy(bt)
    for i in range(len(At) - 1,0,-1):
        if(i == len(At) - 1):
            x[i] = bt[i] / At[i][i]
        else:
            x[i] = ( bt[i] - At[i][i+1] ) / At[i][i]
    return x
        

n = 7 
A1 = np.diag(np.ones(n))*3
A2 = np.diag(np.ones(n-1),1) 
A = A1 + A2 + A2.T 
b = np.arange(n,2*n)*1.

result1, result2 = triangular(A, b)
np.set_printoptions(precision = 2)
print('X \n')
print(back_subs(result1, result2))

n = 8 
np.random.seed(3)
A1 = np.diag(np.random.rand(n))
A2 = np.diag(np.random.rand(n-1),1)
A = A1 + A2 + A2.T 
b = np.random.rand(n)

result3, result4 = triangular(A, b)
print()
print('X \n')
print(back_subs(result3, result4))
