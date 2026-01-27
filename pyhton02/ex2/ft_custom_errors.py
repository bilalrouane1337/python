#!/usr/bin/env python3

class GardenError(Exception):
    """
    Base exception for all garden-related errors.
    """


class PlantError(GardenError):
    """
    Exception raised for plant-related problems.
    """

    def __init__(self, name):
        message = f"The {name} plant is wilting!"
        super().__init__(message)


class WaterError(GardenError):
    """
    Exception raised for watering-related problems.
    """

    def __init__(self):
        message = "Not enough water in the tank!"
        super().__init__(message)


def main():
    """
    Demonstrate custom garden error handling.
    """
    print("=== Custom Garden Errors Demo ===\n")

    try:
        print("Testing PlantError...")
        raise PlantError("tomato")
    except PlantError as error:
        print(f"Caught PlantError: {error}\n")

    try:
        print("Testing WaterError...")
        raise WaterError()
    except WaterError as error:
        print(f"Caught WaterError: {error}\n")

    print("Testing catching all garden errors...")
    for error in [PlantError("tomato"), WaterError()]:
        try:
            raise error
        except GardenError as caught_error:
            print(f"Caught a garden error: {caught_error}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
