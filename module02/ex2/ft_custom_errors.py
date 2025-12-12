#!/usr/bin/env python3

class GardenError(Exception):
    """Main Garden error class"""
    def __init__(self, message=None):
        if (message is not None):
            super().__init__(message)


class WaterError(GardenError):
    """Main Garden Water related error class"""
    def __init__(self):
        super().__init__("Not enough water in the tank!")


class PlantError(GardenError):
    """Main Garden Plant related error class"""
    def __init__(self):
        super().__init__("The tomato plant is wilting!")


def get_water(water_volume: int) -> int:
    """Get water from the well"""
    if (water_volume <= 50):
        raise WaterError()
    else:
        water_volume -= 50


def get_plant_status(plant_water_level: int) -> None:
    """Get plant status according to its water level"""
    if (plant_water_level <= 0):
        raise PlantError()
    else:
        plant_water_level -= 5


def test_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        get_plant_status(-5)
    except PlantError as e:
        print(f"Caught PlantError: {e.args[0]}")

    print("\nTesting WaterError...")
    try:
        get_water(20)
    except WaterError as e:
        print(f"Caught WaterError: {e.args[0]}")

    print("\nTesting catching all garden errors...")
    try:
        get_plant_status(-5)
    except GardenError as e1:
        print(f"Caught a garden error: {e1.args[0]}")
        try:
            get_water(20)
        except GardenError as e:
            print(f"Caught a garden error: {e.args[0]}")

    print("\nAll custom error types work correctly!")


test_errors()
