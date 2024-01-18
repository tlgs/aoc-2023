import collections
import math
import sys
from abc import ABC, abstractmethod


class Module(ABC):
    def __init__(self, name, state, targets):
        self.name = name
        self.state = state
        self.targets = targets

    @abstractmethod
    def process(self, source, high):
        pass


class FlipFlop(Module):
    def process(self, source, high):
        if high:
            return []

        self.state = not self.state
        return [(self.name, target, self.state) for target in self.targets]


class Conjunction(Module):
    def process(self, source, high):
        self.state[source] = high
        pulse = not all(self.state.values())
        return [(self.name, target, pulse) for target in self.targets]


class Broadcast(Module):
    def process(self, _, high):
        return [(self.name, target, high) for target in self.targets]


def parse_input(puzzle_input):
    modules = {}
    for line in puzzle_input.splitlines():
        left, right = line.split(" -> ")

        if left.startswith("%"):
            cls, name, state = FlipFlop, left[1:], False
        elif left.startswith("&"):
            cls, name, state = Conjunction, left[1:], {}
        elif left == "broadcaster":
            cls, name, state = Broadcast, left, None
        else:
            raise ValueError(f"bad module name {left}")

        modules[name] = cls(name, state, right.split(", "))

    # instantiate Conjuction modules' inputs
    for name, module in modules.items():
        for target in module.targets:
            if isinstance((m := modules.get(target)), Conjunction):
                m.state[name] = False

    return (modules,)


def part_one(modules):
    counts = {False: 0, True: 0}
    for _ in range(1000):
        todo = collections.deque([("button", "broadcaster", False)])
        while todo:
            source, relay, signal = todo.popleft()
            counts[signal] += 1

            if relay not in modules:
                continue
            todo.extend(modules[relay].process(source, signal))

    return counts[False] * counts[True]


def part_two(modules):
    deps = set(modules["jm"].state)  # there's only `&jm -> rx`

    i, periods = 0, {}
    while deps:
        i += 1
        todo = collections.deque([("button", "broadcaster", False)])
        while todo:
            source, relay, signal = todo.popleft()
            if relay not in modules:
                continue
            todo.extend(modules[relay].process(source, signal))

            if signal and source in deps:
                if source not in periods:
                    periods[source] = i
                    continue

                periods[source] = i - periods[source]
                deps.remove(source)

    return math.lcm(*periods.values())


class Test:
    example1 = """\
broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a
"""

    example2 = """\
broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output
"""

    def test_one(self):
        assert part_one(*parse_input(self.example1)) == 32000000
        assert part_one(*parse_input(self.example2)) == 11687500


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    sys.exit(main())
