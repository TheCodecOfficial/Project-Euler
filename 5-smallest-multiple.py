from math import lcm
from functools import reduce

print(reduce(lcm, [i for i in range(2, 21)]))
