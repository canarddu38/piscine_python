#!/usr/bin/env python3

import math
import sys


def parse_pos(text: str) -> tuple:
    try:
        print(f"Parsing coordinates: \"{text}\"")
        lst = text.split(',')
        if (len(lst) != 3):
            raise Exception(f"Invalid pos '{text}'")
        return create_pos(int(lst[0]), int(lst[1]), int(lst[2]))
    except Exception as e:
        print(f"Caught an Exception: {e.args[0]}")
        print(f"Error details - Type: ValueError, Args: {e.args}")


def create_pos(x: int, y: int, z: int) -> tuple:
    t = (x, y, z)
    print(f"Position created: {t}")
    return t


def distance(a: tuple, b: tuple) -> float:
    (x1, y1, z1) = a
    (x2, y2, z2) = b
    dist = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print(f"Distance between {a} and {b}: {float(int(dist * 100) / 100)}")
    return dist


scores = []
print("=== Game Coordinate System ===")


for arg in sys.argv[1:]:
    print("")
    pos2 = parse_pos(arg)
    if (pos2 is not None):
        distance((0, 0, 0), pos2)


print("\nUnpacking demonstration:")
x, y, z = create_pos(3, 4, 9)
print(f"Player at x={x}, y={y}, z={z}")
print(f"Coordinates: X={x}, Y={y}, Z={z}")
