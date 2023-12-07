import math
import re
import sys


def parse_input(puzzle_input):
    fst, snd = puzzle_input.splitlines()
    t, d = re.findall(r"\d+", fst), re.findall(r"\d+", snd)
    return (t, d)


def root_diff(a, b, c):
    x = (-b + (b**2 - 4 * a * c) ** 0.5) / (2 * a)
    y = (-b - (b**2 - 4 * a * c) ** 0.5) / (2 * a)
    return math.ceil(x) - math.floor(y) - 1


def part_one(times, distances):
    count = 1
    for t, d in zip(times, distances):
        count *= root_diff(1, -int(t), int(d))

    return count


def part_two(times, distances):
    t, d = "".join(times), "".join(distances)
    return root_diff(1, -int(t), int(d))


class Test:
    example = """\
Time:      7  15   30
Distance:  9  40  200
"""

    def test_one(self):
        assert part_one(*parse_input(self.example)) == 288

    def test_two(self):
        assert part_two(*parse_input(self.example)) == 71503


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    sys.exit(main())
