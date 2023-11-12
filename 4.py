ln = int(input())
parray = []
narray = []
for i in range(ln):
	n = int(input())
	if(n < 0):
		narray.append(n)
	else:
		parray.append(n)
narray.sort(reverse = True)
parray.sort()
#print(parray.join(' '), narray.join(' '))
print(*parray, *narray)
