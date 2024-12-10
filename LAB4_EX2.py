# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 16:12:01 2021

@author: mikel
"""
#%%
import math
#%%

def bisection(f,a,b,tol,maxiter):
    if f(a)*f(b)>0:
        print('Sign never changes')
        return 0
    elif f(a)==0:
        print('Root')
        return a,0
    elif f(b)==0:
        print('Root')
        return b,0
    
    lastx = 0
    iterations = 1
    x = (a + b) / 2
    i = 1
    while i < maxiter and (math.fabs(x-lastx) > tol or lastx==0):
        if (f(a)*f(x) < 0):
            b = x
        elif (f(a)*f(x) > 0):
            a = x
        else:
            return x
        lastx = x
        x = (a + b) / 2
        iterations += 1
    return x, iterations

f = lambda x : x**5 - 3 * x**2 + 1.6
g = lambda x : (x + 2) * math.cos(2*x)
tol = 1e-6
maxiter = 100

print(bisection(f,-0.7,-0.6,tol,maxiter))
print(bisection(f,0.8,0.9,tol,maxiter))
print(bisection(f,1.2,1.3,tol,maxiter))
print()
print(bisection(g,0.7,0.8,tol,maxiter))

