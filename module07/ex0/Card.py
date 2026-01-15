from abc import ABC, abstractmethod


class Card(ABC):
    """
    Abstract base class representing a card in the game.

    Attributes:
        name (str): The name of the card.
        cost (int): The mana cost to play the card.
        rarity (str): The rarity level of the card.
    """
    def __init__(self, name: str, cost: int, rarity: str):
        """
        Initialize a new Card instance.

        Args:
            name (str): The name of the card.
            cost (int): The mana cost of the card.
            rarity (str): The rarity of the card.
        """
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """
        Abstract method to play the card.

        Args:
            game_state (dict): The current state of the game.

        Returns:
            dict: The result of playing the card.
        """
        pass

    def get_card_info(self) -> dict:
        """
        Get the information about the card.

        Returns:
            dict: A dictionary containing the card's name, cost, and rarity.
        """
        return {
            'name': self.name,
            'cost': self.cost,
            'rarity': self.rarity
        }

    def is_playable(self, available_mana: int) -> bool:
        """
        Check if the card can be played with the available mana.

        Args:
            available_mana (int): The amount of mana available.

        Returns:
            bool: True if the card can be played, False otherwise.
        """
        return available_mana >= self.cost
