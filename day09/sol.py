#!/usr/bin/python3
import sys
import os
sys.path.append(f"{os.path.dirname(__file__)}/..")
import util
import math

# First time getting on the global leaderboard this year :)
# Interesting problem, all about index tracking and iterating over
# the right parts of the list. Part 2 could certainly be optimized
# by skipping checking the very small and very large slices, but that
# requires more algorithmic complexity than two for loops.

fn = f"{os.path.dirname(__file__)}/in.txt"

l = util.filetointlist(fn)

ans1 = 0
for i in range(25, len(l)):
    passed = False
    for j in range(i - 25, i):
        for k in range(j + 1, i):
            if l[j] + l[k] == l[i]:
                passed = True
                break
        if passed:
            break
    if not passed:
        ans1 = l[i]
        break
print("Part 1 Solution:")
print(ans1)
ans2 = 0

for i in range(0, len(l) - 1):
    for j in range(i + 2, len(l) + 1):
        if sum(l[i:j]) == ans1:
            ans2 = min(l[i:j]) + max(l[i:j])
            break
    if ans2 != 0:
        break
print("Part 2 Solution:")
print(ans2)
