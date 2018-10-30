import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as const


def aufg2(#a) Der Nenner des Wirkungsquerschnitts wird in der Nähe von vielfachen von pi klei# Die Teilung durch eine kleine Zahl führt zur Instabilitä#b) Die Formel wird stabilisiert durch die Umformung i# = alpha**2/s * (sin**2+2)*gamma**2/(gamma**2 * sin**2 + cos**#c) Der Stabilitätsunterschied wird sichtbar wenn man sich die Maxima an den Pol#anguck#d) K = |theta * (2sin()cos()(-3*Beta**2+1))/((2+sin**2)*(1 - Beta**2 * cos**2)**2#Problem ist schlecht für K >= 1 konditioniert. Im Graphen wird schlechte von gut#Konditionierung durch die Linie unterschiedebeta = np.sqrt(1 - ((511*1000)/(50*10**9))**s = (2*50*10**9)*gamma = (50*10**9)/(511*100def wirkungsqwinkelinstabil(x)return (const.alpha**2)/s * ((2 + np.sin(x)**2)/(1 - (beta**2) * np.cos(x)**2)def wirkungsqwinkelstabil(x):return (const.alpha**2)/s * (2+np.sin(x)**2)*gamma**2/(gamma**2*np.sin(x)**2 + np.cos(x)**2)def ableitungwirkungssqwinkelinstabil(x):
return (const.alpha**2)/s * (2*np.sin(x)*np.cos(x)*(-3*beta**2+1))/(1-beta**2*np.cos(x)**2)**2

def konditionszahl(x):
    return np.abs(x * ableitungwirkungssqwinkelinstabil(x)/wirkungsqwinkelinstabil(x))

    theta = np.linspace(-0.01,2.1*np.pi,1000000)
    theta2 = np.linspace(0.99999999*np.pi,1.00000001*np.pi,1000000)

    plt.subplot(2,1,1)
    plt.plot(theta, wirkungsqwinkelinstabil(theta), 'r-', label = 'Wirkungsquerschnitt')
    plt.yscale('log')
    plt.xticks([0, np.pi / 2, np.pi, 3 * np.pi / 2,  2 * np.pi],[r"$0$", r"$\frac{1}{2}\,\pi$", r"$\pi$", r"$\frac{3}{2}\,\pi$", r"$2\pi$"])
    plt.ylabel(r'ln(d$\sigma$/d$\Omega$)')
    plt.xlabel(r'$\theta$')
    plt.legend()

    plt.subplot(2,1,2)
    plt.plot(theta, wirkungsqwinkelstabil(theta), 'r-', label = 'Stabiler Wirkungsquerschnitt')
    plt.yscale('log')
    plt.xticks([0, np.pi / 2, np.pi, 3 * np.pi / 2,  2 * np.pi],[r"$0$", r"$\frac{1}{2}\,\pi$", r"$\pi$", r"$\frac{3}{2}\,\pi$", r"$2\pi$"])
    plt.ylabel(r'ln(d$\sigma$/d$\Omega$)')
    plt.xlabel(r'$\theta$')
    plt.legend()

    plt.tight_layout()
    plt.savefig('wirkungsquerschnitt1.pdf')
    plt.clf()

    plt.subplot(2,1,1)
    plt.plot(theta2, wirkungsqwinkelinstabil(theta2), 'r-', label = 'Wirkungsquerschnitt')
    plt.yscale('log')
    plt.ylabel(r'ln(d$\sigma$/d$\Omega$)')
    plt.xlabel(r'$\theta$')
    plt.legend()

    plt.subplot(2,1,2)
    plt.plot(theta2, wirkungsqwinkelstabil(theta2), 'r-', label = 'Stabiler Wirkungsquerschnitt')
    plt.yscale('log')
    plt.ylabel(r'ln(d$\sigma$/d$\Omega$)')
    plt.xlabel(r'$\theta$')
    plt.legend()

    plt.tight_layout()
    plt.savefig('wirkungsquerschnitt2.pdf')
    plt.clf()

    plt.plot(theta, konditionszahl(theta), 'r-', label = 'Konditionszahl')
    plt.plot((-0.1,1.1*np.pi),(1,1), label = 'K$\geq$1')
    plt.grid()
    plt.ylabel(r'ln(K)')
    plt.xlabel(r'$\theta$')
    plt.xlim(0,1.01*np.pi)
    plt.yscale('log')
    plt.legend()
    plt.tight_layout()
    plt.savefig('konditionierung.pdf')
    plt.clf()

if __name__ == '__main__':
    aufg2()
