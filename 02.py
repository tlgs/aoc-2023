import sys


def parse_input(puzzle_input):
    games = []
    for i, line in enumerate(puzzle_input.splitlines(), start=1):
        label, reveals = line.split(": ")

        _, id_ = label.split()
        assert i == int(id_)

        sets = []
        for reveal in reveals.split("; "):
            r = g = b = 0
            for cubes in reveal.split(", "):
                match cubes.split():
                    case [x, "red"]:
                        r = int(x)
                    case [x, "green"]:
                        g = int(x)
                    case [x, "blue"]:
                        b = int(x)

            sets.append((r, g, b))

        games.append(sets)

    return (games,)


def part_one(games):
    total = 0
    for i, game in enumerate(games, start=1):
        for r, g, b in game:
            if r > 12 or g > 13 or b > 14:
                break
        else:
            total += i

    return total


def part_two(games):
    total = 0
    for game in games:
        mr = mg = mb = 0
        for r, g, b in game:
            mr, mg, mb = max(mr, r), max(mg, g), max(mb, b)

        total += mr * mg * mb

    return total


class Test:
    example = """\
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

    def test_one(self):
        assert part_one(*parse_input(self.example)) == 8

    def test_two(self):
        assert part_two(*parse_input(self.example)) == 2286


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    sys.exit(main())
