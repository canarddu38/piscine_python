from .elements import create_water, create_fire, create_air, create_earth


def healing_potion():
    """
    Brew a healing potion.

    Returns:
        str: Description of the brewed healing potion.
    """
    return f"Healing potion brewed with {create_fire()} and {create_water()}"


def strength_potion():
    """
    Brew a strength potion.

    Returns:
        str: Description of the brewed strength potion.
    """
    return f"Strength potion brewed with {create_earth()} and {create_fire()}"


def invisibility_potion():
    """
    Brew an invisibility potion.

    Returns:
        str: Description of the brewed invisibility potion.
    """
    return f"Invisibility potion brewed with \
{create_air()} and {create_water()}"


def wisdom_potion():
    """
    Brew a wisdom potion.

    Returns:
        str: Description of the brewed wisdom potion.
    """
    return f"Wisdom potion brewed with all elements: \
{create_fire()} {create_earth()} {create_air()} {create_earth()}"
