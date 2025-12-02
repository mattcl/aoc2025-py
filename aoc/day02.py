# You can copy/paste this template to start a new day

"""02: gift shop"""
import math

import aoc.util


# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        self.p1 = 0
        self.p2 = 0

        for segment in input.strip().split(","):
            parts = segment.split('-')
            digits_left = len(parts[0])
            digits_right = len(parts[1])
            left = int(parts[0])
            right = int(parts[1])

            seen = set()

            a, b = find_invalid(digits_left, digits_right, left, right, seen)
            self.p1 += a
            self.p2 += a + b

    def part_one(self) -> int:
        return self.p1

    def part_two(self) -> int:
        return self.p2


def find_invalid(digits_left, digits_right, left, right, seen):
    a = 0
    b = 0

    w_left = left
    w_right = right

    if digits_right % 2 == 1:
        w_right = 10 ** (digits_right - 1) - 1
        w_digits_right = digits_right - 1
    else:
        w_digits_right = digits_right

    if digits_left < w_digits_right:
        w_left = 10 ** (w_digits_right - 1)

    half_shift = 10 ** (w_digits_right // 2)
    cur = w_left // half_shift

    while True:
        candidate = cur * half_shift + cur

        if candidate > w_right:
            break

        if candidate >= w_left:
            seen.add(candidate)
            a += candidate

        cur += 1

    # part 2
    digits_cur = 1
    if digits_left < digits_right:
        cur = 1
    else:
        cur = left
        while cur >= 10:
            cur = cur // 10

    while True:
        shift = 10 ** digits_cur
        for replicas in range(max(digits_left // digits_cur, 3), (digits_right // digits_cur) + 1):
            candidate = build_candidate(cur, shift, replicas)

            if candidate > right:
                continue

            if candidate >= left and candidate not in seen:
                seen.add(candidate)
                b += candidate

        cur += 1
        digits_cur = int(math.log10(cur)) + 1

        if digits_cur > digits_right // 3:
            break

    return a, b


def build_candidate(chunk, shift, replicas):
    out = 0
    for _ in range(0, replicas):
        out = out * shift + chunk

    return out
