#!/usr/bin/env python3

from ex1 import Deck, SpellCard, ArtifactCard
from ex0 import CreatureCard


def main():
    print("\n=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")
    deck = Deck()
    deck.add_card(SpellCard(
        "Lightning Bolt",
        3,
        "Rare",
        "damage"
    ))
    deck.add_card(ArtifactCard(
        "Mana Crystal",
        2,
        "Rare",
        1,
        "mana"
    ))
    deck.add_card(CreatureCard(
        "Fire Dragon",
        7,
        "Legendary",
        12,
        50
    ))
    print(f"Deck stats: {deck.get_deck_stats()}")
    while len(deck.cards) > 0:
        card = deck.draw_card()
        print(f"\nDrew: {card.name} (\
{card.__class__.__name__.replace('Card', '')})")
        result = card.play({'mana': 999})
        print(f"Play result: {result}")

    print("\nPolymorphism in action: Same interface, \
different card behaviors!")


if __name__ == "__main__":
    main()
