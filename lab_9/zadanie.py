import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import rc

rc('animation', html='jshtml')

def initialize_grid(size):
    return np.random.choice([0, 1], size=(size, size))

def update_grid(grid):
    new_grid = grid.copy()
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            total = int((grid[i, (j - 1) % grid.shape[1]] + grid[i, (j + 1) % grid.shape[1]] +
                         grid[(i - 1) % grid.shape[0], j] + grid[(i + 1) % grid.shape[0], j] +
                         grid[(i - 1) % grid.shape[0], (j - 1) % grid.shape[1]] + grid[
                             (i - 1) % grid.shape[0], (j + 1) % grid.shape[1]] +
                         grid[(i + 1) % grid.shape[0], (j - 1) % grid.shape[1]] + grid[
                             (i + 1) % grid.shape[0], (j + 1) % grid.shape[1]]))

            if grid[i, j] == 1:
                if (total < 2) or (total > 3):
                    new_grid[i, j] = 0
            else:
                if total == 3:
                    new_grid[i, j] = 1
    return new_grid

grid_size = 50
grid = initialize_grid(grid_size)

def evolve(frame_num, mat, grid):
    new_grid = update_grid(grid)
    mat.set_data(new_grid)
    grid[:] = new_grid[:]
    return mat

fig, ax = plt.subplots()
mat = ax.imshow(grid, interpolation='nearest', cmap='binary')
ani = animation.FuncAnimation(fig, evolve, fargs=(mat, grid), frames=314, interval=100, save_count=50)
plt.show()