#!/usr/bin/python3
import sys
import os
sys.path.append(f"{os.path.dirname(__file__)}/..")
import util
import math

fn = f"{os.path.dirname(__file__)}/in.txt"

# An iteration over all possible combinations was sufficient.
# I added logic so that different orderings of the same combinations
# of numbers are not used.

l = util.filetointlist(fn)

for i in range(len(l)):
    for j in range(i):
        if l[i] + l[j] == 2020:
            print("Part 1 Solution:")
            print(l[i] * l[j])
        for k in range(j):
            if l[i] + l[j] + l[k] == 2020:
                print("Part 2 Solution")
                print(l[i] * l[j] * l[k])