import math
import re
import sys
from typing import NamedTuple


class Part(NamedTuple):
    x: int
    m: int
    a: int
    s: int


def parse_input(puzzle_input):
    fst, snd = puzzle_input.split("\n\n")

    workflows = {}
    for line in fst.splitlines():
        name, rest = line.split("{")

        *raw, last = rest[:-1].split(",")
        rules = [tuple(r.split(":")) for r in raw]
        rules.append((None, last))

        workflows[name] = rules

    parts = [Part(*map(int, re.findall(r"\d+", line))) for line in snd.splitlines()]

    return workflows, parts


def do(part, workflow):
    for cond, dest in workflow:
        if cond is None:
            return dest

        cat, op, n = cond[0], cond[1], int(cond[2:])
        if op == ">" and getattr(part, cat) > n:
            return dest
        elif op == "<" and getattr(part, cat) < n:
            return dest

    raise RuntimeError


def part_one(workflows, parts):
    total, end = 0, set("AR")
    for part in parts:
        curr = "in"
        while curr not in end:
            curr = do(part, workflows[curr])

        total += (curr == "A") * (part.x + part.m + part.a + part.s)

    return total


def part_two(workflows, _):
    total = 0

    todo = [("in", {"x": (1, 4001), "m": (1, 4001), "a": (1, 4001), "s": (1, 4001)})]
    while todo:
        curr, intervals = todo.pop()
        if curr == "R":
            continue
        elif curr == "A":
            total += math.prod(map(lambda t: t[1] - t[0], intervals.values()))
            continue

        for cond, dest in workflows[curr]:
            nxt = intervals.copy()
            if cond is not None:
                cat, op, n = cond[0], cond[1], int(cond[2:])
                a, b = intervals[cat]
                match op:
                    case ">":
                        nxt[cat] = (max(a, n + 1), min(b, 4001))
                        intervals[cat] = (max(a, 1), min(b, n + 1))
                    case "<":
                        nxt[cat] = (max(a, 1), min(b, n))
                        intervals[cat] = (max(a, n), min(b, 4001))

            todo.append((dest, nxt))

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
