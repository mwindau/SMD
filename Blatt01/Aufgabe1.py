import numpy as np
import matplotlib.pyplot as plt


def aufg1():
    x = np.logspace(-6, 6, 1000)
    x2 = np.logspace(-20, 20, 10000)
    x3 = np.logspace(4, 6, 10000)
    x4 = np.logspace(-6, -4, 10000)

    def f(x):
        return (x**3+1/3)-(x**3-1/3)

    def g(x):
        return ((3+x**3/3)-(3-x**3/3))/(x**3)

    def c(x):
        return -1+x*0

    def c2(x):
        return 1+x*0

    print('x Werte: ', np.array([x]))
    print('f(x) Werte: ', np.array([f(x)]))
    print('g(x) Werte: ', np.array([g(x)]))

    plt.plot(x, f(x), 'g-', label='f(x)')
    plt.plot(x, g(x), 'b--', label='g(x)')
    plt.xscale('log')
    plt.title('Aufgabe 1.1')
    plt.xlabel('x')
    plt.ylabel('Numerisches Ergebnis von f(x) bzw. g(x)')
    plt.legend(loc='best')
    plt.savefig('aufgabe11.pdf')
    plt.clf()

    plt.plot(x3, (f(x3)-(2/3))*(3/2)*100, 'b-', label=r'Relative Abweichung f(x) von $\frac{2}{3}$')
    plt.plot(x3, c(x3), 'r-', label=r'obere und untere Grenze 1%')
    plt.plot(x3, c2(x3), 'r-')
    plt.xscale('log')
    plt.title('Aufgabe 1.2')
    plt.xlabel('x')
    plt.ylabel('Abweichung in %')
    plt.legend(loc='best')
    plt.savefig('aufgabe12.pdf')
    plt.clf()

    plt.plot(x4, (g(x4)-(2/3))*(3/2)*100, 'b-', label=r'Relative Abweichung g(x) von $\frac{2}{3}$')
    plt.plot(x4, c(x4), 'r-', label=r'obere und untere Grenze 1%')
    plt.plot(x4, c2(x4), 'r-')
    plt.xscale('log')
    plt.title('Aufgabe 1.3')
    plt.xlabel('x')
    plt.ylabel('Abweichung in %')
    plt.legend(loc='best')
    plt.savefig('aufgabe13.pdf')
    plt.clf()

    plt.plot(x2, f(x2), 'r-', label='f(x)')
    plt.plot(x2, g(x2), 'b--', label='g(x)')
    plt.xscale('log')
    plt.title('Aufgabe 1.4')
    plt.legend(loc='best')
    plt.savefig('aufgabe14.pdf')
    plt.clf()

if __name__ == '__main__':
    aufg1()
