#!/usr/bin/env python3
"""Garden security module.

Provides a SecurePlant class enforcing non-negative properties.
"""


class SecurePlant:
    """A plant that validates height and age updates."""

    def set_height(self, height: int) -> bool:
        """Set the plant height if non-negative.

        Returns True when accepted, False otherwise.
        """
        if (height < 0):
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
            return False
        else:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")
            return True

    def set_age(self, age: int) -> bool:
        """Set the plant age if non-negative.

        Returns True when accepted, False otherwise.
        """
        if (age < 0):
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
            return False
        else:
            self.__age = age
            print(f"Age updated: {age} days [OK]")
            return True

    def get_age(self) -> int:
        """Return current age in days."""
        return self.__age

    def get_height(self) -> int:
        """Return current height in centimeters."""
        return self.__height

    def __init__(self, name, height, age):
        """Initialize a secure plant and validate initial values."""
        self.name = name
        print(f"Plant created: {name}")
        if (not self.set_height(height)):
            print("Security: Negative height rejected")
        if (not self.set_age(age)):
            print("Security: Negative age rejected")
        print("")


print("=== Garden Security System ===")
plant = SecurePlant("Rose", 25, 30)
plant.set_height(-5)
print(
    f"\nCurrent plant: {plant.name} ("
    f"{plant.get_height()}cm, {plant.get_age()} days)"
)
