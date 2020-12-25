#!/usr/bin/python3
import sys
import os
sys.path.append(f"{os.path.dirname(__file__)}/..")
import util

# Last day! The solution is to brute-force the loop size
# for one of the public keys and apply it to the other
# public key.

def transform(subj_num, loop_size):
    return pow(subj_num, loop_size, 20201227)

def num_transforms(public_key):
    val = 1
    loop_size = 0
    while True:
        if val == public_key:
            return loop_size
        loop_size += 1
        val = val * 7 % 20201227

fn = f"{os.path.dirname(__file__)}/in.txt"

l = util.filetointlist(fn)

print("Part 1 Solution:")
print(transform(l[1], num_transforms(l[0])))

print("Part 2 Solution:")
print("N/A")