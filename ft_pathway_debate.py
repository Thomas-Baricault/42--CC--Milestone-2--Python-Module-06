#!/usr/bin/python3

def absolute_imports() -> None:
    print("Testing Absolute Imports (from basic.py):")
    from alchemy.transmutation.basic import lead_to_gold, stone_to_gem
    print("lead_to_gold():", lead_to_gold())
    print("stone_to_gem():", stone_to_gem())
    print()


def relative_imports() -> None:
    print("Testing Relative Imports (from advanced.py):")
    from alchemy.transmutation.advanced import (philosophers_stone,
                                                elixir_of_life)
    print("philosophers_stone():", philosophers_stone())
    print("elixir_of_life():", elixir_of_life())
    print()


def package_access() -> None:
    print("Testing Package Access:")
    import alchemy
    print("alchemy.transmutation.lead_to_gold():",
          alchemy.transmutation.lead_to_gold())
    print("alchemy.transmutation.philosophers_stone():",
          alchemy.transmutation.philosophers_stone())
    print()


if __name__ == "__main__":
    print()
    print("=== Pathway Debate Mastery ===")
    print()
    absolute_imports()
    relative_imports()
    package_access()
    print("Both pathways works! Absolute: clear, Relative: concise")
