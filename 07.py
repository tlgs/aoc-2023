import sys
from collections import Counter


def parse_input(puzzle_input):
    hands = [tuple(line.split()) for line in puzzle_input.splitlines()]
    return (hands,)


def run(hands, key):
    ranked = sorted(hands, key=key)
    return sum(rank * int(bid) for rank, (_, bid) in enumerate(ranked, start=1))


def part_one(hands):
    def f(hand):
        cards, _ = hand

        types = [
            (1, 1, 1, 1, 1),
            (1, 1, 1, 2),
            (1, 2, 2),
            (1, 1, 3),
            (2, 3),
            (1, 4),
            (5,),
        ]
        signature = tuple(sorted(Counter(cards).values()))
        kind = types.index(signature)

        ordering = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
        strengths = tuple(map(ordering.index, cards))

        return (kind, *strengths)

    return run(hands, f)


def part_two(hands):
    def f(hand):
        cards, _ = hand

        signature = tuple(sorted(Counter(c for c in cards if c != "J").values()))
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
            case t:
                raise ValueError(t)

        ordering = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
        strengths = tuple(map(ordering.index, cards))

        return (kind, *strengths)

    return run(hands, f)


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

    print("part 1:", part_one(*puzzle))  # NOT: 251036598
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    sys.exit(main())
