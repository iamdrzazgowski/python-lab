import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 51)
plt.figure(figsize=(12,10))
for a in np.linspace(0.25, 2, 8):
    plt.plot(x, x**a, color=(a/2, 0, 1-a/2), label='$x^{%s}$' % a)
plt.legend()
plt.show()
