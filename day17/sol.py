#!/usr/bin/python3
import sys
import os
sys.path.append(f"{os.path.dirname(__file__)}/..")
import util
import math

# Another Game of Life simulation, generalized to higher dimensions

def simulate_life(lines, dimensions, cycles):
    locs = set()
    # Initialize locations
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "#":
                locs.add((x, y) + (0,) * (dimensions - 2))
    # Run simulation
    for _ in range(cycles):
        to_update = {}
        for loc in locs:
            # If loc hasn't been seen yet, add it.
            if not loc in to_update:
                to_update[loc] = 0
            # Iterate over adjacent locations, adding 1 to neighbor count
            for adj in util.adj_all(loc):
                if adj in to_update:
                    to_update[adj] += 1
                else:
                    to_update[adj] = 1
        # Iterate over locations that need to be updated
        for update in to_update:
            # If the location is active and doesn't satisfy the activity requirement, remove it
            if update in locs and to_update[update] != 2 and to_update[update] != 3:
                locs.remove(update)
            # If the location is not active and satisfies the activity requirement, add it
            elif not update in locs and to_update[update] == 3:
                locs.add(update)
    return len(locs) 


fn = f"{os.path.dirname(__file__)}/in.txt"

l = util.filetolist(fn)

print("Part 1 Solution:")
print(simulate_life(l, 3, 6))
print("Part 2 Solution:")
print(simulate_life(l, 4, 6))
