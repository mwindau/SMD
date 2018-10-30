import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Der Code könnte in vielen Teilen mit dem
#von Felix übereinstimmen. Wir haben die
#Aufgabe gemeinsam bearbeitet.
def generator(x0, a, b, m):  #dieser Generator ist dafür da nur so viele Zahlen
    x = np.array([x0])       #zu generieren bis sich eine wiederholt, damit wir
    x_j = 0                  #anhand der Länge des Arrays die Periodenlänge bestimmen
    for i in range(m-1):     #können.
        x_j = np.mod(a * x0 + b, m)
        if (x_j in x) == True:
            return x
        else:
            x = np.append(x, x_j)
            x0 = x_j
    return x

def generatorc(x0, a, b, m):    #dieser Generator erstellt für Teil c in jedem Fall
    x = np.array([x0])          #m Zahlen.
    x_j = 0
    for i in range(m-1):
        x_j = np.mod(a * x0 + b, m)
        x = np.append(x, x_j)
        x0 = x_j
    return x

def generator2d(x0, a, b, m):   #dieser Generator ist für den 2D Plot.
    x = np.array([x0])          #In dem Fall, dass die Länge der Periode
    y = np.array([np.mod(a * x0 + b, m)])   #nicht durch 2 bzw. später durch 3
    x0 = np.mod(a * x0 + b, m)  #teilbar ist wird die "Zeile" mit den passenden
    x_j = 0                     #Zahlen aufgefüllt.
    for i in range(m-1):
        x_j = np.mod(a * x0 + b, m)
        if (i%2) == 0:
            x = np.append(x, x_j)
        else:
            y = np.append(y, x_j)
        x0 = x_j
    if ((m-1)%2)!=0:
        y = np.append(y, 0)
    return x, y

def generator3d(x0, a, b, m):   #dieser Generator ist für den 3D Plot
    x = np.array([x0])
    y = np.array([np.mod(a * x0 + b, m)])
    x0 = np.mod(a * x0 + b, m)
    z = np.array([np.mod(a * x0 + b, m)])
    x0 = np.mod(a * x0 + b, m)
    x_j = 0
    for i in range(m-1):
        x_j = np.mod(a * x0 + b, m)
        if (i%3) == 0:
            x = np.append(x, x_j)
        elif ((i+2)%3) == 0:
            y = np.append(y, x_j)
        else:
            z = np.append(z, x_j)

        x0 = x_j
    return x, y, z

def periode_a(x0, b, m):
    laenge = np.array([0])  #Die 0 ist lediglich als Platzhalter da, damit wir das Array vorab definiert haben.
    for i in range(1, 10):
        x = len(generator(x0, i, b, m))
        laenge = np.append(laenge, x)
    return laenge

def aufg2a():
    b = 3
    m = 1024
    laenge = periode_a(0, b, m)
    i = np.arange(0, 10)
    print("Die Periodenlängen in Abh. von a ", laenge)
    plt.plot(i, laenge, 'bx', label="Periodenlaengen")
    plt.xlabel(r"$a$")
    plt.ylabel("Periodenlänge")
    plt.tight_layout
    plt.savefig('aPerioden.pdf')
    plt.clf()

def aufg2c():
    a = 1601
    b = 3456
    m = 10000
    zufallszahlen = generatorc(0, a, b, m) / m
    plt.hist(zufallszahlen, bins=25, range=[zufallszahlen.min(), zufallszahlen.max()], density=False)
    plt.xlabel("Bins")
    plt.ylabel("# Anzahl")
    plt.tight_layout
    plt.savefig('Hist.pdf')
    plt.clf()

    plt.tight_layout
    zufallszahlen = generatorc(50, a, b, m) / m
    plt.hist(zufallszahlen, bins=25, range=[zufallszahlen.min(), zufallszahlen.max()], density=False)
    plt.xlabel("Bins")
    plt.ylabel("# Anzahl")
    plt.savefig('x0var50Hist.pdf')
    plt.clf()

    zufallszahlen = generatorc(100, a, b, m) / m
    plt.hist(zufallszahlen, bins=25, range=[zufallszahlen.min(), zufallszahlen.max()], density=False)
    plt.xlabel("Bins")
    plt.ylabel("# Anzahl")
    plt.tight_layout
    plt.savefig('x0var100Hist.pdf')
    plt.clf()

def aufg2d():
    a = 1601
    b = 3456
    m = 10000

    x2, y2 = generator2d(0, a, b, m)
    x2 = x2/m
    y2 = y2/m
    x3, y3, z3 = generator3d(0, a, b, m)
    x3 = x3/m
    y3 = y3/m
    z3 = z3/m

    fig = plt.figure()
    a2 = fig.add_subplot(1, 1, 1)
    a2.scatter(x2, y2, lw=0, s=5,)
    plt.xlabel('erste Komponente')
    plt.ylabel('zweite Komponente')
    plt.savefig('2D.pdf')
    plt.clf()

    fig = plt.figure()
    a3 = fig.add_subplot(1, 1, 1, projection='3d')
    a3.scatter(x3, y3, z3, lw=0, s=5,)
    plt.xlabel('erste Komponente')
    plt.ylabel('zweite Komponente')
    plt.savefig('3D.pdf')
    plt.clf()

def aufg2e():
    uniform = np.random.uniform(0, 1, 10000) #theoretisch müsste man hier diese
                                            #Zahlen nun in 2 bzw. 3 arrays aufgeteilt
                                            #speichern und wie zuvor ploten. Jedoch
                                            #wissen wir nicht genau wie. Bisher haben
                                            #wir das ja direkt beim erstellen der
                                            #Zahlen so angeordnet.

def aufg2f():
    a = 1601
    b = 3456
    m = 10000

    anzahl05 = np.array([0])

    for i in range(1, 100):
        zufallszahlen = generatorc(i, a, b, m) / m
        anzahl = len(zufallszahlen[zufallszahlen == 1/2])
        if anzahl != 0:
            print("Für x0 = ", i, " ist 1/2 unter den Zufallszahlen")
        anzahl05 = np.append(anzahl05, anzahl)

    i = np.arange(0, 100)
    plt.plot(i, anzahl05, 'bx', label=r"Menge der $\frac{1}{2}$")
    plt.xlabel(r"$x_0$")
    plt.ylabel("# Anzahl")
    plt.tight_layout
    plt.savefig('Anzahl.pdf')
    plt.clf()

if __name__ == '__main__':
    aufg2a()
    aufg2c()
    aufg2d()
    aufg2f()
