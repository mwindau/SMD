import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as const

def aufg5():

    u = np.random.uniform(0,1,20)

    def gleichverteilungxminxmax(xmin,xmax,u):
        return u*(xmax - xmin) + xmin

    def exponentialgesetz(tau,u):
        return -tau*np.log(1-u)

    def potenzgesetz(xmin,xmax,n,u):
        assert n > 1
        try:
            return (u * (xmax**(1-n) - xmin**(1-n)) + xmin**(1-n)) **(1/(1-n))
        except ZeroDivisionError:
            print("Grenze darf nicht 0 sein")

    def cauchyverteilung(xmin,xmax,u):
        return np.tan(u * (np.arctan(xmax) - np.arctan(xmin)) + np.arctan(xmin))

if __name__ == '__main__':
    aufg5()
