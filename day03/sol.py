#!/usr/bin/python3
import sys
import os
sys.path.append(f"{os.path.dirname(__file__)}/..")
import util
import math
from functools import reduce

# To find a specific location on the slope, modular arithmetic converts
# any location into one contained by the input file. Counting the trees
# is a matter of tracing the path using vector addition and checking if each
# location along the path before the bottom has a tree in it.

def trees_on_slope(l, v):
    loc = (0, 0)
    trees = 0
    while loc[1] < len(l):
        i = loc[0] % len(l[loc[1]])
        if l[loc[1]][i] == "#":
            trees = trees + 1
        loc = util.vecadd(loc, v)
    return trees

fn = f"{os.path.dirname(__file__)}/in.txt"

l = util.filetolist(fn)

vecarray = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

print("Part 1 Solution")
print(trees_on_slope(l, (3, 1)))
print("Part 2 Solution")
print(reduce(lambda x, y : x * trees_on_slope(l, y), vecarray, 1))
