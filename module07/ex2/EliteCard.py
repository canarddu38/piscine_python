from ex0 import Card
from ex2 import Magical, Combatable


class EliteCard(Card, Combatable, Magical):
    """
    An elite card combining capabilities of Card, Combatable, and Magical.

    Attributes:
        attack_power (int): The attack power of the card.
        defense (int): The defense stat of the card.
        mana (int): The current mana pool of the card.
    """
    def __init__(self, name: str, cost: int, rarity: str,
                 attack_power: int = 5, defense: int = 3, mana: int = 4):
        """
        Initialize a new EliteCard instance.

        Args:
            name (str): The name of the card.
            cost (int): The mana cost of the card.
            rarity (str): The rarity of the card.
            attack_power (int, optional): The attack power. Defaults to 5.
            defense (int, optional): The defense stat. Defaults to 3.
            mana (int, optional): The mana pool. Defaults to 4.
        """
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.defense = defense
        self.mana = mana

    def play(self, game_state: dict) -> dict:
        """
        Play the elite card.

        Args:
            game_state (dict): The current state of the game.

        Returns:
            dict: The result of playing the card.
        """
        return {
            'action': 'play',
            'card': self.name,
            'effect': 'Enters the battlefield with combat and magic \
capabilities'
        }

    def attack(self, target) -> dict:
        """
        Attack a target using the elite card.

        Args:
            target: The target of the attack.

        Returns:
            dict: The result of the attack, including damage and combat type.
        """
        return {
            'attacker': self.name,
            'target': target,
            'damage': self.attack_power,
            'combat_type': 'melee'
        }

    def defend(self, incoming_damage: int) -> dict:
        """
        Defend against incoming damage.

        Args:
            incoming_damage (int): The amount of damage to defend against.

        Returns:
            dict: The result of defense, including damage taken and blocked.
        """
        damage_taken = max(0, incoming_damage - self.defense)
        return {
            'defender': self.name,
            'damage_taken': damage_taken,
            'damage_blocked': self.defense,
            'still_alive': True
        }

    def get_combat_stats(self) -> dict:
        """
        Get the combat statistics of the elite card.

        Returns:
            dict: The combat stats (attack and defense).
        """
        return {
            'attack': self.attack_power,
            'defense': self.defense
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """
        Cast a spell on targets.

        Args:
            spell_name (str): The name of the spell.
            targets (list): The targets of the spell.

        Returns:
            dict: The result of casting the spell.
        """
        return {
            'caster': self.name,
            'spell': spell_name,
            'targets': targets,
            'mana_used': self.mana
        }

    def channel_mana(self, amount: int) -> dict:
        """
        Channel additional mana for the card.

        Args:
            amount (int): The amount of mana to add.

        Returns:
            dict: The result of channeling, including total mana.
        """
        self.mana += amount
        return {
            'channeled': amount,
            'total_mana': self.mana
        }

    def get_magic_stats(self) -> dict:
        """
        Get the magic statistics of the elite card.

        Returns:
            dict: The magic stats (mana).
        """
        return {
            'mana': self.mana
        }
