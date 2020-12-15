#!/usr/bin/python3
import sys
import os
sys.path.append(f"{os.path.dirname(__file__)}/..")
import util
import math
import parse
from parse import compile

# Cool problem today, definitely a brain teaser. Coming up with these 20-odd lines of code
# took me a bit, but I'm satisfied with how concise it is. The trick is to realize that remembering
# only one index per number is necessary: the difference is *always* between i-1 and the stored
# index when the number has been said before.

def solve(starting_numbers, ans_index):
    mem = {}
    for i, n in enumerate(starting_numbers[0:-1]):
        mem[n] = i
    prev = starting_numbers[-1]
    for i in range(len(starting_numbers), ans_index):
        if prev in mem:
            curr = (i - 1) - mem[prev]
        else:
            curr = 0
        mem[prev] = i - 1
        prev = curr
    return prev

fn = f"{os.path.dirname(__file__)}/in.txt"

l = util.filetolist(fn)
starting_numbers = list(map(lambda x: int(x), l[0].split(",")))

print("Part 1 Solution:")
print(solve(starting_numbers, 2020))
print("Part 2 Solution:")
print(solve(starting_numbers, 30000000))
