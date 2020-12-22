#!/usr/bin/python3
import sys
import os
sys.path.append(f"{os.path.dirname(__file__)}/..")
import util
import math

# Implementation of the classic "war" card game with a recursive
# twist at the end. Very fun :) For part 1 and 2 I used lists
# where the end of the list is the top of the deck. It seemed
# easier.

def deck_score(deck):
    ans = 0
    for i, val in enumerate(deck):
        ans += ((i + 1) * val)
    return ans

def combat(p1_original_deck, p2_original_deck):
    p1_deck = p1_original_deck.copy()
    p2_deck = p2_original_deck.copy()
    while len(p1_deck) > 0 and len(p2_deck) > 0:
        top_p1 = p1_deck.pop()
        top_p2 = p2_deck.pop()
        if top_p1 > top_p2:
            p1_deck = [top_p2, top_p1] + p1_deck
        else:
            p2_deck = [top_p1, top_p2] + p2_deck
    return deck_score(p1_deck if len(p1_deck) > 0 else p2_deck)

# Returns a pair of values. A boolean representing the winner (T => p1 and F => p2)
# and the deck score of the winner.
def recursive_combat(p1_original_deck, p2_original_deck):
    p1_deck = p1_original_deck.copy()
    p2_deck = p2_original_deck.copy()
    prev_states = set()
    while True:
        # End conditions
        if len(p1_deck) == 0:
            return False, deck_score(p2_deck)
        if len(p2_deck) == 0:
            return True, deck_score(p1_deck)
        game_state = (tuple(p1_deck), tuple(p2_deck))
        if game_state in prev_states:
            return True, deck_score(p1_deck)
        # If didn't terminate, add to set of game states
        prev_states.add(game_state)

        top_p1 = p1_deck.pop()
        top_p2 = p2_deck.pop()
        winner = False
        if top_p1 <= len(p1_deck) and top_p2 <= len(p2_deck):
            winner = recursive_combat(p1_deck[-top_p1:], p2_deck[-top_p2:])[0]
        else:
            winner = top_p1 > top_p2
        if winner:
            p1_deck = [top_p2, top_p1] + p1_deck
        else:
            p2_deck = [top_p1, top_p2] + p2_deck

fn = f"{os.path.dirname(__file__)}/in.txt"

l = util.filetolist(fn)

p1 = []
p2 = []

on_p1 = True
for line in l:
    if line:
        try:
            val = int(line)
            if on_p1:
                p1.insert(0, val)
            else:
                p2.insert(0, val)
        except:
            pass
    else:
        on_p1 = not on_p1

print("Part 1 Solution:")
print(combat(p1, p2))

print("Part 2 Solution:")
print(recursive_combat(p1, p2)[1])
