import sys


def parse_input(puzzle_input):
    return (puzzle_input.splitlines(),)


def part_one(parsed_input):
    values = []
    for line in parsed_input:
        raw_ints = list(filter(str.isdigit, line))
        values.append(int(raw_ints[0] + raw_ints[-1]))
    return sum(values)


def part_two(parsed_input):
    spelled = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    values = []
    for line in parsed_input:
        raw_ints = []
        for i, c in enumerate(line):
            for k in spelled:
                if line[i:].startswith(k):
                    raw_ints.append(spelled[k])
                    break

            if c.isdigit():
                raw_ints.append(c)

        values.append(int(raw_ints[0] + raw_ints[-1]))

    return sum(values)


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
