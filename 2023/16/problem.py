from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
import sys
from pprint import pprint
import math


def get_data():
    grid = {}
    for row, line in enumerate(open(sys.argv[1])):
        for col, c in enumerate(line.strip()):
            grid[Pt(row, col)] = c
    return grid, row + 1, col + 1


@dataclass(frozen=True)
class Pt:
    y: int
    x: int

    def __add__(self, other: Pt) -> Pt:
        return Pt(self.y + other.y, self.x + other.x)

    def __sub__(self, other: Pt) -> Pt:
        return Pt(self.y - other.y, self.x - other.x)

    def __neg__(self) -> Pt:
        return Pt(-self.y, -self.x)

    def __invert__(self) -> Pt:
        return Pt(self.x, self.y)


@dataclass(frozen=True)
class Beam:
    pos: Pt
    dir: Pt


def cont(beam: Beam) -> list[Beam]:
    return [Beam(beam.pos + beam.dir, beam.dir)]


def split(beam: Beam) -> list[Beam]:
    new_dir = ~beam.dir
    return [
        Beam(beam.pos - new_dir, -new_dir),
        Beam(beam.pos + new_dir, new_dir),
    ]


def deflect(beam: Beam, inv: bool) -> list[Beam]:
    new_dir = ~beam.dir if not inv else -(~beam.dir)
    return [Beam(beam.pos + new_dir, new_dir)]


def new_beams(beam: Beam, g: str) -> list[Beam]:
    match g:
        case '.':
            return cont(beam)
        case '\\':
            return deflect(beam, False)
        case '/':
            return deflect(beam, True)
        case '|':
            return split(beam) if beam.dir.x else cont(beam)
        case '-':
            return split(beam) if beam.dir.y else cont(beam)


def visit(grid, n_rows, n_cols, start_beam):
    visited = defaultdict(set)
    beams = deque([start_beam])
    while beams:
        beam = beams.popleft()
        if beam.pos not in visited or beam.dir not in visited[beam.pos]:
            visited[beam.pos].add(beam.dir)
            for new_beam in new_beams(beam, grid[beam.pos]):
                if 0 <= new_beam.pos.y < n_rows and 0 <= new_beam.pos.x < n_cols:
                    beams.append(new_beam)
    return visited

def a(data):
    grid, n_rows, n_cols = data
    print(len(visit(grid, n_rows, n_cols, Beam(Pt(0, 0), Pt(0, 1)))))


def b(data):
    grid, n_rows, n_cols = data
    max_val = 0
    for row in range(n_rows):
        v0 = visit(grid, n_rows, n_cols, Beam(Pt(row, 0), Pt(0, 1)))
        v1 = visit(grid, n_rows, n_cols, Beam(Pt(row, n_cols - 1), Pt(0, -1)))
        max_val = max(max_val, len(v0), len(v1))
    for col in range(n_cols):
        v0 = visit(grid, n_rows, n_cols, Beam(Pt(0, col), Pt(1, 0)))
        v1 = visit(grid, n_rows, n_cols, Beam(Pt(n_rows - 1, col), Pt(-1, 0)))
        max_val = max(max_val, len(v0), len(v1))
    print(max_val)


def main():
    data = get_data()
    a(data)
    print()
    b(data)


if __name__ == "__main__":
    main()
