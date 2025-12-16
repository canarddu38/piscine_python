#!/usr/bin/env python3


class Plant:
    """Simple plant used by the factory demo."""

    def __init__(self, name, height, days):
        """Initialize a plant and announce its creation."""
        self.name = name
        self.height = height
        self.days = days
        print(f"Created: {name} ({height}cm, {days} days)")


class PlantFactory:
    """Streamlines creation of many plants at once."""

    @staticmethod
    def create_plants(initial_data: list[tuple[str, int, int]]) -> list[Plant]:
        return [Plant(name, height, age) for name, height, age in initial_data]


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plant_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]
    plants = PlantFactory.create_plants(plant_data)
    print(f"\nTotal plants created: {len(plants)}")
