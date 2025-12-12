#!/usr/bin/env python3

class GardenError(Exception):
    """Main Garden error class"""
    def __init__(self, message=None):
        if (message is not None):
            super().__init__(message)


class WaterError(GardenError):
    """Main Garden Water related error class"""
    def __init__(self, message: str) -> None:
        super().__init__(message)


class PlantError(GardenError):
    """Main Garden Plant related error class"""
    def __init__(self, message: str) -> None:
        super().__init__(message)


class Plant:
    """Basic plant class for our garden"""
    def __init__(self, name: str, water_level: int,
                 sunlight_level: int) -> None:
        if (name is None):
            raise PlantError("Plant name cannot be empty!")
        self.name = name
        self.water_level = water_level
        self.sunlight_level = sunlight_level


class GardenManager:
    """
    Garden Manager that can handle multiple plants and water them
    """
    def __init__(self):
        print("=== Garden Management System ===\n")
        self.plants = []
        self.tank = 100

    def get_water(self, amount: int) -> int:
        """Fetch water from the tank"""
        if (amount <= self.tank and amount > 0):
            self.tank -= amount
            return amount
        else:
            raise GardenError("Not enough water in tank")

    def check_plant_health(self) -> None:
        """Validate user input and returns plant status if no failure"""
        for plant in self.plants:
            try:
                if (plant.water_level < 1):
                    raise WaterError(f"Water level {plant.water_level} is too\
 low (min 1)")
                if (plant.water_level > 10):
                    raise WaterError(f"Water level {plant.water_level} is too\
 high (max 10)")
                if (plant.sunlight_level < 2):
                    raise PlantError(f"Sunlight hours {plant.sunlight_level} \
is too low (min 2)")
                if (plant.sunlight_level > 12):
                    raise PlantError(f"Sunlight hours {plant.sunlight_level} \
is too high (max 2)")
                print(f"{plant.name}: healthy (water: {plant.water_level}, \
sun: {plant.sunlight_level})")
            except GardenError as e:
                print(f"Error checking {plant.name}: {e.args[0]}")

    def add_plant(self, plant_name: str, water_level: int,
                  sunlight_level: int) -> None:
        try:
            self.plants.append(Plant(plant_name, water_level,
                                     sunlight_level))
            print(f"Added {plant_name} successfully")
        except PlantError as e:
            print(f"Error adding plant: {e.args[0]}")

    def water_plant(self) -> None:
        """Function to water the plants"""
        print("Opening watering system")
        try:
            for plant in self.plants:
                try:
                    plant.water_level += self.get_water(5)
                    print(f"Watering {plant.name} - success")
                except GardenError as e:
                    print(f"Caught GardenError: {e.args[0]}")
        finally:
            print("Closing watering system (cleanup)")


def test_garden_manager() -> None:
    """Test garden manager"""
    try:
        manager = GardenManager()
        manager.add_plant("tomato", 0, 8)
        manager.add_plant("lettuce", 10, 8)
        manager.add_plant(None, 5, 8)

        print("\nWatering plants...")
        manager.water_plant()

        print("\nChecking plant health...")
        manager.check_plant_health()

        print("\nTesting error recovery...")
        try:
            manager.get_water(100)
        except GardenError as e:
            print(f"Caught GardenError: {e.args[0]}")
        finally:
            print("System recovered and continuing...")
    finally:
        print("\nGarden management system test complete!")


test_garden_manager()
