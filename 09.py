import sys
from functools import reduce
from itertools import pairwise


def parse_input(puzzle_input):
    histories = []
    for line in puzzle_input.splitlines():
        values = list(map(int, line.split()))
        histories.append(values)

    return (histories,)


def part_one(histories):
    total = 0
    for values in histories:
        diffs, stack = values[:], [values[-1]]
        while sum(diffs := [b - a for a, b in pairwise(diffs)]) != 0:
            stack.append(diffs[-1])

        total += sum(stack)

    return total


def part_two(histories):
    total = 0
    for values in histories:
        diffs, stack = values[:], [values[0]]
        while sum(diffs := [b - a for a, b in pairwise(diffs)]) != 0:
            stack.append(diffs[0])

        total += reduce(lambda a, b: b - a, stack[::-1])

    return total


class Test:
    example = """\
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""

    def test_one(self):
        assert part_one(*parse_input(self.example)) == 114

    def test_two(self):
        assert part_two(*parse_input(self.example)) == 2


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    sys.exit(main())
