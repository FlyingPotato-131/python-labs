import numpy as np
import matplotlib.pyplot as plt

with open('u0.txt') as file:
	u0 = np.array(list(map(float, file.readlines())))
	A = np.identity(np.size(u0))
	for i in range(np.size(u0)):
		A[i, i - 1] = -1
	fig, ax = plt.subplots()
	while(1):
		done = 0
		plot, = ax.plot(u0)
		plt.ion()
		plt.show()

		u = u0

		plt.minorticks_on()
		plt.grid(True, "major", "both", color = "#888888")
		plt.grid(True, "minor", "both", linestyle = '--')

		for i in range(255):
			u = u - 0.5 * A @ u
			plot.set_ydata(u)

			plt.pause(0.1)

			if(not plt.fignum_exists(fig.number)):
				done = 1
				break

		if(done):
			break

		plt.pause(1)
		ax.clear()
