"""
Created on Wed Mar 10 15:35:55 2021

@author: mikel
"""
#%%
import numpy as np
import matplotlib.pyplot as plt
import math
#%%

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
x = np.linspace(0,1.5)              
OX = 0*x                             

plt.figure()
plt.plot(x,f(x))               
plt.plot(x,OX,'k-')            
plt.show()

print(incrementalSearch(f,-1,1.5,25))
print()

g = lambda x : (x + 2) * math.cos(2*x)

print(incrementalSearch(g,0,10,100))