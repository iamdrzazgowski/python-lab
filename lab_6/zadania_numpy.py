import numpy as np
import matplotlib.pyplot as plt
import math

t = np.array([1, 2, 3])  # tworzenie tablicy
t1 = np.zeros((3, 5))  # tablica wypełniona zerami
t2 = np.ones(10)  # tablica wypełniona jedynkami

l = np.linspace(0, 1, 11)  # tworzenie przestrzeni liniowej
l1 = np.linspace(0, 1, 6)
l2 = np.arange(0, 1, 0.2)

x = np.arange(1, 5, 1)
x2 = np.array([i for i in range(11)])

x3 = np.array(([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# x = [i for i in range(1, 11)]
# y = list(map(lambda x: x ** 2, x))
# plt.scatter(x, y, marker="o")
# plt.show()

# x = [i/100 for i in range(0,628)]
# y = list(map(lambda i: math.sin(i), x))
# plt.scatter(x,y)
# plt.show()

x = np.linspace(-1, 1, 20)
plt.scatter(x, x**2)
plt.scatter(x, x**3)
# plt.legend()
plt.show()