# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 21:09:31 2021

@author: faruukkamis
"""

import numpy as np
import matplotlib.pyplot as plt

def dyn(wn,EE,A,tt):
    '''
    
    Parameters
    ----------
    wn : TYPE: Float.
        DESCRIPTION: Circular natural frequency.
    EE : TYPE: Float.
        DESCRIPTION: Damping ratio.
    A : TYPE: Float.
        DESCRIPTION: Constant.
    t : TYPE: Float.
        DESCRIPTION: End time.
    phi : TYPE: Float.
        DESCRIPTION: Constant.    
    Returns
    -------
    L : TYPE: List.
        DESCRIPTION: Displacement function.
    t : TYPE: List.
        DESCRIPTION: Time interval.

    '''
    
    L = []
    k = tt/5000
    t = []
    for i in range(5000):
        t.append(k)
        a = A*np.exp(-EE*wn*k)*np.sin(wn*np.sqrt(1-EE**2)*k+ 1)
        L.append(a)
        k = k+ tt/5000
    return L,t

x1, t1 = dyn(12.5, 0.0276,5,6)
x2, t2 = dyn(12.5, 0.1,5,6)

# Plotting
plt.title(' Viscously Damped Free Vibration')
plt.ylabel(' x(t) ')
plt.xlabel(' time(sec) ')
plt.plot(t1, x1, color = 'orange', label = 'for first EE')
plt.plot(t2, x2, color = 'green', label = 'for second EE')
plt.legend(loc = 'lower right')
fig = plt.gcf()
fig.set_size_inches(14, 7)
fig.savefig('freevib.png', dpi=100)