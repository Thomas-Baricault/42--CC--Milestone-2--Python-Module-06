def record_spell(spell_name: str, ingredients: str) -> str:
    """Record a spell

    Parameters
    ----------
    spell_name : str
        The spell name
    ingredients : str
        The ingredients

    Returns
    -------
    str
        "Spell recorded: [validation result]" on success, "Spell rejected:
        [validation result]" otherwise
    """

    from . import validate_ingredients

    validation = validate_ingredients(ingredients)
    if validation.endswith("- VALID"):
        return f"Spell recorded: {spell_name} ({validation})"
    return f"Spell rejected: {spell_name} ({validation})"
