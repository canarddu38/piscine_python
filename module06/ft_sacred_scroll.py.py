#!/usr/bin/env python3

import alchemy as alchemy
import alchemy.elements as direct


def call_fn(name: str) -> str:
    try:
        match (name):
            case "create_fire":
                return alchemy.create_fire()
            case "create_water":
                return alchemy.create_water()
            case "create_earth":
                return alchemy.create_earth()
            case "create_air":
                return alchemy.create_air()
    except AttributeError:
        return "AttributeError - not exposed"


def main() -> None:
    print("\n=== Sacred Scroll Mastery ===\n")
    print("Testing direct module access:")
    print(f"alchemy.elements.create_fire(): {direct.create_fire()}")
    print(f"alchemy.elements.create_water(): {direct.create_water()}")
    print(f"alchemy.elements.create_earth(): {direct.create_earth()}")
    print(f"alchemy.elements.create_air(): {direct.create_air()}")

    print("\nTesting package-level access (controlled by __init__.py):")
    print(f"alchemy.create_fire(): {call_fn('create_fire')}")
    print(f"alchemy.create_water(): {call_fn('create_water')}")
    print(f"alchemy.create_earth(): {call_fn('create_earth')}")
    print(f"alchemy.create_air(): {call_fn('create_air')}")

    print("\nPackage metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


if __name__ == "__main__":
    main()
