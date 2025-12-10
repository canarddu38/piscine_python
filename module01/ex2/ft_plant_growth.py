#!/usr/bin/env python3

class Plant:
    def __init__(self, _name, _height, _days):
        self.name = _name
        self.height = _height
        self.days = _days

    def grow(self, height):
        self.height += height

    def age(self, days):
        self.days += days
        self.grow(days)

    def get_info(self):
        print(f"{self.name}: {self.height} cm, {self.days} days old")
        return self.height


plant = Plant("Rose", 20, 30)
print("=== Day 1 ===")
growth = plant.get_info()
plant.age(6)
print("=== Day 7 ===")
growth = plant.get_info() - growth
print(f"Growth this week: +{growth}cm")
