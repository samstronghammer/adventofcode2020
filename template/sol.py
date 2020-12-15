#!/usr/bin/python3
import sys
import os
sys.path.append(f"{os.path.dirname(__file__)}/..")
import util
import math
import parse
from parse import compile

fn = f"{os.path.dirname(__file__)}/in.txt"

l = util.filetolist(fn)

p = compile("")
for line in l:
    r = p.parse(line)
    print(r.fixed)
