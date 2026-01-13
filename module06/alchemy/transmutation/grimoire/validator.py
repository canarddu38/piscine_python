def validate_ingredients(ingredients: str) -> str:
    """
    Validates if the provided ingredients contain a valid element.

    Args:
        ingredients (str): A string containing the ingredients to check.

    Returns:
        str: A string indicating whether the ingredients are VALID or INVALID.
    """
    if "fire" in ingredients\
        or "air" in ingredients\
            or "earth" in ingredients\
            or "water" in ingredients:
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
