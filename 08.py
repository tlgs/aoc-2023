import math
import re
import sys
from itertools import cycle


def parse_input(puzzle_input):
    fst, snd = puzzle_input.split("\n\n")
    instructions = [0 if c == "L" else 1 for c in fst]

    network = {}
    for line in snd.splitlines():
        src, left, right = re.findall(r"\w+", line)
        network[src] = (left, right)

    return (instructions, network)


def part_one(instructions, network):
    i, curr = 0, "AAA"
    for i, direction in enumerate(cycle(instructions), start=1):
        if (curr := network[curr][direction]) == "ZZZ":
            break

    return i


def part_two(instructions, network):
    """
    This one is sort of messed up as the input data is carefully crafted
    such that the problem is significantly easier:
      - There's a single **Z node in each loop
      - The **Z node is hit exacly at every multiple of the cycle length

    I figured this out by iteratively looking at the loop starts and lengths,
    and the **Z node index. A general solution for the described problem would have
    been much more complicated.
    """
    lengths = []
    for curr in filter(lambda node: node.endswith("A"), network):
        for i, direction in enumerate(cycle(instructions), start=1):
            if (curr := network[curr][direction]).endswith("Z"):
                break

        lengths.append(i)

    return math.lcm(*lengths)


class Test:
    example1 = """\
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""

    example2 = """\
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""

    example3 = """\
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""

    def test_one(self):
        assert part_one(*parse_input(self.example1)) == 2
        assert part_one(*parse_input(self.example2)) == 6

    def test_two(self):
        assert part_two(*parse_input(self.example3)) == 6


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    sys.exit(main())
