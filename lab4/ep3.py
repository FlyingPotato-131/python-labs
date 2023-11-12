from sympy import Function, dsolve, Derivative, checkodesol, pprint
from sympy.abc import x
import sympy
import math
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np

def F(t, y):
	return -2 * y

y = Function('y')
# pprint(dsolve(Derivative(y(x), x, x) + 9 * y(x), y(x)))
ageneral = dsolve(Derivative(y(x), x) + 2 * y(x), y(x), ics = {y(0) : sympy.sqrt(2)})
print('analytic equasion solution:')
pprint(ageneral)
# print(ageneral.rhs)

ngeneral = sympy.lambdify(x, ageneral.rhs)

numeric = solve_ivp(F, [0, 10], [math.sqrt(2)], t_eval = np.linspace(0, 10, num = 1000))
# print(numeric)

fig, ax = plt.subplots()

plt.minorticks_on()
plt.grid(True, "major", "both", color = "#888888")
plt.grid(True, "minor", "both", linestyle = '--')

ax.plot(numeric.t, numeric.y[0], label = 'numeric')
x = np.linspace(0, 10, num = 1000)
ax.plot(x, ngeneral(x), label = 'analytic')
plt.legend()
plt.title('numeric and analytic solution for y(x)')
plt.xlabel('x')
plt.ylabel('y')

plt.show()

fig, ax = plt.subplots()

plt.minorticks_on()
plt.grid(True, "major", "both", color = "#888888")
plt.grid(True, "minor", "both", linestyle = '--')

plt.title('difference between numeric and analytic solution for y(x)')
plt.xlabel('x')
plt.ylabel('ya - yn')

ax.plot(x, ngeneral(x) - numeric.y[0])
plt.show()
