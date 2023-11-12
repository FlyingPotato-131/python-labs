# class Car():
# 	def __init__(self, c, v, n):
# 		self.capacity = c
# 		self.speed = v
# 		self.number = n

# 	def __str__(self):
# 		return "<Car capacity:{} speed:{} number:{}>".format(self.capacity, self.speed, self.number)

# 	def __eq__(self, other):
# 		return type(other) == type(self) and self.number == other.number

# 	def __hash__(self):
# 		return hash(self.capacity * self.speed * len(self.number))

# a = Car(100, 100, "asd")
# b = Car(100, 100, "zzz")
# c = Car(200, 50, "asd")

# # Эти не равны
# print(a == b)
# # Эти равны
# print(a == c)

# print(a == None)
# print(a == 1)

# s = set()
# s.add(a)
# s.add(b)
# s.add(c)
# s.add(a)
# s.add(a)

# # Ожидаем увидеть номера двух машин,
# # так как всё остальное в описанной логике является дублями
# print("=== Cars in set ===")
# for z in sorted(s, key=lambda e: e.number):
#     print(z.number)

# class RaceCar(Car):
# 	def __init__(self, v):
# 		self.capacity = 0
# 		self.speed = v
# 		self.number = None
# 		# self = Car(0, v, None)

# c = Car(1, 2, 3)
# print(c)
# r = RaceCar(10)
# print(r.capacity)

# class MoneyBox:
# 	def __init__(self):
# 		self.money = 0
# 		self.coins = 0

# 	def add_coin(self, value):
# 		self.money += value
# 		self.coins += 1

# 	def get_coins_number(self):
# 		return self.coins

# 	def get_coins_value(self):
# 		return self.money

# m = MoneyBox()
# # Добавили монетку достоинством 10
# m.add_coin(10)
# # Добавили монетку достоинством 5
# m.add_coin(5)

# # Ожидаем, что монеток внутри 2 штуки
# print(m.get_coins_number())
# # Ожидаем, что общее достоинство всех монеток 15
# print(m.get_coins_value())

class Car:
    def __init__(self, c, s, n):
        self.capacity = int(c)
        self.speed = int(s)
        self.number = n

# Грузовик
class Truck(Car):
    pass

# Автобус
class Bus(Car):
    pass

class Garage:
	def __init__(self):
		self.cars = []
		self.trucks = []
		self.buses = []

	def park(self, v):
		if(type(v) == Car):
			self.cars.append(v)
		elif(type(v) == Truck):
			self.trucks.append(v)
			self.cars.append(v)
		elif(type(v) == Bus):
			self.buses.append(v)
			self.cars.append(v)

	def count(self, t):
		if(t == Car):
			return len(self.cars)
		if(t == Truck):
			return len(self.trucks)
		if(t == Bus):
			return len(self.buses)

	def get_fastest_of_type(self, t):
		if(t == Car):
			return max(self.cars, key = lambda vehicle : vehicle.speed)
		if(t == Truck):
			return max(self.trucks, key = lambda vehicle : vehicle.speed)
		if(t == Bus):
			return max(self.buses, key = lambda vehicle : vehicle.speed)

g = Garage()
# Паркуем машины
g.park(Car(1, 100, "abc"))
g.park(Truck(1000, 150, "zzz"))
g.park(Bus(100, 50, "QWE"))
g.park(Bus(100, 80, "ASD"))
g.park(Bus(100, 20, "ZXC"))

# Сколько всего машин? Ожидаем 5, потому что грузовик и автобус - тоже машины.
print(g.count(Car))
# Сколько всего грузовиков? Ожидаем 1.
print(g.count(Truck))
# Сколько всего автобусов? Ожидаем 3.
print(g.count(Bus))
# Получим самую быструю машину и выведем её номер. Ожидаем zzz, потому что грузовик внезапно самый быстрый.
print(g.get_fastest_of_type(Car).number)
# Получим самый быстрый грузовик и выведем его номер. Ожидаем zzz.
print(g.get_fastest_of_type(Truck).number)
# Получим самый быстрый автобус и выведем его номер. Ожидаем ASD.
print(g.get_fastest_of_type(Bus).number)