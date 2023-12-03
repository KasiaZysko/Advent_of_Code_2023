from collections import defaultdict
from functools import reduce
from aocd.models import Puzzle

"""
Remember to add AOC_SESSION as an environment variable. It is a cookie from AOC website called session..
"""


def get_puzzle():
    puzzle = Puzzle(year=2023, day=2)
    data = puzzle.input_data
    return data


def part_1():
    puzzle_lines = get_puzzle().splitlines()
    cube_limits = {'red': 12, 'green': 13, 'blue': 14}

    valid_sums = sum(
        game_id
        for line in puzzle_lines
        if all(
            all(
                int(cube.split()[0]) <= cube_limits[cube.split()[1]]
                for cube in game_values.split(", ")
            )
            for game_values in line.split(": ")[1].split("; ")
        )
        for game_id in [int(line.split(": ")[0].split()[1])]
    )

    return valid_sums


def part_2():
    puzzle_lines = get_puzzle().splitlines()
    product_list = []
    for _, line in enumerate(puzzle_lines):
        print(line)
        key, values_str = line.split(": ")
        cubes = [cube for game in values_str.split("; ") for cube in [cube.split() for cube in game.split(", ")]]
        cube_limits = defaultdict(int)

        for count, color in cubes:
            cube_limits[color] = max(cube_limits[color], int(count))

        product = reduce(lambda x, y: x * y, map(int, cube_limits.values()), 1)
        product_list.append(product)

    return sum(product_list)


print(f"Answer for part 1 is {part_1()}")
print(f"Answer for part 2 is {part_2()}")
