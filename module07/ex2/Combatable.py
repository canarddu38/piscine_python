from abc import ABC, abstractmethod


class Combatable(ABC):
    """
    Abstract base class for combat-capable entities.
    """
    @abstractmethod
    def attack(self, target) -> dict:
        """
        Attack a target.

        Args:
            target: The target of the attack.

        Returns:
            dict: The result of the attack.
        """
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        """
        Defend against incoming damage.

        Args:
            incoming_damage (int): The amount of incoming damage.

        Returns:
            dict: The result of the defense.
        """
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict:
        """
        Get combat statistics.

        Returns:
            dict: A dictionary containing combat statistics.
        """
        pass
