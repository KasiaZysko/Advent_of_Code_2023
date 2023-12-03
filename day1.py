import re
from aocd.models import Puzzle

"""
Remember to add AOC_SESSION as an environment variable. It is a cookie from AOC website called session..
"""


def get_puzzle():
    puzzle = Puzzle(year=2023, day=1)
    data = puzzle.input_data
    return data


def replace_text_numbers(text):
    number_mapping = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }
    sorted_mapping = sorted(number_mapping.items(), key=lambda x: text.find(x[0]))
    # Replace words with digits
    for word, digit in sorted_mapping:
        text = text.replace(word, digit + word)
    return text


def part_1(puzzle_value):
    puzzle_value = [re.sub(r'[^0-9]', '', line) for line in puzzle_value.splitlines()]
    values = [int(line[0] + line[-1]) for line in puzzle_value]
    return sum(values)


def part_2(puzzle_value):
    puzzle_value = [replace_text_numbers(text) for text in puzzle_value.splitlines()]
    puzzle_value = [re.sub(r'[^0-9]', '', line) for line in puzzle_value]
    values = [int(line[0] + line[-1]) for line in puzzle_value]
    return sum(values)


print(f"Answer for part 1 is {part_1(get_puzzle())}")
print(f"Answer for part 2 is {part_2(get_puzzle())}")

