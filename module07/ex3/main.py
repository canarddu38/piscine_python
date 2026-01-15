#!/usr/bin/env python3

from ex3 import GameEngine, AggressiveStrategy, FantasyCardFactory


def main():
    """
    Main function to game simulation with factories and strategies.
    """
    print("\n=== DataDeck Game Engine ===\n")

    engine = GameEngine()
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    print("Configuring Fantasy Card Game...")
    engine.configure_engine(factory, strategy)

    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")

    print(f"Available types: {factory.get_supported_types()}")

    print()
    engine.simulate_turn()

    print("\nGame Report:")
    print(engine.get_engine_status())

    print("\nAbstract Factory + Strategy Pattern: \
Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
