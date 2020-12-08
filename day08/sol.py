#!/usr/bin/python3
import sys
import os
sys.path.append(f"{os.path.dirname(__file__)}/..")
import util
import math

# The first of the "simulate a computer" problems of the year :)

fn = f"{os.path.dirname(__file__)}/in.txt"

# Returns a tuple, (<did it terminate?>, <what was the acc value?>)
def get_output(ops):
    acc = 0
    i = 0
    iset = set()
    while True:
        iset.add(i)
        inst = ops[i]
        if inst[0] == "acc":
            acc += inst[1]
            i += 1
        elif inst[0] == "nop":
            i += 1
        else:
            i += inst[1]
        if i in iset:
            return (False, acc)
        if i >= len(ops) or i < 0:
            return (True, acc)

def flip_index(ops, i):
    assert ops[i][0] != "acc"
    if ops[i][0] == "jmp":
        ops[i] = ("nop", ops[i][1])
    else:
        ops[i] = ("jmp", ops[i][1])

l = util.filetolist(fn)

ops = []
for line in l:
    toks = line.split()
    ops.append((toks[0], int(toks[1])))

output = get_output(ops)
print("Part 1 Solution:")
print(output[1])
print("Part 2 Solution:")

# try flipping every instruction that isn't an "acc". If it terminates, terminate.
for i in range(len(ops)):
    if ops[i][0] != "acc":
        flip_index(ops, i)
        output = get_output(ops)
        if output[0]:
            print(output[1])
            break
        flip_index(ops, i)
