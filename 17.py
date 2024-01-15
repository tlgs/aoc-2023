import heapq
import sys


def parse_input(puzzle_input):
    grid = {}
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(line):
            grid[(x, y)] = int(c)

    return grid, (x, y)


def neighbors_one(pos, inertia):
    d, c = inertia
    ds = {(1, 0), (-1, 0), (0, 1), (0, -1)} - {(-d[0], -d[1])}
    if c == 3:
        ds.remove(d)

    for dx, dy in ds:
        ni = (d, c + 1) if d == (dx, dy) else ((dx, dy), 1)
        yield (pos[0] + dx, pos[1] + dy), ni


def part_one(grid, target):
    seen = set(((0, 0), ((1, 0), 0)))
    todo = [(0, (0, 0), ((1, 0), 0))]
    while todo:
        cost, pos, inertia = heapq.heappop(todo)

        for neighbor, ni in neighbors_one(pos, inertia):
            if neighbor == target:
                return cost + grid[target]

            if neighbor not in grid or (neighbor, ni) in seen:
                continue

            seen.add((neighbor, ni))
            todo.append((cost + grid[neighbor], neighbor, ni))

    raise RuntimeError


def neighbors_two(pos, inertia):
    d, c = inertia
    if d is not None and c < 4:
        yield (pos[0] + d[0], pos[1] + d[1]), (d, c + 1)
        return

    ds = {(1, 0), (-1, 0), (0, 1), (0, -1)}
    if d is not None:
        ds.remove((-d[0], -d[1]))

    if c == 10:
        ds.remove(d)

    for dx, dy in ds:
        ni = (d, c + 1) if d == (dx, dy) else ((dx, dy), 1)
        yield (pos[0] + dx, pos[1] + dy), ni


def part_two(grid, target):
    seen = set(((0, 0), (None, None)))
    todo = [(0, (0, 0), (None, None))]
    while todo:
        cost, pos, inertia = heapq.heappop(todo)

        for neighbor, ni in neighbors_two(pos, inertia):
            if neighbor == target:
                return cost + grid[target]

            if neighbor not in grid or (neighbor, ni) in seen:
                continue

            seen.add((neighbor, ni))
            todo.append((cost + grid[neighbor], neighbor, ni))

    raise RuntimeError


class Test:
    example = """\
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
"""

    def test_one(self):
        assert part_one(*parse_input(self.example)) == 102

    def test_two(self):
        assert part_two(*parse_input(self.example)) == 94


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    sys.exit(main())
