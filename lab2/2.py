import pandas as pd

paperfile = input()
linkfile = input()

papers = pd.read_csv(paperfile, sep = ';', dtype = {'id' : 'i', 'title' : 'str', 'author' : 'str'})
links = pd.read_csv(linkfile, sep = ';', dtype = {'paper_id' : 'i', 'reference' : 'str'})

paperData = pd.merge(papers, pd.DataFrame([(title, links['reference'].value_counts()[title] if title in links['reference'].values else 0) for title in papers['title']], columns = ['title', 'nlinks']), on = 'title')

authorData = pd.Series({author : paperData[paperData['author'] == author]['nlinks'].mean() for author in set(paperData['author'])}).sort_values(ascending = False)
for author in authorData.head(3).keys():
	print(author, '{:.3f}'.format(authorData[author]))
