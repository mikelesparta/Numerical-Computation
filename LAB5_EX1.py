# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 15:39:00 2021

@author: mikel
"""
#%%
import numpy as np
import math
import matplotlib.pyplot as plt
#%%

def secantf(f, x0, x1, tol, maxiter):
    i = 0
    xk = 0
    error = 1
    iterations = 0
    for i in range(maxiter):
        while(error > tol):
            xk=x1-f(x1)*((x1-x0)/(f(x1)-f(x0)))
            error = math.fabs(xk-x1)
            x0 = x1
            x1 = xk
            iterations = iterations + 1
    return xk, iterations
    
def incrementalSearch(f,a,b,n):
    dx = (b-a) / n
    c = 0
    intervals = np.zeros((n,2))
    while a<b: 
        y=a+dx
        if ((f(a)*f(y)) < 0):
            intervals[c][0] = a
            intervals[c][1] = y
            a=y
            c = c + 1
        else:
            a=y
    intervals = intervals[:c,:]
    return intervals



f = lambda x : x**5 - 3 * x**2 + 1.6
tol=1e-6
maxiter=100

print(incrementalSearch(f,-1,1.5,25))

x0 = -0.7
x1 = -0.6
xk1, it1 = secantf(f,x0,x1,tol,maxiter)
print(secantf(f,x0,x1,tol,maxiter))

x2 = 0.8
x3 = 0.9
xk2, it2 = secantf(f,x2,x3,tol,maxiter)
print(secantf(f,x2,x3,tol,maxiter))

x4 = 1.2
x5 = 1.3
xk3, it3 =secantf(f,x4,x5,tol,maxiter)
print(secantf(f,x4,x5,tol,maxiter))

x = np.linspace(-1,1.5)              
OX = 0*x 
r = np.zeros(3)
r[0] = xk1
r[1] = xk2
r[2] = xk3

plt.figure()
plt.plot(x,f(x))               
plt.plot(x,OX,'k-')   
plt.plot(r,r*0,'ro')         
plt.show()