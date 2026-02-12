#!/usr/bin/env python3

def test_error_types():

    """Demonstrate different error handling."""

    print("=== Garden Error Types Demo ===\n")

    try:
        print("Testing ValueError...")
        int("abc")
    except ValueError:
        print(f"Caught ValueError: invalid literal for int()\n")

    try:
        print("Testing ZeroDivisionError...")
        10 / 0
    except ZeroDivisionError as err:
        print(f"Caught ZeroDivisionError: {err}\n")

    try:
        print("Testing FileNotFoundError...")
        file_name = "missing.txt"
        open(file_name, "r")
    except FileNotFoundError:
        print(f"Caught FileNotFoundError: No such file '{file_name}'\n")

    try:
        print("Testing KeyError...")
        data = {}
        print(data["missing_plant"])
    except KeyError as err:
        print(f"Caught KeyError: {err}\n")

    try:
        print("Testing multiple errors together...")
        int("abc")
        10 / 0
        open("missing.txt", "r")
        data = {}
        print(data["missing_plant"])
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
