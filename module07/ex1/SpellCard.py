from ex0 import Card, CreatureCard


class SpellCard(Card):
    """
    A class representing a spell card, inheriting from Card.

    Attributes:
        effect_type (str): The type of effect the spell has.
    """
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        """
        Initialize a new SpellCard instance.

        Args:
            name (str): The name of the card.
            cost (int): The mana cost of the card.
            rarity (str): The rarity of the card.
            effect_type (str): The type of effect the spell has.
        """
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        """
        Play the spell card.

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
                'effect': f'Deal {self.cost} {self.effect_type} to target'
            }
        else:
            return {"success": False}

    def resolve_effect(self, targets: list) -> dict:
        """
        Resolve the effect of the spell on targets.

        Args:
            targets (list): A list of targets for the spell.

        Returns:
            dict: The result of resolving the effect.
        """
        affected_creatures = []
        for target in targets:
            if isinstance(target, CreatureCard):
                affected_creatures.append(target.name)
        return {
            'action': 'resolve_effect',
            'affected_targets': affected_creatures,
            'status': 'resolved'
        }
