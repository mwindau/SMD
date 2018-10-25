import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.optimize import newton, brentq, minimize

def f(x):
    return (x**3 + 1/3) - (x**3 - 1/3)

def g(x):
    return ((3 + x**3/3) - (3 - x**3/3))/x**3

#x_0 = newton(f, 1)

i = 0

#for i in range(101):
#    print(f(i))


#print("2/3 =", 2/3)

#def horizontalline(x):
#    return 2/3 18000 0.667 0.665

#x = np.linspace(-10**5,10**5,10000)
x = np.linspace(0.001,100000,10000)
#plt.plot(x, f(x))
#plt.xscale('log')
plt.plot(x, g(x))
#plt.xscale('log')
#plt.xlabel('x')
#plt.ylabel('f(x)')
#plt.plot((-10**5,10**5), (2/3,2/3), 'k-')
#plt.plot((-10**5,10**5), (2/3+2/3*0.01,2/3+2/3*0.01), 'r-')
#plt.plot((-10**5,10**5), (2/3-2/3*0.01,2/3-2/3*0.01), 'r-')
#plt.axes([0.45,0.56,0.3,0.3])
#plt.plot(x, f(x))
#plt.xlim(-18000,18000)
#plt.ylim(0.68,0.66)
#plt.savefig('bereiche1a.pdf')
plt.show()
