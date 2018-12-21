# solving y = 2*b*x with least sqaures
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.least_squares.html
import numpy as np
import random as rd
from scipy.optimize import least_squares

y_  = np.array([-1,0.1,1]) #observed data
x   = np.linspace(-1,1,3) #x values
#objective function, returning residual, b will be optimized
def fun(b,x,y_):
    return 2*b*x-y_

b0 = 0 #start point

s = least_squares(fun,b0, args=(x, y_))
print('solution of y=2*b*x ' + str(s.x[0]))


# solving y = b[0] + 2*b[1]*x = a+b*2*x with least sqaures



y_  = np.array([-2,-1.1,0]) #observed data

#objective function, returning residual, b will be optimized
def fun2(b,x,y_):
    return b[0] + 2*b[1]*x-y_

b0 = np.array([0,0]) #start point

s = least_squares(fun2,b0, args=(x, y_))


print('solution 0f y=2*b ' + str(s.x[0]))

#some more data - some more noise

x = np.repeat(x,2)
y_ = np.repeat(y_,2)
y_[5]=0.25;y_[0]=-1.9
y_

s = least_squares(fun2,b0, args=(x, y_))


#fitting polynom

x = np.linspace(-4,4,16)
x_ = np.concatenate((x, x), axis=None)
y_ = [x**2 + rd.random()/20-0.1 for x in x]
y2_ = [x**2 + rd.random()/20-0.1 for x in x]
y_ = np.concatenate((y_, y2_), axis=None)

def poly2(b,x,y_):
    return  b[0]*x + b[1]*x**2 -y_
b0 = np.ones(2)
poly2(b0,1,1)
s = least_squares(poly2,b0, args=(x_, y_))
s.x

#glm mith poisson


x = np.linspace(0.5,8,16)
x = np.concatenate((x, x), axis=None)


y_ = [1/x + 1/x*(rd.random()/20-0.1) for x in x]
y2_ = [1/x + 1/x*(rd.random()/20-0.1) for x in x]
y_ = np.concatenate((y_, y2_), axis=None)
mu = np.mean(y_)
mu_ln = np.log(E_Y)


