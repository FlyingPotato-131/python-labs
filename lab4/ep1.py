from sympy import symbols
from sympy import Matrix
from sympy import pprint
from scipy import linalg
import numpy as np

mu, lmd, rho = symbols('mu lambda rho')
matrix = Matrix([[0, 0, 0, -1/rho, 0, 0, 0, 0, 0],
				   [0, 0, 0, 0, -1/rho, 0, 0, 0, 0],
				   [0, 0, 0, 0, 0, -1/rho, 0, 0, 0],
				   [-(lmd+2*mu), 0, 0, 0, 0, 0, 0, 0, 0],
				   [0, -mu, 0, 0, 0, 0, 0, 0, 0],
				   [0, 0, -mu, 0, 0, 0, 0, 0, 0],
				   [-lmd, 0, 0, 0, 0, 0, 0, 0, 0],
				   [0, 0, 0, 0, 0, 0, 0, 0, 0],
				   [-lmd, 0, 0, 0, 0, 0, 0, 0, 0]])

print('входная матрица')
pprint(matrix)
print('собственные значения и их кратности')
for value in list(matrix.eigenvals().items()):
	pprint(value)
# print(linalg.det(matrix))