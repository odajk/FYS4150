import numpy as np
import matplotlib.pyplot as plt


def plotter(filename):
	data = np.loadtxt(filename, dtype = float)
	
	plt.plot(data[:,0], data[:,2])
	plt.title('Expectation value for energy as a function of MCcycles')
	plt.xlabel('Number of Monte Carlo cycles')
	plt.ylabel('Energy expectation value')
	plt.show()


	plt.plot(data[:,0], data[:,6])
	plt.title('Absolute value of magnetic moment as a function of MCcycles')
	plt.xlabel('Number of Monte Carlo cycles')
	plt.ylabel('Absolute value of magnetic moment')
	plt.show()
	

plotter('lattice20')





