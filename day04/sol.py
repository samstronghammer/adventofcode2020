#!/usr/bin/python3
import sys
import os
sys.path.append(f"{os.path.dirname(__file__)}/..")
import util
import math
import re

# Very string-heavy day. Logistically I found parsing the passports to
# be the most interesting part, because the rest was implementing string
# validation rules.

reqfields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
eye_colors = set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])

def field_valid(field, val):
    if field == "byr" and (int(val) < 1920 or int(val) > 2002):
        return False
    elif field == "iyr" and (int(val) < 2010 or int(val) > 2020):
        return False
    elif field == "eyr" and (int(val) < 2020 or int(val) > 2030):
        return False
    elif field == "hgt":
        if val[-2:] == "cm":
            numunits = int(val[0:-2])
            if int(numunits) < 150 or int(numunits) > 193:
                return False
        elif val[-2:] == "in":
            numunits = int(val[0:-2])
            if int(numunits) < 59 or int(numunits) > 76:
                return False
        else:
            return False
    elif field == "hcl" and not re.match("^#[0-9a-f]{6}$", val):
        return False
    elif field == "ecl" and not val in eye_colors:
        return False
    elif field == "pid" and not re.match("^[0-9]{9}$", val):
        return False
    return True


fn = f"{os.path.dirname(__file__)}/in.txt"

l = util.filetolist(fn)
countp1 = 0
countp2 = 0
i = 0
while i < len(l): 
    newreq = reqfields.copy()
    valid = True
    while i < len(l) and l[i] != '':
        toks = l[i].split()
        for tok in toks:
            field, val = tok.split(":")
            valid = valid and field_valid(field, val)
            if field != "cid": 
                newreq.remove(tok[0:3])
        i += 1
    if len(newreq) == 0:
        countp1 += 1
        if valid:
            countp2 += 1
    i += 1

print("Part 1 Solution:")
print(countp1)
print("Part 2 Solution")
print(countp2)