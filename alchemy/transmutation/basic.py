from alchemy.elements import create_fire, create_earth


def lead_to_gold() -> str:
    """Transmute lead into gold

    Returns
    -------
    str
        The text result
    """

    return f"Lead transmuted to gold using {create_fire()}"


def stone_to_gem() -> str:
    """Transmute stone into gem

    Returns
    -------
    str
        The text result
    """

    return f"Stone transmuted to gem using {create_earth()}"
