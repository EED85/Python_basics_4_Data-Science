import numpy as np
from scipy.optimize import minimize


# easy unconstrained optimzation
def y(x):
    return x**2

s = minimize(y,1)
print('Minimum of y=x**2 is ' + str(round(s.x[0],2)))



#easy constrained optimization
#min y=x**2 with x>=1

def y(x):
    return x[0]**2

x0 = np.array([4])
c = ({'type': 'ineq', 'fun': lambda x:  x[0] - 1}) #x>=1
s = minimize(y, x0,  constraints=c,method='SLSQP')
print('Minimum of y=x**2 with respect to x >=1 is ' + str(round(s.x[0],2)))

# solving y = 2*b*x with least sqaures
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.least_squares.html
from scipy.optimize import least_squares

y_  = np.array([-1,0.1,1]) #observed data
x   = np.linspace(-1,1,3) #x values
#objective function, returning residual, b will be optimized
def fun(b,x,y_):
    return 2*b*x-y_

b0 = 0 #start point

s = least_squares(fun,b0, args=(x, y_))
print('solution 0f y=2*b'str(s.x[0]))


