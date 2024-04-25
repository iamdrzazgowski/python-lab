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

# X, Y = np.meshgrid(np.linspace(-10, 10, 11 ), np.linspace(-10, 10, 11))
# Z = X**2 + Y**2
# plt.contourf(X, Y, Z, levels=80)
# plt.show()

c = -0.4 + 0.6j

x = []
y = []
colors = []

def julia_set(z, c):
    for i in range(300):
        z = z**2 + c

        if abs(z) > 2:
            return 1
    return 300

d = 1000

for i in range(d):
    for j in range(d):
        xi = -1.5 + 3/d*i
        yi = -1.5 + 3/d*j
        x.append(xi)
        y.append(yi)
        colors.append(julia_set(xi+yi*1j, c))

plt.figure(figsize=(15,15))
plt.scatter(x, y, c=colors, s=0.1, cmap='prism')
plt.axis('square')
plt.show()