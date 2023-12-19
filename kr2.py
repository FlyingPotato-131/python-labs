# import re

# nums = re.findall(r'[0-9]', input())
# B = int(input())
# print(int(nums[0] + nums[-1]) - B)



# import numpy as np

# N = int(input())
# data = np.empty([0, 15])
# names = []
# for i in range(N):
# 	row = input().split()
# 	data = np.append(data, [row[1:]], axis = 0).astype('i')
# 	names.append(row[0])

# winners = [] 
# nums = list(map(int, input().split()))
# for n in nums:
# 	data = (data != n) * data
# 	# print(data)
# 	# print()
# 	for i in range(np.shape(data)[0]):
# 		if(np.all(data[i, :] == 0)):
# 			winners.append(i)
# 	if(winners != []):
# 		break

# # print(winners)
# wnames = []
# for w in winners:
# 	wnames.append(names[w])
# print(*sorted(wnames))




# N = int(input())
# data = []
# for i in range(N):
# 	visit = input().replace(' ', '')
# 	visit = visit.replace('О', 'O').replace('0', 'O')
# 	visit = visit.replace('Д', 'D')
# 	visit = visit.replace('С', 'S').replace('C', 'S')
# 	visit = visit.split(';')
# 	data.append(tuple(visit))

# print(len(dict(data).keys()))
# print(len(set(data)))
# right = [visit for visit in data if visit[1] == 'OD']
# print(len(set(right)))
# left = [visit for visit in data if visit[1] == 'OS']
# print(len(set(left)))




# import numpy as np
# from PIL import Image

# path = input()
# img = Image.open(path)
# data = np.array(img, dtype = 'i')
# # print(data)
# H, W = np.shape(data)
# # print(H, W)
# compressed = np.empty([H // 2, W // 2], dtype = 'i')

# for h in range(H // 2):
# 	for w in range(W // 2):
# 		compressed[h, w] = int(0.25 * (data[2*h, 2*w] + data[2*h+1, 2*w] + data[2*h, 2*w+1] + data[2*h+1, 2*w+1]))

# print(np.min(compressed), np.max(compressed))
# # Image.fromarray(compressed).convert('RGB')




# import numpy as np

# vertices = np.array(input().split(), dtype = 'i')
# N = int(input())
# edges = np.empty([0, 2], dtype = 'i')
# for i in range(N):
# 	edges = np.append(edges, [list(map(int, input().split()))], axis = 0)
# start = int(input())
# K = int(input())

# reached = [start]
# for i in range(K):
# 	reached_new = []
# 	for vertex in reached:
# 		for edge in edges:
# 			if(edge[0] == vertex):
# 				reached_new.append(edge[1])
# 			if(edge[1] == vertex):
# 				reached_new.append(edge[0])
# 	reached = reached + reached_new

# print(*set(sorted(reached)))




# import numpy as np

# H, W = map(int, input().split())
# heightmap = np.empty([0, W], dtype = 'i')
# for i in range(H):
# 	heightmap = np.append(heightmap, [list(map(int, input().split()))], axis = 0)
# heightmap = (heightmap > 0) * heightmap
# # print(heightmap)

# max_x = 0
# max_y = 0
# it = np.nditer(heightmap, flags = ['multi_index'], op_flags = ['readonly'])
# for coord in it:
# 	# print(coord)
# 	if(it.multi_index[0] + 1 < H and abs(heightmap[it.multi_index[0] + 1, it.multi_index[1]] - heightmap[it.multi_index[0], it.multi_index[1]]) > max_y):
# 		max_y = abs(heightmap[it.multi_index[0] + 1, it.multi_index[1]] - heightmap[it.multi_index[0], it.multi_index[1]])
# 	if(it.multi_index[1] + 1 < W and abs(heightmap[it.multi_index[0], it.multi_index[1] + 1] - heightmap[it.multi_index[0], it.multi_index[1]]) > max_x):
# 		max_x = abs(heightmap[it.multi_index[0], it.multi_index[1] + 1] - heightmap[it.multi_index[0], it.multi_index[1]])
# print(max(max_x, max_y))




# import numpy as np

# apath = input()
# bpath = input()
# cpath = input()
# N = int(input())

# with open(apath) as file:
# 	A = np.array([list(map(float, row.split())) for row in file.readlines()], dtype = 'f')
# 	A = A.astype('i')
# with open(bpath) as file:
# 	B = np.array([list(map(float, row.split())) for row in file.readlines()], dtype = 'f')
# with open(cpath) as file:
# 	C = np.array([list(map(float, row.split())) for row in file.readlines()], dtype = 'f')

# for i in range(N):
# 	A = (B @ A + C @ np.transpose(A)).astype('i')
# print(np.min(A), np.max(A))




import regex as re

def digit(string):
	if(string == 'one'):
		return 1
	if(string == 'two'):
		return 2
	if(string == 'three'):
		return 3
	if(string == 'four'):
		return 4
	if(string == 'five'):
		return 5
	if(string == 'six'):
		return 6
	if(string == 'seven'):
		return 7
	if(string == 'eight'):
		return 8
	if(string == 'nine'):
		return 9
	return int(string)

nums = re.findall(r'[0-9]|one|two|three|four|five|six|seven|eight|nine', input().lower(), overlapped = 1)
a = 0
if(len(nums) == 1):
	a = int(str(digit(nums[0])) + str(digit(nums[0])))
elif(len(nums) != 0):
	a = int(str(digit(nums[0])) + str(digit(nums[-1])))
print(a - int(input()))