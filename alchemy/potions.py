from .elements import create_fire, create_air, create_earth, create_water


def healing_potion() -> str:
    """Prepare a healing potion

    Returns
    -------
    str
        The text result
    """

    return f"Healing potion brewed with {create_fire()} and {create_water()}"


def strength_potion() -> str:
    """Prepare a strength potion

    Returns
    -------
    str
        The text result
    """

    return f"Strength potion brewed with {create_earth()} and {create_fire()}"


def invisibility_potion() -> str:
    """Prepare an invisibility potion

    Returns
    -------
    str
        The text result
    """

    return (f"Invisibility potion brewed with {create_air()} and "
            + create_water())


def wisdom_potion() -> str:
    """Prepare a wisdom potion

    Returns
    -------
    str
        The text result
    """

    return (f"Wisdom potion brewed with all elements: {create_fire()}, " +
            f"{create_air}, {create_earth()} and {create_water()}")
