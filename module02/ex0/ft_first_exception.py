#!/usr/bin/env python3

def check_temperature(temp_str: str) -> int:
    """Simple temperature checking for plants"""
    print(f"Testing temperature: {temp_str}")
    try:
        temperature = int(temp_str)
        if (temperature < 0):
            print(f"Error: {temperature}°C is too cold for plants (min 0°C)")
        elif (temperature > 40):
            print(f"Error: {temperature}°C is too hot for plants (max 40°C)")
        else:
            print(f"Temperature {temperature}°C is perfect for plants!")
            return temperature
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")


def test_temperature_input() -> None:
    """Tests multiple mandatory tests to check if the function works."""
    print("=== Garden Temperature Checker ===\n")
    test_inputs = ["25", "abc", "100", "-50"]
    for test in test_inputs:
        check_temperature(test)
        print("")
    print("All tests completed - program didn't crash!")


test_temperature_input()
