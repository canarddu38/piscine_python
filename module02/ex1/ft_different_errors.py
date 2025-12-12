#!/usr/bin/env python3

def garden_operations() -> None:
    """List of errors possible for these operations"""
    # ValueError: trying to convert a bad string to int
    print(int("abc"))

    # ZeroDivisionError: dividing by zero
    print(10 / 0)

    # FileNotFoundError: opening a missing file
    with open("missing.txt", "r") as f:
        print(f.read())

    # KeyError: accessing a missing key in a dictionary
    garden = {"rose": "red", "sunflower": "yellow"}
    print(garden["missing_plant"])


def test_error_types():
    """Function to test error types"""
    print("=== Garden Error Types Demo ===\n")

    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError as e:
        print(f"Caught ValueError: {e}")

    print("\nTesting ZeroDivisionError...")
    try:
        print(10 / 0)
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")

    print("\nTesting FileNotFoundError...")
    try:
        with open("missing.txt", "r") as f:
            print(f.read())
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")

    print("\nTesting KeyError...")
    try:
        garden = {"rose": "red", "sunflower": "yellow"}
        print(garden["missing_plant"])
    except KeyError as e:
        print(f"Caught KeyError: {e}")

    print("\nTesting multiple errors together...")
    try:
        print(int("abc"))
        print(10 / 0)
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!")

    print("\nAll error types tested successfully!")


test_error_types()
