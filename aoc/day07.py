"""07: laboratories"""
import aoc.util


class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        self.p1 = 0

        lines = list(input.strip().split("\n"))

        width = len(lines[0])

        timelines = [0] * width

        s_idx = 0
        for i in range(width):
            if lines[0][i] == 'S':
                s_idx = i
                break

        timelines[s_idx] = 1
        offset = s_idx

        for i in range(2, len(lines), 2):
            for j in range(offset, width):
                if lines[i][j] == '^' and timelines[j] > 0:
                    self.p1 += 1

                    prev = timelines[j]
                    timelines[j] = 0

                    timelines[j - 1] += prev
                    timelines[j + 1] += prev

                    offset = min(offset, j - 1)

        self.p2 = sum(timelines)

    def part_one(self) -> int:
        return self.p1

    def part_two(self) -> int:
        return self.p2
