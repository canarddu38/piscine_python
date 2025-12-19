#!/usr/bin/env python3

import math


def distance_3d(p1, p2):
    """Calculate the distance between two 3d point"""
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def parse_coordinates(s):
    """Parse a string representing a 3d coordinate"""
    parts = s.split(',')
    return (int(parts[0]), int(parts[1]), int(parts[2]))


def main():
    """Main function"""
    print("=== Game Coordinate System ===\n")

    origin = (0, 0, 0)
    position = (10, 20, 5)
    print(f"Position created: {position}")
    print(f"Distance between {origin} and {position}: \
{int(distance_3d(origin, position) * 100) / 100}\n")

    coord_str = "3,4,0"
    print(f'Parsing coordinates: "{coord_str}"')
    try:
        pos = parse_coordinates(coord_str)
        print(f"Parsed position: {pos}")
        print(f"Distance between {origin} and {pos}: \
{distance_3d(origin, pos)}\n")
    except Exception as e:
        print(f"Error parsing coordinates: {e}")

    invalid_str = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{invalid_str}"')
    try:
        pos = parse_coordinates(invalid_str)
    except Exception as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}\n")

    print("Unpacking demonstration:")
    x, y, z = (3, 4, 0)
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
