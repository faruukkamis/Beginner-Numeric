# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 18:07:34 2021

@author: faruukkamis
"""

import numpy as np

f = lambda x: 2/(2+x**2)     # Write function here.

def Simpson():
    b1 = float(input(' Enter the lower bound of integral : '))
    b2 = float(input(' Enter the upper bound of integral : '))
    num_intervals = int(input(' Enter the number of intervals : '))
    
    h = (b2-b1)/num_intervals       # step size
    I = f(b1) + f(b2)       # total of boundary values.
    
    for i in range (1,num_intervals):
        d = b1 + i*h
        
        if i%2 == 0:
            I = I + 2*f(d)
        else:
            I = I + 4*f(d)
    I = I*h/3
    
    return I

print(Simpson())



