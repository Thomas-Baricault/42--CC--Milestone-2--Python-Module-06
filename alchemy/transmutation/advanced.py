from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone() -> str:
    """Create the philosopher's stone

    Returns
    -------
    str
        The text result
    """

    return (f"Philosopher's stone created using {lead_to_gold()} and "
            + healing_potion())


def elixir_of_life() -> str:
    """Activate the elixir of life

    Returns
    -------
    str
        The text result
    """

    return "Elixir of life: eternal youth achieved!"
