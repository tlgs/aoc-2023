import itertools
import sys


def parse_input(puzzle_input):
    fst, rest = puzzle_input.split("\n\n", maxsplit=1)
    seeds = [int(v) for v in fst.split(": ")[1].split()]

    mappings = []
    for chunk in rest.split("\n\n"):
        current = []
        _, *lines = chunk.splitlines()
        for line in lines:
            destination, source, length = map(int, line.split())
            current.append((range(source, source + length), destination))

        mappings.append(current)

    return (seeds, mappings)


def part_one(seeds, mappings):
    best = sys.maxsize
    for x in seeds:
        for mapping in mappings:
            for source_range, destination in mapping:
                if x in source_range:
                    x = destination + source_range.index(x)
                    break

        best = min(best, x)

    return best


def part_two(seeds, mappings):
    inverse = []
    for mapping in mappings[::-1]:
        current = []
        for source_range, destination in mapping:
            length = source_range.stop - source_range.start
            current.append(
                (range(destination, destination + length), source_range.start)
            )

        inverse.append(current)

    valid = [range(a, a + b) for a, b in zip(seeds[::2], seeds[1::2])]
    for i in itertools.count():
        x = i
        for mapping in inverse:
            for source_range, destination in mapping:
                if x in source_range:
                    x = destination + source_range.index(x)
                    break

        if any(x in r for r in valid):
            return i

    raise RuntimeError


class Test:
    example = """\
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""

    def test_one(self):
        assert part_one(*parse_input(self.example)) == 35

    def test_two(self):
        assert part_two(*parse_input(self.example)) == 46


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    sys.exit(main())
