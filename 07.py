import sys
from collections import Counter


def parse_input(puzzle_input):
    hands = [tuple(line.split()) for line in puzzle_input.splitlines()]
    return (hands,)


def hand_key(hand):
    cards, _ = hand

    filtered = cards.replace("~", "")
    signature = tuple(sorted(Counter(filtered).values()))
    match signature:
        case (5,) | (4,) | (3,) | (2,) | (1,) | ():
            kind = 6
        case (1, 4) | (1, 3) | (1, 2) | (1, 1):
            kind = 5
        case (2, 3) | (2, 2):
            kind = 4
        case (1, 1, 3) | (1, 1, 2) | (1, 1, 1):
            kind = 3
        case (1, 2, 2):
            kind = 2
        case (1, 1, 1, 2) | (1, 1, 1, 1):
            kind = 1
        case (1, 1, 1, 1, 1):
            kind = 0

    strengths = tuple(map("~23456789TJQKA".index, cards))

    return (kind, *strengths)


def part_one(hands):
    ranked = sorted(hands, key=hand_key)
    return sum(rank * int(bid) for rank, (_, bid) in enumerate(ranked, start=1))


def part_two(hands):
    hands = [(c.replace("J", "~"), b) for c, b in hands]
    ranked = sorted(hands, key=hand_key)
    return sum(rank * int(bid) for rank, (_, bid) in enumerate(ranked, start=1))


class Test:
    example = """\
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

    def test_one(self):
        assert part_one(*parse_input(self.example)) == 6440

    def test_two(self):
        assert part_two(*parse_input(self.example)) == 5905


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    sys.exit(main())
