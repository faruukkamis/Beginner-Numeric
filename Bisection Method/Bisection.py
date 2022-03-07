import numpy as np

#write function here w.r.t x.
f = lambda x: x**3 - 14.8039*x**2 -2175.6765*x + 11019.727    

p1 = float(input(' Enter the first boundary : '))
p2 = float(input(' Enter the second boundary : '))
TOL = float(input(' Enter the tolerance value : '))
num_itr = int(input(' Enter the maximum iteration number : '))

# f(a) and f(b) cannot have the same sign for bisection method.
if f(p1)*f(p2) > 0:
    while f(p1)*f(p2) > 0:
        print('---They have not opposite signs, so please enter new values.')
        p1 = float(input(' Enter the first boundary : '))
        p2 = float(input(' Enter the second boundary : '))
        
def Bisection(f,p1,p2,TOL,num_itr):
    
    # getting midpoint
    m = (p1+p2)/2
    num_itr = num_itr - 1
    # Tolerans value is used as stopping criteria.
    if np.abs(f(m)) < TOL:
        
        return m,num_itr
    if num_itr < 0:
        m = 'could not found'
        return m,num_itr

    # f(m) is used instead of whichever function has the same sign. 
    elif np.sign(f(m)) == np.sign(f(p1)):
        return Bisection(f, m, p2, TOL, num_itr)
    
    elif np.sign(f(m)) == np.sign(f(p2)):
        return Bisection(f, p1, m, TOL, num_itr)

Bi_sec = Bisection(f, p1, p2, TOL, num_itr)

print(' The root is : ', Bi_sec[0], 
      '\n Number of iteration is :', num_itr-Bi_sec[1])
