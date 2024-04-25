import numpy as np
import matplotlib.pyplot as plt

# x = np.linspace(0, 1, 51)
# plt.figure(figsize=(12,10))
# for a in np.linspace(0.25, 2, 8):
#     plt.plot(x, x**a, color=(a/2, 0, 1-a/2), label='$x^{%s}$' % a)
# plt.legend()
# plt.show()


# T = np.linspace(0, 2*np.pi, 1000)
# plt.scatter(np.sin(T), np.cos(T))
# plt.show()

# X = np.linspace(-3,3,500)
# Y = 1/(X**2-1)
# Y[abs(Y) > 5] = np.NaN
# plt.figure(figsize=(15,5))
# plt.plot(X,Y)
# plt.plot([-1, -1], [-10,10], '--')
# plt.show()

X, Y = np.meshgrid(np.linspace(-10, 10, 11 ), np.linspace(-10, 10, 11))
Z = X**2 + Y**2
plt.contourf(X, Y, Z, levels=80)
plt.show()