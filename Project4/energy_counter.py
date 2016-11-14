import matplotlib.pyplot as plt
import numpy as np

data1 = np.loadtxt('lattice20_1_nonrandom', dtype = float, skiprows = 1000)
energies_raw_10 = data1[:,2]
data2 = np.loadtxt('lattice20_24_nonrandom',dtype = float, skiprows = 1000)
energies_raw_24 = data2[:,2]

weights1 = np.ones_like(energies_raw_10)/len(energies_raw_10)
weights2 = np.ones_like(energies_raw_24)/len(energies_raw_24)
plt.subplot(2,1,1)
plt.hist(energies_raw_10, bins = 100, weights = weights1)
plt.ylabel('Number of occurences')
plt.legend(['T = 1'])
plt.subplot(2,1,2)
plt.hist(energies_raw_24 , bins = 100, weights=weights2)
plt.xlabel('Energy')
plt.ylabel('Number of occurences')
plt.legend(['T = 2.4'])
plt.show()