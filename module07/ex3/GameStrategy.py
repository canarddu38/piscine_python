from abc import ABC, abstractmethod


class GameStrategy(ABC):
    """
    Abstract base class for game strategies.
    """
    @abstractmethod
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """
        Execute a turn based on the strategy.

        Args:
            hand (list): The list of cards in hand.
            battlefield (list): The list of cards on the battlefield.

        Returns:
            dict: The result of the turn execution.
        """
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        """
        Get the name of the strategy.

        Returns:
            str: The name of the strategy.
        """
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: list) -> list:
        """
        Prioritize targets for attack.

        Args:
            available_targets (list): The list of available targets.

        Returns:
            list: The list of prioritized targets.
        """
        pass
