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


