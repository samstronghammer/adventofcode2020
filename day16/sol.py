#!/usr/bin/python3
import sys
import os
sys.path.append(f"{os.path.dirname(__file__)}/..")
import util
import math
import parse
from parse import compile
from functools import reduce

# Cool problem. Coming up with an algorithm for part 2 was fun.

def in_range(n, r):
    return r[0] <= n <= r[1]

# Returns total value of invalid ticket fields
def ticket_invalid_sum(ticket, fields):
    total = 0
    for num in ticket:
        passed = False
        for rpair in fields.values():
            if in_range(num, rpair[0]) or in_range(num, rpair[1]):
                passed = True
                break
        if not passed:
            total += num
    return total

fn = f"{os.path.dirname(__file__)}/in.txt"

l = util.filetolist(fn)

p = compile("{}: {:d}-{:d} or {:d}-{:d}")
tickets = []
fields = {}
for line in l:
    r = p.parse(line)
    if r:
        fields[r[0]] = ((r[1], r[2]), (r[3], r[4]))
    else:
        toks = line.split(",")
        if len(toks) > 1:
            tickets.append(list(map(lambda x: int(x), toks)))

myticket = tickets[0]
    
print("Part 1 Solution:")
print(sum(map(lambda x: ticket_invalid_sum(x, fields), tickets)))

tickets = list(filter(lambda x: ticket_invalid_sum(x, fields) == 0, tickets))
tickets.append(myticket)

# opts represents all remaining field possibilities for each location on the ticket
opts = [set(fields.keys()) for field in fields]
# sols is a map from field names to indices
sols = {}
progress = True
while progress:
    progress = False
    # Iterate over each ticket, eliminating opt possibilities
    for t in tickets:
        for i, num in enumerate(t):
            oldopts = opts[i].copy()
            for opt in oldopts:
                two_ranges = fields[opt]
                # If the ticket field value doesn't fit the given opt, or if the opt is already found to be
                # solved remove the opt from opts.
                if (not in_range(num, two_ranges[0]) and not in_range(num, two_ranges[1])) or opt in sols:
                    opts[i].remove(opt)
                    progress = True
                    # If there is only one opt left, it is the answer. Add it to the solution.
                    if len(opts[i]) == 1:
                        sol = opts[i].pop()
                        sols[sol] = i
                        break

print("Part 2 Solution:")
# Multiplies together all items that start with "departure"
print(reduce(lambda acc, item: acc * (myticket[item[1]] if item[0].startswith("departure") else 1), sols.items(), 1))
