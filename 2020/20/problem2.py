import sys
from pprint import pprint
import math
import re


LEFT_EDGE, TOP_EDGE, RIGHT_EDGE, BOTTOM_EDGE = range(4)


class Tile:
    def __init__(self, tile_id, tile_data):
        self.id = tile_id
        self.data = tile_data
        self.flipped = False
        self.rotation = 0
        self.size = len(tile_data)
        self._edge_cache = {}

    def get_edge(self, edge):
        idx = (edge, self.flipped, self.rotation)
        if idx in self._edge_cache:
            return self._edge_cache[idx]
        if edge == LEFT_EDGE:
            ret = self._edge_cache[idx] = ''.join(self.get(row, 0) for row in range(self.size))
        elif edge == TOP_EDGE:
            ret = self._edge_cache[idx] = ''.join(self.get(0, col) for col in range(self.size))
        elif edge == RIGHT_EDGE:
            ret = self._edge_cache[idx] = ''.join(self.get(row, self.size - 1) for row in range(self.size))
        elif edge == BOTTOM_EDGE:
            ret = self._edge_cache[idx] = ''.join(self.get(self.size - 1, col) for col in range(self.size))
        else:
            raise ValueError(f'Edge {edge}?')
        return ret

    def get_data(self, trim=0):
        lines = []
        for row in range(trim, self.size - trim):
            line = []
            for col in range(trim, self.size - trim):
                line.append(self.get(row, col))
            lines.append(''.join(line))
        return lines

    def get(self, row, col):
        offset = self.size - 1
        if self.flipped:
            row = offset - row
        if self.rotation == 1:
            row, col = col, offset - row
        elif self.rotation == 2:
            row, col = offset - row, offset - col
        elif self.rotation == 3:
            row, col = offset - col, row
        return self.data[row][col]


def read_tiles():
    tiles = {}
    tile_strings = sys.stdin.read().split('\n\n')
    for tile_string in tile_strings:
        lines = tile_string.split('\n')
        tile_header, tile_data = lines[0], lines[1:]
        tile_id = int(re.search(r'\d+', tile_header).group(0))
        tile = Tile(tile_id, tile_data)
        tiles[tile_id] = tile
    return tiles


def fits(tile, board, row, col):
    if row > 0:
        if col > 0:
            return (
                tile.get_edge(LEFT_EDGE) == board[row][col - 1].get_edge(RIGHT_EDGE)
                and tile.get_edge(TOP_EDGE) == board[row - 1][col].get_edge(BOTTOM_EDGE)
            )
        else:
            return tile.get_edge(TOP_EDGE) == board[row - 1][col].get_edge(BOTTOM_EDGE)
    else:
        if col > 0:
            return tile.get_edge(LEFT_EDGE) == board[row][col - 1].get_edge(RIGHT_EDGE)
        else:
            return True


def solve(tiles, remaining, board):
    if not remaining:
        return True

    idx = len(tiles) - len(remaining)
    nn = len(board)
    row = idx // nn
    col = idx - (nn * row)
    for tile_id in remaining:
        tile = tiles[tile_id]
        tile.flipped = False
        for ii in range(4):
            tile.rotation = ii
            if fits(tile, board, row, col):
                board[row][col] = tile
                if solve(tiles, remaining - {tile_id}, board):
                    return True
        tile.flipped = True
        for ii in range(4):
            tile.rotation = ii
            if fits(tile, board, row, col):
                board[row][col] = tile
                if solve(tiles, remaining - {tile_id}, board):
                    return True
    return False


def a(tiles):
    print(len(tiles), 'tiles')
    nn = int(len(tiles) ** 0.5)
    board = [[None for _ in range(nn)] for _ in range(nn)]
    assert solve(tiles, set(tiles.keys()), board)
    print(board[0][0].id * board[0][-1].id * board[-1][0].id * board[-1][-1].id)
    return board


def make_full_image(board):
    img_lines = []
    for tile_row in board:
        img_tile_row = []
        for tile in tile_row:
            img_tile_row.append(tile.get_data(1))
        for ii in range(tile.size - 2):
            img_lines.append(''.join(td[ii] for td in img_tile_row))
    return Tile(0, img_lines)


def num_sea_monsters(image):
    sea_monster_pattern = [
        (0, 18),
        (1, 0), (1, 5), (1, 6), (1, 11), (1, 12), (1, 17), (1, 18), (1, 19),
        (2, 1), (2, 4), (2, 7), (2, 10), (2, 13), (2, 16),
    ]
    for flip in (False, True):
        image.flipped = flip
        for rot in range(4):
            image.rotation = rot
            fr_image = image.get_data(0)
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


def b(board):
    full_image = make_full_image(board)
    print(sum(line.count('#') for line in full_image.data) - num_sea_monsters(full_image) * 15)


def main():
    tiles = read_tiles()
    board = a(tiles)
    print()
    b(board)


if __name__ == '__main__':
    main()
