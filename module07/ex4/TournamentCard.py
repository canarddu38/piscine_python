from ex0 import Card
from ex2 import Combatable
from ex4 import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """
    A class representing a tournament card that can be played, fight, and rank.

    Attributes:
        attack_power (int): Attack power of the card.
        defense_power (int): Defense power of the card.
        rating (int): ELO rating of the card.
        wins (int): Number of wins.
        losses (int): Number of losses.
    """
    def __init__(self, name: str, cost: int, rarity: str, attack_power: int,
                 defense_power: int, rating: int = 1000):
        """
        Initialize a new TournamentCard instance.

        Args:
            name (str): The name of the card.
            cost (int): The mana cost.
            rarity (str): The rarity of the card.
            attack_power (int): The attack power.
            defense_power (int): The defense power.
            rating (int, optional): The initial rating. Defaults to 1000.
        """
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.defense_power = defense_power
        self.rating = rating
        self.wins = 0
        self.losses = 0

    def play(self, game_state: dict) -> dict:
        """
        Play the tournament card.

        Args:
            game_state (dict): The current game state.

        Returns:
            dict: The result of playing the card.
        """
        return {
            "action": "play_tournament_card",
            "card": self.name,
            "game_state": game_state
        }

    def attack(self, target) -> dict:
        """
        Attack a target.

        Args:
            target: The target entity.

        Returns:
            dict: The result of the attack.
        """
        damage = self.attack_power
        if hasattr(target, 'defense_power'):
            damage = max(0, self.attack_power - target.defense_power)

        return {
            "attacker": self.name,
            "target": target.name if hasattr(target, 'name') else "Unknown",
            "damage_dealt": damage
        }

    def defend(self, incoming_damage: int) -> dict:
        """
        Defend against incoming damage.

        Args:
            incoming_damage (int): The damage amount.

        Returns:
            dict: The result of the defense.
        """
        damage_taken = max(0, incoming_damage - self.defense_power)
        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_mitigated": self.defense_power
        }

    def get_combat_stats(self) -> dict:
        """
        Get combat statistics.

        Returns:
            dict: Combat stats including attack and defense.
        """
        return {
            "attack": self.attack_power,
            "defense": self.defense_power
        }

    def calculate_rating(self) -> int:
        """
        Get the current rating.

        Returns:
            int: The current rating.
        """
        return self.rating

    def update_wins(self, wins: int) -> None:
        """
        Update win count.

        Args:
            wins (int): Number of wins to add.
        """
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        """
        Update loss count.

        Args:
            losses (int): Number of losses to add.
        """
        self.losses += losses

    def get_rank_info(self) -> dict:
        """
        Get rank information.

        Returns:
            dict: Rank info including rating, wins, losses.
        """
        return {
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses
        }

    def get_tournament_stats(self) -> dict:
        """
        Get comprehensive tournament statistics.

        Returns:
            dict: Stats combining card info, combat stats, and rank info.
        """
        return {
            "name": self.name,
            **self.get_card_info(),
            **self.get_combat_stats(),
            **self.get_rank_info()
        }
