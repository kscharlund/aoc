import sys
from pprint import pprint
import math
import re


def read_tiles():
    tiles = {}
    tile_strings = sys.stdin.read().split('\n\n')
    for tile_string in tile_strings:
        lines = tile_string.split('\n')
        tile_header, tile_data = lines[0], lines[1:]
        tile_id = int(re.search(r'\d+', tile_header).group(0))
        tiles[tile_id] = tile_data
    return tiles


def get_edges(tile):
    nn = len(tile)
    lr = [(tile[row][0], tile[row][-1]) for row in range(nn)]
    tb = [(tile[0][col], tile[-1][col]) for col in range(nn)]
    le, re = [''.join(x) for x in zip(*lr)]
    te, be = [''.join(x) for x in zip(*tb)]
    return (le, te, re, be)


def flip_edges(edges):
    le, te, re, be = edges
    return (le[::-1], be, re[::-1], te)


def rotate_edges(edges, clockwise_quarter_turns):
    le, te, re, be = edges
    if clockwise_quarter_turns == 0:
        return edges
    elif clockwise_quarter_turns == 1:
        return (be, le[::-1], te, re[::-1])
    elif clockwise_quarter_turns == 2:
        return (re[::-1], be[::-1], le[::-1], te[::-1])
    elif clockwise_quarter_turns == 3:
        return (te[::-1], re, be[::-1], le)
    else:
        raise ValueError(f'Clockwise quarter turns: {clockwise_quarter_turns}')


def fits(edges, board, row, col):
    if row > 0:
        if col > 0:
            return (
                edges[0] == board[row][col - 1][2]
                and edges[1] == board[row - 1][col][3]
            )
        else:
            return edges[1] == board[row - 1][col][3]
    else:
        if col > 0:
            return edges[0] == board[row][col - 1][2]
        else:
            return True


def solve(tiles, remaining, board, assignment):
    if not remaining:
        return True

    idx = len(tiles) - len(remaining)
    nn = len(board)
    row = idx // nn
    col = idx - (nn * row)
    for tile_id in remaining:
        edges = get_edges(tiles[tile_id])
        for ii in range(4):
            r_edges = rotate_edges(edges, ii)
            if fits(r_edges, board, row, col):
                board[row][col] = r_edges
                assignment[row][col] = (tile_id, False, ii)
                if solve(tiles, remaining - {tile_id}, board, assignment):
                    return True
        f_edges = flip_edges(edges)
        for ii in range(4):
            r_edges = rotate_edges(f_edges, ii)
            if fits(r_edges, board, row, col):
                board[row][col] = r_edges
                assignment[row][col] = (tile_id, True, ii)
                if solve(tiles, remaining - {tile_id}, board, assignment):
                    return True

    return False


def a(tiles):
    print(len(tiles), 'tiles')
    nn = int(len(tiles) ** 0.5)
    board = [[None for _ in range(nn)] for _ in range(nn)]
    assignment = [[None for _ in range(nn)] for _ in range(nn)]
    assert solve(tiles, set(tiles.keys()), board, assignment)
    print(assignment[0][0][0] * assignment[0][-1][0] * assignment[-1][0][0] * assignment[-1][-1][0])
    return assignment


def get_image(tile, flip, rotations, cut_borders):
    mm = len(tile)
    if flip:
        get_coord = lambda row, col: (mm - 1 - row, col)
    else:
        get_coord = lambda row, col: (row, col)
    if rotations == 0:
        get_rot_coord = get_coord
    elif rotations == 1:
        get_rot_coord = lambda row, col: get_coord(mm - 1 - col, row)
    elif rotations == 2:
        get_rot_coord = lambda row, col: get_coord(mm - 1 - row, mm - 1 - col)
    elif rotations == 3:
        get_rot_coord = lambda row, col: get_coord(col, mm - 1 - row)
    image = []
    for row in range(0 + cut_borders, mm - cut_borders):
        line = []
        for col in range(0 + cut_borders, mm - cut_borders):
            r, c = get_rot_coord(row, col)
            line.append(tile[r][c])
        image.append(''.join(line))
    return image


def make_full_image(tiles, assignment):
    img_lines = []
    for assigned_row in assignment:
        tile_row = []
        for assigned_tile in assigned_row:
            tile_id, flip, rotations = assigned_tile
            tile_row.append(get_image(tiles[tile_id], flip, rotations, 1))
        mm = len(tile_row[0])
        for ii in range(mm):
            img_lines.append(''.join(tile[ii] for tile in tile_row))
    return img_lines


def num_sea_monsters(image):
    sea_monster_pattern = [
        (0, 18),
        (1, 0), (1, 5), (1, 6), (1, 11), (1, 12), (1, 17), (1, 18), (1, 19),
        (2, 1), (2, 4), (2, 7), (2, 10), (2, 13), (2, 16),
    ]
    for flip in (False, True):
        for rot in range(4):
            fr_image = get_image(image, flip, rot, 0)
            num_monsters = 0
            for row in range(len(fr_image) - 2):
                for col in range(len(fr_image) - 19):
                    for dy, dx in sea_monster_pattern:
                        if fr_image[row + dy][col + dx] != '#':
                            break
                    else:
                        num_monsters += 1
            if num_monsters:
                return num_monsters


def b(tiles, assignment):
    full_image = make_full_image(tiles, assignment)
    print(sum(line.count('#') for line in full_image) - num_sea_monsters(full_image) * 15)


def main():
    tiles = read_tiles()
    assignment = a(tiles)
    print()
    b(tiles, assignment)


if __name__ == '__main__':
    main()
