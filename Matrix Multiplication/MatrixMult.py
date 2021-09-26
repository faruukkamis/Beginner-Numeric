# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 21:18:33 2021

@author: faruukkamis
"""
import numpy as np

while True:   
    x = input('Are you writing the matrices (w) or reading from the file (r) ? press (w) or (r) :').lower()
    if x == 'r' or x == 'w':
        break
    
if x == 'w':

    #Column and row numbers of matrix.
    i = int(input('Number of row for first matrix:'))
    j = int(input('Number of column for first matrix:'))
    k = int(input('Number of column for first matrix:'))
    
    A = np.zeros((i,j))
    B = np.zeros((j,k))
    
    def MatM():  
        
        #Entering values of Matrix A.
        for m in range(i):
            for n in range(j):
                A[m][n] = int(input(f'Enter the {m}. row {n}. columns of matrix A:'))
        
        #Entering values of Matrix B.
        for m in range(j):
            for n in range(k):
                B[m][n] = int(input(f'Enter the {m}. row {n}. columns of matrix B:'))
        
        result = []
        
        #Multiplication of matrices.
        for m in range(len(A)):
            row = []
            for n in range(len(B[0])):
                mult = 0
                for l in range(len(A[0])):
                    mult += A[m][l] * B[l][n]
                row.append(mult)
            result.append(row)
        
        for m in range(len(result)):
            print(result[m],'\n')
    MatM()
    
elif x == 'r':
    #Files must be in the same folder with code and extension of file is .csv.
    A = input('Enter the file name of first matrix with extension:')
    B = input('Enter the file name of second matrix with extension:')
    A = np.genfromtxt(A, delimiter=',')
    B = np.genfromtxt(B, delimiter=',')
    
    def MatM():  
        
        result = []
        
        #Multiplication of matrices.
        for m in range(len(A)):
            row = []
            for n in range(len(B[0])):
                mult = 0
                for l in range(len(A[0])):
                    mult += A[m][l] * B[l][n]
                row.append(mult)
            result.append(row)
        
        for m in range(len(result)):
            print(result[m],'\n')
    MatM()
    
#res = np.matmul(A,B) --> To multiplication of matrices without using loops.