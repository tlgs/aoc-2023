import sys


def parse_input(puzzle_input):
    return (puzzle_input.rstrip().split(","),)


def h(string):
    curr = 0
    for char in string:
        curr = ((curr + ord(char)) * 17) % 256

    return curr


def part_one(sequence):
    return sum(map(h, sequence))


def part_two(sequence):
    hashmap = [{} for _ in range(256)]
    for string in sequence:
        match string[-1]:
            case "-":
                label = string[:-1]

                box = h(label)
                hashmap[box].pop(label, None)
            case _:
                label = string[:-2]
                focal_length = int(string[-1])

                box = h(label)
                hashmap[box][label] = focal_length

    power = 0
    for i, box in enumerate(hashmap, start=1):
        for j, (_, v) in enumerate(box.items(), start=1):
            power += i * j * v

    return power


class Test:
    example = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""

    def test_one(self):
        assert part_one(*parse_input(self.example)) == 1320

    def test_two(self):
        assert part_two(*parse_input(self.example)) == 145


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    sys.exit(main())
