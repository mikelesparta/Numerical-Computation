# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:09:28 2021
plot the graph
"""
import numpy as np
import matplotlib.pyplot as plt
#%%
f = lambda x: np.exp(x) #e^x
a = -1.; b = 1.
x = np.linspace(a,b,5) #w/o the 5 the graph is clearer
#x1 = np.arrange(a,b+0.1,0.5)
y = f(x) #vectorization
#%%
import time
z = np.linspace(-10,10,10**6)
zy = np.zeros_like(z)

t0 = time.time()
for i in range(len(z)):
    zy[i] = f(z[i])
t1 = time.time()-t0   
print('Without vectorization: ', t1,' seconds') 

t0 = time.time()
zy = f(z)
t1 = time.time()-t0   
print('Without vectorization: ', t1,' seconds') 
#%%
plt.figure()
plt.plot(x,y) 
plt.show()
plt.plot(x,y,'o-')
#%%
f = lambda x: np.sin(20*x) 
a = -1.; b = 1.
x = np.linspace(a,b) #w/o the 5 the graph is clearer
y = f(x) #vectorization
#%%
plt.figure()
plt.plot(x,y,'-') 
plt.show()
#%%
f = lambda x: np.exp(x) #e^x
a = -1.; b = 1.
x = np.linspace(a,b) #w/o the 5 the graph is clearer
y = f(x) #vectorization
ox = 0*x
#%%
plt.figure()
plt.plot(x,y, label ='f(x) = $e^x$') 
plt.plot(x,ox,'k',label ='OX axis') 
plt.legend()
plt.title('Example of graph')
plt.show()







