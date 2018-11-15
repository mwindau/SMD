import numpy as np
from numpy.linalg import inv
import pandas as pd
import matplotlib.pyplot as plt



def aufgabe12():
    df = pd.read_hdf('zwei_populationen.h5', key='P_0_10000')
    df2 = pd.read_hdf('zwei_populationen.h5', key='P_1')

    #a):
    print("Mittelwert mu_P0_x: ",df['x'].mean())
    print("Mittelwert mu_P0_y: ",df['y'].mean())
    print("Mittelwert mu_P1_x: ",df2['x'].mean())
    print("Mittelwert mu_P1_y: ",df2['y'].mean())

    mu0 = pd.DataFrame({'x' : [df['x'].mean(),df['y'].mean()]}, index=['x','y'])
    mu1 = pd.DataFrame({'x' : [df2['x'].mean(),df2['y'].mean()]}, index=['x','y'])

    print(mu0)
    print(mu1)
    #b):
    print("Kovarianzmatrix von P0: \n",df.cov())
    print("Kovarianzmatrix von P1: \n",df2.cov())
    kombinierte_kovarianzmatrix = df.cov() + df2.cov()
    print("Kombinierte Kovarianzmatrix: \n",kombinierte_kovarianzmatrix)

    #c):
    mu_differenz = (mu1 - mu0)
    fisher_diskriminante = np.dot(inv(kombinierte_kovarianzmatrix),mu_differenz)
    print("Fisher-Diskrimante: ",fisher_diskriminante)

    #d):
    fisher_diskriminante2 = np.array([fisher_diskriminante[0][0],fisher_diskriminante[1][0]])

    df0 = np.zeros(shape=(1000,2))

    for i in range(1000):
        df0[i] = ([df['x'][i],df['y'][i]])
    p0 = np.empty([1000,1])
    for i in range(1000):
        p0[i] = 1/(np.dot(fisher_diskriminante2,fisher_diskriminante2)) * (np.dot(fisher_diskriminante2,df0[i]))

    df1 = np.zeros(shape=(1000,2))

    for i in range(1000):
        df1[i] = ([df2['x'][i],df2['y'][i]])

    p1 = np.empty([1000,1])

    for i in range(1000):
        p1[i] = 1/(np.dot(fisher_diskriminante2,fisher_diskriminante2)) * (np.dot(fisher_diskriminante2,df1[i]))


    plt.hist(p0,bins=50, label="Signal")
    plt.hist(p1,bins=50, label="Untergrund")
    plt.legend(loc="best")
    #plt.savefig('hist.pdf')
    plt.clf()

    #e)
    cut = np.linspace(-3,3,1000)

    def tp(xcut):
        xtp = p0 <= xcut
        laengetp = p0[xtp==1]
        return len(laengetp)

    def fp(xcut):
        xfp = p1 <= xcut
        laengefp = p1[xfp==1]
        return len(laengefp)

    def fn(xcut):
        xfn = p0 >= xcut
        laengefn = p0[xfn==1]
        return len(laengefn)

    def reinheit(xcut):
        tp1 = tp(xcut)
        fp1 = fp(xcut)
        if tp1 == 0 and fp1 == 0:
            return 1
        elif (tp1+fp1) == 0:
            return tp1
        else: return tp1/(tp1+fp1)

    def effizienz(xcut):
        tp2 = tp(xcut)
        fn2 = fn(xcut)
        if tp2 == 0 and fn2 == 0:
            return 1
        elif (tp2+fn2) == 0:
            return tp2
        else: return tp2/(tp2+fn2)

    reinheit_plot = np.empty(1000)
    effizienz_plot = np.empty(1000)
    for i in range(1000):
        reinheit_plot[i] = reinheit(cut[i])
        effizienz_plot[i] = effizienz(cut[i])

    plt.plot(cut, reinheit_plot, label="Reinheit")
    plt.plot(cut, effizienz_plot, label="Effizienz")
    plt.legend(loc="best")
    #plt.savefig('reinheit.pdf')
    plt.clf()
if __name__ == '__main__':
    aufgabe12()
