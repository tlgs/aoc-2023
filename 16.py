import sys
from enum import Enum
from functools import partial


class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4


MIRROR = {
    "\\": {
        Direction.RIGHT: Direction.DOWN,
        Direction.LEFT: Direction.UP,
        Direction.UP: Direction.LEFT,
        Direction.DOWN: Direction.RIGHT,
    },
    "/": {
        Direction.RIGHT: Direction.UP,
        Direction.LEFT: Direction.DOWN,
        Direction.UP: Direction.RIGHT,
        Direction.DOWN: Direction.LEFT,
    },
}


def parse_input(puzzle_input):
    grid = {}
    for y, row in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(row):
            grid[x, y] = c

    return (grid,)


def part_one(grid, start=(0, 0, Direction.RIGHT)):
    seen, todo = set(), [start]
    while todo:
        x, y, d = todo.pop()
        seen.add((x, y, d))

        nxt = []
        if grid[x, y] == "|" and d in {Direction.RIGHT, Direction.LEFT}:
            nxt.append((x, y - 1, Direction.UP))
            nxt.append((x, y + 1, Direction.DOWN))

        elif grid[x, y] == "-" and d in {Direction.UP, Direction.DOWN}:
            nxt.append((x - 1, y, Direction.LEFT))
            nxt.append((x + 1, y, Direction.RIGHT))

        else:
            if grid[x, y] in MIRROR:
                d = MIRROR[grid[x, y]][d]

            match d:
                case Direction.RIGHT:
                    nxt.append((x + 1, y, Direction.RIGHT))
                case Direction.LEFT:
                    nxt.append((x - 1, y, Direction.LEFT))
                case Direction.UP:
                    nxt.append((x, y - 1, Direction.UP))
                case Direction.DOWN:
                    nxt.append((x, y + 1, Direction.DOWN))

        for x, y, d in nxt:
            if (x, y) in grid and (x, y, d) not in seen:
                todo.append((x, y, d))

    return len({(x, y) for (x, y, _) in seen})


def part_two(grid):
    mx, my = max(x for x, _ in grid), max(y for _, y in grid)

    f = partial(part_one, grid)
    right = max(f((0, y, Direction.RIGHT)) for y in range(0, my + 1))
    left = max(f((mx, y, Direction.LEFT)) for y in range(0, my + 1))
    up = max(f((x, my, Direction.UP)) for x in range(0, mx + 1))
    down = max(f((x, 0, Direction.DOWN)) for x in range(0, mx + 1))

    return max(right, left, up, down)


class Test:
    example = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
"""

    def test_one(self):
        assert part_one(*parse_input(self.example)) == 46

    def test_two(self):
        assert part_two(*parse_input(self.example)) == 51


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    sys.exit(main())
