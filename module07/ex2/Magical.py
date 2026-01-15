from abc import ABC, abstractmethod


class Magical(ABC):
    """
    Abstract base class for magical entities.
    """
    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """
        Cast a spell on targets.

        Args:
            spell_name (str): The name of the spell.
            targets (list): The targets of the spell.

        Returns:
            dict: The result of casting the spell.
        """
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        """
        Channel mana to increase mana pool.

        Args:
            amount (int): The amount of mana to channel.

        Returns:
            dict: The result of channeling mana.
        """
        pass

    @abstractmethod
    def get_magic_stats(self) -> dict:
        """
        Get magic statistics.

        Returns:
            dict: A dictionary containing magic statistics.
        """
        pass
