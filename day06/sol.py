#!/usr/bin/python3
import sys
import os
sys.path.append(f"{os.path.dirname(__file__)}/..")
import util
import math
from functools import reduce

# Fun puzzle, it came down to taking unions and intersections
# of each group of strings.

fn = f"{os.path.dirname(__file__)}/in.txt"

l = util.filetolist(fn)
group = []
countp1 = 0
countp2 = 0
for line in l:
    if line:
        group.append(set(list(line)))
    else:
        union = reduce(lambda x, y: x.union(y), group, set())
        countp1 += len(union)
        intersection = reduce(lambda x, y: x.intersection(y), group, group.pop())
        countp2 += len(intersection)
        group = []
print("Part 1 Solution:")
print(countp1)
print("Part 2 Solution:")
print(countp2)
