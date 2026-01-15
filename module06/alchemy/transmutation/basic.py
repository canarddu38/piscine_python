from alchemy.elements import create_fire, create_earth


def lead_to_gold() -> str:
    """
    Transmute lead to gold.

    Returns:
        str: Description of the transmutation result.
    """
    return f"Lead transmuted to gold using {create_fire()}"


def stone_to_gem() -> str:
    """
    Transmute stone to gem.

    Returns:
        str: Description of the transmutation result.
    """
    return f"Stone transmuted to gem using {create_earth()}"
