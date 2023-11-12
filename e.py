# N = int(input())
# print(*dict(sorted(dict([input().split() for _ in range(N)]).items(), key = lambda item : item[1], reverse = True)), sep = '\n')

# exp = input().split()
# try:
# 	if(exp[1] == '+'):
# 		print(int(exp[0]) + int(exp[2]))
# 	elif(exp[1] == '-'):
# 		print(int(exp[0]) - int(exp[2]))
# 	elif(exp[1] == '*'):
# 		print(int(exp[0]) * int(exp[2]))
# 	elif(exp[1] == '^'):
# 		print(int(exp[0]) ** int(exp[2]))
# 	else:
# 		print('Bad input')
# except:
# 	print('Bad input')

# aabb = [list(map(float, input().split())) for _ in range(3)]
# # print(aabb)
# N = int(input())
# Nin = 0
# for i in range(N):
# 	coords = list(map(float, input().split()))
# 	flags = [(coords[i] < aabb[i][1] and coords[i] > aabb[i][0]) for i in range(3)]
# 	if(flags[0] and flags[1] and flags[2]):
# 		Nin += 1
# print(Nin)

# N = int(input())
# T = []
# P = []
# for i in range(N):
# 	data = list(map(float, input().split()))
# 	T.append(data[0])
# 	if(data[0] >= -70 and data[0] <= 80):
# 		P.append(data[1])
# print('{:.4f}'.format(sum(T) / len(T)), '{:.4f}'.format(sum(P) / len(P)))

# def decrypt(string):
# 	ret = ''
# 	for c in string:
# 		if(ord(c) - ord('a') >= 0 and ord(c) - ord('a') <= 26):
# 			ret = ret + (chr((ord(c) - ord('a') - 13) % 26 + ord('a')))
# 		elif(ord(c) - ord('A') >= 0 and ord(c) - ord('A') <= 26):
# 			ret = ret + (chr((ord(c) - ord('A') - 13) % 26 + ord('A')))
# 		else:
# 			ret = ret + c
# 	return ret

# def decryptn(strings):
# 	ret = []
# 	for string in strings:
# 		ret.append(decrypt(string))
# 	return ret

# name = input()
# try:
# 	with open(name) as file:
# 		print(*decryptn(file.readlines()), sep = '\n')

# except:
# 	print('Can not read file')

# class Cursor:
#     # Конструктор, принимающий два параметра - координаты X и Y
#     def __init__(self, x, y):
#     	self.x = x
#     	self.y = y
#     	self.clicks = []

#     # Передвинуть по оси X на n и по оси Y на m
#     # n, m - произвольные целые числа
#     def move(self, n, m):
#     	self.x += n
#     	self.y += m

#     # Клик в текущем положении курсора
#     def click(self):
#     	self.clicks.append([self.x, self.y])

#     # Вернуть количество кликов в заданном прямоугольнике
#     def get_click_count(self, min_x, max_x, min_y, max_y):
#     	n = 0
#     	for click in self.clicks:
#     		if(click[0] > min_x and click[0] < max_x and click[1] > min_y and click[1] < max_y):
#     			n += 1
#     	return n

# c = Cursor(100, 100)
# c.click()
# c.move(10, -10)
# c.click()
# c.move(-10, 10)
# c.click()
# print(c.get_click_count(95, 105, 95, 105))
# print(c.get_click_count(0, 10, 0, 10))

# string = input()
# print('#' * (len(string) + 4))
# print('# ' + string + ' #')
# print('#' * (len(string) + 4))

# print(*sorted(sorted(list(set(input().split()))), key = lambda value : len(value), reverse = True), sep = '\n')

size = list(map(int, input().split()))
mmap = [list(input()) for i in range(size[1])]
h = list(map(int, input().split()))
print(*([''.join(mmap[i][max(0, h[0] - h[2]) : min(h[0] + h[2] + 1, size[0])]) for i in range(max(0, h[1] - h[2]), min(h[1] + h[2] + 1, size[1]))]), sep = '\n')