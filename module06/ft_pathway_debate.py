#!/usr/bin/env python3

from alchemy.transmutation import lead_to_gold, stone_to_gem, \
                                  philosophers_stone, elixir_of_life
import alchemy


def main():
    """
    Main function to demonstrate absolute and relative import pathways.
    """
    print("\n=== Pathway Debate Mastery ===\n")
    print("Testing Absolute Imports (from basic.py):")
    print(f"lead_to_gold(): {lead_to_gold()}")
    print(f"stone_to_gem(): {stone_to_gem()}")

    print("\nTesting Relative Imports (from advanced.py):")
    print(f"philosophers_stone(): {philosophers_stone()}")
    print(f"elixir_of_life(): {elixir_of_life()}")

    print("\nTesting Package Access:")
    print(f"alchemy.transmutation.lead_to_gold(): \
{alchemy.transmutation.lead_to_gold()}")
    print(f"alchemy.transmutation.philosophers_stone(): \
{alchemy.transmutation.philosophers_stone()}")

    print("\nBoth pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    main()
