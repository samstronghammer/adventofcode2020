#!/usr/bin/python3
import sys
import os
sys.path.append(f"{os.path.dirname(__file__)}/..")
import util
import math

# This was a cool little puzzle, and I would imagine rather
# difficult for anyone who doesn't see the binary conversion
# quickly. The second argument to int was my savior here.
# I was particularly proud of how little code needed to be added
# to solve part 2.

def bin_str_to_int(s, oneChar):
    numstr = ""
    for c in s:
        if c == oneChar:
            numstr += "1"
        else:
            numstr += "0"
    return int(numstr, 2)

fn = f"{os.path.dirname(__file__)}/in.txt"

l = util.filetolist(fn)
idset = set()
for line in l:
    row = bin_str_to_int(line[0:7], "B")
    col = bin_str_to_int(line[7:10], "R")
    idset.add(row * 8 + col)

print("Part 1 Solution")
print(max(idset))

print("Part 2 Solution")
for id in idset:
    if id + 2 in idset and not id + 1 in idset:
        print(id + 1)
        break
