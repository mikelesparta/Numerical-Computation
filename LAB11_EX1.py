# -*- coding: utf-8 -*-
"""
Created on Mon May 10 15:46:42 2021

@author: mikel
"""
#%%
import numpy as np
from numpy.linalg import *
np.set_printoptions(precision = 8)   
np.set_printoptions(suppress = True)
#%%

def jacobi(A, b, x0, tol, maxiter=1000):
    iterations = 0
    sol = x0.copy()
    x_prev = x0.copy()
    n = A.shape[0]     
    diff = tol * 2
    while (diff > tol) and (iterations< maxiter):
        for i in range(0, n):
            subs = 0.0
            for j in range(0, n):
                if i != j:
                    subs += A[i,j] * x_prev[j]
            sol[i] = (b[i] - subs ) / A[i,i]
        iterations = iterations + 1
        diff = norm(sol - x_prev) / norm(sol)
        x_prev = sol.copy()
    return sol,  iterations

n = 4
A = np.array([[5, 1, -1, -1], [1, 4, -1, 1], [1, 1, -5, -1], [1, 1, 1, -4]])
b = np.array([1, 1, 1, 1])
tol = 1.e-6
maxiter=1000
xs = np.linalg.solve(A,b)
x0 = np.zeros(n);
sol, i = jacobi(A,b, x0 ,tol, maxiter)

print("--- Data ---")
print("A")
print(A)
print("b")
print(b)
print("\n--- Solution ---")
print(i, "iterations")
print("Apporximate x")
print(sol)
print("Exact x")
print(xs)

n = 9 
A1 = np.diag(np.ones(n))*2 
A2 = np.diag(np.ones(n-1),1)
A = A1 + A2 + A2.T 
b = np.concatenate((np.arange(1,6),np.arange(4,0,-1)))*1
xs = np.linalg.solve(A,b)
x0 = np.zeros(n);
sol, i = jacobi(A,b, x0 ,tol, maxiter)

print("--- Data ---")
print("A")
print(A)
print("b")
print(b)
print("\n--- Solution ---")
print(i, "iterations")
print("Apporximate x")
print(sol)
print("Exact x")
print(xs)


