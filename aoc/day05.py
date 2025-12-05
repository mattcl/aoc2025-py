# You can copy/paste this template to start a new day

"""05: cafeteria"""
import aoc.util


class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        self.p1 = 0
        self.p2 = 0

        parts = input.strip().split("\n\n")

        ranges = []

        for line in parts[0].split("\n"):
            ends = line.split("-")
            x = int(ends[0])
            y = int(ends[1])
            ranges.append((min(x, y), max(x, y)))

        ranges.sort()

        merged = []

        cur = ranges[0]

        for i in range(1, len(ranges)):
            if overlaps(cur, ranges[i]):
                cur = merge(cur, ranges[i])
            else:
                self.p2 += cur[1] - cur[0] + 1
                merged.append(cur)
                cur = ranges[i]

        self.p2 += cur[1] - cur[0] + 1
        merged.append(cur)

        for line in parts[1].split("\n"):
            id = int(line)

            left = 0
            right = len(merged) - 1

            while left <= right:
                mid = left + (right - left) // 2
                start, end = merged[mid]

                if contains(start, end, id):
                    print(id)
                    self.p1 += 1
                    break

                if end < id:
                    left = mid + 1
                elif start > id and mid > 0:
                    right = mid - 1
                else:
                    break

    def part_one(self) -> int:
        return self.p1

    def part_two(self) -> int:
        return self.p2


def contains(start, end, id):
    return id >= start and id <= end


def overlaps(left, right):
    return (left[0] <= right[0] and right[1] <= left[1]) \
            or (right[0] < left[0] and left[1] < right[1]) \
            or (left[0] <= right[0] and right[0] <= left[1] and left[1] < right[1]) \
            or (right[0] < left[0] and left[0] <= right[1] and right[1] <= left[1])


def merge(left, right):
    return (min(left[0], right[0]), max(left[1], right[1]))
