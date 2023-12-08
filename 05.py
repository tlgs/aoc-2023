import sys


def parse_input(puzzle_input):
    fst, rest = puzzle_input.split("\n\n", maxsplit=1)

    _, numbers = fst.split(": ")
    seeds = list(map(int, numbers.split()))

    mappings = []
    for chunk in rest.split("\n\n"):
        current = []
        _, *lines = chunk.splitlines()
        for line in lines:
            current.append(tuple(map(int, line.split())))

        mappings.append(sorted(current, key=lambda t: t[1]))

    return (seeds, mappings)


def run(intervals, mappings):
    for mapping in mappings:
        chunks = []
        for start, size in intervals:
            for dst, src, sz in mapping:
                if src > start:
                    chunk_size = min(src - start, size)
                    chunks.append((start, chunk_size))
                    start, size = start + chunk_size, size - chunk_size

                if src <= start < src + sz:
                    chunk_size = min(src + sz - start, size)
                    chunks.append((dst + start - src, chunk_size))
                    start, size = start + chunk_size, size - chunk_size

                if not size:
                    break

            else:
                chunks.append((start, size))

        intervals = chunks

    return min(s for s, _ in intervals)


def part_one(seeds, mappings):
    intervals = [(n, 1) for n in seeds]
    return run(intervals, mappings)


def part_two(seeds, mappings):
    intervals = list(zip(seeds[::2], seeds[1::2]))
    return run(intervals, mappings)


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
