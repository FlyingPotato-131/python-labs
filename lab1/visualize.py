import matplotlib.pyplot as plt
import os
path = './dead_moroz'
directory = os.listdir(path)

for name in directory:
	with open(path + '/' + name) as file:
		lines = file.readlines()
		# print(lines)
		x = [float(lines[i + 1].split()[0]) for i in range(int(lines[0]))]
		y = [float(lines[i + 1].split()[1]) for i in range(int(lines[0]))]
		# print(data)
		# fig, ax = plt.subplots()
		# plt.figure(figsize=(30, (max(y) - min(y)) * 30 / (max(x) - min(x))), dpi = 50)
		plt.figure(figsize=(30, (max(y) - min(y)) * 30 / (max(x) - min(x))))
		plt.title(name)
		plt.scatter(x, y, s = 1)
		plt.savefig(name + '.svg')
		plt.show()