#!/usr/bin/env python3

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    unit_type = None
    if (unit == "packets"):
        unit_type = "packets available"
    elif (unit == "grams"):
        unit_type = "grams total"
    elif (unit == "area"):
        unit_type = "square meters"
    if (unit_type is not None):
        print(f"{seed_type.title()} seeds: ", end='')
        if (unit == "area"):
            print("covers ", end='')
        print(quantity, end=' ')
        print(unit_type)
    else:
        print("Unknown unit type")
