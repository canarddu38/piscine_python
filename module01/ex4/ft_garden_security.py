#!/usr/bin/env python3

class SecurePlant:
    """A plant that validates height and age updates."""

    def set_height(self, height: int) -> None:
        """Set the plant height if non-negative.

        Returns True when accepted, False otherwise.
        """
        if (height < 0):
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")

    def set_age(self, age: int) -> None:
        """Set the plant age if non-negative.

        Returns True when accepted, False otherwise.
        """
        if (age < 0):
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = age
            print(f"Age updated: {age} days [OK]")

    def get_age(self) -> int:
        """Return current age in days."""
        return self.__age

    def get_height(self) -> int:
        """Return current height in centimeters."""
        return self.__height

    def __init__(self, name, height, age):
        """Initialize a secure plant and validate initial values."""
        self.name = name
        self.__age = age
        self.__height = height
        print(f"Plant created: {name}\n")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose", 25, 30)
    plant.set_height(-5)
    print(
        f"\nCurrent plant: {plant.name} ("
        f"{plant.get_height()}cm, {plant.get_age()} days)"
    )
