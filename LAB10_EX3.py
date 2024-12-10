# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 16:56:57 2021

@author: mikel
"""
#%%
import numpy as np
#%%

def gaussjordan(A):
    m,n = A.shape 
    I = np.eye(m)
    M = np.c_[A,I]
    j = 0
    
    for i in range(m-1):
        if(M[i][i] == 0):
            exit
        pivot = M[i][j]
                        
        for k in range(i+1, m):
            aux = M[k][j]
            multiplier = aux / pivot
            M[k] = M[k] - multiplier * M[i]
        j += 1

    #Upper diagonal
    j = m-1
    for i in range(m-1,0,-1):
        pivot = M[i][j]
        for k in range(i-1,-1,-1):
            target = M[k][j]
            multiplier = target / pivot
            M[k] = M[k] - multiplier * M[i]
        j -= 1

    for i in range(m):
        M[i] /= M[i][i]
            
    return M[:,m:]

U = np.array([[2, 1, 1], [1, 2, 1], [1, 1, 2]])
U_inv = gaussjordan(U)

V = np.array([[0.55, 0.71, 0.29, 0.51, 0.89], [0.9, 0.13, 0.21, 0.05, 0.44], [0.03, 0.46, 0.65, 0.28, 0.68], [0.59, 0.02, 0.56, 0.26, 0.42], [0.28, 0.69, 0.44, 0.16, 0.54]])
V_inv = gaussjordan(V)

print("Matrix")
print(U)
print("Inversed matrix")
print(U_inv)
print("\n Matrix")
print(V)
print("Inversed matrix")
print(V_inv)
   