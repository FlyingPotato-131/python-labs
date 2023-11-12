import matplotlib.pyplot as plt

with open('frames.dat') as file:
	lines = file.readlines()
	x = [list(map(float, lines[2 * i    ].split())) for i in range(len(lines) // 2)]
	y = [list(map(float, lines[2 * i + 1].split())) for i in range(len(lines) // 2)]
	xmax = max([max(xi) for xi in x])
	xmin = min([min(xi) for xi in x])
	ymax = max([max(yi) for yi in y]) * 1.1
	ymin = min([min(yi) for yi in y]) * 1.1
	# print(xmin)
	# print(xmax)

	# print(x)
	for i in range(len(x)):
		fig, ax = plt.subplots()
		ax.set_xlim(xmin, xmax)
		ax.set_ylim(ymin, ymax)
		plt.minorticks_on()
		plt.grid(True, "major", "both", color = "#888888")
		plt.grid(True, "minor", "both", linestyle = '--')	
		plt.title('frame ' + str(i))
		ax.plot(x[i], y[i])
		plt.savefig('frame-' + str(i) + '.svg')
		plt.show()