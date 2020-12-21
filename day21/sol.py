#!/usr/bin/python3
import sys
import os
sys.path.append(f"{os.path.dirname(__file__)}/..")
import util
import math

fn = f"{os.path.dirname(__file__)}/in.txt"

l = util.filetolist(fn)

recipes = []
all_ingredients = set()
all_allergens = set()

# Parse out sets of allergens and ingredients
for line in l:
    toks = line.split(" (contains ")
    ingredients = set(toks[0].split())
    allergens = toks[1].split(", ")
    # Remove trailing ")"
    allergens[-1] = allergens[-1][:-1]
    allergens = set(allergens)
    all_ingredients.update(ingredients)
    all_allergens.update(allergens)
    recipes.append((ingredients, allergens))

# Set up map from each allergen to possible ingredients that they correspond to (starting with a set containing all ingredients)
allergen_possibilities = {}
for allergen in all_allergens:
    allergen_possibilities[allergen] = all_ingredients.copy()

# Every time an allergen is listed in a recipe, it must correspond to one of the ingredients of the recipe. So,
# the allergen's possibilities are intersected with the ingredients in the recipe.
for recipe in recipes:
    for allergen in recipe[1]:
        allergen_possibilities[allergen] = allergen_possibilities[allergen].intersection(recipe[0])

# Create a set of all possible allergens
maybe_allergen = set()
for val in allergen_possibilities.values():
    maybe_allergen.update(val)

# Iterate through each recipe, counting the ingredients that are definitely not allergens
not_allergens = 0
for recipe in recipes:
    for ingredient in recipe[0]:
        if not ingredient in maybe_allergen:
            not_allergens += 1

print("Part 1 Solution:")
print(not_allergens)

# Iterate until all allergens have been resolved. 
progress = True
allergen_solutions = {}
while progress:
    progress = False
    for allergen, possibilities in allergen_possibilities.items():
        # If there's only one possible solution, record it.
        if len(possibilities) == 1:
            allergen_solutions[allergen] = possibilities.pop()
            progress = True
        else:
            # If there's more than one possible solution, see if any possibilities can be eliminated
            # by examining the solved allergens.
            for sol in allergen_solutions.values():
                if sol in possibilities:
                    progress = True
                    possibilities.remove(sol)

print("Part 2 Solution:")
print(",".join(list(map(lambda x: allergen_solutions[x], sorted(list(all_allergens))))))
