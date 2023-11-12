N, M, K, Ta, Tb, Tc = map(float, input().split(' '))
elTime = Ta * abs(K - N) + Tb + Tb + Ta * abs(M - N) + Tb
strTime = abs(M - N) * Tc
if(elTime <= strTime):
	print('elevator')
else:
	print('stairs')
