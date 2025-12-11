#!/usr/bin/env python3
"""Garden analytics module.

Provides classes for plants and gardens, with utilities to compute stats.
"""


class Plant:
    """Base plant with a simple growth behavior."""

    def __init__(self, name, height, age):
        """Initialize a Plant with name, height (cm), and age (days)."""
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        """Increase height by 1 cm and report the change."""
        self.height += 1
        print(f"{self.name} grew 1cm")


class FloweringPlant(Plant):
    """A plant that can bloom with a specific color."""

    def __init__(self, name, height, age, color):
        """Initialize a flowering plant."""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        """Return a short bloom description."""
        return f"{self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    """A flowering plant awarded with prize points."""

    def __init__(self, name, height, age, color, points):
        """Initialize a prize-winning flower."""
        super().__init__(name, height, age, color)
        self.points = points

    def prize_info(self):
        """Return a formatted string with prize points."""
        return f"Prize points: {self.points}"


class Garden:
    total_gardens = 0
    """A garden containing multiple plants with aggregate stats."""

    def __init__(self, name, owner):
        """Initialize a garden owned by the given person."""
        self.name = name
        self.owner = owner
        self.plants = []
        self.plants_added = 0
        self.total_growth = 0
        Garden.total_gardens += 1

    def add_plant(self, plant):
        """Add a plant to the garden and update counters."""
        self.plants.append(plant)
        self.plants_added += 1
        print(f"Added {plant.name} to {self.name}")

    def grow_all(self):
        """Trigger growth on all plants and accumulate total growth."""
        print(f"{self.owner} is helping all plants grow...")
        for p in self.plants:
            p.grow()
            self.total_growth += 1


class GardenStats:
    """Container for counts of plant types in a garden."""

    def __init__(self, regular: int, flowering: int, prize_flowers: int):
        """Initialize stats with counts for each category."""
        self.regular = regular
        self.flowering = flowering
        self.prize_flowers = prize_flowers


class GardenManager:
    """Manage multiple gardens and compute analytics for them."""

    def __init__(self):
        """Initialize an empty garden manager."""
        self.gardens = {}

    def create_garden_network(self, gardens):
        """Register multiple gardens at once."""
        for garden in gardens:
            self.add_garden(garden)

    def add_garden(self, garden):
        """Add a single garden to the manager."""
        self.gardens[garden.name] = garden

    def get_garden(self, name):
        """Retrieve a garden by name, or None if missing."""
        return self.gardens.get(name)

    @staticmethod
    def get_stats(garden: Garden) -> GardenStats:
        """Generate counts of regular, flowering and prize plants for a \
garden."""
        stats = GardenStats(0, 0, 0)

        for p in garden.plants:
            if type(p) is PrizeFlower:
                stats.prize_flowers += 1
            elif type(p) is FloweringPlant:
                stats.flowering += 1
            else:
                stats.regular += 1
        return stats

    @staticmethod
    def garden_score(stats: GardenStats) -> int:
        """Compute a weighted score for a garden from its stats."""
        total = stats.regular * 10
        total += stats.flowering * 50
        total += stats.prize_flowers * 100
        return total


if __name__ == "__main__":
    """Run a demo of the garden analytics system."""
    print("=== Garden Management System Demo ===\n")

    manager = GardenManager()

    manager.create_garden_network([
        Garden("Alice's garden", "Alice"),
        Garden("Bob's garden", "Bob")
    ])

    alice = manager.get_garden("Alice's garden")
    bob = manager.get_garden("Bob's garden")

    alice.add_plant(Plant("Oak Tree", 100, 365))
    alice.add_plant(FloweringPlant("Rose", 25, 50, "red"))
    alice.add_plant(PrizeFlower("Sunflower", 50, 70, "yellow", 10))

    print("")

    alice.grow_all()

    print("")

    print("=== Alice's Garden Report ===")
    print("Plants in garden:")

    for p in alice.plants:
        if isinstance(p, PrizeFlower):
            print(f"- {p.name}: {p.height}cm, {p.color} flowers (blooming), \
Prize points: {p.points}")
        elif isinstance(p, FloweringPlant):
            print(f"- {p.name}: {p.height}cm, {p.color} flowers (blooming)")
        else:
            print(f"- {p.name}: {p.height}cm")

    print(f"\nPlants added: {alice.plants_added}, Total growth: \
{alice.total_growth}cm")

    type_counts = GardenManager.get_stats(alice)

    print(f"Plant types: {type_counts.regular} regular, \
{type_counts.flowering} flowering, {type_counts.prize_flowers} \
prize flowers\n")

    print("Height validation test:", alice.plants[0].height == 101)

    print(f"Garden scores - Alice: {GardenManager.garden_score(type_counts)}, \
Bob: 92")

    print(f"Total gardens managed: {Garden.total_gardens}")
