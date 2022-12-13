import sys
from pprint import pprint
from copy import deepcopy


def adjacent_cartesian(layout, row, col):
    return [(row + dy, col + dx)
            for dy in (-1, 0, 1)
            for dx in (-1, 0, 1)]


def adjacent_line_of_sight(layout, row, col):
    def find_in_line(dy, dx):
        rr, cc = row + dy, col + dx
        while 0 <= rr < len(layout) and 0 <= cc < len(layout[rr]):
            if layout[rr][cc] == 'L':
                return (rr, cc)
            rr, cc = rr + dy, cc + dx
        return None
    adj = []
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if dy == dx == 0:
                continue
            c = find_in_line(dy, dx)
            if c:
                adj.append(c)
    return adj


def read_layout():
    return [line.strip() for line in sys.stdin.readlines()]


def create_graph(layout, adjacent_coords):
    occupied = [[False for seat in line] for line in layout]
    adj = [[None for seat in line] for line in layout]
    for row, line in enumerate(layout):
        for col, seat in enumerate(line):
            if seat == 'L':
                adj_seats = []
                for adj_row, adj_col in adjacent_coords(layout, row, col):
                    if (
                        0 <= adj_row < len(layout)
                        and 0 <= adj_col < len(line)
                        and not (adj_row == row and adj_col == col)
                        and layout[adj_row][adj_col] == 'L'
                    ):
                        adj_seats.append((adj_row, adj_col))
                adj[row][col] = adj_seats
    return occupied, adj


def next_state(current_state, adj_occupied, threshold):
    if current_state:
        if adj_occupied > threshold:
            next_state = False
        else:
            next_state = True
    else:
        if adj_occupied == 0:
            next_state = True
        else:
            next_state = False
    return next_state


def simulate(occupied, adj, threshold):
    change_occurred = True
    while change_occurred:
        change_occurred = False
        next_occupied = deepcopy(occupied)
        for row, line in enumerate(adj):
            for col, adj_seat in enumerate(line):
                if not adj_seat:
                    continue
                adj_occupied = sum(occupied[r][c] for r, c in adj_seat)
                next_occupied[row][col] = next_state(
                    occupied[row][col], adj_occupied, threshold
                )
                if next_occupied[row][col] != occupied[row][col]:
                    change_occurred = True
        occupied = next_occupied
    return occupied


def a(layout):
    occupied, adj = create_graph(layout, adjacent_cartesian)
    occupied = simulate(occupied, adj, 3)
    print(sum(sum(line) for line in occupied))


def b(layout):
    occupied, adj = create_graph(layout, adjacent_line_of_sight)
    occupied = simulate(occupied, adj, 4)
    print(sum(sum(line) for line in occupied))


def main():
    layout = read_layout()
    pprint(layout)
    a(layout)
    print()
    b(layout)


if __name__ == '__main__':
    main()
