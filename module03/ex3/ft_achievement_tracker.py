#!/usr/bin/env python3

players = {
    "alice": {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'},
    "bob": {'first_kill', 'level_10', 'boss_slayer', 'collector'},
    "charlie": {'level_10', 'treasure_hunter', 'boss_slayer',
                'speed_demon', 'perfectionist'}
}

print("=== Achievement Tracker System ===\n")
for player, achievements in players.items():
    print(f"Player {player} achievements: {achievements}")

print("\n=== Achievement Analytics ===")

A = players['alice']
B = players['bob']
C = players['charlie']

all_achievements = A | B | C
print(f"All unique achievements: {all_achievements}")
print(f"Total unique achievements: {len(all_achievements)}")

common_achievements = A & B & C
print(f"\nCommon to all players: {common_achievements}")

rare_achievements = all_achievements - (A & B) - (A & C) - (B & C)
print(f"Rare achievements (1 player): {rare_achievements}")

print(f"\nAlice vs Bob common: {A & B}")
print(f"\nAlice unique: {A - B}")
print(f"\nBob unique: {B - A}")
