#!/usr/bin/python3
import sys
import os
sys.path.append(f"{os.path.dirname(__file__)}/..")
import util
import math

fn = f"{os.path.dirname(__file__)}/in.txt"

# 

l = util.filetolist(fn)
numvalid = 0
numvalid2 = 0
for i in range(len(l)):
    toks = l[i].split()
    minval = int(toks[0].split("-")[0])
    maxval = int(toks[0].split("-")[1])
    char = toks[1][0]
    pword = toks[2]
    count = pword.count(char)
    if count <= maxval and count >= minval:
        numvalid = numvalid + 1
    if (pword[minval - 1] == char) != (pword[maxval - 1] == char):
        numvalid2 = numvalid2 + 1
print("Part 1 Solution:")
print(numvalid)
print("Part 2 Solution:")
print(numvalid2)