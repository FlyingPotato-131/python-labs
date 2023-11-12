W, H = map(int, input().split())

facade = [[0 for w in range(W)] for h in range(H)]

nwindows = int(input())
broken = False

for i in range(nwindows):
	w1, w2, h1, h2 = map(int, input().split())
	if(w1 < 0 or w2 > W or h1 < 0 or h2 > H):
		broken = True
	else:
		for h in range(h1, h2):
			for w in range(w1, w2):
				if(facade[h][w] == 1):
					broken = True
				facade[h][w] = 1

if(broken):
	print('broken')
else:
	print('correct')