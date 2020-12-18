#!/usr/bin/python3.9
import sys
import os
sys.path.append(f"{os.path.dirname(__file__)}/..")
import util
import math
import arithmetic_parsing
import json

# The arithmetic_parsing package is very new and doesn't have much documentation yet. 
# I got very stuck on some of the intricacies of how the object produced by arithmetic_parsing
# is structured.

# Applies the given func to the expression
def apply_func(expr, op_func, parse_func):
    op_string = list(expr.keys())[0]
    return op_func(parse_func(expr[op_string]["children"][0]), parse_func(expr[op_string]["children"][1]))

# Parses tree given by arithmetic_parsing
def parse_expr(expr):
    try:
        val = int(expr)
        return val
    except:
        if "+" in expr:
            return apply_func(expr, lambda x, y: x + y, parse_expr)
        elif "*" in expr:
            return apply_func(expr, lambda x, y: x * y, parse_expr)
        else:
            print("Uh oh")

fn = f"{os.path.dirname(__file__)}/in.txt"

l = util.filetolist(fn)

parser = arithmetic_parsing.Parser()

total = 0
total2 = 0
for line in l:
    # Reverse the string to help the parser construct the tree in a left-to-right order.
    # Also change * into - to have the parser treat it with the same precedence as +
    newline = line.replace("*", "-")[::-1].replace("(", "<").replace(")", "(").replace("<", ")")
    # After parsing the string, change the - back to *.
    parsed = json.loads(parser.parse(newline).as_json().replace("-", "*"))
    ans = parse_expr(parsed["base"]["children"][0])
    total += ans
    
    # Swap the * and + operations so the parser treats their precedence as swapped
    newline2 = line.replace("*", "-").replace("+", "*").replace("-", "+")    
    # Swap the operators back to make parse_expr work
    parsed2 = json.loads(parser.parse(newline2).as_json().replace("*", "-").replace("+", "*").replace("-", "+"))
    ans2 = parse_expr(parsed2["base"]["children"][0])
    total2 += ans2

print("Part 1 Solution:")
print(total)
print("Part 2 Solution")
print(total2)