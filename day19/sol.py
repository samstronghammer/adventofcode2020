#!/usr/bin/python3
import sys
import os
sys.path.append(f"{os.path.dirname(__file__)}/..")
import util
import math

# I hardly had to modify my code for part 2-- left recursion worked fine on
# the new rules I was given. This solution works well on the rules given by
# the problem, but I think it would break if any rule mapped to the empty string
# or if the loops were more complex.

def match(s, rulelist, rules):
    if len(s) == 0 or len(rulelist) == 0:
        # If the string and rulelist are both consumed, success.
        # If just one is consumed, fail.
        if len(s) == 0 and len(rulelist) == 0:
            return True
        else:
            return False
    rule = rules[rulelist[0]]
    # If the rule maps to a letter, consume the letter and the rule and recur.
    # If the letter doesn't match the first letter of the string, fail.
    if rule == "a" or rule == "b":
        if s.startswith(rule):
            return match(s[1:], rulelist[1:], rules)
        else:
            return False
    # Otherwise, if the rule maps to other rules, try replacing the first element
    # in the rulelist with the new rules.
    for newruletuple in rule:
        if match(s, list(newruletuple) + rulelist[1:], rules):
            return True
    # If no rule works, fail.
    return False

fn = f"{os.path.dirname(__file__)}/in.txt"

l = util.filetolist(fn)

rules = {}
messages = []
for line in l:
    if line.startswith("a") or line.startswith("b"):
        messages.append(line)
    elif line:
        toks = line.split()
        id = int(toks[0][0:-1])
        if toks[1] == '"a"' or toks[1] == '"b"':
            rules[id] = toks[1][1]
        else:
            ruleset = set()
            rulelist = []
            for tok in toks[1:]:
                if tok == "|":
                    ruleset.add(tuple(rulelist))
                    rulelist = []
                else:
                    rulelist.append(int(tok))
            ruleset.add(tuple(rulelist))
            rules[id] = ruleset

rules2 = rules.copy()
rules2[8] = set([(42,), (42, 8)])
rules2[11] = set([(42, 31), (42, 11, 31)])

print("Part 1 Solution:")
print(len(list(filter(lambda x: match(x, [0], rules), messages))))
print("Part 2 Solution:")
print(len(list(filter(lambda x: match(x, [0], rules2), messages))))