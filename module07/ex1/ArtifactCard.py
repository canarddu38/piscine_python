from ex0 import Card


class ArtifactCard(Card):
    """
    A class representing an artifact card, inheriting from Card.

    Attributes:
        durability (int): The durability of the artifact.
        effect (str): The effect description of the artifact.
    """
    def __init__(self, name: str, cost: int, rarity: str, durability: int,
                 effect: str):
        """
        Initialize a new ArtifactCard instance.

        Args:
            name (str): The name of the card.
            cost (int): The mana cost of the card.
            rarity (str): The rarity of the card.
            durability (int): The durability of the artifact.
            effect (str): The effect description of the artifact.
        """
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        """
        Play the artifact card.

        Args:
            game_state (dict): The current state of the game.

        Returns:
            dict: Result of playing the card, including effect and mana used.
        """
        mana = game_state['mana']
        if type(mana) is int and self.is_playable(mana):
            return {
                'card_played': self.name,
                'mana_used': self.cost,
                'effect': f'Permanent: +1 {self.effect} per turn'
            }
        else:
            return {"success": False}

    def activate_ability(self) -> dict:
        """
        Activate the ability of the artifact.

        Returns:
            dict: Result of activating the ability, including current status.
        """
        if self.durability > 0:
            self.durability -= 1
            status = "active"
        else:
            status = "broken"

        return {
            'card': self.name,
            'ability_stats': {
                'effect': self.effect,
                'durability': self.durability,
                'status': status
            }
        }
