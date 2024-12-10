# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 16:12:50 2021

@author: mikel
"""
#%%
import numpy as np
import matplotlib.pyplot as plt
#%%
def horner(p,x0):
    q = np.zeros_like(p)
    q[0] = p[0]
    for i in range(1, len(p)):
        q[i] = p[i] + q[i -1]*x0
    return q

def HornerV(p, x):
    y = np.zeros_like(x)
    for i in range(0, len(x)):
        y[i]=horner(p,x[i])[-1]
    return y


p = np.array([1., -1, 2, -3, 5, -2])
r = np.array([1., -1, -1, 1, -1, 0, -1, 1])

x = np.linspace(-1,1)
plt.plot(x,0*x,'k')
plt.plot(x,HornerV(p, x), label = 'P')
plt.plot(x,HornerV(r, x), label = 'R')
plt.legend()
plt.show()