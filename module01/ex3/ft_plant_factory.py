#!/usr/bin/env python3
"""Plant factory demo.

Creates several Plant instances and displays a summary.
"""


class Plant:
    """Simple plant used by the factory demo."""

    def __init__(self, _name, _height, _days):
        """Initialize a plant and announce its creation."""
        self.name = _name
        self.height = _height
        self.days = _days
        print(f"Created: {_name} ({_height}cm, {_days} days)")


print("=== Plant Factory Output ===")
plants = [Plant("Rose", 25, 30),
          Plant("Oak", 200, 365),
          Plant("Cactus", 5, 90),
          Plant("Sunflower", 80, 45),
          Plant("Fern", 15, 120)]
print("\nTotal plants created: 5")
