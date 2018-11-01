import numpy as np
import matplotlib.pyplot as plt

def aufg3c():
    x = np.linspace(0, 8, 1000)
    y = np.linspace(0, 4, 1000)
    x, y = np.meshgrid(x, y)
    mux, muy = 4, 2
    sigx, sigy = 3.5, 1.5
    plt.contour(x, y, (x-4)**2/12.25 - 1.6*(x-4)/3.5*(y-2)/1.5 + (y-2)**2/2.25, [9/25], colors='red')
    plt.errorbar(mux, muy, sigy, sigx, fmt='kx', label=r'$\mu \pm \sigma$')
    plt.xlim([0, 8])
    plt.ylim([0, 4])
    plt.legend(loc="best")
    plt.tight_layout
    plt.savefig("plotc.pdf")

if __name__ == '__main__':
    aufg3c()
