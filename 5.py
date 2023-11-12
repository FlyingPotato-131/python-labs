n = input()
while int(n) > 9:
	s = 0
	for i in n:
		s += int(i)
	n = str(s)
print(n)
