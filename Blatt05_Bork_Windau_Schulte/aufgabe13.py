import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

np.random.seed(8)
#a)-----------------
u = np.random.uniform(0,1,10**5)

def energy_neutrino(u):
    return (1-u)**(-1/1.7)

neutrino = energy_neutrino(u)
#print(neutrino.shape)

Energy = pd.DataFrame(neutrino)

#b)-----------------------
def probability(E):
    return (1-np.exp(-E/2))**3


#plt.plot(u,probability(neutrino))
v = np.random.uniform(0,1,10**5)
accepted_values_mask = (v <= probability(neutrino))

print(len(neutrino), len(accepted_values_mask))

plt.hist(neutrino, bins=np.logspace(0,2,100), density=True, histtype='bar', alpha=0.6, label='Neutrinoenergie')
plt.hist(neutrino[accepted_values_mask], bins=np.logspace(0,2,100), density=True, histtype='bar', alpha=0.5, label='Wahrscheinlichkeit')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()

AcceptanceMask =pd.DataFrame(accepted_values_mask)

#c)---------------------------------


normal_distribution = np.random.normal(loc=10*E, scale=2*E, )
