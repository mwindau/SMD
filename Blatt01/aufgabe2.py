import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as const

def wirkungsqwinkelinstabil(theta):
    return (const.alpha**2)/((2*50*10**9)**2) * ((2+np.sin(theta)**2)/(1-(1-((50*10**9)/(511*10**3))**(-2))*np.cos(theta)**2))

#1-beta**2 = 1/gamma**2 , sin2+cos+=1
#a**2/s * ((2+sin**2)/())
def wirkungsqwinkelstabil(theta):
    return (const.alpha**2)/((2*50*10**9)**2) * (2+np.sin(theta)**2) / (1/((50*10**9)/(511*10**3))**2 * (1 + np.sin(theta)**2) + 1)

theta = np.linspace(0,2*np.pi,100000)

#print(wirkungsqwinkel(-5*np.pi))
#print(wirkungsqwinkel(-4*np.pi))
#print(wirkungsqwinkel(-2*np.pi))
#print(wirkungsqwinkel(1*np.pi))
#print(wirkungsqwinkel(0.456*np.pi))
#print(wirkungsqwinkel(2*np.pi))

#plt.subplot(2,1,1)
plt.plot(theta, wirkungsqwinkelinstabil(theta), 'r-')
#plt.show()

#plt.hist(wirkungsqwinkel(theta),bins=10)
#plt.show()

#plt.subplot(2,1,2)
#plt.plot(theta, wirkungsqwinkelstabil(theta))
#plt.grid()
#plt.tight_layout()
plt.show()
