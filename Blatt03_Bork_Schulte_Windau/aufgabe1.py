import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
import time
import datetime


def aufgabe1():
    f20 = 0.0000165

    def verteilung_ableitung(x):
        return 15/np.pi**4 * x**2 / (np.exp(x)-1) * (3 - x*np.exp(x)/(np.exp(x)-1))

    ableitung_nullstelle = brentq(verteilung_ableitung,1,7)

#print(ableitung_nullstelle)


    def verteilung(x):
        return 15/np.pi**4 * x**3/(np.exp(x)-1)

    max_y = verteilung(ableitung_nullstelle)
#print(verteilung(ableitung_nullstelle))

    xi = np.random.uniform(0,20,10**5)
#max_y = np.amax(verteilung(xi))
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
        w = len(yi[A==0])
        if len(xi_neu) == len(xi):
            return xi_neu, yi_neu, w
        else:
            l = len(xi) - len(xi_neu)
            #xi_neu.extend(rueckweisungsverfahren(xcut,ymax,l))
            xi_neu2, yi_neu2, wneu = rueckweisungsverfahren(xcut,ymax,l)
            xi_neu = np.append(xi_neu,xi_neu2)
            yi_neu = np.append(yi_neu,yi_neu2)
            w = w + wneu
            return xi_neu, yi_neu, w

#start_time = datetime.datetime.now()
#x, y, w = rueckweisungsverfahren(20,max_y,10**5)
#stop_time = datetime.datetime.now()
#elapsed_time = (stop_time - start_time).total_seconds()
#print(elapsed_time)
#print(w)



    def majorantenschnittpunkt(x):
            return 200*15/np.pi**4 * x**(-0.1)*np.exp(-x**(0.9)) - max_y

            def majorante1(x):
                return max_y + (x-x)

            def majorante2(x):
                return 200*15/np.pi**4 * x**(-0.1)*np.exp(-x**(0.9))

    schnittpkt_majoranten = brentq(majorantenschnittpunkt, 2.7,15)

    def split(arr, cond):
        return [arr[cond], arr[~cond]]

    def majoranteinvers(u):
        return (schnittpkt_majoranten**(9/10)-np.log(1-u))**(10/9)

    def rueckweisungsverfahrenmajorant(xcut,ymax,N):
    #xi = np.random.uniform(0,xcut,N)
    #max_y = np.amax(verteilung(xi))
    #yi = np.random.uniform(0,ymax,N)
        N1 = int(N*0.8)
        N2 = int(N*0.2)
        R = (schnittpkt_majoranten*ymax/(1+schnittpkt_majoranten*ymax))/(1-(schnittpkt_majoranten*ymax/(1+schnittpkt_majoranten*ymax)))

        yi1 = np.random.uniform(0,ymax,N1)
        x01 = np.random.uniform(0,1,N2)
        xi2 = majoranteinvers(x01)
        xi1 = np.random.uniform(0,schnittpkt_majoranten,N1)
        yi2 = majorante2(xi2)*np.random.uniform(0,1,len(xi2))
        #yi = np.append(yi1,yi2)
        #xi = np.append(xi1,xi2)
        A = yi1 <= verteilung(xi1)
        B = yi2 <= verteilung(xi2)
        verworfen21 = len(xi1[A==0])
        verworfen22 = len(xi2[B==0])
        xi1_neu = xi1[A==1]
        xi2_neu = xi2[B==1]
        yi1_neu = yi1[A==1]
        yi2_neu = yi2[B==1]
        xi_neu = np.append(xi1_neu,xi2_neu)
        yi_neu = np.append(yi1_neu,yi2_neu)
        xi = np.append(xi1,xi2)
        yi = np.append(yi1,yi2)
        if len(xi_neu) == len(xi):
            return xi_neu, yi_neu, verworfen21, verworfen22
        else:
            l = len(xi) - len(xi_neu)
            #xi_neu.extend(rueckweisungsverfahren(xcut,ymax,l))
            xi_neu2, yi_neu2, verworfen21_neu, verworfen22_neu = rueckweisungsverfahrenmajorant(xcut,ymax,l)
            xi_neu = np.append(xi_neu,xi_neu2)
            yi_neu = np.append(yi_neu,yi_neu2)
            verworfen21 = (verworfen21+verworfen21_neu)
            verworfen22 = (verworfen22+verworfen22_neu)
            return xi_neu, yi_neu, verworfen21, verworfen22



    x1 = np.linspace(0,6,10000)
    x2 = np.linspace(5.5,20,10000)
#start_time = datetime.datetime.now()
#x3,y3,w31,w32 = rueckweisungsverfahrenmajorant(20,max_y,10**5)
#stop_time = datetime.datetime.now()
#elapsed_time = (stop_time - start_time).total_seconds()
#print(elapsed_time)
#print(w31+w32)

#plt.clf()
#plt.plot(x1,majorante1(x1),'r--')
#plt.plot(x2,majorante2(x2),'k--')
#plt.plot(x3,y3,'g.')
#plt.savefig('majorante.pdf')
#print(x3)
#plt.plot(x3, y3, 'g.')
#plt.savefig('planck.pdf')
#plt.clf()
#plt.show()
#
#x,y = rueckweisungsverfahren(20,max_y,10**3) # soll nur zeigen, dass diesmal wirklich
#                                             # einzelne Punkte geplottet werden (ist erst bei weniger Werten sichtbar)
#plt.plot(x,y,'b.')
#plt.savefig('unwichtigesbeispiel.pdf')
if __name__ == '__main__':
    aufgabe1()
