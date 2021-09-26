import numpy as np

f = lambda x: x**3 + 4*x**2 - 10    #write function here w.r.t x.

p1 = float(input(' Enter the first boundary : '))
p2 = float(input(' Enter the second boundary : '))
TOL = float(input(' Enter the tolerance value : '))

# f(a) and f(b) cannot have the same sign for bisection method.
if f(p1)*f(p2) > 0:
    while f(p1)*f(p2) > 0:
        p1 = float(input(' Enter the first boundary : '))
        p2 = float(input(' Enter the second boundary : '))

def Bisection(f,p1,p2,TOL):
    
    # getting midpoint
    m = (p1+p2)/2
    
    # Tolerans value is used as stopping criteria.
    if np.abs(f(m)) < TOL:
        return m
    
    # f(m) is used instead of whichever function has the same sign. 
    elif np.sign(f(m)) == np.sign(f(p1)):
        return Bisection(f, m, p2, TOL)
    
    elif np.sign(f(m)) == np.sign(f(p2)):
        return Bisection(f, p1, m, TOL)

print(' The root is : ', Bisection(f, p1, p2, TOL))

