import numpy as np
import sys

sys.path.append("../")
from utils import product


with open("grid.txt") as f:
    grid = []
    for line in f:
        nums = list(map(int, line.strip().split(" ")))
        grid.append(nums)

    w, h = len(grid[0]), len(grid)
    for i in range(h):
        for j in range(w):
            pass
    horiz = [product(grid[i][j : j + 4]) for i in range(h) for j in range(w - 3)]
    vert = [(grid[i : i + 4][j]) for i in range(h - 3) for j in range(w)]
    print(vert)
