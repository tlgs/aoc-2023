import sys


def parse_input(puzzle_input):
    raw = puzzle_input.split("\n\n")
    patterns = [pattern.split() for pattern in raw]
    return (patterns,)


def f(pattern, target=0):
    for i, _ in enumerate(pattern[1:], start=1):
        diff = sum(
            a != b
            for up, down in zip(pattern[i - 1 :: -1], pattern[i:])
            for a, b in zip(up, down)
        )
        if diff == target:
            return i

    return 0


def part_one(patterns):
    return sum(100 * f(pat) + f([*zip(*pat)]) for pat in patterns)


def part_two(patterns):
    return sum(100 * f(pat, 1) + f([*zip(*pat)], 1) for pat in patterns)


class Test:
    example = """\
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""

    def test_one(self):
        assert part_one(*parse_input(self.example)) == 405

    def test_two(self):
        assert part_two(*parse_input(self.example)) == 400


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    sys.exit(main())
