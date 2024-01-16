import sys
from itertools import pairwise


def parse_input(puzzle_input):
    dig_plan = []
    for line in puzzle_input.splitlines():
        c, raw_n, raw_rgb = line.split()
        n, rgb = int(raw_n), raw_rgb[2:-1]
        dig_plan.append((c, n, rgb))

    return (dig_plan,)


def part_one(dig_plan):
    x, y, path = 0, 0, [(0, 0)]
    for c, n, _ in dig_plan:
        match c:
            case "U":
                y += n
            case "D":
                y -= n
            case "L":
                x -= n
            case "R":
                x += n
            case _:
                raise ValueError

        path.append((x, y))

    assert (x, y) == (0, 0)  # closed loop

    # Shoelace formula
    area = abs(sum(a * d - b * c for (a, c), (b, d) in pairwise(path))) // 2

    # Pick's theorem
    boundary = sum(abs((b - a) + (d - c)) for (a, c), (b, d) in pairwise(path))
    interior = area - boundary // 2 + 1

    return boundary + interior


def translate(rgb):
    raw_n, raw_c = rgb[:-1], rgb[-1]

    n = int(raw_n, 16)
    c = {"0": "R", "1": "D", "2": "L", "3": "U"}[raw_c]
    return c, n


def part_two(dig_plan):
    x, y, path = 0, 0, [(0, 0)]
    for _, _, rgb in dig_plan:
        c, n = translate(rgb)
        match c:
            case "U":
                y += n
            case "D":
                y -= n
            case "L":
                x -= n
            case "R":
                x += n
            case _:
                raise ValueError

        path.append((x, y))

    assert (x, y) == (0, 0)  # closed loop

    # Shoelace formula
    area = abs(sum(a * d - b * c for (a, c), (b, d) in pairwise(path))) // 2

    # Pick's theorem
    boundary = sum(abs((b - a) + (d - c)) for (a, c), (b, d) in pairwise(path))
    interior = area - boundary // 2 + 1

    return boundary + interior


class Test:
    example = """\
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
"""

    def test_one(self):
        assert part_one(*parse_input(self.example)) == 62

    def test_two(self):
        assert part_two(*parse_input(self.example)) == 952408144115


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    sys.exit(main())
