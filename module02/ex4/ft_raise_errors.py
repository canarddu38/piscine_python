#!/usr/bin/env python3

def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> str:
    """Validate user input and returns plant status if no failure"""
    if (plant_name is None):
        raise ValueError("Plant name cannot be empty")
    if (water_level < 1):
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if (water_level > 10):
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    if (sunlight_hours < 2):
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    if (sunlight_hours > 12):
        raise ValueError(f"Sunlight hours {sunlight_hours} is too high \
(max 2)")
    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    """Simple plant checking testing function"""
    print("=== Garden Plant Health Checker ===\n")
    try:
        print("Testing good values...")
        print(check_plant_health("tomato", 5, 5))
    except ValueError as e:
        print(f"Error: {e.args[0]}")

    try:
        print("\nTesting empty plant name...")
        check_plant_health(None, 5, 5)
    except ValueError as e:
        print(f"Error: {e.args[0]}")

    try:
        print("\nTesting bad water level...")
        check_plant_health("tomato", 15, 5)
    except ValueError as e:
        print(f"Error: {e.args[0]}")

    try:
        print("\nTesting bad sunlight hours...")
        check_plant_health("tomato", 5, 0)
    except ValueError as e:
        print(f"Error: {e.args[0]}")

    print("\nAll error raising tests completed!")


test_plant_checks()
