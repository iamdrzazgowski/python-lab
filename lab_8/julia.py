import numpy as np
import matplotlib.pyplot as plt
import time

c = -0.1 + 0.65j
d = 400

x = np.array([])
y = np.array([])

colors = np.array([])

def julia_set(z, c):
    for i in range(300):
        z = z ** 2 + c
        if abs(z) > 2:
            return i
    return 300

start_t = time.time()
for i in range(d):
    for j in range(d):
        xi = -1.5 + 3 / d * i
        yi = -1.5 + 3 / d * j
        x = np.append(x, xi)
        y = np.append(y, yi)
        colors = np.append(colors, [julia_set(xi + yi * 1j, c)])

print(time.time() - start_t)
plt.figure(figsize=(10,10))
plt.scatter(x, y, c=colors, s=0.3)
plt.axis('square')
plt.show()