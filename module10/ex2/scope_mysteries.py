#!/usr/bin/env python3

def mage_counter() -> callable:
    counter = 0
    def inc():
        nonlocal counter
        counter += 1
        return counter
    return inc


def spell_accumulator(initial_power: int) -> callable:
	power = initial_power
	def inc(amount):
		nonlocal power
		power += amount
		return power
	return inc


def enchantment_factory(enchantment_type: str) -> callable:
	def enchant(item_name):
		return f"{enchantment_type.capitalize()} {item_name.capitalize()}"
	return enchant


def memory_vault() -> dict[str, callable]:
	data = {}
	def store(key, value):
		nonlocal data
		data[key] = value
	
	def recall(key):
		nonlocal data
		v = data.get(key) or "Memory not found"
		return v
	
	return {
		'store': store,
		'recall': recall
	}


def main() -> None:
	print()
	print("Testing mage counter...")
	fn = mage_counter()
	for i in range(1, 3 + 1):
		print(f"Call {i}: {fn()}")

	print()
	print("Testing enchantment factory...")
	fn1 = enchantment_factory("flaming")
	fn2 = enchantment_factory("frozen")
	print(fn1("Sword"))
	print(fn2("Shield"))


if __name__ == "__main__":
	main()
