# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 21:22:16 2021

@author: faruukkamis
"""

# Drilled Piers HW

import numpy as np
from scipy import linalg
from numpy import savetxt
import pandas as pd

EE = -3         # -(Ep*Ap + 2t1)
length = 10     # length of pile
n = 100         # number of pieces
k1 = 0.001
P0 = 800
K = 100
dz = length/n

# matrix should be (n-1)x(n-21) b/c no 0. and n. element
stiffMat = [ [ 0 for i in range(n-1) ] for j in range(n-1) ]    
forceMat = np.zeros(n-1,float)

stiffMat[0][0] = -EE + k1*dz    # w1 coeff.
stiffMat[0][1] = EE             # w2 coeff.
forceMat[0] = P0*k1*dz/EE       # first element of force matrix.

for i in range(1,n-2):
    stiffMat[i][i-1] = k1*dz**2 + EE
    stiffMat[i][i] = -2*EE
    stiffMat[i][i+1] = EE
    
# last row elements 
stiffMat[n-2][n-3] = EE + k1*dz                     
stiffMat[n-2][n-2] = ((-EE+2*K*dz)/(1-(K*dz/EE)))

# solving
defMat = []
defMat = np.linalg.solve(stiffMat,forceMat)

# to get good looking dataframe
savetxt('stiffMat.csv', stiffMat, delimiter=',')
StifnessMat = pd.read_csv('stiffMat.csv', header = None )





