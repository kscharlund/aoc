import sys
from pprint import pprint
import math


def parse_game(line: str):
    name, rest = line.split(": ")
    game_id = int(name.split()[-1])
    cube_sets = []
    for draw in rest.split("; "):
        d = {}
        for cubes in draw.split(", "):
            count, color = cubes.split()
            d[color] = int(count)
        cube_sets.append(d)
    return (game_id, cube_sets)


def get_data():
    return [parse_game(line) for line in open(sys.argv[1])]


def possible(cube_sets):
    for cube_set in cube_sets:
        if cube_set.get("red", 0) > 12:
            return False
        if cube_set.get("green", 0) > 13:
            return False
        if cube_set.get("blue", 0) > 14:
            return False
    return True


def a(data):
    print(sum(game_id for game_id, cube_sets in data if possible(cube_sets)))


def needed_cubes(cube_sets):
    needed = {"red": 0, "green": 0, "blue": 0}
    for cube_set in cube_sets:
        for color in cube_set:
            needed[color] = max(needed[color], cube_set[color])
    return needed


def b(data):
    print(sum(math.prod(needed_cubes(cube_sets).values()) for _, cube_sets in data))


def main():
    data = get_data()
    a(data)
    print()
    b(data)


if __name__ == "__main__":
    main()
