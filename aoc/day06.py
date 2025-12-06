"""06: trash compactor"""
import aoc.util


class Value:
    def __init__(self, col_idx, mul=False):
        self.col_idx = col_idx
        self.last_idx = 10000000
        self.column = [0, 0, 0, 0, 0]
        self.normal = 1 if mul else 0
        self.max_col = 0
        self.mul = mul

    def append_normal(self, val):
        if self.mul:
            self.normal *= val
        else:
            self.normal += val

    def insert_digit(self, col, digit):
        self.column[col] = 10 * self.column[col] + digit
        self.max_col = max(self.max_col, col)

    def column_val(self):
        out = self.column[0]
        if self.mul:
            for i in range(1, self.max_col + 1):
                out *= self.column[i]
        else:
            for i in range(1, self.max_col + 1):
                out += self.column[i]

        return out


class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        self.p1 = 0
        self.p2 = 0

        lines = [line for line in input.strip().split("\n")]

        vals = []

        for idx, ch in enumerate(lines.pop()):
            if ch == '*':
                vals.append(Value(idx, True))
            elif ch == '+':
                vals.append(Value(idx, False))
            else:
                continue

            le = len(vals)
            if le > 1:
                vals[le - 2].last_idx = idx - 1

        for line in lines:
            for i in range(len(vals)):
                cur = 0
                stop = min(vals[i].last_idx, len(line))
                for cur_idx in range(vals[i].col_idx, stop):
                    b = line[cur_idx]
                    if b.isdigit():
                        d = int(b)
                        rel_idx = cur_idx - vals[i].col_idx
                        cur = cur * 10 + d
                        vals[i].insert_digit(rel_idx, d)

                if cur > 0:
                    vals[i].append_normal(cur)

        for val in vals:
            self.p1 += val.normal
            self.p2 += val.column_val()

    def part_one(self) -> int:
        return self.p1

    def part_two(self) -> int:
        return self.p2
