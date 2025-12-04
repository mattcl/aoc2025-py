# You can copy/paste this template to start a new day

"""04: printing department"""
from collections import deque

import aoc.util


# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        self.p1 = 0
        self.p2 = 0

        removed = deque()

        grid = [list(line) for line in input.strip().split("\n")]

        height = len(grid)
        width = len(grid[0])
        seen = [[0 for _ in range(width)] for _ in range(height)]

        for row in range(height):
            for col in range(width):
                if grid[row][col] != '@':
                    continue

                count = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        nr = row + i
                        nc = col + j

                        if nr == row and nc == col:
                            continue

                        if nr >= 0 and nr < height and nc >= 0 and nc < width:
                            if grid[nr][nc] == '@':
                                count += 1

                if count < 4:
                    self.p1 += 1
                    removed.append((row, col))

                seen[row][col] = count

        while len(removed) > 0:
            row, col = removed.pop()
            seen[row][col] = 0
            self.p2 += 1

            for i in range(-1, 2):
                for j in range(-1, 2):
                    nr = row + i
                    nc = col + j

                    if nr == row and nc == col:
                        continue

                    if nr >= 0 and nr < height and nc >= 0 and nc < width:
                        if seen[nr][nc] == 4:
                            removed.append((nr, nc))

                        seen[nr][nc] -= 1

    def part_one(self) -> int:
        return self.p1

    def part_two(self) -> int:
        return self.p2
