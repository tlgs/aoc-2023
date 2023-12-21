import sys
from functools import partial


def parse_input(puzzle_input):
    grid = {}
    for y, row in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(row):
            grid[complex(x, y)] = c

    return (grid,)


def part_one(grid, start=(0j, 1)):
    seen, todo = set(), [start]
    while todo:
        p, d = todo.pop()
        if p not in grid or (p, d) in seen:
            continue

        seen.add((p, d))

        match grid[p], d:
            case ("|", 1) | ("|", -1):
                todo.append((p - 1j, -1j))
                todo.append((p + 1j, 1j))
                continue
            case ("-", 1j) | ("-", -1j):
                todo.append((p - 1, -1))
                todo.append((p + 1, 1))
                continue
            case "/", _:
                d = -complex(d.imag, d.real)
            case "\\", _:
                d = complex(d.imag, d.real)

        todo.append((p + d, d))

    return len({p for p, _ in seen})


def part_two(grid):
    mx, my = int(max(p.real for p in grid)), int(max(p.imag for p in grid))

    f = partial(part_one, grid)
    right = max(f((complex(0, y), 1)) for y in range(0, my + 1))
    left = max(f((complex(mx, y), -1)) for y in range(0, my + 1))
    up = max(f((complex(x, my), -1j)) for x in range(0, mx + 1))
    down = max(f((complex(x, 0), 1j)) for x in range(0, mx + 1))

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
