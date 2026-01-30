#!/usr/bin/env python3

import math

def calculate_3d_distance(p0, p1):

    distance = math.sqrt( pow(p0[0] - int(p1[0]), 2) + pow(p0[1] - int(p1[1]), 2) + pow(p0[2] - int(p1[2]), 2))
    return f"Distance between {p0} and {p1}: {distance:.2f}\n"


def split_coordinates(coord_string):
    parts = coord_string.split(",")
    return (int(parts[0]), int(parts[1]), int(parts[2]))


if __name__ == "__main__":

    zero_position = (0, 0, 0)

    initial_position = (10, 20, 5)
    print(f"Position created: {initial_position}")
    try:
        message = calculate_3d_distance(zero_position, initial_position)
    except Exception as e:
        print(e)
    else:
        print(message)

    parsing_position = split_coordinates("3,4,0")
    print(f"Parsing coordinates: \"{parsing_position[0]},{parsing_position[1]},{parsing_position[2]}\"")
    try:
        message = calculate_3d_distance(zero_position, parsing_position)
    except Exception as e:
        print(e)
    else:
        print(message)

    invalid_position = ("abc", "def", "ghi")
    print("Parsing invalid coordinates: \"abc,def,ghi\"")
    try:
        message = calculate_3d_distance(zero_position, invalid_position)
    except Exception as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
    else:
        print(message)

