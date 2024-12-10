# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 15:06:56 2021

@author: mikel
"""
#%%
import numpy as np
import matplotlib.pyplot as plt
#%%
p = np.array([1, -1, 2, -3,  5, -2])
p0, p1, p2, p3, p4, p5 = p

g = lambda x: p0*x**5 + p1*x**4 + p2*x**3 + p3*x**2 + p4*x + p5
d1g = lambda x: 5*p0*x**4 + 4*p1*x**3 + 3*p2*x**2 + 2*p3*x + p4
d2g = lambda x: 20*p0*x**3 + 12*p1*x**2 + 6*p2*x + 2*p3

a = -1.; b = 1.
x = np.linspace(a,b)
plt.plot(x,0*x,'k')
plt.plot(x,g(x), label = 'g')
plt.plot(x,d1g(x), label = 'd1g')
plt.plot(x,d2g(x), label = 'd2g')
plt.legend()
plt.show()

x0 = -0.5
print('P value at point ', x0)
print('With polyval:          ', np.polyval(p, x0))
print('With lambda function g:', g(x0))

def horner(p,x0):
    q = np.zeros_like(p)
    q[0] = p[0]
    for i in range(1, len(p)):
        q[i] = p[i] + q[i -1]*x0
    return q

p0 = np.array([1.,2,1])
x0 = 1.

p1 = np.array([1., -1, 2, -3,  5, -2])
x1 = 1.

p2 = np.array([1., -1, -1, 1, -1, 0, -1, 1])
x2 = -1.

a = -1.; b = 1.
x = np.linspace(a,b)
plt.plot(x,0*x,'k')
plt.plot(x,horner(p0, x0), label = 'P0')
plt.plot(x,horner(p1, x1), label = 'P1')
plt.plot(x,horner(p2, x2), label = 'P2')
plt.legend()
plt.show()

