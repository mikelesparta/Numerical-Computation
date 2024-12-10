# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 13:13:56 2021

@author: mikel
"""
#%%
import numpy as np
import matplotlib.pyplot as plt
#import math
#%%

def lagrange_fundamental(k,x,z):
    lk = 1
    length = len(x)
    for i in range (length):
        if( i == k ):
            lk *= 1
        else:
            lk *= (z - x[i]) / (x[k] - x[i])
    return lk



x = np.array([-1., 0, 2, 3, 5])
y = np.array([ 1., 3, 4, 3, 1])

xp = np.linspace(min(x),max(x))
p  = np.polyfit(x,y,len(x)-1)
yp = np.polyval(p,xp)

plt.figure()
plt.plot(xp,yp,'b-', label = 'interpolant polynomial')
plt.plot( x, y,'ro', label = 'points')
plt.legend()
plt.show()

k = 2
z = 1.3
yz = lagrange_fundamental(k,x,z)
print(yz)
print()

k = 2
z = np.array([1.3, 2.1, 3.2])
yz = lagrange_fundamental(k,x,z)
print(yz)
print()


po = 1
for i in range(len(y)):
    po += y[i] * lagrange_fundamental(i,x,z)


plt.figure()
plt.plot(x,po,'b-')
#plt.plot( x, yz,'ro')
plt.legend()
plt.show()

print(np.eye(len(x)))