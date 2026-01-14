from ex0 import Card
from ex2 import Magical, Combatable


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack_power: int = 5, defense: int = 3, mana: int = 4):
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.defense = defense
        self.mana = mana

    def play(self, game_state: dict) -> dict:
        return {
            'action': 'play',
            'card': self.name,
            'effect': 'Enters the battlefield with combat and magic \
capabilities'
        }

    def attack(self, target) -> dict:
        return {
            'attacker': self.name,
            'target': target,
            'damage': self.attack_power,
            'combat_type': 'melee'
        }

    def defend(self, incoming_damage: int) -> dict:
        damage_taken = max(0, incoming_damage - self.defense)
        return {
            'defender': self.name,
            'damage_taken': damage_taken,
            'damage_blocked': self.defense,
            'still_alive': True
        }

    def get_combat_stats(self) -> dict:
        return {
            'attack': self.attack_power,
            'defense': self.defense
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        return {
            'caster': self.name,
            'spell': spell_name,
            'targets': targets,
            'mana_used': self.mana
        }

    def channel_mana(self, amount: int) -> dict:
        self.mana += amount
        return {
            'channeled': amount,
            'total_mana': self.mana
        }

    def get_magic_stats(self) -> dict:
        return {
            'mana': self.mana
        }
