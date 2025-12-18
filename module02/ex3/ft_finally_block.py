#!/usr/bin/env python3

def water_plants(plant_list: list[str]) -> None:
    """Function to water the plants"""
    print("Opening watering system")
    try:
        for plant in plant_list:
            print("Watering "+plant)
        print("Watering completed successfully!")
    except Exception:
        print(f"Error: Cannot water {plant} - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """Simple test function for the garden watering system"""
    print("=== Garden Watering System ===\n")
    try:
        print("Testing normal watering...")
        water_plants(["tomato", "lettuce", "carrots"])

        print("\nTesting with error...")
        water_plants(["tomato", None])
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("\nCleanup always happens, even with errors!")


# test_watering_system()
