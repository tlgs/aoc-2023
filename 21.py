import sys


def parse_input(puzzle_input):
    grid = {}
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(line):
            if c in ".S":
                grid[x, y] = c

    return grid, y + 1


def neighbors(x, y):
    yield x, y - 1
    yield x, y + 1
    yield x + 1, y
    yield x - 1, y


def part_one(grid, _, steps=64):
    plots = {p for p in grid if grid[p] == "S"}
    for _ in range(steps):
        plots = {n for t in plots for n in neighbors(*t) if n in grid}

    return len(plots)


def part_two(grid, size, steps=26501365):
    plots = {p for p in grid if grid[p] == "S"}

    done = []
    offset = size // 2
    check = {offset, offset + size, offset + 2 * size}
    for i in range(offset + 2 * size + 1):
        if i in check:
            done.append(len(plots))

        plots = {
            (x, y)
            for t in plots
            for x, y in neighbors(*t)
            if (x % size, y % size) in grid
        }

    n = steps // size
    a, b, c = done
    return a + n * (b - a + (n - 1) * (c - b - b + a) // 2)


class Test:
    example = """\
...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
"""

    def test_one(self):
        assert part_one(*parse_input(self.example), 6) == 16


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    sys.exit(main())
