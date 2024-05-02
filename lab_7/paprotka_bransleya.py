import matplotlib.pyplot as plt
import numpy as np

def f1(x, y):
    return 0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6

def f2(x, y):
    return -0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44

def f3(x, y):
    return 0.20 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6

def f4(x, y):
    return 0, 0.16 * y

p0 = np.array([0, 0])

num_steps = 100000

probabilities = [0.85, 0.07, 0.07, 0.01]
functions = [f1, f2, f3, f4]

points = [p0]

for _ in range(num_steps):
    func_idx = np.random.choice(range(4), p=probabilities)
    next_point = functions[func_idx](*points[-1])
    points.append(next_point)

x = [point[0] for point in points]
y = [point[1] for point in points]

plt.figure(figsize=(8, 6))
plt.scatter(x, y, s=0.1, c='green')
plt.title('Zbiór punktów wygenerowany przez przekształcenia')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
