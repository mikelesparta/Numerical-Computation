# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 13:38:35 2021

@author: mikel
"""
#%%
import math
#%%

def newton(f, df, x0, tol,maxiter):
    error = 1
    iterations = 0
    x = x0
    while (error > tol):
        Xk = x - (f(x) / df(x))
        error = math.fabs(Xk-x)
        x = Xk
        iterations += 1
    return Xk, iterations-1


f = lambda x : x**5 - 3 * x**2 + 1.6
df = lambda x : 5 * x**4 - 6 * x

g = lambda x : (x + 2) * math.cos(2*x)
dg = lambda x : math.cos(2*x)-2*(x +2)* math.sin(2*x)
tol = 1e-6
maxiter = 100

print(newton(f,df,-0.6,tol,maxiter))
print(newton(f,df,0.9,tol,maxiter))
print(newton(f,df,1.3,tol,maxiter))
print()
print(newton(g,dg,0.7,tol,maxiter))

