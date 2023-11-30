import sys


def parse_input(puzzle_input):
    return (puzzle_input,)


def part_one(parsed_input):
    return 0


def part_two(parsed_input):
    return 0


class Test:
    example = """\
"""

    def test_one(self):
        assert part_one(*parse_input(self.example)) == 0

    def test_two(self):
        assert part_two(*parse_input(self.example)) == 0


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    sys.exit(main())
