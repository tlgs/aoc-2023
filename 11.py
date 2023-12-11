import bisect
import itertools
import sys


def parse_input(puzzle_input):
    lines = puzzle_input.splitlines()
    max_y, max_x = len(lines), len(lines[0])

    galaxies = set()
    ax, ay = set(range(max_x)), set(range(max_y))
    for y, row in enumerate(lines):
        for x, c in enumerate(row):
            if c == "#":
                galaxies.add((x, y))
                ax.discard(x)
                ay.discard(y)

    # solving the problem here to avoid looping twice :^)
    empty_x, empty_y = sorted(ax), sorted(ay)
    part_one, partials = 0, []
    for (xa, ya), (xb, yb) in itertools.combinations(galaxies, 2):
        dx, dy = abs(xa - xb), abs(ya - yb)

        cx = abs(bisect.bisect(empty_x, xa) - bisect.bisect(empty_x, xb))
        cy = abs(bisect.bisect(empty_y, ya) - bisect.bisect(empty_y, yb))

        part_one += dx + cx + dy + cy
        partials.append((dx + dy, cx + cy))

    return (part_one, partials)


def part_one(answer, _):
    return answer


def part_two(_, partials, m=1_000_000):
    return sum(distance + (m - 1) * counts for distance, counts in partials)


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
