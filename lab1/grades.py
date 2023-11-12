import csv
import matplotlib.pyplot as plt

def readTable(name):
	with open(name) as file:
		data = list(csv.reader(file))
		return [data[i][0].split(';') for i in range(len(data))]

# print(readTable('students.csv'))
data = readTable('students.csv')

prepsdata = {data[i][0] : [] for i in range(len(data))}
for i in range(len(data)):
	prepsdata[data[i][0]].append(data[i][2])
pdatamod = {prep : {} for prep in prepsdata.keys()}
for prep in prepsdata.keys():
	pdatamod[prep] = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0}
	for grade in prepsdata[prep]:
		# if(int(grade) in pdatamod[prep].keys()):
		# print(grade)
		pdatamod[prep][int(grade)] += 1
		# else:
		# 	pdatamod[prep][int(grade)] = 1
	pdatamod[prep] = dict(sorted(pdatamod[prep].items(), key = lambda item : item[0]))

	
# print(prepsdata)
# print(pdatamod)

fig, ax = plt.subplots()
plt.title('marks per prep')
# ax.legend()
for prep in pdatamod.keys():
	ax.bar(prep, [list(pdatamod[prep].values())[k] for k in range(len(list(pdatamod[prep].keys())))], bottom = [sum(list(pdatamod[prep].values())[0 : k]) for k in range(len(list(pdatamod[prep].keys())))], color = ['w', 'k', 'b', 'g', 'r', 'c', 'm', 'y', '#BB6622', '#888888'], label = [k + 1 for k in range(len(list(pdatamod[prep].keys())))] if prep == list(pdatamod.keys())[0] else None)
	# ax.legend(list(pdatamod[prep].keys()))
# ax.legend([str(i) for i in range(3, 11)], ncols = 7)
ax.legend(loc = 'upper right')
plt.show()


groupdata = {data[i][1] : [] for i in range(len(data))}
for i in range(len(data)):
	groupdata[data[i][1]].append(data[i][2])
gdatamod = {prep : {} for prep in groupdata.keys()}
for group in groupdata.keys():
	gdatamod[group] = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0}
	for grade in groupdata[group]:
		# if(int(grade) in pdatamod[prep].keys()):
		# print(grade)
		gdatamod[group][int(grade)] += 1
		# else:
		# 	pdatamod[prep][int(grade)] = 1
	gdatamod[group] = dict(sorted(gdatamod[group].items(), key = lambda item : item[0]))

	
# print(prepsdata)
# print(gdatamod)

fig, ax = plt.subplots()
plt.title('marks per group')
for group in gdatamod.keys():
	# print(list(gdatamod[group].values()))
	ax.bar(group, [list(gdatamod[group].values())[k] for k in range(len(list(gdatamod[group].keys())))], bottom = [sum(list(gdatamod[group].values())[0 : k]) for k in range(len(list(gdatamod[group].keys())))], color = ['w', 'k', 'b', 'g', 'r', 'c', 'm', 'y', '#BB6622', '#888888'], label = [k + 1 for k in range(len(list(gdatamod[group].keys())))] if group == list(gdatamod.keys())[0] else None)
ax.legend(loc = 'upper right')
plt.show()
