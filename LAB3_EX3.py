# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 16:25:10 2021

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
        f = A[i+1][0] / A[i][1]
        At[i+1][0] = A[i+1][0] - f * A[i][1]
        At[i+1][1] = A[i+1][1] - f * A[i][2]
        bt[i+1] = b[i+1] - f * b[i]
    return At, bt


def back_subs(At, bt):
    x = np.copy(bt)
    for i in range(len(At) - 1,0,-1):
        if(i == len(At) - 1):
            x[i] = bt[i] / At[i][1]
        else:
            x[i] = ( bt[i] - At[i][2] ) / At[i-1][1]
    return x    
    
n = 7 

Ar = np.zeros((n,3))
Ar[:,0] = np.concatenate((np.array([0]),np.ones((n-1),)))
Ar[:,1] = np.ones((n),)*3
Ar[:,2] = np.concatenate((np.ones((n-1),),np.array([0])))

b = np.arange(n,2*n)*1.

print('Ar')
print(Ar)
print()
print('b')
print(b)
print()

result1, result2 = triangular(Ar, b)
np.set_printoptions(precision = 2)

print('---- TRIANGULAR SYSTEM ----\n At')
print(result1)
print('---- SOLUTION ----\n x')
print(back_subs(result1, result2))


n = 8

np.random.seed(3)
Ar = np.zeros((n,3))
Ar[:,1] = np.random.rand(n)
Ar[:,0] = np.concatenate((np.array([0]),np.random.rand(n-1)))
Ar[0:n-1,2] = Ar[1:n,0]

b = np.random.rand(n)

print('Ar')
print(Ar)
print()
print('b')
print(b)
print()

result3, result4 = triangular(Ar, b)
np.set_printoptions(precision = 2)

print('---- TRIANGULAR SYSTEM ----\n At')
print(result3)
print('---- SOLUTION ----\n x')
print(back_subs(result3, result4))
