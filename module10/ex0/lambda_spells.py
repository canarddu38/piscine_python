#!/usr/bin/env python3

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
	return sorted(artifacts, key=lambda dic: dic.get("power", 0), reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
	return list(filter(lambda mage: mage.get("power", 0) >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
	return list(map(lambda name: f"* {name} *", spells))


def mage_stats(mages: list[dict]) -> dict:
	func = lambda x: x.get("power", 0)
	max_power = func(max(mages, key=func))
	min_power = func(min(mages, key=func))
	if len(mages) == 0:
		avg_power = 0
	else:
		avg_power = int(100 * sum(map(func, mages)) / len(mages)) / 100
	
	return {'max_power': max_power, 'min_power': min_power, 'avg_power': avg_power}
	

def main() -> None:
	print("Testing artifact sorter...")
	data = [
		{
			'name': 'Fire Staff',
			'power': 92,
			'type': 'unknown'
		},
		{
			'name': 'Crystal Orb',
			'power': 85,
			'type': 'unknown'
		}
	]
	r = artifact_sorter(data)
	print(f"{r[0]['name']} ({r[0]['power']} power) comes before {r[1]['name']} ({r[1]['power']} power)")

	print("\nTesting spell transformer...")
	spells = ["fireball", "heal", "shield"]
	r = spell_transformer(spells)
	print(" ".join(r))


if __name__ == "__main__":
	main()
