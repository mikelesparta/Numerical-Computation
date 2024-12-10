# -*- coding: utf-8 -*-
"""
Taylor
e^x approx 1 + x^1/1! + x^2/2! + x^3/3!
"""
import numpy as np
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
x0 = 0.5
degree = 3
p = P(x0,degree)
print('P3(0.5)     = ', p)
print('np.exp(0.5) = ', np.exp(x0))
'''
i = 0
x0**0 -> 1.
factorial -> 1.
term    ->1.
polynomial->0.+1.->1.

factorial ->1.*1 ->1.
#%%
i = 1
x0**1 -> xo^1
factorial -> 1.
term    ->x0/1
polynomial->1.+x0/1

factorial ->1.*2

#%%
i = 2
x0**2 -> x0^2
factorial -> 1*2
term    ->x0^2/(1,*2)
polynomial->1.+x0/1 + x0^2/(1.*2)

factorial ->1.*2*3

#%%
i = 2
x0**2 -> x0^2
factorial -> 1*2
term    ->x0^2/(1,*2)
polynomial->1.+x0/1 + x0^2/(1.*2)

factorial ->1.*2*3

e^x approx 
'''