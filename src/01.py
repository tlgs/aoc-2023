import functools
import sys


def parse_input(puzzle_input):
    return (puzzle_input.splitlines(),)


def part_one(parsed_input):
    total = 0
    for line in parsed_input:
        raw = [int(c) for c in line if c.isdigit()]
        total += raw[0] * 10 + raw[-1]

    return total


def part_two(parsed_input):
    pairs = [
        ("one", "o1e"),
        ("two", "t2o"),
        ("three", "t3e"),
        ("four", "4"),
        ("five", "5e"),
        ("six", "6"),
        ("seven", "7"),
        ("eight", "e8t"),
        ("nine", "n9e"),
    ]
    mangled = [
        functools.reduce(lambda x, y: x.replace(*y), pairs, line)
        for line in parsed_input
    ]
    return part_one(mangled)


class Test:
    example = """\
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

    example2 = """\
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

    def test_one(self):
        assert part_one(*parse_input(self.example)) == 142

    def test_two(self):
        assert part_two(*parse_input(self.example2)) == 281


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    sys.exit(main())
