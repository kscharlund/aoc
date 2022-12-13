import sys
from pprint import pprint
import math
import re
from copy import copy


def parse_input():
    foods = []
    for line in sys.stdin:
        match = re.match(r'(.*) \(contains ([^)]+)\)', line)
        ingredients = set(match.group(1).split())
        allergens = match.group(2).split(', ')
        foods.append((ingredients, allergens))
    return foods


def a(foods):
    pprint(foods)

    allergen_foods = {}
    for ii, food in enumerate(foods):
        for allergen in food[1]:
            allergen_foods.setdefault(allergen, []).append(ii)

    allergen_ingredients = {}
    for allergen, food_ids in allergen_foods.items():
        common_ingredients = None
        for ii in food_ids:
            if common_ingredients is None:
                common_ingredients = set(foods[ii][0])
            else:
                common_ingredients &= foods[ii][0]
        allergen_ingredients[allergen] = common_ingredients
    all_allergen_ingredients = set()
    for ingredients in allergen_ingredients.values():
        all_allergen_ingredients |= ingredients

    all_ingredients = set()
    for food in foods:
        all_ingredients |= food[0]

    non_allergen_ingredients = all_ingredients - all_allergen_ingredients
    count = 0
    for ingredient in non_allergen_ingredients:
        for food in foods:
            if ingredient in food[0]:
                count += 1
    print(count)
    return allergen_ingredients


def b(allergen_ingredients):
    pprint(allergen_ingredients)
    decided = {a for a, i in allergen_ingredients.items() if len(i) == 1}
    undecided = set(allergen_ingredients.keys()) - decided
    while undecided:
        for ii in decided:
            for jj in undecided:
                allergen_ingredients[jj] -= allergen_ingredients[ii]
        decided = {a for a, i in allergen_ingredients.items() if len(i) == 1}
        undecided = set(allergen_ingredients.keys()) - decided
        pprint(allergen_ingredients)
    ingredients = [allergen_ingredients[a].pop() for a in sorted(allergen_ingredients)]
    print(','.join(ingredients))


def main():
    foods = parse_input()
    allergen_ingredients = a(foods)
    print()
    b(allergen_ingredients)


if __name__ == '__main__':
    main()
