import numpy as np
import os
import matplotlib.pyplot as plt

for path in os.listdir('./signals'):
	with open('./signals/' + path) as file:
		raw = np.array(list(map(float, file.readlines())))
		filtered = np.array([np.mean(raw[max(0, i - 9) : i + 1]) for i in range(np.size(raw))])
		fig, ax = plt.subplots()
		ax.plot(raw, linewidth = 1, label = 'raw')
		ax.plot(filtered, linewidth = 3, color = 'red', label = 'filtered')
		plt.minorticks_on()
		plt.grid(True, "major", "both", color = "#888888")
		plt.grid(True, "minor", "both", linestyle = '--')
		plt.legend()
		plt.title('raw and filtered data for ' + path)
		plt.show()