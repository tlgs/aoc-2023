import itertools
import math
import re
import sys


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
    instructions = itertools.cycle(instructions)
    while curr != "ZZZ":
        i += 1
        curr = network[curr][next(instructions)]

    return i


def part_two(instructions, network):
    n = len(instructions)
    starts = [node for node in network if node[-1] == "A"]
    found = []
    for start in starts:
        curr, seen = start, {start: 0}
        interesting = []
        for i, instr in enumerate(itertools.cycle(instructions)):
            curr = network[curr][instr]
            if (curr, i % n) in seen:
                break

            seen[(curr, i % n)] = i + 1
            if curr[-1] == "Z":
                interesting.append((i + 1, curr))

        assert len(interesting) == 1

        marker = (curr, i % n)
        cycle_start = seen[marker]
        cycle_length = len(seen) - cycle_start

        assert interesting[0][0] == cycle_length
        found.append(cycle_length)

    return math.lcm(*found)


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
