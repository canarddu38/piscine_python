#!/usr/bin/env python3
"""Intro module for the garden project.

Runs a simple script that prints basic information about a plant.
"""

if (__name__ == "__main__"):
    """Entry point for the intro script.

    Prints a welcome banner and details for a sample plant.
    """
    name = "Rose"
    height = 25
    age = 30
    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")
    print("=== End of Program ===")
