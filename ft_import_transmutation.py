#!/usr/bin/python3

def full_module_import() -> None:
    print("Method 1 - Full module import:")
    import alchemy
    print("alchemy.elements.create_fire():", alchemy.elements.create_fire())
    print()


def specific_function_import() -> None:
    print("Method 2 - Specific function import:")
    from alchemy.elements import create_water
    print("create_water():", create_water())
    print()


def aliased_import() -> None:
    print("Method 3 - Aliased import:")
    from alchemy.potions import healing_potion as heal
    print("heal():", heal())
    print()


def multiple_imports() -> None:
    print("Method 3 - Multiple imports:")
    from alchemy.elements import create_earth, create_fire
    from alchemy.potions import strength_potion
    print("create_earth():", create_earth())
    print("create_fire():", create_fire())
    print("strength_potion():", strength_potion())
    print()


if __name__ == "__main__":
    print()
    print("=== Import Transmutation Mastery ===")
    print()
    full_module_import()
    specific_function_import()
    aliased_import()
    multiple_imports()
    print("All import transmutation methods mastered!")
