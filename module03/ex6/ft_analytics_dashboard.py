#!/usr/bin/env python3

def get_score(item: tuple) -> int:
    return item[1].get('score', 0)


print("=== Game Analytics Dashboard ===\n")

players = {
    'alice': {
        'score': 2300,
        'active': True,
        'achievements': {'first_kill', 'winner'},
        'region': 'central'
    },
    'bob': {
        'score': 1800,
        'active': True,
        'achievements': {'level_10', 'top_player', 'winner'},
        'region': 'north'
    },
    'charlie': {
        'score': 2150,
        'active': True,
        'achievements': {'boss_slayer', 'winner', 'top_player'},
        'region': 'east'
    },
    'diana': {
        'score': 2050,
        'active': False,
        'achievements': {'top_player'},
        'region': 'west'
    },
}

print("=== List Comprehension Examples ===")
high_scorers = [name for name, player in players.items()
                if player.get("score", 0) > 2000]
scores_doubled = [player.get("score", 0) * 2 for player in players.values()]
active = [name for name, player in players.items()
          if player.get("active", False)]

print(f"High scorers (>2000): {high_scorers}")
print(f"Scores doubled: {scores_doubled}")
print(f"Active players: {active}")

print("\n=== Dict Comprehension Examples ===")
scores = {
    name: player.get("score", 0) for name, player in players.items()
    if player.get("active", False)
}
categories = {
    'high': len([
        name for name, player in players.items()
        if player.get("score", 0) > 2000
    ]),
    'medium': len([
        name for name, player in players.items()
        if 2000 > player.get("score", 0) > 1000
    ]),
    'low': len([
        name for name, player in players.items()
        if 1000 > player.get("score", 0) > 0
    ]),
}
achivements_count = {
    name: len(player.get("achievements", {}))
    for name, player in players.items()
    if player.get("active", False)
}
print(f"Player scores: {scores}")
print(f"Score categories: {categories}")
print(f"Achievement counts: {achivements_count}")

print("\n=== Set Comprehension Examples ===")
unique_players = {name for name in players}
unique_achievements = {
    achievement
    for player in players.values()
    for achievement in player['achievements']
}
regions = {
    player.get("region", "no-region") for player in players.values()
    if player.get("active", False)
}

print(f"Unique players: {unique_players}")
print(f"Unique achievement: {unique_achievements}")
print(f"Active regions: {regions}")


avg_score = sum([score for score in scores.values()]) / len(scores)
best_scorer_name, best_scorer_data = max(players.items(), key=get_score)

print("\n=== Combined Analysis ===")
print(f"Total players: {len(players)}")
print(f"Total unique achievements: {len(unique_achievements)}")
print(f"Average score: {int(avg_score * 100) / 100}")
print(f"Top performer: {best_scorer_name} ({best_scorer_data.get('score', 0)} \
points, {len(best_scorer_data.get('achievements', {}))} achievements)")
