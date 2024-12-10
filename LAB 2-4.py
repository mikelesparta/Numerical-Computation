# -*- coding: utf-8 -*-
"""
Taylor
e^x approx 1 + x^1/1! + x^2/2! + x^3/3!
"""
import numpy as np
import matplotlib.pyplot as plt
#%%
def P(x0, degree):
    polynomial = 0.
    factorial  = 1.
    
    for i in range(degree + 1):
        term = x0**i / factorial
        polynomial += term
        factorial *= i+1
    return polynomial

#%%
x = np.linspace(-3,3)

plt.figure()
plt.plot(x,np.exp(x),label='f')
plt.plot(x,0*x,'k')

for degree in range(1,5):
    plt.plot(x,P(x,degree), label='P'+str(degree))
    plt.legend()
    plt.pause(2)
plt.show()






