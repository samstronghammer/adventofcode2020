#!/usr/bin/python3
import sys
import os
sys.path.append(f"{os.path.dirname(__file__)}/..")
import util
import math

# Lots of working with strings today--combining them with masks manually then converting
# them back into numbers.

# Combine a number with a mask
def mask_num(num, mask):
    num_bits = str(bin(num))[2:]
    num_bits = ("0" * (len(mask) - len(num_bits))) + num_bits
    ans = ""
    for i in range(len(mask)):
        if mask[i] == "X":
            ans += num_bits[i]
        else:
            ans += mask[i]
    return int(ans, 2)

# Recursive helper that tries every possible combination to fill the floating bits
def mask_mem_helper(num_str):
    try:
        i = num_str.index("X")
        num_list = list(num_str)
        num_list[i] = "0"
        part0 = mask_mem_helper("".join(num_list))
        num_list[i] = "1"
        return part0 + mask_mem_helper("".join(num_list))
    except:
        return [int(num_str, 2)]
        
# Returns a list of memory locations given the original location and the mask
def mask_mem(num, mask):
    num_bits = str(bin(num))[2:]
    num_bits = ("0" * (len(mask) - len(num_bits))) + num_bits
    ans = ""
    for i in range(len(mask)):
        if mask[i] == "0":
            ans += num_bits[i]
        else:
            ans += mask[i]
    return mask_mem_helper(ans)
    

fn = f"{os.path.dirname(__file__)}/in.txt"

l = util.filetolist(fn)

mem = {}
mem2 = {}
mask = ""
for line in l:
    toks = line.split(" = ")
    if toks[0] == "mask":
        mask = toks[1]
    else:
        memloc = int(toks[0][4:-1])
        val = int(toks[1])
        # Part 1 logic
        masked = mask_num(val, mask)
        mem[memloc] = masked
        # Part 2 logic
        masked2 = mask_mem(memloc, mask)
        for loc in masked2:
            mem2[loc] = val
print("Part 1 Solution:")
print(sum(mem.values()))
print("Part 2 Solution:")
print(sum(mem2.values()))        
