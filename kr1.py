# n, k, m = map(int, input().split())
# d = map(int, input().split())

# for i in d:
# 	n -= i
# 	if(n <= 0):
# 		break
# 	n += i * k
# print(n)

# def get_winner(board):
# 	for row in board:
# 		if(row == ['X', 'X', 'X']):
# 			return 'X'	
# 		if(row == ['0', '0', '0']):
# 			return '0'
# 	for column in range(3):
# 		if(board[0][column] == 'X' and board[1][column] == 'X' and board[2][column] == 'X'):
# 			return 'X'
# 		if(board[0][column] == '0' and board[1][column] == '0' and board[2][column] == '0'):
# 			return '0'
# 	if(board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X'):
# 		return 'X'
# 	if(board[0][0] == '0' and board[1][1] == '0' and board[2][2] == '0'):
# 		return '0'
# 	if(board[2][0] == 'X' and board[1][1] == 'X' and board[0][2] == 'X'):
# 		return 'X'
# 	if(board[2][0] == '0' and board[1][1] == '0' and board[0][2] == '0'):
# 		return '0'
# 	return '?'

# board = []
# for row in range(3):
# 	board.append(list(input()))
# # print(board)
# print(get_winner(board))

# name = input()
# try:
# 	with open(name) as file:
# 		results = file.readlines()
# 		for row in range(len(results)):
# 			results[row] = results[row].split(';')
# 		amounts = dict(sorted({results[i][0] : sum(list(map(int, results[i][1:]))) for i in range(len(results))}.items(), key=lambda item : item[1], reverse = True))

# 		print(*list(amounts.keys())[0:3], sep = '\n')

# except:
# 	print("no data")

# n, k = map(int, input().split())
# pages = [1] * n
# for day in range(k):
# 	start, end = map(int, input().split())
# 	for i in range(start - 1, end):
# 		pages[i] = 0
# print(sum(pages))

class GasHolder:
    def __init__(self, volume):
    	if(volume < 0):
    		raise ValueError('negative volume')
    	else:
    		self.volume = volume
    	# self.amounts = {} 
    	self.amount = 0
    	self.temp = 273

    def inject(self, m, M):
    	if(m < 0 or M < 0):
    		raise ValueError('negative mass or molar mass')
    	else:
    		# if(M in self.amounts.keys()):
    		# 	self.amounts[M] += m / M
    		# else:
    		# 	self.amounts[M] = m / M 
    		self.amount += m / M

    def heat(self, dT):
    	self.temp += dT

    def cool(self, dT):
    	self.temp = max(0, self.temp - dT)

    def get_pressure(self):
    	return self.amount * 8.31 * self.temp / self.volume
    	# return sum([self.amounts[i] * 8.31 * self.temp / self.volume for i in self.amounts.keys()])

h = GasHolder(1.0)
h.inject(29, 29)
print(f'Pressure after operation: {h.get_pressure()} Pa')
h.inject(29, 29)
print(f'Pressure after operation: {h.get_pressure()} Pa')
h.heat(273)
print(f'Pressure after operation: {h.get_pressure()} Pa')
h.cool(373)
print(f'Pressure after operation: {h.get_pressure()} Pa')
h.cool(373)
print(f'Pressure after operation: {h.get_pressure()} Pa')


# h = GasHolder(0.5)
# h.inject(16, 32)
# print(h.get_pressure())

# n = int(input())
# colors = []
# for painting in range(n):
# 	colors = colors + input().split(';')[1].split(',')
# for i in range(len(colors)):
# 	colors[i] = colors[i].strip().lower()
# print(*sorted(set(sorted(colors))), sep = ', ')

# def J(channel1, channel2):
# 	only1 = channel1
# 	for sub in channel2:
# 		if(sub in channel1):
# 			only1.remove(sub)
# 	print(only1)
# 	only2 = channel2
# 	for sub in channel1:
# 		if(sub in channel2):
# 			only2.remove(sub)
# 	print(only2)
# 	both = []
# 	for sub in channel1:
# 		if(sub in channel2):
# 			both.append(sub)
# 	print(both)
# 	print()
# 	return len(both) / (len(only1) + len(only2) + len(both))

# def J(channel1, channel2):
# 	# print(channel1)
# 	# print(channel2)
	
# 	both = []
# 	for sub in channel1:
# 		if(sub in channel2):
# 			both.append(sub)
# 	only1 = channel1.copy()
# 	only2 = channel2.copy()
# 	for sub in both:
# 		only1.remove(sub)
# 		only2.remove(sub)
# 	return len(both) / (len(only1) + len(only2) + len(both))

# n = int(input())
# channels = {}
# for i in range(n):
# 	cid, sids = input().split(': ')
# 	channels[int(cid)] = list(map(int, sids.split(', ')))
# bots = list(map(int, input().split(', ')))
# given = int(input())

# # print(channels)
# for bot in bots:
# 	for channel in channels.keys():
# 		channels[channel].remove(bot)
# # print(channels)

# chids = list(channels.keys())
# chids.remove(given)
# # print({channel : J(channels[channel], channels[given]) for channel in chids})
# print(max({channel : J(channels[channel], channels[given]) for channel in chids}.items(), key = lambda item : item[1])[0])

# n = int(input())
# notes = []
# for note in range(n):
# 	notes.append(list(map(int, input().split())))
# # print(notes)	
# length = max(notes, key = lambda item : item[1])[1]
# # amounts = []
# maxfingers = 0
# last = 0
# for tick in range(length):
# 	setLast = True
# 	amount = 0
# 	doubles = []
# 	for note in notes[last: ]:
# 		if(note[0] == tick):
# 			pair = []
# 			for note1 in notes[0:note[0]]:
# 				if(note1[1] == tick):
# 					pair = note1
# 					break
# 			if(pair != [] and not(note in doubles or pair in doubles)):
# 				doubles.extend([note, pair])

# 		if(note[0] <= tick and note[1] >= tick):
# 			amount += 1
# 			if(setLast):
# 				last = note
# 				setLast = False
# 	# print(amount)
# 	# print(doubles)
# 	# print()
# 	amount -= len(doubles) // 2
# 	# amounts.append(amount)
# 	if(amount > maxfingers):
# 		maxfingers = amount
# # print(amounts)		
# # print(max(amounts))
# print(maxfingers)
