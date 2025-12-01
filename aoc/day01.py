# You can copy/paste this template to start a new day

"""01: secret entrance"""
import aoc.util


# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        self.zeroes = 0
        self.pass_zeroes = 0
        sum = 50

        for line in input.strip().split("\n"):
            d = line[0]
            v = int(line[1:])

            if d == 'L':
                v = -v

            if v < 0:
                self.pass_zeroes += (100 - sum - v) // 100
                if sum == 0:
                    self.pass_zeroes -= 1
            else:
                self.pass_zeroes += (sum + v) // 100

            sum += v
            sum %= 100

            if sum == 0:
                self.zeroes += 1

    def part_one(self) -> int:
        return self.zeroes

    def part_two(self) -> int:
        return self.pass_zeroes
