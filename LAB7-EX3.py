# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 18:06:26 2021

@author: mikel
"""
#%%
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
#%%

def Matrix(f,a,b,d):
    n=d+1
    N=np.zeros((n,n))
    B=np.zeros(n)
    
    for i in range(n):
        h= lambda z: f(z)*z**(i)
        B[i]= quad(h,a,b)[0]
        
        for j in range(0,n):
            g=lambda z: z**(i+j)
            N[i,j]=quad(g,a,b)[0] 
            
    return N,B 

def approx2(f,d,a,b):
    N, B = Matrix(f,a,b,d)
    aux = np.linalg.solve(N,B) 
    A = aux[::-1] 
    return A 

a = 0
b = 2
d = 2

xp=np.linspace(a,b) 

f = lambda x:np.sin(x)
y = f(xp)

plt.plot() 
plt.plot(xp,y,'r',label='function') 
plt.plot(xp,np.polyval(approx2(f,d,a,b),xp),'b', label='fitting polynomial')
plt.legend()
plt.show()

A, B = Matrix(f,a,b,d)

print('Coefficient matrix')
print(A)
print()
print('Right-hand side term')
print(B)
print()
print('System solution')
print(approx2(f,d,a,b))
print()
print()

a = -2
b = 0
x2 = np.linspace(-1,1,10)
f2 = lambda x:np.cos(np.arctan(x))-np.log(x+5)
y = f2(x2)
A, B = Matrix(f2,a,b,d)

print('Coefficient matrix')
print(A)
print()
print('Right-hand side term')
print(B)
print()
print('System solution')
print(approx2(f2,d,a,b))