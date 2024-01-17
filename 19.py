import math
import re
import sys


def parse_input(puzzle_input):
    fst, snd = puzzle_input.split("\n\n")

    workflows = {}
    for line in fst.splitlines():
        name, rest = line.split("{")
        *raw, last = rest[:-1].split(",")

        rules = []
        for r in raw:
            cond, dest = r.split(":")
            cat, op, n = cond[0], cond[1], int(cond[2:])
            rules.append(((cat, op, n), dest))

        workflows[name] = rules + [(None, last)]

    parts = []
    for line in snd.splitlines():
        values = map(int, re.findall(r"\d+", line))
        parts.append(dict(zip("xmas", values)))

    return workflows, parts


def part_one(workflows, parts):
    total = 0
    for part in parts:
        curr = "in"
        while curr not in {"A", "R"}:
            for cond, dest in workflows[curr]:
                if cond is None:
                    curr = dest
                    break

                cat, op, n = cond
                if (op == ">" and part[cat] > n) or (op == "<" and part[cat] < n):
                    curr = dest
                    break

        total += (curr == "A") * sum(part.values())

    return total


def part_two(workflows, _):
    total, todo = 0, [("in", dict(zip("xmas", [(1, 4001)] * 4)))]
    while todo:
        curr, intervals = todo.pop()
        if curr == "R":
            continue
        if curr == "A":
            total += math.prod(b - a for a, b in intervals.values())
            continue

        for cond, dest in workflows[curr]:
            forward = intervals.copy()

            if cond is None:
                todo.append((dest, forward))
                break

            cat, op, n = cond
            start, end = intervals[cat]
            if op == ">":
                forward[cat] = (max(start, n + 1), end)
                intervals[cat] = (start, min(end, n + 1))
            else:
                forward[cat] = (start, min(end, n))
                intervals[cat] = (max(start, n), end)

            todo.append((dest, forward))

    return total


class Test:
    example = """\
px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
"""

    def test_one(self):
        assert part_one(*parse_input(self.example)) == 19114

    def test_two(self):
        assert part_two(*parse_input(self.example)) == 167409079868000


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    sys.exit(main())
