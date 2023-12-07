import re
import sys
from functools import reduce
from itertools import repeat
from operator import add


def parse_input(puzzle_input):
    t, d = map(re.findall, repeat(r"\d+"), puzzle_input.splitlines())
    return (t, d)


def part_one(times, distances):
    count = 1
    for t, d in zip(map(int, times), map(int, distances)):
        i = 0
        while i * (t - i) <= d:
            i += 1
        count *= (t // 2 - i + 1) * 2 - (t % 2 == 0)

    return count


def part_two(times, distances):
    t, d = map(int, map(reduce, repeat(add), (times, distances)))

    lo, hi = 1, t
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if mid * (t - mid) > d:
            hi = mid - 1
        else:
            lo = mid + 1

    return (t // 2 - lo + 1) * 2 - (t % 2 == 0)


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
