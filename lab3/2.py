import numpy as np

H, W = list(map(int, input().split()))
navmap = np.empty([H, W], dtype = 'i')

for h in range(H):
	navmap[h, :] = list(map(int, input().split()))
# print(navmap)
print((navmap < -5).sum())
print(abs(((navmap < 0) * navmap).sum()))
print(np.max(navmap))