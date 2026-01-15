from ex3 import CardFactory
from ex0 import Card, CreatureCard
from ex1 import ArtifactCard, SpellCard


class FantasyCardFactory(CardFactory):
    """
    A concrete factory for creating fantasy themed cards.
    """
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        """
        Create a fantasy creature card.

        Args:
            name_or_power (str | int | None, optional): Name of the creature.

        Returns:
            Card: A new creature card.
        """
        if isinstance(name_or_power, str) and \
                     (name_or_power.lower() == 'dragon'):
            return CreatureCard("Fire Dragon", 5, "Rare", 5, 5)
        return CreatureCard("Goblin Warrior", 2, "Common", 5, 2)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        """
        Create a fantasy spell card.

        Args:
            name_or_power (str | int | None, optional): Name of the spell.

        Returns:
            Card: A new spell card.
        """
        if isinstance(name_or_power, str) and \
                     (name_or_power.lower() == 'fireball'):
            return SpellCard("Fireball", 4, "Uncommon", "Fire")
        return SpellCard("Lightning Bolt", 3, "Common", "Lightning")

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        """
        Create a fantasy artifact card.

        Args:
            name_or_power (str | int | None, optional): Name of the artifact.

        Returns:
            Card: A new artifact card.
        """
        return ArtifactCard("Mana Ring", 3, "Uncommon", 5, "Mana")

    def create_themed_deck(self, size: int) -> dict:
        """
        Create a fantasy themed deck.

        Args:
            size (int): The size of the deck.

        Returns:
            dict: The created deck.
        """
        return {
            'deck': [self.create_creature() for _ in range(size)]
        }

    def get_supported_types(self) -> dict:
        """
        Get supported fantasy card types.

        Returns:
            dict: The supported types (creatures, spells, artifacts).
        """
        return {
            'creatures': ['dragon', 'goblin'],
            'spells': ['fireball'],
            'artifacts': ['mana_ring']
        }
