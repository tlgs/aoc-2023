import itertools
import sys


def parse_input(puzzle_input):
    galaxies = set()
    for y, row in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(row):
            if c == "#":
                galaxies.add((x, y))

    return (galaxies,)


def part_one(galaxies):
    mx, my = max(x for x, _ in galaxies), max(y for _, y in galaxies)

    ax, ay = set(range(mx + 1)), set(range(my + 1))
    for x, y in galaxies:
        ax.discard(x)
        ay.discard(y)

    marked_x, marked_y = sorted(ax), sorted(ay)

    total = 0
    for a, b in itertools.combinations(galaxies, 2):
        xa, xb = sorted((a[0], b[0]))
        ya, yb = sorted((a[1], b[1]))

        dx = xb - xa + sum(xa < x < xb for x in marked_x)
        dy = yb - ya + sum(ya < y < yb for y in marked_y)

        total += dx + dy

    return total


def part_two(galaxies, larger=1_000_000):
    mx, my = max(x for x, _ in galaxies), max(y for _, y in galaxies)

    ax, ay = set(range(mx + 1)), set(range(my + 1))
    for x, y in galaxies:
        ax.discard(x)
        ay.discard(y)

    marked_x, marked_y = sorted(ax), sorted(ay)

    total = 0
    for a, b in itertools.combinations(galaxies, 2):
        xa, xb = sorted((a[0], b[0]))
        ya, yb = sorted((a[1], b[1]))

        dx = xb - xa + (larger - 1) * sum(xa < x < xb for x in marked_x)
        dy = yb - ya + (larger - 1) * sum(ya < y < yb for y in marked_y)

        total += dx + dy

    return total


class Test:
    example = """\
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""

    def test_one(self):
        assert part_one(*parse_input(self.example)) == 374

    def test_two(self):
        assert part_two(*parse_input(self.example), 10) == 1030
        assert part_two(*parse_input(self.example), 100) == 8410


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    sys.exit(main())
