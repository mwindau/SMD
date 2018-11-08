import numpy as np
import matplotlib.pyplot as plt


f20 = 0.0000165

def verteilung(x):
    return 15/np.pi**4 * x**3/(np.exp(x)-1)

xi = np.random.uniform(0,20,10**5)
max_y = np.amax(verteilung(xi))
yi = np.random.uniform(0,max_y,10**5)


#def rueckweisungsverfahren(xcut,ymax,xi,yi):
#    for i in range(len(xi)):
#        if yi[i] <= verteilung(xi(i)):
#            xi_neu[i] = xi[i]
#            #yi_neu[i] = yi[i]
#        else r

#def rueckweisungsverfahren(xcut,ymax,xi,yi):
#    A = yi <= verteilung(xi)
#    xi_neu = xi[A==1]
#    if len(xi_neu) == len(xi):
#        return xi_neu
#    else:

def rueckweisungsverfahren(xcut,ymax,N):
    xi = np.random.uniform(0,xcut,N)
    #max_y = np.amax(verteilung(xi))
    yi = np.random.uniform(0,ymax,N)
    A = yi <= verteilung(xi)
    xi_neu = xi[A==1]
    yi_neu = yi[A==1]
    if len(xi_neu) == len(xi):
        return xi_neu, yi_neu
    else:
        l = len(xi) - len(xi_neu)
        #xi_neu.extend(rueckweisungsverfahren(xcut,ymax,l))
        xi_neu2, yi_neu2 = rueckweisungsverfahren(xcut,ymax,l)
        xi_neu = np.append(xi_neu,xi_neu2)
        yi_neu = np.append(yi_neu,yi_neu2)
        return xi_neu, yi_neu

x, y = rueckweisungsverfahren(20,max_y,10**5)

xtest = np.linspace(0,20,10000)

plt.plot(x,y,'g.')
#plt.plot(xtest, verteilung(xtest))
plt.savefig('planck.pdf')
plt.clf()

x,y = rueckweisungsverfahren(20,max_y,10**3) # soll nur zeigen, dass diesmal wirklich
                                             # einzelne Punkte geplottet werden (ist erst bei weniger Werten sichtbar)
plt.plot(x,y,'b.')
plt.savefig('unwichtigesbeispiel.pdf')
