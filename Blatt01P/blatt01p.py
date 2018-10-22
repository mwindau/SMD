import numpy as np
import matplotlib.pyplot as plt

#%matplotlib inline

#plt.rcParams.update({'figure.figsize': (12, 8), 'font.size': 12})

gewicht, groesse = np.genfromtxt('Groesse_Gewicht.txt', unpack=True)
gewicht, groesse

#print(gewicht)
#print(groesse)

#plt.rcParams.update({'figure.figsize': (12, 8), 'font.size': 12})

##plt.hist(gewicht, bins=80)
#plt.hist(groesse, bins=80)
#
##plt.show()
#
##plt.hist(gewicht, bins=20, range=[55, 120], histtype='step', label='Gewicht')
##plt.hist(groesse, bins=20, range=[1, 2.2], histtype='step', label='Groesse')
#
##plt.figuresize
#
#plt.subplot(3,2,1)
#plt.hist(groesse, bins=5)
#plt.title('Sophie')
#
#plt.subplot(3,2,2)
#plt.hist(groesse, bins=10)
#plt.title('riecht')
#
#plt.subplot(3,2,3)
#plt.hist(groesse, bins=15)
#plt.title('gerne')
#
#plt.subplot(3,2,4)
#plt.hist(groesse, bins=20)
#plt.title('an')
#
#plt.subplot(3,2,5)
#plt.hist(groesse, bins=30)
#plt.title('UHU')
#
#plt.subplot(3,2,6)
#plt.hist(groesse, bins=50)
#plt.title('Kleber')
#
#plt.tight_layout()

#plt.show()

blub = np.random.uniform(1, 100, 100000)
plt.hist(blub, bins=10000)
plt.show()
