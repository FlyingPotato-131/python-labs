import numpy as np

W, H = list(map(int, input().split()))
field = np.zeros([H, W], dtype = 'b')
# print(field)
K = int(input())
for i in range(K):
	x, y, d = list(map(int, input().split()))
	with np.nditer(field[max(0, y - d) : min(H, y + d + 1), max(0, x - d) : min(W, x + d + 1)], op_flags = ['readwrite']) as it:
		for cell in it:
			cell[...] = 1
print((field == 0).sum())
# print(field)