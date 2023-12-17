import itertools
import sys


def parse_input(puzzle_input):
    platform = []
    for line in puzzle_input.splitlines():
        platform.append(list(line))

    return (platform,)


def part_one(platform):
    platform = [inner[:] for inner in platform]

    total, ymax = 0, len(platform)
    for y, row in enumerate(platform):
        for x, c in enumerate(row):
            if c != "O":
                continue

            i = y - 1
            while i >= 0 and platform[i][x] == ".":
                i -= 1

            platform[y][x] = "."
            platform[i + 1][x] = "O"

            total += ymax - (i + 1)

    return total


def part_two(platform):
    platform = [inner[:] for inner in platform]

    memory, rev = {}, {}
    for i in itertools.count():
        h = tuple(tuple(inner) for inner in platform)
        if h in memory:
            break

        memory[h], rev[i] = i, h

        for _ in range(4):
            for y, row in enumerate(platform):
                for x, c in enumerate(row):
                    if c != "O":
                        continue

                    j = y - 1
                    while j >= 0 and platform[j][x] == ".":
                        j -= 1

                    platform[y][x] = "."
                    platform[j + 1][x] = "O"

            platform = list(map(list, zip(*reversed(platform))))

    offset = memory[h]
    pos = (1000000000 - offset) % (i - offset) + offset
    return sum(len(platform) - y for y, r in enumerate(rev[pos]) for c in r if c == "O")


class Test:
    example = """\
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""

    def test_one(self):
        assert part_one(*parse_input(self.example)) == 136

    def test_two(self):
        assert part_two(*parse_input(self.example)) == 64


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    sys.exit(main())
