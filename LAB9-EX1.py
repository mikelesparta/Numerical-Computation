# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 16:41:31 2021

@author: mikel
"""
#%%
import numpy as np
import sympy as sym
#%%

x = sym.Symbol('x', real=True) 
fs = sym.log(x)
f = lambda x: np.log(x)
a = 1
b = 3
Ie = sym.integrate(fs, (x, a, b))
print(Ie)
Ie = float(Ie)
print(Ie)

def midpoint(f,a,b) :
      return (b - a) * f((a + b) / 2)  
   
I_mid = midpoint(f,a,b)
print('---------------------------------\n')
print('The approximate value is = ', I_mid)
print('The exact value is = ', Ie)
print('---------------------------------\n')

def trapez(f,a,b):
    return ((b - a) /2) * (f(a) + f(b)) 

I_tra = trapez(f,a,b)

print('The approximate value is = ', I_tra)
print('The exact value is = ', Ie)
print('---------------------------------\n')

def simpson(f,a,b):
    return ((b-a)/6) * (f(a)+4*f((a+b)/2)+f(b))

I_sim = simpson(f,a,b)
print('The approximate value is = ', I_sim)
print('The exact value is = ', Ie)
