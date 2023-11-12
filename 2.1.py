def fib(n):
	fibs = [0, 1]
	for i in range(2, n):
		fibs.append(fibs[i-2] + fibs[i-1])
	return fibs[n - 1]

def nonn(n):
	nons = ([0] * 8) + [1]
	for i in range(9, n):
		nons.append(sum(nons[i - k] for k in range(1, 10)))
	return nons[n - 1]

# print(max(map(int, input().split())))

# orig = [int(n) for n in input().split()]
# ret = []
# for i in range(len(orig)):
# 	if not(orig[i] in orig[i+1 : ] or orig[i] in orig[ : i]):
# 		ret.append(orig[i])
# print(max(ret))

# words = input().split()
# ret = {}
# for word in words:
# 	if word in ret:
# 		ret[word] = ret[word] + 1
# 	else:
# 		ret[word] = 1

out = dict(sorted(dict(sorted(ret.items(), key = lambda item: item[0])).items(), key = lambda item: item[1], reverse = True))

# for word in out:
# 	print(out[word], word)

# with open(input(), 'r') as file:
# 	print(max(' '.join(file).split(), key = lambda word: len(word)))

words = []
for path in input().split():
	try:
		with open(path) as file:
			words = words + ' '.join(file).split()

	except(FileNotFoundError):
		True

print(*sorted([*{*words}]))