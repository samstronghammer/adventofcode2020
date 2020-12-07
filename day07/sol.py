#!/usr/bin/python3
import sys
import os
sys.path.append(f"{os.path.dirname(__file__)}/..")
import util
import math

# Excellent puzzle! I really enjoyed cleaning up my solution after rushing one out.
# Part 1 required marking every bag as a solution or not a solution, expanding
# out from bags that contained the shiny gold bag and bags that contained no bags, 
# respectively. Part 2 lent itself well to a recursive function which found the 
# number of bags an arbitrary bag contained and using empty bags as the base case.

fn = f"{os.path.dirname(__file__)}/in.txt"

l = util.filetolist(fn)
bags = {}
for line in l:
    toks = line.split(" bags contain ") # [<color>, <... list of bags>]
    color = toks[0]
    inner = {}
    if toks[1] != "no other bags.":
        # remove period and split inner bags from each other
        toks2 = toks[1][0:-1].split(", ") # [<x color bag(s)>, <y color bag(s)>, ...]
        # parse each inner bag
        for t in toks2:
            toks3 = t.split() # [<n>, <color part 1>, <color part 2>, bag(s)]
            num = int(toks3[0])
            inner_color = " ".join(toks3[1:-1])
            inner[inner_color] = num
    bags[color] = inner

# Resulting bags dictionary example: 
# {"red": {"purple": 2}, "yellow": {}, "green": {"red": 7, "yellow": 1}, "purple": {}}

sols = set()
nsols = set()
# Iterate until no further progress can be made. Progress is made
# whenever a bag is classified as a solution or not a solution
# during an iteration.
done = False
while not done:
    done = True
    for color in bags:
        # Skip bags that are categorized already
        if not color in sols and not color in nsols:
            # If the bag has no inner bags or all of the inner bags are not 
            # solutions, then this bag is not a solution.
            if len(bags[color]) == 0 or all(map(lambda x: x in nsols, bags[color].keys())):
                done = False
                nsols.add(color)
            else:
                # If the bag contains a shiny gold bag or contains a solution,
                # it is a solution.
                if any(map(lambda x: x in sols or x == "shiny gold", bags[color].keys())):
                    sols.add(color)
                    done = False
print("Part 1 Solution:")
print(len(sols))

# Counts the number of bags contained by the given color.
def num_bags(color):
    num = 0
    for c in bags[color]:
        num += bags[color][c] * (num_bags(c) + 1)
    return num

print("Part 2 Solution:")
print(num_bags("shiny gold"))



