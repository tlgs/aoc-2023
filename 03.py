import re
import sys
from collections import defaultdict


def adjacent(start, end, y):
    yield start - 1, y
    yield end, y

    for x in range(start - 1, end + 1):
        yield x, y - 1
        yield x, y + 1


def parse_input(puzzle_input):
    numbers, symbols = defaultdict(list), {}
    for y, row in enumerate(puzzle_input.splitlines()):
        for m in re.finditer(r"(\d+)", row):
            for a in adjacent(*m.span(), y):
                numbers[a].append(int(m.group()))

        for m in re.finditer(r"([^\d\.])", row):
            symbols[m.start(), y] = m.group()

    return numbers, symbols


def part_one(numbers, symbols):
    matches = numbers.keys() & symbols.keys()
    return sum(sum(numbers[k]) for k in matches)


def part_two(numbers, symbols):
    two = {k for k, v in numbers.items() if len(v) == 2}
    stars = {k for k, v in symbols.items() if v == "*"}
    return sum(numbers[k][0] * numbers[k][1] for k in two & stars)


class Test:
    example = """\
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

    def test_one(self):
        assert part_one(*parse_input(self.example)) == 4361

    def test_two(self):
        assert part_two(*parse_input(self.example)) == 467835


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    sys.exit(main())
