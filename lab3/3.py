import numpy as np

Afile = input()
bfile = input()
v = np.array(list(map(float, input().split())))
# print(v)
A = np.empty(0)
with open(Afile) as file:
	h = 0
	for line in file.readlines():
		A = np.append(A, list(map(float, line.split())))
		h += 1
	A = np.resize(A, [h, h])

b = np.empty(0)
with open(bfile) as file:
	b = np.append(b, list(map(float, file.readlines()[0].split())))

# print(np.dot(b, np.matmul(v, np.matmul(A, A))))
print(A @ A @ v @ b)