import matplotlib.pyplot as plt
from elkpower.grid import Grid

grid = Grid()

fname = "simple.toml"
grid.read_configuration(fname)
grid.read_grid()
grid.draw()
plt.plot()
plt.show()
