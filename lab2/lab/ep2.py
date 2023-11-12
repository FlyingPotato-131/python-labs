import pandas as pd
import matplotlib.pyplot as plt

flights = pd.read_csv('flights.csv', index_col = 0, header = 0, dtype = {'CARGO' : 'str', 'PRICE' : 'i', 'WEIGHT' : 'i'}, names = ['airline', 'price', 'mass'])
# print(flights)
airlines = set(flights['airline'])
# for airline in airlines:
airlineData = pd.DataFrame([(airline, flights[flights['airline'] == airline].shape[0], flights[flights['airline'] == airline]['price'].sum(), flights[flights['airline'] == airline]['mass'].sum()) for airline in airlines], columns = ['airline', 'amount of flights', 'total price transported', 'total mass transported'])
print(airlineData)

airlineData.plot(x = 'airline', y = 'amount of flights', kind = 'bar')
airlineData.plot(x = 'airline', y = 'total price transported', kind = 'bar')
airlineData.plot(x = 'airline', y = 'total mass transported', kind = 'bar')
plt.show()
