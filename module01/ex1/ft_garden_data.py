#!/usr/bin/env python3
"""Data structures for the garden project.

Defines a simple Plant class and prints a registry of plants.
"""


class Plant:
    """Represents a plant with a name, height, and age."""

    def __init__(self, _name, _height, _age):
        """Initialize a new plant.

        Parameters:
            _name: The plant name.
            _height: The plant height in centimeters.
            _age: The plant age in days.
        """
        self.name = _name
        self.height = _height
        self.age = _age


print("=== Garden Plant Registry ===")
plants = [Plant("Rose", 20, 30),
          Plant("Lilas", 50, 150),
          Plant("Cactus", 15, 120)]
for plant in plants:
    print(f"{plant.name}: {plant.height} cm, {plant.age} days old")
