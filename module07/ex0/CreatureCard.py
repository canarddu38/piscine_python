from ex0 import Card


class CreatureCard(Card):
    """
    A class representing a creature card, inheriting from Card.

    Attributes:
        health (int): The health points of the creature.
        attack (int): The attack points of the creature.
    """
    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int):
        """
        Initialize a new CreatureCard instance.

        Args:
            name (str): The name of the card.
            cost (int): The mana cost of the card.
            rarity (str): The rarity of the card.
            attack (int): The attack points of the creature.
            health (int): The health points of the creature.
        """
        super().__init__(name, cost, rarity)
        self.health = 0
        self.attack = 0
        if health > 0:
            self.health = health
        else:
            print("Invalid CreatureCard health (<=0)")
        if attack > 0:
            self.attack = attack
        else:
            print("Invalid CreatureCard attack (<=0)")

    def play(self, game_state: dict) -> dict:
        """
        Play the creature card.

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
                'effect': 'Creature summoned to battlefield'
            }
        else:
            return {"success": False}

    def get_card_info(self) -> dict:
        """
        Get the information about the creature card.

        Returns:
            dict: Dictionary containing card details including attack/health.
        """
        return {
            'name': self.name,
            'cost': self.cost,
            'rarity': self.rarity,
            'type': CreatureCard.__name__.replace("Card", ""),
            'attack': self.attack,
            'health': self.health
        }

    def attack_target(self, target) -> dict:
        """
        Attack a target creature card.

        Args:
            target (CreatureCard): The target creature card to attack.

        Returns:
            dict: result of the attack or failure message.
        """
        if type(target) is CreatureCard:
            print(f"{self.name} attacks {target.name}:")
            target.health -= self.attack
            return {
                'attacker': self.name,
                'target': target.name,
                'damage_dealt': self.attack,
                'combat_resolved': (target.health <= 0)
            }
        else:
            return {"success": False}
