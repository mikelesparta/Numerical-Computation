# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 22:57:27 2021

@author: mikel
"""
#%%
import numpy as np
#%%

#FORWARD
def df_f(f,x0,h):
    return (f(x0+h)-f(x0))/h

#BACKWARD
def df_b(f,x0,h):
    return (f(x0)-f(x0-h))/h

#CENTERED
def df_c(f,x0,h):
    return ((df_f(f,x0,h)+df_b(f,x0,h))/2)

def df_fOrder2(f,x0,h):
    return (-3*f(x0)+4*f(x0+h)-f(x0+2*h))/(2*h)

def df_bOrder2(f,x2,h):
    return (f(x2-2*h)-4*f(x2-h)+3*f(x2))/(2*h)

f= lambda x: x**3 + x**2 + x
df= lambda x: 3*x**2 + 2*x + 1

a=0
b=1
h=0.02

xp = np.arange(a,b+h,h)

dfa=np.zeros(len(xp))
dfa[0] = df_f(f,xp[0],h)
dfa[-1] = df_b(f,xp[-1],h)
dfa[1:-1] = df_c(f,xp[1:-1],h)

dfb=np.zeros(len(xp))
dfb[0] = df_fOrder2(f,xp[0],h)
dfb[-1] = df_bOrder2(f,xp[-1],h)
dfb[1:-1] = df_c(f,xp[1:-1],h)

error1 = np.linalg.norm(df(xp)-dfa)/np.linalg.norm(df(xp))
error2 = np.linalg.norm(df(xp)-dfb)/np.linalg.norm(df(xp))

print('Error with order 1 approximation =',error1)
print('Error with order 2 approximation =',error2)