import itertools
import math
import sys
from abc import ABC, abstractmethod
from collections import deque


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
        todo = deque([("button", "broadcaster", False)])
        while todo:
            source, relay, signal = todo.popleft()
            counts[signal] += 1

            if relay not in modules:
                continue
            todo.extend(modules[relay].process(source, signal))

    return counts[False] * counts[True]


def part_two(modules):
    # &jm -> rx
    deps = {k: None for k in modules["jm"].state}

    periods = {}
    for i in itertools.count():
        todo = deque([("button", "broadcaster", False)])
        while todo:
            source, relay, signal = todo.popleft()
            if relay not in modules:
                continue
            todo.extend(modules[relay].process(source, signal))

            if signal and source in deps:
                if deps[source] is None:
                    deps[source] = i
                elif source not in periods:
                    periods[source] = i - deps[source]
                    if len(periods) == len(deps):
                        return math.lcm(*periods.values())

    raise RuntimeError


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

    def test_two(self):
        assert True


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    sys.exit(main())
