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

    #grid
plt.plot(x,x**2)
plt.grid(True)
plt.show()
    #format
# http://www.engineer101.com/matlab-plot-formatting/

plt.plot(x,np.sin(x),'m--+')
plt.show()



#plotting several funcs in one figure

plt.plot(t,np.sin(t),'r',label='sin')
plt.plot(t,np.cos(t),'y',label = 'cos')
plt.legend(loc='upper left')
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



plt.plot(x,lfunc(x))
plt.show()
#easy plotting probability

#histogramm

np.random.seed(19680801)
mu, sigma = 1,2 
x = np.random.normal(mu, sigma, 10000)
    # the histogram of the data
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)
plt.show()

#pmf: = Density / cdf:=distribution / ppf:=inverse distribution 
from scipy.stats import poisson
mu = 1
plt.plot(t,1-poisson.cdf(mu,t),label = 'Distribution')
plt.plot(t,poisson.pmf(mu,t),label = 'density')
plt.legend(loc='upper right')
plt.title('Poisson Verteilung mit ' + r'$\mu$=' + str(mu))
plt.grid(True)
plt.show()


P = np.arange(0,1,0.01)
plt.plot(P,poisson.ppf(P,mu))
plt.title('inverse Poisson Verteilung mit ' + r'$\mu$=' + str(mu))
plt.show()



