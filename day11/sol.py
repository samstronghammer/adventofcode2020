#!/usr/bin/python3
import sys
import os
sys.path.append(f"{os.path.dirname(__file__)}/..")
import util
import math

# I really like these kind of simulation problems. They seem like riffs
# on Conway's Game of Life.

# Runs the seating simulation for part 1 or 2, depending on the arguments
def simulate_seating(filled_func, max_surrounding, seats):
    changed = True
    while changed:
        changed = False
        newseats = {}
        for loc in seats:
            char = seats[loc]
            if char != ".":
                filled = filled_func(loc, seats)
                if filled == 0 and char == "L":
                    newseats[loc] = "#"
                    changed = True
                elif filled >= max_surrounding and char == "#":
                    newseats[loc] = "L"
                    changed = True
                else:
                    newseats[loc] = seats[loc]
            else:
                newseats[loc] = "."
        seats = newseats
    return list(seats.values()).count("#")

# Calculates number of adjacent seats that are filled
def adj_8_filled(loc, seats):
    adj = util.adj8(loc)
    filled = 0
    for loc2 in adj:
        if loc2 in seats and seats[loc2] == "#":
            filled += 1
    return filled

# Calculates number of visible seats that are filled
def visible_8_filled(loc, s):
    vecs = util.adj8((0, 0))
    count = 0
    for v in vecs:
        newloc = loc
        while True:
            newloc = util.vecadd(newloc, v)
            if newloc in s:
                if s[newloc] == "L":
                    break
                elif s[newloc] == "#":
                    count += 1
                    break
            else:
                break
    return count

fn = f"{os.path.dirname(__file__)}/in.txt"
l = util.filetolist(fn)
# Convert the list of strings to a map from locations to characters
# (much easer to check if a location is in the map and requires less
# nesting)
seats = {}
for r in range(len(l)):
    for c in range(len(l[r])):
        seats[(r, c)] = l[r][c]

print("Part 1 Solution:")
print(simulate_seating(adj_8_filled, 4, seats))
print("Part 2 Solution:")
print(simulate_seating(visible_8_filled, 5, seats))

            
