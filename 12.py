import functools
import sys


def parse_input(puzzle_input):
    rows = []
    for line in puzzle_input.splitlines():
        records, groups = line.split()
        groups = tuple(map(int, groups.split(",")))
        rows.append((records, groups))

    return (rows,)


@functools.cache
def solve(record, groups, curr=0):
    if record == "":
        return len(groups) == 0 and curr == 0

    elif (groups and curr > groups[0]) or (not groups and curr):
        return 0

    c, rest = record[0], record[1:]
    total = 0

    if c in "#?":
        total += solve(rest, groups, curr + 1)

    if c in ".?":
        if curr == 0:
            total += solve(rest, groups)
        elif curr == groups[0]:
            total += solve(rest, groups[1:])

    return total


def part_one(rows):
    return sum(solve(r + ".", g) for r, g in rows)


def part_two(rows):
    return sum(solve("?".join([r] * 5) + ".", g * 5) for r, g in rows)


class Test:
    example = """\
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""

    def test_one(self):
        assert part_one(*parse_input(self.example)) == 21

    def test_two(self):
        assert part_two(*parse_input(self.example)) == 525152


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    sys.exit(main())
