#!/usr/bin/env python3

def spell_combiner(spell1: callable, spell2: callable) -> callable:
	return lambda *args, **kwargs: (spell1(*args, **kwargs), spell2(*args, **kwargs))


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
	return lambda *args, **kwargs: multiplier * base_spell(*args, **kwargs)


def conditional_caster(condition: callable, spell: callable) -> callable:
	return lambda *args, **kwargs: spell(*args, **kwargs) if condition(*args, **kwargs) else "Spell fizzled"


def spell_sequence(spells: list[callable]) -> callable:
	return lambda *args, **kwargs: [spell(*args, **kwargs) for spell in spells]


def main() -> None:
	print("Testing spell combiner...")
	fireball = lambda arg: f"Fireball hits {arg}"
	heal = lambda arg: f"Heals {arg}"
	combined = spell_combiner(fireball, heal)
	print("Combined spell result:", ", ".join(combined("Dragon")))

	print("\nTesting power amplifier...")
	original = lambda: 10
	amplified = power_amplifier(original, 3)
	print(f"Original: {original()}, Amplified: {amplified()}")

	print("\nTesting conditional spell")
	r = conditional_caster(lambda arg: len(arg)==0, fireball)
	print(r("Test"))

	print("\nTesting spell sequence")
	r = spell_sequence([fireball, heal])
	print(r("Test"))

if __name__ == "__main__":
	main()
