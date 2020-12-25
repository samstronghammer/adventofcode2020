#!/usr/bin/python3
import sys
import os
sys.path.append(f"{os.path.dirname(__file__)}/..")
import util
import math

# Another interesting Game of Life simulation, this time in hexagonal space.
# I used the two-axis method. Other methods can be found here: 
# https://www.redblobgames.com/grids/hexagons

fn = f"{os.path.dirname(__file__)}/in.txt"

l = util.filetocharlistlist(fn)

# e = (1, 0), ne = (0, 1)
# The rest are derived from those two.
str_to_vec = {"e": (1, 0), "ne": (0, 1), "w": (-1, 0), "nw": (-1, 1), "se": (1, -1), "sw": (0, -1)}

locs = set()
for line in l:
    loc = (0, 0)
    i = 0
    while i < len(line):
        c = line[i]
        if c in {"e", "w"}:
            loc = util.vecadd(loc, str_to_vec[c])
        else:
            loc = util.vecadd(loc, str_to_vec[c + line[i + 1]])
            i += 1
        i += 1
    if loc in locs:
        locs.remove(loc)
    else:
        locs.add(loc)

print("Part 1 Solution:")
print(len(locs))

for _ in range(100):
    # adj_count contains a map from every location that matters (locations in locs or locations 
    # adjacent to locs) to how many neighbors it has that are flipped
    adj_count = {}
    for loc in locs:
        # If this location is not already in adj_count, add it.
        if not loc in adj_count:
            adj_count[loc] = 0
        # Increment each neighbor
        for vec in str_to_vec.values():
            adj = util.vecadd(loc, vec)
            if adj in adj_count:
                adj_count[adj] += 1
            else:
                adj_count[adj] = 1
    # Check each case, whether each tile ought to be flipped.
    for loc in adj_count:
        if loc in locs and (adj_count[loc] == 0 or adj_count[loc] > 2):
            locs.remove(loc)
        elif not loc in locs and adj_count[loc] == 2:
            locs.add(loc)
print("Part 2 Solution:")
print(len(locs))
