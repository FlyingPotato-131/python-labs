# array = map(int, input().split())
# print(*sorted(sorted(array, reverse = True)[:int(input())]), sep = '\n')

# import re
# print(sum(map(int, re.findall(r" [+,-]?[0-9]+ ", ' ' + input() + ' '))))

# import re
# n = input()
# print(float(n) - 10**(-len(re.findall(r"[0-9]", str(re.search(r"[.][0-9]+", n))))))

# n = input()
# parts = n.split('.')
# if(len(parts) > 1):
# 	print("{:.{prec}f}".format(float(n) - 10**-len(parts[1]), prec = len(parts[1])))
# else:
# 	print(int(n) - 1)

# print(len(max(input().split('0'))))

# import re

# name = input()
# try:
# 	with open(name) as file:
# 		print(len(re.findall(' ' + input().lower() + ' ', ' ' + ' '.join(file.readlines()).lower().replace('\n', '') + ' ')))
# except:
# 	print(0)
# finally:
# 	print('e')

# class GasStation:
#     # Конструктор, принимающий один параметр - ёмкость резервуара колонки
#     # Резервуар создаётся пустой
#     def __init__(self, capacity):
#     	self.capacity = capacity
#     	self.fuel = 0

#     # Залить в резервуар колонки n литров топлива
#     # Если столько не влезает в резервуар - не заливать ничего, выбросить exception
#     def fill(self, n):
#     	if(self.fuel + n <= self.capacity):
#     		self.fuel += n
#     	else:
#     		raise Exception

#     # Заправиться, забрав при этом из резервура n литров топлива
#     # Если столько нет в резервуаре - не забирать из резервуара ничего, выбросить exception
#     def tank(self, n):
#     	if(n <= self.fuel):
#     		self.fuel -= n
#     	else:
#     		raise Exception
# 
#     # Запросить остаток топлива в резервуаре
#     def get_limit(self):
#     	return self.fuel

# s = GasStation(1000)
# s.fill(300)
# print(s.get_limit())
# s.tank(100)
# s.fill(300)
# print(s.get_limit())
# for i in range(5):
#     s.tank(50)
# print(s.get_limit())
# s.fill(1000)
# for i in range(50):
#     s.tank(100)
# print(s.get_limit())

# N = int(input())
# words = {}
# for i in range(N):
# 	for word in input().split():
# 		if(word.lower() in words.keys()):
# 			if(word not in words[word.lower()]):
# 				words[word.lower()].append(word)
# 		else:
# 			words[word.lower()] = [word]

# nwords = {word: len(words[word]) for word in words.keys() if len(words[word]) > 2}

# # print(words)	
# # print(nwords)

# out = dict(sorted(dict(sorted(nwords.items(), key = lambda item: item[0])).items(), key = lambda item: item[1], reverse = True))
# print(*out.keys(), sep = '\n')

nevents = int(input())

state = {}
prevT = 0

for i in range(nevents):
	cmd = input().split()
	print(cmd[0])
	if(prevT in state.keys()):
		state[int(cmd[0]) + 1] = state[prevT].copy()
	else:
		state[int(cmd[0]) + 1] = {}
	if(cmd[1] == 'SET'):
		# state[cmd[0]] = {cmd[2]: cmd[3]}
		state[int(cmd[0]) + 1][cmd[2]] = cmd[3]
	if(cmd[1] == 'DELETE'):
		del state[int(cmd[0]) + 1][cmd[2]]

	prevT = int(cmd[0]) + 1
	print(*state.items(), sep = '\n')
	print()

state = dict(sorted(state.items(), key = lambda item: item[0]))

ncalls = int(input())

for i in range(ncalls):
	time = int(input())
	tstamp = 0
	for i in state.keys():
		if(i > time):
			tstamp = i
			break
		if(i == time):
			tstamp = i
			break
	if(tstamp == 0 or state[tstamp] == {}):
		print('(none)')
	else:
		print(*[str(list(state[tstamp].keys())[i]) + ' : ' + str(list(state[tstamp].values())[i]) for i in range(len(state[tstamp]))], sep = '\n')

