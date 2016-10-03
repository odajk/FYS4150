import numpy as np
import matplotlib.pyplot as plt

def plotter (rho, omega_list):
	a = 'non_inter_'
	b = 'inter_'

	for omega in omega_list:
		filename_1 = a + omega + '.txt'
		filename_2 = b + omega + '.txt'
		c = np.loadtxt(filename_1)
		d = np.loadtxt(filename_2) 
		plt.plot(rho, filename_1)
		plt.hold('on')
		plt.plot(rho,filename_2)
		xlabel('rho')
		ylabel('')
		plt.show()

	 

