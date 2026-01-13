def record_spell(spell_name: str, ingredients: str) -> str:
    """
    Records a spell in the spellbook after validating its ingredients.

    Args:
        spell_name (str): The name of the spell to record.
        ingredients (str): A string containing the ingredients required for\
 the spell.

    Returns:
        str: A message indicating whether the spell was successfully recorded \
or rejected.
    """
    from .validator import validate_ingredients
    result = validate_ingredients(ingredients)
    if "INVALID" in result:
        return f"Spell rejected: {spell_name} ({result})"
    else:
        return f"Spell recorded: {spell_name} ({result})"
