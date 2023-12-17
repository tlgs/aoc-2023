import sys


def parse_input(puzzle_input):
    platform = []
    for line in puzzle_input.splitlines():
        platform.append(list(line))

    return (platform,)


def tilt(platform):
    top = [0] * len(platform[0])
    for y, row in enumerate(platform):
        for x, c in enumerate(row):
            if c == ".":
                continue

            if c == "#":
                top[x] = y + 1
                continue

            platform[y][x] = "."
            platform[top[x]][x] = "O"
            top[x] += 1

    return None


def total_load(platform):
    total = 0
    for y, row in enumerate(platform[::-1], start=1):
        for c in row:
            total += (c == "O") * y

    return total


def part_one(platform):
    platform = [row[:] for row in platform]

    tilt(platform)
    return total_load(platform)


def part_two(platform, target=1_000_000_000):
    platform = [row[:] for row in platform]

    i, found, memory = 0, False, {}
    while i < target:
        hash_ = tuple(tuple(row) for row in platform)
        if hash_ in memory and not found:
            found = True
            length = i - memory[hash_]
            i += length * ((target - i) // length)

        memory[hash_] = i

        for _ in range(4):
            tilt(platform)
            platform = list(map(list, zip(*reversed(platform))))

        i += 1

    return total_load(platform)


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
