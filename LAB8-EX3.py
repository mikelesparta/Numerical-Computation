# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 20:51:11 2021

@author: mikel
"""
#%%
import numpy as np
import matplotlib.pyplot as plt
#%%

def D2f(f,x1,h):
    return (f(x1-h)-2*f(x1)+f(x1+h))/(h**2)

f = lambda x: np.cos(2*np.pi*x)
d2f = lambda x: -4*np.pi**2*np.cos(2*np.pi*x)

a=-1
b=0
h=0.001

xp=np.arange(a,b+h,h)
d2_f=D2f(f,xp[1:-1],h)

plt.plot(xp[1:-1],d2f(xp[1:-1]),label='Second derivative')
plt.plot(xp[1:-1],d2_f,label='Second derivative 2')
plt.legend()
plt.show()

E = np.linalg.norm(d2f(xp[1:-1])-d2_f)/np.linalg.norm(d2f(xp[1:-1]))

print('Relative error',E)