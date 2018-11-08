import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)

def metropolisalg(xi, s, f, n):
    x = np.array([xi])
    i = 1
    while i<=n:                                     # Schleife zur Berechnung von n Zufallszahlen.
        xj = np.random.uniform(xi-s, xi+s)          # Zuerst xj aus Schrittvorschlags PDF.
        while xj <= 0:                              # Prüfen ob xj in passendem Bereich liegt.
            xj = np.random.uniform(xi-s, xi+s)
        Mij = min(1, f(xj)/f(xi))                   # Berechne Mij und chi.
        chi = np.random.uniform(0,1)
        while chi == 0:                             # absichern, dass chi > 0.
            chi = np.random.uniform(0,1)
        if chi <= Mij:                              # Vergleich chi und Mij.
            x = np.append(x, xj)
            xi = xj
        else:
            x = np.append(x, xi)
        i = i+1
    return x

def planck(x):
    return 15/(np.pi**4) * (x**3)/(np.exp(x)-1)

def aufg9c():
    x_0 = 30
    step_size = 2
    x = metropolisalg(x_0, step_size, planck, 100000)
    w = np.linspace(0.00001, 15, 1000)
    plt.plot(w, planck(w), 'r-', label='Planckverteilung')
    plt.hist(x, bins=30, range=[min(x),max(x)], edgecolor='w', density=True, label='Gezogene Planckverteilung')
    plt.xlabel('Zufallszahl')
    plt.ylabel('Häufigkeit')
    plt.legend(loc="best")
    plt.tight_layout()
    plt.savefig('plot1.pdf')
    plt.clf()

def aufg9d():
    l = np.linspace(0, 100000, 100001)
    x_0 = 30
    step_size = 2
    x = metropolisalg(x_0, step_size, planck, 100000)

    plt.plot(l, x, 'b-', label='Trace Plot')
    plt.xlabel('Iteration')
    plt.ylabel('Zufallszahl')
    plt.legend(loc="best")
    plt.tight_layout()
    plt.savefig('plot2.pdf')

if __name__ == '__main__':
    aufg9c()
    aufg9d()
