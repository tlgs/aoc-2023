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
def solve(s, groups, curr=0):
    if not s:
        return len(groups) == 0 and curr == 0

    count = 0
    if s[0] in "#?":
        count += solve(s[1:], groups, curr + 1)

    if s[0] in ".?":
        if curr == 0:
            count += solve(s[1:], groups)
        elif groups and groups[0] == curr:
            count += solve(s[1:], groups[1:])

    return count


def part_one(rows):
    total = 0
    for records, groups in rows:
        total += solve(records + ".", groups)

    return total


def part_two(rows):
    total = 0
    for records, groups in rows:
        expanded = "?".join([records] * 5) + ".", groups * 5
        total += solve(*expanded)

    return total


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
