import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def generator(x0, a, b, m):    #soll aus Startwert x0 m-1 neue Zufallszahlen erzeugen
    laengenarray = [x0]                             #Array mit zunächst einem Eintrag
    for i in range(m-1):                            #Schleife sorgt für Abbruch nach m-1. Zahl
        x_j = np.mod(a * x0 + b, m)                 #erzeugt eine neue Zufallszahl aus der vorherigen Zahl
        laengenarray = np.append(laengenarray, x_j) #erstellt neues Array-Element mit neuer Zufallszahl
        x0 = x_j                                    #setzt neues x_j als Ausgangswert für die Rekursionsformel
    return laengenarray

def generatorohnewiederholung(x0, a, b, m): #soll nach Ende einer Periode aufhören, Zahlen zu generieren
    laengenarray = [x0]                             #beginnt wie der normale Generator
    for i in range(m-1):
        x_j = np.mod(a * x0 + b,m)
        if (x_j in laengenarray) == True:           #wenn ein Wert bereits vorgekommen ist
            return laengenarray                     #wird die Generation abgebrochen und das Array ausgegeben
        else:
            laengenarray = np.append(laengenarray, x_j) #sonst wird normal weitergemacht
            x0 = x_j
    return laengenarray                             #falls die Abbruchbedingung nicht erfüllt wird,
                                                    #wird spätestens nach dem m-ten Glied abgebrochen,
                                                    #weil m die maximale Periodenlänge ist



def periode_a(x0, b, m):                            #soll die Länge der generierten Arrays angeben
    laenge = [0]                                    #erzeugt ein Array für die Periodenlängen (Wert in [0] wird nicht beachtet)
    for i in range(1, 100):                         #lässt a von durchlaufen
        x = len(generatorohnewiederholung(x0, i, b, m)) #prüft die Periodenlänge für die verschiedenen as
        laenge = np.append(laenge, x)               #hängt für das entsprechende a ein Arrayelement mit der Periodenlänge an
    return laenge

def generator2d(x0, a, b, m):   #soll den 2D-Plot generieren
    x = [x0]                                        #speichert den Startwert in ein Array
    y = [np.mod(a * x0 + b, m)]                     #und den folgenden Wert in ein anderes Array
    x0 = np.mod(a * x0 + b, m)                      #aktualisiert Rekursionsvariable
    for i in range(m-1):                            #
        x_j = np.mod(a * x0 + b, m)                 #ein neues x_j wird aus dem vorangegangenen Wert erzeugt
        if (i%2) == 0:                              #falls die mitzählende Variable gerade ist,
            x = np.append(x, x_j)                   #wird der Wert im ersten Array gespeichert
        else:                                       #falls die Variable ungerade ist,
            y = np.append(y, x_j)                   #wird der Wert im 2.Array gespeichert
        x0 = x_j                                    #Ausgangswert für die nächste Rekursion wird geändert
    if ((m-1)%2)!=0:                                #falls eine ungerade Elementanzahl vorliegt,
        y = np.append(y, 0)                         #wird dafür gesort, dass beide Arrays gleichlang sind
    return x, y

def generator3d(x0, a, b, m):   #soll den 3D-Plot generieren
    x = np.array([x0])                              #speichert die erste Zahl im ersten Array
    y = np.array([np.mod(a * x0 + b, m)])           #speichert die zweite Zahl im zweiten Array
    x0 = np.mod(a * x0 + b, m)                      #aktualisiert die Rekursionsvariable
    z = np.array([np.mod(a * x0 + b, m)])           #speichert die dritte Zahl in drittem Array
    x0 = np.mod(a * x0 + b, m)                      #aktualisiert Rekursionsvariable
    for i in range(m-1):                            #
        x_j = np.mod(a * x0 + b, m)                 #macht genau das gleiche wie beim 2D-Plot
        if (i%3) == 0:                              #nur, dass diesmal mit der Hilfe von % jede
            x = np.append(x, x_j)                   #3.Zahl im selben Array landet
        elif ((i+2)%3) == 0:
            y = np.append(y, x_j)
        else:
            z = np.append(z, x_j)
        x0 = x_j                                    #Aktualisierung Rekursionsvariable
    return x, y, z









def aufg2a():
    b = 3
    m = 1024
    laenge = periode_a(0, b, m)
    i = np.arange(0, 100)
    print("Die Periodenlängen in Abh. von a: ", laenge)
    plt.plot(i, laenge, 'bx', label="Periodenlaengen")
    plt.xlabel(r"$a$")
    plt.ylabel("Periodenlänge")
    plt.tight_layout
    plt.savefig('aPerioden.pdf')
    plt.clf()


def aufg2b():
    a = 1601
    b = 3456
    m = 10000

    zufallszahlen = generator(0, a, b, m)/m
    plt.hist(zufallszahlen, bins=100)
    plt.xlabel("Zufallszahlen")
    plt.ylabel("Häufigkeit der Zufallszahlen")
    plt.tight_layout
    plt.savefig('Histogrammb.pdf')
    plt.clf()

    zufallszahlen = generator(1, a, b, m)/m
    plt.hist(zufallszahlen, bins=100)
    plt.xlabel("Zufallszahlen")
    plt.ylabel("Häufigkeit der Zufallszahlen")
    plt.tight_layout
    plt.savefig('Histogrammb2.pdf')
    plt.clf()

    zufallszahlen = generator(2, a, b, m)/m
    plt.hist(zufallszahlen, bins=100)
    plt.xlabel("Zufallszahlen")
    plt.ylabel("Häufigkeit der Zufallszahlen")
    plt.tight_layout
    plt.savefig('Histogrammb3.pdf')
    plt.clf()

    zufallszahlen = generator(100, a, b, m)/m
    plt.hist(zufallszahlen, bins=100)
    plt.xlabel("Zufallszahlen")
    plt.ylabel("Häufigkeit der Zufallszahlen")
    plt.tight_layout
    plt.savefig('Histogrammb4.pdf')
    plt.clf()

    zufallszahlen = generator(1000, a, b, m)/m
    plt.hist(zufallszahlen, bins=100)
    plt.xlabel("Zufallszahlen")
    plt.ylabel("Häufigkeit der Zufallszahlen")
    plt.tight_layout
    plt.savefig('Histogrammb5.pdf')
    plt.clf()

    zufallszahlen = generator(10000, a, b, m)/m
    plt.hist(zufallszahlen, bins=100)
    plt.xlabel("Zufallszahlen")
    plt.ylabel("Häufigkeit der Zufallszahlen")
    plt.tight_layout
    plt.savefig('Histogrammb6.pdf')
    plt.clf()

    zufallszahlen = generator(0.5, a, b, m)/m
    plt.hist(zufallszahlen, bins=100)
    plt.xlabel("Zufallszahlen")
    plt.ylabel("Häufigkeit der Zufallszahlen")
    plt.tight_layout
    plt.savefig('Histogrammb7.pdf')
    plt.clf()

    zufallszahlen = generator(np.pi, a, b, m)/m
    plt.hist(zufallszahlen, bins=100)
    plt.xlabel("Zufallszahlen")
    plt.ylabel("Häufigkeit der Zufallszahlen")
    plt.tight_layout
    plt.savefig('Histogrammb8.pdf')
    plt.clf()

    blub=3/7
    zufallszahlen = generator(blub , a, b, m)/m
    plt.hist(zufallszahlen, bins=100)
    plt.xlabel("Zufallszahlen")
    plt.ylabel("Häufigkeit der Zufallszahlen")
    plt.tight_layout
    plt.savefig('Histogrammb9.pdf')
    plt.clf()

def aufg2c():
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


def aufg2d():

    zufallszahlen = np.random.uniform(0, 1, 10000)
    plt.hist(zufallszahlen, bins=100)
    plt.xlabel("Zufallszahlen")
    plt.ylabel("Häufigkeit der Zufallszahlen")
    plt.tight_layout
    plt.savefig('Histogrammd.pdf')
    plt.clf()




    x = np.random.uniform(0, 1, size=1000)
    y = np.random.uniform(0, 1, size=1000)
    z = np.random.uniform(0, 1, size=1000)

    fig = plt.figure()
    a2 = fig.add_subplot(1, 1, 1)
    a2.scatter(x, y, lw=0, s=5,)
    plt.xlabel('erste Komponente')
    plt.ylabel('zweite Komponente')
    plt.savefig('2Dd.pdf')
    plt.clf()

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, lw=0, s=5)
    plt.xlabel('erste Komponente')
    plt.ylabel('zweite Komponente')
    plt.savefig('3Dd.pdf')
    plt.clf()




def aufg2e():
    a = 3
    b = 3
    m = 1024


    i = 511
    zufallszahlen = generator(i, a, b, m)/m
    anzahl = len(zufallszahlen[zufallszahlen == 1/2])

    j = 348672
    zufallszahlen2 = generator(j, a, b, m)/m
    anzahl2 = len(zufallszahlen2[zufallszahlen2 == 1/2])

    k = 2
    zufallszahlen3 = generator(k, a, b, m)/m
    anzahl3 = len(zufallszahlen3[zufallszahlen3 == 1/2])

    print('Für den Startwert', i, 'kommt 1/2 unter den Zufallszahlen', anzahl, 'mal vor.')
    print('Für den Startwert', j, 'kommt 1/2 unter den Zufallszahlen', anzahl2, 'mal vor.')
    print('Für den Startwert', k, 'kommt 1/2 unter den Zufallszahlen', anzahl3, 'mal vor.')













if __name__ == '__main__':
    aufg2a()
    aufg2b()
    aufg2c()
    aufg2d()
    aufg2e()
