import math
import re
import sys
from collections import defaultdict


def parse_input(puzzle_input):
    bags = []
    for line in puzzle_input.splitlines():
        maximums = defaultdict(int)
        for n, c in re.findall(r"(\d+) (\w+)", line):
            maximums[c] = max(maximums[c], int(n))

        bags.append(maximums)

    return (bags,)


def part_one(bags):
    return sum(
        i + 1
        for i, d in enumerate(bags)
        if d["red"] < 13 and d["green"] < 14 and d["blue"] < 15
    )


def part_two(bags):
    return sum(math.prod(bag.values()) for bag in bags)


class Test:
    example = """\
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

    def test_one(self):
        assert part_one(*parse_input(self.example)) == 8

    def test_two(self):
        assert part_two(*parse_input(self.example)) == 2286


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    sys.exit(main())
