import sys
from pprint import pprint
import math


def get_data():
    mapping, image_data = open(sys.argv[1]).read().split("\n\n")
    image = {}
    for y, line in enumerate(image_data.split()):
        for x, v in enumerate(line):
            image[(y, x)] = 1 if v == "#" else 0
    return mapping, image, y, x


def encode_neighborhood(image, y, x, outside):
    n = 0
    n += image.get((y - 1, x - 1), outside) << 8
    n += image.get((y - 1, x), outside) << 7
    n += image.get((y - 1, x + 1), outside) << 6
    n += image.get((y, x - 1), outside) << 5
    n += image.get((y, x), outside) << 4
    n += image.get((y, x + 1), outside) << 3
    n += image.get((y + 1, x - 1), outside) << 2
    n += image.get((y + 1, x), outside) << 1
    n += image.get((y + 1, x + 1), outside) << 0
    return n


def a(data, iters=2):
    mapping, image, max_y, max_x = data
    min_y, min_x = 0, 0
    outside = 0
    for _ in range(iters):
        new_image = {}
        new_outside = 1 if mapping[511 * outside] == "#" else 0
        for y in range(min_y - 1, max_y + 1 + 1):
            for x in range(min_x - 1, max_x + 1 + 1):
                n = encode_neighborhood(image, y, x, outside)
                new_image[(y, x)] = 1 if mapping[n] == "#" else 0
        min_y -= 1
        min_x -= 1
        max_y += 1
        max_x += 1
        image, outside = new_image, new_outside
    assert not outside
    print(sum(image.values()))


def b(data):
    a(data, 50)


def main():
    data = get_data()
    a(data)
    print()
    b(data)


if __name__ == "__main__":
    main()
