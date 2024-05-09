import matplotlib.pyplot as plt

c = -0.1 + 0.65j

x = []
y = []

colors = []


def julia_set(z, c):
    for i in range(300):
        z = z ** 2 + c
        if abs(z) > 2:
            return i
    return 300

d = 400

for i in range(d):
    for j in range(d):
        xi = -1.5 + 3 / d * i
        yi = -1.5 + 3 / d * j
        x.append(xi)
        y.append(yi)
        colors.append(julia_set(xi + yi * 1j, c))

plt.scatter(x, y, c=colors, s=0.3)
plt.axis('square')
plt.show()