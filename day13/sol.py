#!/usr/bin/python3
import sys
import os
sys.path.append(f"{os.path.dirname(__file__)}/..")
import util
import math
from functools import reduce

# Interesting problem today. Part 1 requires taking the departure time modulo 
# the bus ID and inverting it (bus ID - the modulo result). Part 2 needs the 
# Chinese Remainder Theorem to solve the system of modular equations that are 
# created by the problem's constraints.

# Used Chinese Remainder Theorem solver from https://rosettacode.org/wiki/Chinese_remainder_theorem#Python

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

fn = f"{os.path.dirname(__file__)}/in.txt"

l = util.filetolist(fn)

timestamp = int(l[0])
ids = list(map(lambda x: x if x == "x" else int(x), l[1].split(",")))
inservice = list(filter(lambda x: x != "x", ids))

# Determine the wait time for the given busid.
def wait_time(busid, timestamp):
    remainder = timestamp % busid
    return remainder if remainder == 0 else busid - remainder

# Map each bus to a tuple containing the wait time then find the tuple with the minimum
# wait time.
ans = min(map(lambda x: (x, wait_time(x, timestamp)), inservice), key=lambda x: x[1])
print("Part 1 Solution:")
print(ans[0] * ans[1])

# Each bus constraint can be written in the following form:
# t_ans + bus_index mod bus_id = 0
# This can be rearranged to be of the form:
# t_ans = -1 * bus_index mod bus_id
# Systems of equations of this form can be solved using the Chinese Remainder Theorem.
# This CRT functions accepts two lists, one of the remainders and one of the modulo bases, 
# and solves for t_ans.
intids = list(map(lambda x: x if x == "x" else int(x), ids))
n = []
a = []
for i in range(len(intids)):
    if intids[i] != "x":
        a.append(i * -1)
        n.append(intids[i])
print("Part 2 Solution:")
print(chinese_remainder(n, a))
