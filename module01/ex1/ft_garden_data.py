#!/usr/bin/env python3

class Plant:
    def __init__(self, _name, _height, _age):
        self.name = _name
        self.height = _height
        self.age = _age


print("=== Garden Plant Registry ===")
plants = [Plant("Rose", 20, 30),
          Plant("Lilas", 50, 150),
          Plant("Cactus", 15, 120)]
for plant in plants:
    print(f"{plant.name}: {plant.height} cm, {plant.age} days old")
