# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 14:54:01 2021

@author: faruukkamis
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

Tn = 3.1416
D = 0.1
J = 0
t = 0
m = 1
Tf = 5*Tn       # data are needed until this time.
dt = 0.1
wn = 2*np.pi/Tn
U0 = 1
dU0 = 0

def Duh(t,J,m,Tn,wn):
    if J<2*Tn:
        F = m
    else:
        F=0
    
    return F*np.exp(-D*wn*(t-J))*np.sin(wn*(t-J))


    

U = np.zeros(int(Tf/dt)+1)
time = np.arange(0,Tf,dt)

for i in range(0,int(Tf/dt)+1):
    
    for j in range(i,int(Tf/dt)+1):
        
        Integrate, error = quad(Duh, 0, time[i], args=(J,m,Tn,wn))
        U[j] = (1/(m*wn))*Integrate + np.exp(-D*wn*time[i])*(U0*np.cos(wn*time[i])+((dU0/wn)+D*U0)*np.sin(wn*time[i])) + U[j]
        
    
    J = J + dt
    

plt.title(' Response of 1 d.o.f damped system')
plt.xlabel(' time (sec)')
plt.ylabel(' U(t) (m)') 
fig = plt.plot(time,U)
plt.grid()
fig = plt.gcf()
fig.set_size_inches(24, 14)
#fig.savefig('Q5.png', dpi=300)

