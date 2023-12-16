import sys


def parse_input(puzzle_input):
    return (puzzle_input.split("\n\n"),)


def transform(line):
    b = line.replace("#", "1").replace(".", "0")
    return int(b, base=2)


def flip(lines):
    n, m = len(lines), len(lines[0])
    flipped = ["".join(lines[i][j] for i in range(n)) for j in range(m)]
    return flipped


def find(numbers):
    reflections, n = [], len(numbers)
    for curr in range(1, n):
        i, j = curr, curr - 1
        while j >= 0 and i < n:
            if numbers[i] != numbers[j]:
                break
            i, j = i + 1, j - 1
        else:
            reflections.append(curr)

    return reflections


def try_smudges(rows, n, known):
    for i, x in enumerate(rows):
        for j in range(n):
            v = x ^ (1 << j)

            for r in find(rows[:i] + [v] + rows[i + 1 :]):
                if r != known:
                    return r

    return None


def run(patterns):
    part_one, known = 0, []
    for pattern in patterns:
        lines = pattern.split()

        rows = [transform(line) for line in lines]
        if reflections := find(rows):
            found, *_ = reflections

            part_one += 100 * found
            known.append((0, found))
            continue

        columns = [transform(line) for line in flip(lines)]
        reflections = find(columns)
        found, *_ = reflections

        part_one += found
        known.append((1, found))

    part_two = 0
    for pattern, (t, k) in zip(patterns, known):
        lines = pattern.split()

        n = len(lines[0])
        rows = [transform(line) for line in lines]
        if found := try_smudges(rows, n, k if t == 0 else None):
            part_two += 100 * found
            continue

        n = len(lines)
        columns = [transform(line) for line in flip(lines)]
        found = try_smudges(columns, n, k if t == 1 else None)
        part_two += found

    return part_one, part_two


class Test:
    example = """\
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""

    def test_one(self):
        part_one, _ = run(*parse_input(self.example))
        assert part_one == 405

    def test_two(self):
        _, part_two = run(*parse_input(self.example))
        assert part_two == 400


def main():
    puzzle = parse_input(sys.stdin.read())

    part_one, part_two = run(*puzzle)
    print("part 1:", part_one)
    print("part 2:", part_two)


if __name__ == "__main__":
    sys.exit(main())
