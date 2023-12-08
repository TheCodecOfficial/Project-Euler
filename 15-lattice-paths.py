import numpy as np
from utils import binomial_coeff

n = 20

grid = np.zeros((n + 1, n + 1), dtype=int)
for i in range(n + 1):
    grid[0, i] = 1
    grid[i, 0] = 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        grid[i, j] = grid[i, j - 1] + grid[i - 1, j]

print(grid[n, n])

# Short solution:
print(binomial_coeff(2 * n, n))
