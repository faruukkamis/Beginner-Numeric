# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 17:06:37 2021

@author: faruukkamis
"""

import numpy as np

f = lambda x: x**3 + 4*x**2 -10     # Write function here.

p1 = float(input(' Enter the first value to approximation: '))
p2 = float(input(' Enter the second value to approximation: '))
TOL = float(input(' Enter the tolerance value: '))
iterations = int(input(' Enter the number of iteration: '))

def Secant(p1,p2,TOL,iterations):
    
    if p1 == p2:
        print(' p1 cannot be equal to p2! ')
    
    elif p1 != p2:  
        for i in range (iterations):
            p = p2 - (f(p2)*(p2-p1))/(f(p2)-f(p1))
            
            if f(p) < TOL:
                print(' Root is : ',p)
                print(f' Found at {i+1}. iteration. ')
                break
            else:
                p1 = p2
                p2 = p
                     
Secant(p1, p2, TOL, iterations)



