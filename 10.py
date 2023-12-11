import sys
from itertools import pairwise


def neighbors(x, y, shape):
    match shape:
        case "|":
            yield from [(x, y - 1), (x, y + 1)]
        case "-":
            yield from [(x + 1, y), (x - 1, y)]
        case "L":
            yield from [(x, y - 1), (x + 1, y)]
        case "J":
            yield from [(x - 1, y), (x, y - 1)]
        case "7":
            yield from [(x - 1, y), (x, y + 1)]
        case "F":
            yield from [(x + 1, y), (x, y + 1)]
        case _:
            raise ValueError(shape)


def parse_input(puzzle_input):
    tiles, start = {}, None
    for y, row in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(row):
            if c == "S":
                start = (x, y)
            tiles[(x, y)] = c

    assert start is not None

    # determine start pipe shape
    x, y = start
    north, east, south, west = map(
        tiles.get, [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]
    )

    possible = set("|-LJ7F")
    if north and north in "|7F":
        possible -= set("-7F")
    if east and east in "-J7":
        possible -= set("|J7")
    if south and south in "|LJ":
        possible -= set("-LJ")
    if west and west in "-LF":
        possible -= set("|LF")

    assert len(possible) == 1
    shape = possible.pop()

    # walk the loop
    path = [start]
    prev, curr = start, next(neighbors(*start, shape))
    while curr != start:
        path.append(curr)
        prev, curr = curr, (set(neighbors(*curr, tiles[curr])) - {prev}).pop()

    return (path, tiles)


def part_one(path, tiles):
    return len(path) // 2


def part_two(path, tiles):
    v = [t for t in path if tiles[t] not in "|-"]

    # Shoelace formula: <https://en.wikipedia.org/wiki/Shoelace_formula>
    area = abs(sum(a * d - b * c for (a, c), (b, d) in pairwise(v + v[:1]))) // 2

    # Pick's theorem: <https://en.wikipedia.org/wiki/Pick%27s_theorem>
    return area - len(path) // 2 + 1


class Test:
    example1 = """\
.....
.S-7.
.|.|.
.L-J.
.....
"""

    example2 = """\
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
"""

    example3 = """\
...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
"""

    example4 = """\
.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
"""

    example5 = """\
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
"""

    def test_one(self):
        assert part_one(*parse_input(self.example1)) == 4
        assert part_one(*parse_input(self.example2)) == 8

    def test_two(self):
        assert part_two(*parse_input(self.example3)) == 4
        assert part_two(*parse_input(self.example4)) == 8
        assert part_two(*parse_input(self.example5)) == 10


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    sys.exit(main())
