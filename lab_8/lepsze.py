import numpy as np
import matplotlib.pyplot as plt
import time

c = -0.1 + 0.65j
d = 400

X, Y = np.meshgrid(np.linspace(-1.5, 1.5, d), np.linspace(-1.5, 1.5, d))


def julia_set(z, c):
    for i in range(300):
        z = z ** 2 + c
    return np.abs(z)

start_t = time.time()
colors = julia_set(X + Y * 1j, c)
print(time.time() - start_t)
plt.figure(figsize=(10,10))
plt.scatter(X, Y, c=colors, s=0.4)
plt.axis('square')
plt.show()
