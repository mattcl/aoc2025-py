# You can copy/paste this template to start a new day

"""03: lobby"""
import aoc.util


# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        self.p1 = 0
        self.p2 = 0

        for line in input.strip().split("\n"):
            max_pos = 0
            max_v = 0

            for i in range(0, len(line) - 12):
                v = int(line[i])
                if v > max_v:
                    max_v = v
                    max_pos = i

                    if v == 9:
                        break

            shrunk = line[max_pos:]

            self.p1 += best2(shrunk)
            self.p2 += best12(shrunk)

    def part_one(self) -> int:
        return self.p1

    def part_two(self) -> int:
        return self.p2


def best2(choices):
    first = int(choices[0])
    max_pos = 0

    if first != 9:
        for i in range(1, len(choices) - 1):
            v = int(choices[i])
            if v > first:
                first = v
                max_pos = i

                if v == 9:
                    break

    second = 0
    for i in range(max_pos + 1, len(choices)):
        v = int(choices[i])
        if v > second:
            second = v

            if v == 9:
                break

    return first * 10 + second


def best12(choices):
    max = 0
    start = 0
    for pos in range(0, 12):
        exclude = 11 - pos
        max_idx = 0
        max_digit = 0
        for i in range(start, len(choices) - exclude):
            v = int(choices[i])
            if v > max_digit:
                max_digit = v
                max_idx = i

                if v == 9:
                    break

        start = max_idx + 1
        max += max_digit * (10 ** (11 - pos))

    return max
