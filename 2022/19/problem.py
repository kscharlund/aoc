from dataclasses import dataclass
from functools import cache, reduce
import re
import sys
from pprint import pprint
import math


ROBOT_TYPES = 4
BLUEPRINT_PATTERN = re.compile(
    r"Blueprint \d+: Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian."
)


@dataclass(frozen=True)
class Int4:
    vals: tuple[int, int, int, int]

    def __add__(self, other):
        return Int4(tuple(self[i] + other[i] for i in range(4)))

    def __getitem__(self, i):
        return self.vals[i]

    def __len__(self):
        return 4

    def __sub__(self, other):
        return Int4(tuple(self[i] - other[i] for i in range(4)))

    def max(self, other):
        return Int4(tuple(max(self[i], other[i]) for i in range(4)))

    def min(self, other):
        return Int4(tuple(min(self[i], other[i]) for i in range(4)))


def parse_blueprint(line):
    ore_ore, clay_ore, obs_ore, obs_clay, geo_ore, geo_obs = BLUEPRINT_PATTERN.match(
        line
    ).groups()
    return (
        Int4((int(ore_ore), 0, 0, 0)),
        Int4((int(clay_ore), 0, 0, 0)),
        Int4((int(obs_ore), int(obs_clay), 0, 0)),
        Int4((int(geo_ore), 0, int(geo_obs), 0)),
    )


def get_data():
    return [parse_blueprint(line) for line in open(sys.argv[1])]


@cache
def geodes_mined(robots, resources, time):
    if time == 1:
        return resources[-1] + robots[-1]

    max_cost = reduce(lambda x, y: x.max(y), blueprint)
    max_cost = Int4((max_cost[0] * 2, max_cost[1] * 2, max_cost[2] * 2, 100))
    new_resources = resources + robots
    res = []
    for ri in reversed(range(ROBOT_TYPES)):
        cost = blueprint[ri]
        if all(r >= 0 for r in resources - cost):
            new_robot = Int4(tuple(1 if i == ri else 0 for i in range(ROBOT_TYPES)))
            res.append(
                geodes_mined(
                    robots + new_robot,
                    max_cost.min(new_resources - cost),
                    time - 1,
                )
            )
    res.append(
        geodes_mined(
            robots,
            max_cost.min(new_resources),
            time - 1,
        )
    )
    return max(res)


def a(data):
    global blueprint
    ore_robot = Int4((1, 0, 0, 0))
    no_resources = Int4((0, 0, 0, 0))
    for blueprint in data:
        print(geodes_mined(ore_robot, no_resources, 24))
        geodes_mined.cache_clear()


def b(data):
    global blueprint
    ore_robot = Int4((1, 0, 0, 0))
    no_resources = Int4((0, 0, 0, 0))
    for blueprint in data[:3]:
        print(geodes_mined(ore_robot, no_resources, 32))
        geodes_mined.cache_clear()


def main():
    data = get_data()
    a(data)
    print()
    b(data)


if __name__ == "__main__":
    main()
