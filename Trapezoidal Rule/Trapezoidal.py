# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 00:23:14 2021

@author: faruukkamis
"""

import numpy as np
import matplotlib.pyplot as plt

def Func(x):
    return np.exp(x) + x**2 + x     # Write function here.

a = float(input('Starting point:'))
b = float(input('End point:'))
c = float(input('Space between points:'))

x = np.arange(a,b,c)

y = []

for i in range (len(x)):
    y.append(Func(x[i]))

def Trep():
    t1 = 0
    for i in range(len(x)-2):
        t1 += y[i+1]*2
        
    return ((t1 + y[0]+ y[-1])*0.5)*(b-a)/len(x)    

print(Trep())

# Trapezoidal rule w/out using loop and function, dx is the space btw points.
#print(np.trapz(y,x,dx=0.4)) 
    

