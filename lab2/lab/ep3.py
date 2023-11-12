import pandas as pd
import matplotlib.pyplot as plt
import re

def first_int(places):
	return int(re.search(r"[0-9]+", places)[0])

def iint(number):
	return int(number) if number != '' else 0

students = pd.read_excel('students_info.xlsx', names = ['User', 'group_faculty', 'group_out'], dtype = {'login' : 'str', 'group_faculty' : 'i', 'group_out' : 'i'})
results = pd.read_html('results_ejudge.html', converters = {'Place' : first_int, 'User' : str, 'A' : iint, 'B' : iint, 'C' : iint, 'D' : iint, 'E' : iint, 'F' : iint, 'G' : iint, 'H' : iint, 'Solved' : int, 'Score' : int})[0]

data = pd.merge(students, results, on = 'User').sort_values('Place')
# print(data)
print('student transfer with partially solved G and H problems')
print(pd.concat([data[data['G'] > 10], data[data['H'] > 10]]).drop_duplicates().loc[:, ['User', 'group_faculty', 'group_out']])


pd.DataFrame([(group, data[data['group_faculty'] == group]['Solved'].mean()) for group in set(data['group_faculty'])], columns = ['group_faculty', 'average solved']).plot(x = 'group_faculty', kind = 'bar')
pd.DataFrame([(group, data[data['group_out'] == group]['Solved'].mean()) for group in set(data['group_out'])], columns = ['group_out', 'average solved']).plot(x = 'group_out', kind = 'bar')
plt.show()
