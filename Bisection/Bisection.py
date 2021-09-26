import numpy as np

f = lambda x: x**3 + 4*x**2 - 10 #write function here w.r.t x.

a = float(input(' Enter the first boundary : '))
b = float(input(' Enter the second boundary : '))
TOL = float(input(' Enter the tolerans value : '))
iteration = int(input(' Enter the max iteration number : '))

# f(a) and f(b) cannot have the same sign for bisection method.
if f(a)*f(b) > 0:
    while f(a)*f(b) > 0:
        a = float(input(' Enter the first boundary : '))
        b = float(input(' Enter the second boundary : '))

def Bisection(f,a,b,TOL,iteration):
    
    # getting midpoint
    m = (a+b)/2
    
    # Tolerans value is used as stopping criteria.
    if np.abs(f(m)) < TOL:
        return m
    
    # f(m) is used instead of whichever function has the same sign. 
    elif np.sign(f(m)) == np.sign(f(a)):
        return Bisection(f, m, b, TOL, iteration)
    
    elif np.sign(f(m)) == np.sign(f(b)):
        return Bisection(f, a, m, TOL, iteration)

print(' The root is : ', Bisection(f, a, b, TOL, iteration))

