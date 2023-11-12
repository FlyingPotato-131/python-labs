import pandas as pd

transactions = pd.read_csv('transactions.csv', dtype = {'CONTRACTOR' : 'str', 'STATUS' : 'str', 'SUM' : 'i'}, index_col = 0, names = ['contractor', 'status', 'sum'], header = 0)
# print(transactions)
top3 = transactions[transactions['status'] == 'OK'].sort_values('sum', ascending = False).head(3).values
print('top 3 payments')
for transaction in top3:
	print('contractor: {}, sum: {}'.format(transaction[0], transaction[2]))
print()	
print('sum of payments to Umbrella, Inc: {}'.format(transactions[transactions['contractor'] == 'Umbrella, Inc']['sum'].sum()))
