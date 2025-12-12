#!/usr/bin/env python3

import sys
import math


def parse_pos(text: str) -> tuple:
    try:
        print(f"Parsing coordinates: \"{text}\"")
        lst = text.split(',')
        if (len(lst) != 3):
            raise Exception(f"Invalid pos '{text}'")
        return create_pos(int(lst[0]), int(lst[1]), int(lst[2]))
    except Exception as e:
        print(f"Caught an Exception: {e.args[0]}")


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
print("=== Game Coordinate System ===\n")

pos1 = create_pos(10, 20, 5)
distance((0, 0, 0), pos1)

print("")
pos2 = parse_pos("3,4,0")
distance((0, 0, 0), pos2)

print("")
pos2 = parse_pos("abc,def,ghi")
distance((0, 0, 0), pos2)