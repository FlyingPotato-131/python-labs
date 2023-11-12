import numpy as np
import matplotlib.pyplot as plt

with open('main-system') as file:
	system = file.readlines()
	# print(system)
	A = np.empty([0, int(system[0])], dtype = 'f')
	for i in range(int(system[0])):
		A = np.append(A, [system[i + 1].split()], axis = 0).astype('f')
	# print(A)
	b = np.array(system[-1].split(), dtype = 'f')
	# print(b)
	solution = np.linalg.solve(A, b)
	fig, ax = plt.subplots()

	plt.minorticks_on()
	plt.grid(True, "major", "both", color = "#888888")
	# plt.grid(True, "minor", "both", linestyle = '--')

	plt.xlabel('i')
	plt.ylabel('x[i]')

	ax.bar([i for i in range(int(system[0]))], solution)
	plt.show()