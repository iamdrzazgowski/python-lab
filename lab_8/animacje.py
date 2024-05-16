import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

x = np.linspace(0, 2*np.pi, 200)
y = np.sin(x)

plot = ax.plot(x, y)
line = plot[0]


def animate(frame):
    y[:-1] = y[1:]
    y[-1] = np.sin(2 * np.pi * (frame / 100))
    line.set_data(x, y)
    return line


animation = FuncAnimation(fig, animate, frames=100, interval=1)
plt.show()
