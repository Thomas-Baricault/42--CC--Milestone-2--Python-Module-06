#!/usr/bin/python3

def ingredient_validation() -> None:
    print("Testing ingredient validation:")
    from alchemy.grimoire import validate_ingredients
    print("validate_ingredients(\"fire air\"):",
          validate_ingredients("fire air"))
    print("validate_ingredients(\"dragon scales\"):",
          validate_ingredients("dragon scales"))
    print()


def spell_recording() -> None:
    print("Testing spell recording with validation:")
    from alchemy.grimoire import record_spell
    print("record_spell(\"Fireball\", \"fire air\"):",
          record_spell("Fireball", "fire air"))
    print("record_spell(\"Dark Magic\", \"shadow\"):",
          record_spell("Dark Magic", "shadow"))
    print()


def late_import() -> None:
    from alchemy.grimoire import record_spell
    print("Testing late import technique:")
    print("record_spell(\"Lightning\", \"air\"):",
          record_spell("Lightning", "air"))
    print()


if __name__ == "__main__":
    print()
    print("=== Circular Curse Breaking ===")
    print()
    ingredient_validation()
    spell_recording()
    late_import()
    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")
