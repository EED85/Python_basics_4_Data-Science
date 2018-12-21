import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-4,4,1000)
t = np.arange(0., 5., 0.2)

#plotting of build in functions

plt.plot(x,np.sin(x))
plt.show()

# important options
    #Labels
plt.plot(x,np.sin(x))
plt.ylabel('sin(x)')
plt.xlabel('x')

plt.title('My first plot')
plt.show()

    #Labels using latex

plt.plot(x,x**2)

# plt.rc('font', family='serif')
plt.title(r'$x^2$')
plt.show()


    #format
# http://www.engineer101.com/matlab-plot-formatting/

plt.plot(x,np.sin(x),'m--+')
plt.show()



#plotting several funcs in one figure

plt.plot(t,np.sin(t),'r',t,np.cos(t),'y')
plt.title('COS vs SIN')
plt.show()

#subplot
plt.subplot(211)
plt.plot(t,np.sin(t))
plt.subplot(212)
plt.plot(t,np.cos(t))
plt.show()


# easy plotting of UDF

def lfunc(x):
    return 2*x+2

y = [lfunc(x) for x in range(-5,5)]



plt.plot(x,lfunc(x))
plt.show()

from scipy.stats import poisson


