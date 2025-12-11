#!/usr/bin/env python3
"""Plant growth simulation utilities.

Provides a Plant class with methods to grow and age the plant.
"""


class Plant:
    """Represents a plant with basic growth behavior."""

    def __init__(self, _name, _height, _days):
        """Initialize a plant.

        Parameters:
            _name: Plant name.
            _height: Height in centimeters.
            _days: Current age in days.
        """
        self.name = _name
        self.height = _height
        self.days = _days

    def grow(self, height):
        """Increase plant height by the given amount in cm."""
        self.height += height

    def age(self, days):
        """Increase plant age and grow by the same number of days."""
        self.days += days
        self.grow(days)

    def get_info(self):
        """Print and return the current height of the plant."""
        print(f"{self.name}: {self.height} cm, {self.days} days old")
        return self.height


plant = Plant("Rose", 20, 30)
print("=== Day 1 ===")
growth = plant.get_info()
plant.age(6)
print("=== Day 7 ===")
growth = plant.get_info() - growth
print(f"Growth this week: +{growth}cm")
