#!/usr/bin/env python3
import sys
import math

def create_position(x, y, z):
    return (x, y, z)


def distance_3d(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt(
        (x2 - x1) ** 2 +
        (y2 - y1) ** 2 +
        (z2 - z1) ** 2
    )


def parse_coordinates(coord_string):
    parts = coord_string.split(",")
    return (int(parts[0]), int(parts[1]), int(parts[2]))


if __name__ == "__main__":
    print("=== Game Coordinate System ===")

    zero_position = (0, 0, 0)
    initial_position = create_position(10, 20, 5)
    print(f"Position created: {initial_position}")

    dist = distance_3d(zero_position, initial_position)
    print(f"Distance between {zero_position} and {initial_position}: {dist:.2f}")

    coord_text = "3,4,0"
    print(f'Parsing coordinates: "{coord_text}"')
    parsed_position = parse_coordinates(coord_text)
    print(f"Parsed position: {parsed_position}")

    dist2 = distance_3d(zero_position, parsed_position)
    print(f"Distance between {zero_position} and {parsed_position}: {dist2}")

    invalid_text = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{invalid_text}"')
    try:
        parse_coordinates(invalid_text)
    except Exception as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")

    print("Unpacking demonstration:")
    x, y, z = parsed_position
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")
