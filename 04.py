import sys
from functools import cache


def parse_input(puzzle_input):
    cards = []
    for line in puzzle_input.splitlines():
        _, rest = line.split(": ")
        fst, snd = rest.split(" | ")
        winning = {int(n) for n in fst.split()}
        numbers = {int(n) for n in snd.split()}

        cards.append((winning, numbers))

    return (cards,)


def part_one(cards):
    return sum(2 ** (n - 1) for a, b in cards if (n := len(a & b)))


def part_two(cards):
    w = {i: list(range(i + 1, i + 1 + len(a & b))) for i, (a, b) in enumerate(cards)}

    @cache
    def f(i):
        return 1 + sum(f(j) for j in w[i])

    return sum(f(i) for i in w)


class Test:
    example = """\
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

    def test_one(self):
        assert part_one(*parse_input(self.example)) == 13

    def test_two(self):
        assert part_two(*parse_input(self.example)) == 30


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    sys.exit(main())
