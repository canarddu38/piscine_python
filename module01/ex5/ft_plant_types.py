#!/usr/bin/env python3
"""Different plant types for the garden project.

Defines base Plant and specialized subclasses: Flower, Tree, Vegetable.
"""


class Plant:
    """Base class representing a generic plant."""

    def __init__(self, name: str, height: int, age: int):
        """Initialize a Plant.

        Parameters:
            name: Plant name.
            height: Height in centimeters.
            age: Age in days.
        """
        self.name = name
        self.age = age
        self.height = height

    def info(self):
        """Return a formatted string describing the plant."""
        return f"{self.name}: {self.height}cm, {self.age} days"


class Flower(Plant):
    """A flowering plant with a color attribute."""

    def __init__(self, color: str, name: str, height: int, age: int) -> None:
        """Initialize a Flower derived from Plant."""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        """Print a bloom message."""
        print(f"{self.name} is blooming beautifully!")

    def info(self):
        """Return a formatted description including the flower color."""
        return f"{self.name} (Flower): {self.height}cm, {self.age} days, \
{self.color} color"


class Tree(Plant):
    """A tree with a trunk diameter attribute."""

    def __init__(
        self,
        trunk_diameter: int,
        name: str,
        height: int,
        age: int,
    ) -> None:
        """Initialize a Tree derived from Plant."""
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        """Print an estimation of produced shade area."""
        print(
            f"{self.name} provides {self.trunk_diameter * 1.56} "
            "square meters of shade"
        )


class Vegetable(Plant):
    """An edible plant with harvest season and nutritional value."""

    def __init__(
        self,
        harvest_season: int,
        nutritional_value: int,
        name: str,
        height: int,
        age: int,
    ) -> None:
        """Initialize a Vegetable derived from Plant."""
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        super().__init__(name, height, age)

    def info(self):
        """Return a formatted description including harvest season."""
        return (f"{self.name} (Vegetable): {self.height}cm, {self.age} days, "
                f"{self.harvest_season} harvest")

    def nutrition(self):
        """Print the key nutritional value."""
        print(f"{self.name} is rich in {self.nutritional_value}")


rose = Flower("red", "Rose", 25, 30)
tulip = Flower("yellow", "Tulip", 20, 25)

oak = Tree(50, "Oak", 500, 1825)
pine = Tree(40, "Pine", 600, 2000)

tomato = Vegetable("summer", "vitamin C", "Tomato", 80, 90)
carrot = Vegetable("autumn", "beta-carotene", "Carrot", 30, 70)


print("=== Garden Plant Types ===")
print(rose.info())
rose.bloom()
print("")
print(oak.info())
oak.produce_shade()
print("")
print(tomato.info())
tomato.nutrition()
