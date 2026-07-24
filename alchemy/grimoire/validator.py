def validate_ingredients(ingredients: str) -> str:
    """Validate if ingredients are valid

    Parameters
    ----------
    ingredients : str
        The ingredients

    Returns
    -------
    str
        "[ingredients] - VALID" is valid, "[ingredients] - INVALID" otherwise
    """

    for ingredient in ingredients.split(' '):
        if (
            ingredient == "fire" or
            ingredient == "water" or
            ingredient == "earth" or
            ingredient == "air"
        ):
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
