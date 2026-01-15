from abc import ABC, abstractmethod
from ex0 import Card


class CardFactory(ABC):
    """
    Abstract factory for creating cards.
    """
    @abstractmethod
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        """
        Create a creature card.

        Args:
            name_or_power (str | int | None, optional): Name or power hint.

        Returns:
            Card: A new creature card.
        """
        pass

    @abstractmethod
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        """
        Create a spell card.

        Args:
            name_or_power (str | int | None, optional): Name or power hint.

        Returns:
            Card: A new spell card.
        """
        pass

    @abstractmethod
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        """
        Create an artifact card.

        Args:
            name_or_power (str | int | None, optional): Name or power hint.

        Returns:
            Card: A new artifact card.
        """
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict:
        """
        Create a themed deck.

        Args:
            size (int): The number of cards in the deck.

        Returns:
            dict: A dictionary containing the deck.
        """
        pass

    @abstractmethod
    def get_supported_types(self) -> dict:
        """
        Get supported card types.

        Returns:
            dict: The supported card types.
        """
        pass
