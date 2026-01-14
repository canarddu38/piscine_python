#!/usr/bin/env python3

from ex4 import TournamentPlatform, TournamentCard


def main():
    print("=== DataDeck Tournament Platform ===\n")

    platform = TournamentPlatform()

    print("Registering Tournament Cards...\n")

    dragon = TournamentCard(
        "Fire Dragon",
        cost=5,
        rarity="Legendary",
        attack_power=80,
        defense_power=60,
        rating=1200
    )
    wizard = TournamentCard(
        "Ice Wizard",
        cost=4,
        rarity="Epic",
        attack_power=70,
        defense_power=40,
        rating=1150
    )

    dragon_id = platform.register_card(dragon)
    print(f"{dragon.name} (ID: {dragon_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {dragon.calculate_rating()}")
    print(f"- Record: {dragon.wins}-{dragon.losses}\n")

    wizard_id = platform.register_card(wizard)
    print(f"{wizard.name} (ID: {wizard_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {wizard.calculate_rating()}")
    print(f"- Record: {wizard.wins}-{wizard.losses}")

    print("Creating tournament match...")
    result = platform.create_match(dragon_id, wizard_id)
    print(f"Match result: {result}\n")

    print("Tournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for i, entry in enumerate(leaderboard, 1):
        print(f"{i}. {entry['name']} - Rating: {entry['rating']} \
({entry['record']})")

    print("Platform Report:")
    print(platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
