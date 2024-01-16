import heapq
import sys


def parse_input(puzzle_input):
    grid = {}
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(line):
            grid[x, y] = int(c)

    return grid, (x, y)


def part_one(grid, target):
    seen = set()
    todo = [(0, (0, 0), (1, 0)), (0, (0, 0), (0, 1))]
    while todo:
        cost, pos, d = heapq.heappop(todo)
        if pos == target:
            return cost
        elif (pos, d) in seen:
            continue
        seen.add((pos, d))

        turns = {(1, 0), (-1, 0), (0, 1), (0, -1)} - {(d[0], d[1]), (-d[0], -d[1])}
        for dx, dy in turns:
            v = cost
            for i in range(1, 4):
                if (np := (pos[0] + dx * i, pos[1] + dy * i)) not in grid:
                    break

                v += grid[np]
                heapq.heappush(todo, (v, np, (dx, dy)))

    raise RuntimeError


def part_two(grid, target):
    seen = set()
    todo = [(0, (0, 0), (1, 0)), (0, (0, 0), (0, 1))]
    while todo:
        cost, pos, d = heapq.heappop(todo)
        if pos == target:
            return cost
        elif (pos, d) in seen:
            continue
        seen.add((pos, d))

        turns = {(1, 0), (-1, 0), (0, 1), (0, -1)} - {(d[0], d[1]), (-d[0], -d[1])}
        for dx, dy in turns:
            v = cost
            for i in range(1, 11):
                if (np := (pos[0] + dx * i, pos[1] + dy * i)) not in grid:
                    break

                v += grid[np]
                if i >= 4:
                    heapq.heappush(todo, (v, np, (dx, dy)))

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
