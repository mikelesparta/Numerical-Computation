# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 18:59:08 2021

@author: mikel
"""
#%%
import numpy as np
import matplotlib.pyplot as plt
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

a = 1
b = 2.1
h1 = 0.1
h2 = 0.01

f = lambda x: np.log(x)
df = lambda x: 1/x

xp = np.arange(a,b+h1,h1)

# h = 0.1
plt.plot(xp[1:-1],df(xp[1:-1]),label='df') 
plt.plot(xp[1:-1],df_f(f,xp[1:-1],h1),label='df_f')
plt.plot(xp[1:-1],df_b(f,xp[1:-1],h1),label='df_b')
plt.plot(xp[1:-1],df_c(f,xp[1:-1],h1),label='df_c')
plt.legend()
plt.show()

ErrorG_f=np.linalg.norm(df(xp[1:-1])-df_f(f,xp[1:-1],h1))/np.linalg.norm(df(xp[1:-1]))
ErrorG_b= np.linalg.norm(df(xp[1:-1])-df_b(f,xp[1:-1],h1))/np.linalg.norm(df(xp[1:-1]))
ErrorG_c= np.linalg.norm(df(xp[1:-1])-df_c(f,xp[1:-1],h1))/np.linalg.norm(df(xp[1:-1]))

print("h = 0.1")
print('ErrorG_f',ErrorG_f)
print('ErrorG_b',ErrorG_b)
print('ErrorG_c',ErrorG_c)

#h = 0.01
plt.plot(xp[1:-1],df(xp[1:-1]),label='df2') 
plt.plot(xp[1:-1],df_f(f,xp[1:-1],h2),label='df_f2')
plt.plot(xp[1:-1],df_b(f,xp[1:-1],h2),label='df_b2')
plt.plot(xp[1:-1],df_c(f,xp[1:-1],h2),label='df_c2')
plt.legend()
plt.show()

errorDF_F=abs(df(xp[1:-1])-df_f(f,xp[1:-1],h2))
errorDF_B=abs(df(xp[1:-1])-df_b(f,xp[1:-1],h2))
errorDF_C=abs(df(xp[1:-1])-df_c(f,xp[1:-1],h2))

plt.plot(xp[1:-1],errorDF_F,label='error df_f')
plt.plot(xp[1:-1],errorDF_B,label='error df_b')
plt.plot(xp[1:-1],errorDF_C,label='error df_c')
plt.legend()
plt.show()

ErrorG_f=np.linalg.norm(df(xp[1:-1])-df_f(f,xp[1:-1],h2))/np.linalg.norm(df(xp[1:-1]))
ErrorG_b=np.linalg.norm(df(xp[1:-1])-df_b(f,xp[1:-1],h2))/np.linalg.norm(df(xp[1:-1]))
ErrorG_c=np.linalg.norm(df(xp[1:-1])-df_c(f,xp[1:-1],h2))/np.linalg.norm(df(xp[1:-1]))

print()
print("h = 0.01")
print('ErrorG_f',ErrorG_f)
print('ErrorG_b',ErrorG_b)
print('ErrorG_c',ErrorG_c)



