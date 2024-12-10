# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 17:47:06 2021

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
n = 5
Ie = sym.integrate(fs, (x, a, b))
Ie = float(Ie)

def midpoint(f,a,b) :
      return (b - a) * f((a + b) / 2)  
  
def trapez(f,a,b):
    return ((b - a) /2) * (f(a) + f(b)) 

def simpson(f,a,b):
    return ((b-a)/6) * (f(a)+4*f((a+b)/2)+f(b))

def comp_midpoint(f,a,b,n):
    x=0
    h=(b-a)/n
    for i in range(0,n):
        ai=a+i*h  
        bi=a+(i+1)*h
        x= x+ midpoint(f,ai,bi)
    return x

I_cmid = comp_midpoint(f,a,b,n)
print('The approximate value is = ', I_cmid)
print('The exact value is = ', Ie)
print('---------------------------------\n')


def comp_trapz(f,a,b,n):
    x=0
    h=(b-a)/n
    for i in range(0,n):
        ai=a+i*h #nodo inicial
        bi=a+(i+1)*h #nodo final
        x= x+ trapez(f,ai,bi)
    return x

I_ctrap = comp_trapz(f,a,b,n)
print('The approximate value is = ', I_ctrap)
print('The exact value is = ', Ie)
print('---------------------------------\n')


def comp_simpson(f,a,b,n):
    x=0
    h=(b-a)/n
    for i in range(0,n):
        ai=a+i*h #nodo inicial
        bi=a+(i+1)*h #nodo final
        x= x+ simpson(f,ai,bi)
    return x

I_csim = comp_simpson(f,a,b,n)
print('The approximate value is = ', I_csim)
print('The exact value is = ', Ie)
