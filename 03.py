import re
import sys
from collections import defaultdict


def parse_input(puzzle_input):
    edges, symbols = defaultdict(list), {}
    for y, row in enumerate(puzzle_input.splitlines()):
        for m in re.finditer(r"\d+", row):
            number = int(m.group())

            start, end = m.span()
            edges[start - 1, y].append(number)
            edges[end, y].append(number)
            for x in range(start - 1, end + 1):
                edges[x, y - 1].append(number)
                edges[x, y + 1].append(number)

        for m in re.finditer(r"[^\d\.]", row):
            symbols[m.start(), y] = m.group()

    return edges, symbols


def part_one(edges, symbols):
    matches = edges.keys() & symbols.keys()
    return sum(sum(edges[k]) for k in matches)


def part_two(edges, symbols):
    two = {k for k, v in edges.items() if len(v) == 2}
    stars = {k for k, v in symbols.items() if v == "*"}
    return sum(edges[k][0] * edges[k][1] for k in two & stars)


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
