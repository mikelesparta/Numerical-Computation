# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 16:12:50 2021

@author: mikel
"""
#%%
import numpy as np
#%%
def divisors(m):
    j = 0
    n = 0
    divisors = np.zeros(2*m)
    for i in range(1, m + 1):
        if(m%i == 0):  
            divisors[j] = i
            divisors[j + 1] = -i
            j += 2
            n += 2
    divisors = divisors[:n]
    return divisors

def roots(p):
    aux = horner(p, 1)
    return aux
        
def horner(p,x0):
    quotient = np.zeros_like(p)
    quotient[0] = p[0]
    for i in range(1, len(p)):
        quotient[i] = p[i] + quotient[i -1]*x0
    quotient = quotient[:-1]
    return quotient

p0 = np.array([1., 0, -1])
p1 = np.array([1., -3, -6, 8])
p2 = np.array([1., 2, -16, -2, 15])
p3 = np.array([1.,-5, -13, 53, 60])   
p4 = np.array([1., 4, -56, -206, 343, 490])


print('Divisors of 6 ', divisors(6))
print('Divisors of 18 ', divisors(18))
print('Divisors of 20 ', divisors(20))

print('Roots of p0 ', roots(p0))
print('Roots of p1 ', roots(p1))
print('Roots of p2 ', roots(p2))
print('Roots of p3 ', roots(p3))
print('Roots of p4 ', roots(p4))
