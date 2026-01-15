from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone() -> str:
    """
    Create the Philosopher's Stone.

    Returns:
        str: Description of the creation of the Philosopher's Stone.
    """
    return f"Philosopher's stone created using {lead_to_gold()} \
and {healing_potion()}"


def elixir_of_life() -> str:
    """
    Create the Elixir of Life.

    Returns:
        str: Description of the Elixir of Life.
    """
    return "Elixir of life: eternal youth achieved!"
