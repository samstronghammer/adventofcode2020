#!/usr/bin/python3
import sys
import os
sys.path.append(f"{os.path.dirname(__file__)}/..")
import util
import math

def play_cups(input_string, num_cups, num_iterations):
    l = list(map(lambda x: int(x), list(input_string)))
    # Create dictionary mapping from cup value to next cup value
    cups = {}
    prev_val = None
    for i in range(num_cups):
        val = l[i] if i < len(l) else i + 1
        cups[val] = None
        if prev_val:
            cups[prev_val] = val
        prev_val = val
    cups[prev_val] = l[0]

    current_cup = l[0]
    for _ in range(num_iterations):
        # Remove 3 cups following current value
        removed_cups = []
        next_cup = cups[current_cup]
        for _ in range(3):
            removed_cups.append(next_cup)
            next_cup = cups[next_cup]
            del cups[removed_cups[-1]]
        cups[current_cup] = next_cup
        # Determine label of destination
        dest_label = current_cup - 1
        while not dest_label in cups:
            dest_label -= 1
            if dest_label < 1:
                dest_label = num_cups
        # Put 3 removed cups back in
        end = cups[dest_label]
        next_cup = dest_label
        for label in removed_cups:
            cups[next_cup] = label
            next_cup = label
        cups[next_cup] = end
        # Set new current cup value
        current_cup = cups[current_cup]
    return cups

fn = f"{os.path.dirname(__file__)}/in.txt"
input_string = util.filetolist(fn)[0]

cups = play_cups(input_string, 9, 100)
ans = ""
current_cup = cups[1]
while current_cup != 1:
    ans += str(current_cup)
    current_cup = cups[current_cup]

print("Part 1 Solution:")
print(ans)

cups = play_cups(input_string, 1_000_000, 10_000_000)
print("Part 2 Solution:")
print(cups[1] * cups[cups[1]])

