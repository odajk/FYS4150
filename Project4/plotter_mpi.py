import numpy as np
import matplotlib.pyplot as plt
import sys 


def plotter(filename, Title):

	data = np.loadtxt(filename, dtype = float)
	ax, f = plt.subplots()
	plt.rc('text', usetex = True)
	plt.rc('font', family='serif')
	ax.set_title(Title)
	plt.subplot(2,2,1)
	plt.plot((data[:,1]), data[:,2])
	plt.xlabel('T')
	plt.ylabel(r"Mean energy $<E>$")
	plt.subplot(2,2,2)
	plt.plot((data[:,1]), data[:,6])
	plt.xlabel("T")
	plt.ylabel(r"Mean magnetization $<|M|>$")


	plt.subplot(2,2,3)
	plt.plot((data[:,1]), data[:,3])
	plt.ylabel(r"Specific heat capacity $C_v$")
	plt.xlabel('T')
	plt.subplot(2,2,4)

	plt.plot((data[:,1]), data[:,5])
	plt.xlabel('T')
	plt.ylabel(r"Magnetic susceptibility$\chi$")
	plt.tight_layout()

	plt.show()
		

#plotter('lattice20_1_nonrandom')
#plotter('lattice_random20_1')
#plotter('lattice20_24_nonrandom')
#plotter('lattice_random20_24')
plotter('par_lat140', "Expectation values for L = 140")
plotter('par_lat100.txt', "Expectation values for L = 100")
plotter('par_lat60.txt', "Expectation values for L = 60")

