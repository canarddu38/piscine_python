#!/usr/bin/env python3

from ex0 import CreatureCard


def main():
    """
    Main function to demonstrate abstract base class design with CreatureCard.
    """
    print("\n=== DataDeck Card Foundation ===\n")

    print("Testing Abstract Base Class Design:\n")

    creature = CreatureCard(
        "Fire Dragon",
        5,
        "Legendary",
        7,
        5
    )
    creature2 = CreatureCard(
        "Goblin Warrior",
        5,
        "Legendary",
        7,
        5
    )

    infos = creature.get_card_info()
    mana = 6
    print(f"CreatureCard Info: {infos}\n")
    print(f"Playing {creature.name} with {mana} mana available:")
    result = creature.play({'mana': mana})
    print(f"Playable: {creature.is_playable(mana)}")
    if not result.get("success") or \
            result.get("success") is True:
        print(f"Play result: {result}\n")

    print(creature.attack_target(creature2))
    print()

    mana -= 3
    print(f"Testing insufficient mana ({mana} available):")
    print(f"Playable: {creature.is_playable(mana)}")
    creature.play({'mana': mana})

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
