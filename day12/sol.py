#!/usr/bin/python3
import sys
import os
sys.path.append(f"{os.path.dirname(__file__)}/..")
import util
import math

# Vector math is very precise. Fortunately, I had part 1 set up in such
# a way that part 2 was straightforward.

fn = f"{os.path.dirname(__file__)}/in.txt"

l = util.filetolist(fn)

loc = (0, 0)
vec = (1, 0)

for line in l:
    action = line[0]
    val = int(line[1:])
    if action == "N":
        loc = util.vecadd((0, val), loc)
    elif action == "S":
        loc = util.vecadd((0, -1 * val), loc)
    elif action == "E":
        loc = util.vecadd((val, 0), loc)
    elif action == "W":
        loc = util.vecadd((-1 * val, 0), loc)
    elif action == "L":
        numturns = int(val / 90)
        for i in range(numturns):
            vec = (-1 * vec[1], vec[0])
    elif action == "R":
        numturns = int(val / 90)
        for i in range(numturns):
            vec = (vec[1], -1 * vec[0])
    elif action == "F":
        loc = util.vecadd((vec[0] * val, vec[1] * val), loc)
    else:
        print("OH NO WHAT HAPPENED")
print("Part 1 Solution:")
print(abs(loc[0]) + abs(loc[1]))

ship = (0, 0)
waypoint = (10, 1)

for line in l:
    action = line[0]
    val = int(line[1:])
    if action == "N":
        waypoint = util.vecadd((0, val), waypoint)
    elif action == "S":
        waypoint = util.vecadd((0, -1 * val), waypoint)
    elif action == "E":
        waypoint = util.vecadd((val, 0), waypoint)
    elif action == "W":
        waypoint = util.vecadd((-1 * val, 0), waypoint)
    elif action == "L":
        numturns = int(val / 90)
        for i in range(numturns):
            waypoint = (-1 * waypoint[1], waypoint[0])
    elif action == "R":
        numturns = int(val / 90)
        for i in range(numturns):
            waypoint = (waypoint[1], -1 * waypoint[0])
    elif action == "F":
        for i in range(val):
            ship = util.vecadd(waypoint, ship)
    else:
        print("OH NO WHAT HAPPENED")
print("Part 2 Solution:")
print(abs(ship[0]) + abs(ship[1]))