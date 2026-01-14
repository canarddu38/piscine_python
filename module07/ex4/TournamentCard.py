from ex0 import Card
from ex2 import Combatable
from ex4 import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str, attack_power: int,
                 defense_power: int, rating: int = 1000):
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.defense_power = defense_power
        self.rating = rating
        self.wins = 0
        self.losses = 0

    def play(self, game_state: dict) -> dict:
        return {
            "action": "play_tournament_card",
            "card": self.name,
            "game_state": game_state
        }

    def attack(self, target) -> dict:
        damage = self.attack_power
        if hasattr(target, 'defense_power'):
            damage = max(0, self.attack_power - target.defense_power)

        return {
            "attacker": self.name,
            "target": target.name if hasattr(target, 'name') else "Unknown",
            "damage_dealt": damage
        }

    def defend(self, incoming_damage: int) -> dict:
        damage_taken = max(0, incoming_damage - self.defense_power)
        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_mitigated": self.defense_power
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.attack_power,
            "defense": self.defense_power
        }

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def get_rank_info(self) -> dict:
        return {
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses
        }

    def get_tournament_stats(self) -> dict:
        return {
            "name": self.name,
            **self.get_card_info(),
            **self.get_combat_stats(),
            **self.get_rank_info()
        }
