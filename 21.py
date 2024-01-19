import sys


def parse_input(puzzle_input):
    grid, start = {}, None
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(line):
            if c == "S":
                start, c = (x, y), "."
            grid[x, y] = c

    return grid, start


def neighbors(x, y):
    yield x, y - 1
    yield x, y + 1
    yield x + 1, y
    yield x - 1, y


def part_one(grid, start, steps=64):
    plots = {start}
    for _ in range(steps):
        plots = {n for t in plots for n in neighbors(*t) if grid.get(n) == "."}

    return len(plots)


def part_two(grid, start, steps=26501365):
    size = int(len(grid) ** 0.5)  # grid is a square

    done = []
    plots = {start}
    for i in range(3 * size):
        if (i % size) == (size // 2):
            done.append(len(plots))

        plots = {
            (x, y)
            for t in plots
            for x, y in neighbors(*t)
            if grid.get((x % size, y % size)) == "."
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

    # def test_two(self):
    # assert part_two(*parse_input(self.example), 6) == 16
    # assert part_two(*parse_input(self.example), 10) == 50
    # assert part_two(*parse_input(self.example), 50) == 1594
    # assert part_two(*parse_input(self.example), 100) == 6536
    # assert part_two(*parse_input(self.example), 500) == 167004
    # assert part_two(*parse_input(self.example), 1000) == 668697
    # assert part_two(*parse_input(self.example), 5000) == 16733044


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    sys.exit(main())
