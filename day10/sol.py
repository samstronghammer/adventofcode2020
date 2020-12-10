#!/usr/bin/python3
import sys
import os
sys.path.append(f"{os.path.dirname(__file__)}/..")
import util
import math

# Part 1 had a LOT of words to describe a fairly simple problem:
# counting the differences between values in a sorted list. Part 2
# was an interesting memoization problem-- it made me think of the 
# classic Fibonacci function.

fn = f"{os.path.dirname(__file__)}/in.txt"

l = util.filetointlist(fn)

l.sort()
l.append(l[-1] + 3)
l.insert(0, 0)
diffs = {1: 0, 2: 0, 3: 0}
for i in range(0, len(l) - 1):
    diff = l[i + 1] - l[i]
    diffs[diff] += 1
print("Part 1 Solution:")
print(diffs[1] * diffs[3])

ans = {}
def num_ways(i):
    if i in ans:
        return ans[i]
    else:
        if len(l) - i == 1:
            return 1
        total = 0
        j = i + 1
        while j < len(l) and l[j] <= l[i] + 3:
            total += num_ways(j)
            j += 1
        ans[i] = total
        return total

print("Part 2 Solution:")
print(num_ways(0))
