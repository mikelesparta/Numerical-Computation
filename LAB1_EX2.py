# -*- coding: utf-8 -*-
"""
Exercise 2
"""
import numpy as np
import matplotlib.pyplot as plt
#%%
f = lambda x: np.exp(x)

def funExp(x, tol, maxNumSum):
    polynomial = 0.
    factorial  = 1.
    error = np.inf
    i = 1
    
    while (error > tol and i < maxNumSum):
        term = x**i / factorial
        polynomial += term
        error=np.max(abs(term))
        factorial *= i+1
        i += 1
    return polynomial
    
a = -1.; b = 1.
tol = 1.e-8
maxNumSum = 100

x = np.linspace(a,b) 
y = f(x)
z = funExp(x,tol,maxNumSum)
OX = 0*x                               
plt.figure()
plt.plot(x,y, label = 'f')
plt.plot(x,z,'-', label = 'f approximation')
plt.plot(x,OX,'k') 
plt.title('f apporixmation with McLaurin series') 
plt.legend()                          
plt.show()

