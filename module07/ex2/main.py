from ex2 import Magical, Combatable, EliteCard
from ex0 import Card


def main():
    print("=== DataDeck Ability System ===\n")

    print("EliteCard capabilities:")

    card_methods = [m for m in dir(Card) if not m.startswith('__')
                    and not m.startswith('_')]
    combat_methods = [m for m in dir(Combatable) if not m.startswith('__')
                      and not m.startswith('_')]
    magic_methods = [m for m in dir(Magical) if not m.startswith('__')
                     and not m.startswith('_')]

    print(f"- Card: {card_methods}")
    print(f"- Combatable: {combat_methods}")
    print(f"- Magical: {magic_methods}")

    print("\nPlaying Arcane Warrior (Elite Card):")

    elite_card = EliteCard(
        "Arcane Warrior",
        5,
        "Rare",
        attack_power=5,
        defense=3,
        mana=4
    )

    print("\nCombat phase:")
    print(f"Attack result: {elite_card.attack('Enemy')}")
    print(f"Defense result: {elite_card.defend(5)}")

    print("\nMagic phase:")
    spell = elite_card.cast_spell('Fireball', ['Enemy1', 'Enemy2'])
    print(f"Spell cast: {spell}")
    print(f"Mana channel: {elite_card.channel_mana(3)}")

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
