from abc import ABC, abstractmethod


class Rankable(ABC):
    """
    Abstract base class for rankable entities.
    """
    @abstractmethod
    def calculate_rating(self) -> int:
        """
        Calculate the rating of the entity.

        Returns:
            int: The calculated rating.
        """
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """
        Update the number of wins.

        Args:
            wins (int): The number of wins to add.
        """
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """
        Update the number of losses.

        Args:
            losses (int): The number of losses to add.
        """
        pass

    @abstractmethod
    def get_rank_info(self) -> dict:
        """
        Get ranking information.

        Returns:
            dict: The rank information.
        """
        pass
