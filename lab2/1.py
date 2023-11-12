import pandas as pd

gamefile = input()
ratefile = input()

games = pd.read_csv(gamefile, sep = ';', header = 0, dtype = {'id' : 'i', 'name' : 'str', 'company' : 'str'})
rates = pd.read_csv(ratefile, sep = ';', header = 0, dtype = {'id' : 'i', 'mark' : 'i'})

gamesData = pd.merge(games, pd.DataFrame([(i, rates[rates['id'] == i]['mark'].mean()) for i in set(rates['id'])], columns = ['id', 'mark']), on = 'id').sort_values(by = 'mark', ascending = False)

for i in gamesData.head(3)['id']:
	print(gamesData[gamesData['id'] == i].values[0][1], '{:.3f}'.format(gamesData[gamesData['id'] == i].values[0][3]))

print(*list(gamesData[gamesData['mark'] > 8]['company'].value_counts().to_dict().items())[0])
