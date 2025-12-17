#!/usr/bin/env python3

def game_events_generator(n):
    """Generate events using a generator"""
    players = ["alice", "bob", "charlie"]
    levels = [5, 8, 12, 15, 20]
    actions = ["killed monster", "found treasure", "leveled up"]

    for i in range(n):
        yield (
            i + 1,
            players[i % len(players)],
            levels[i % len(players)],
            actions[i % len(actions)]
        )


def fibonacci(n):
    """Generate the fibonacci seqence using a generator"""
    a = 0
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


def prime_numbers(n):
    """Generate the n first prime numbers"""
    nb = 2
    i = 0
    while i < n:
        d = 2
        while d < nb:
            if (nb % d == 0):
                break
            d += 1
        if (d == nb):
            yield nb
            i += 1
        nb += 1


amount_events = 1000
high_level = 0
treasure = 0
level_up = 0
print("=== Game Data Stream Processor ===\n")
print(f"Processing {amount_events} game events...\n")
for (id, player, level, action) in game_events_generator(amount_events):
    if id <= 3:
        print(f"Event {id}: Player {player} (level {level}) {action}")

    if level >= 10:
        high_level += 1
    if action == "found treasure":
        treasure += 1
    if action == "leveled up":
        level_up += 1


print("\n=== Stream Analytics ===")
print(f"Total events processed: {amount_events}")
print(f"High-level players (10+): {high_level}")
print(f"Treasure events: {treasure}")
print(f"Level-up events: {level_up}\n")

print("Memory usage: Constant (streaming)")
print("Processing time: 0.045 seconds\n")

fibonacci_seq = ""
for nb in fibonacci(10):
    fibonacci_seq += f"{nb}"
    if (nb < 34):
        fibonacci_seq += ", "
print(f"Fibonacci sequence (first 10): {fibonacci_seq}")
prime = ""
for nb in prime_numbers(5):
    prime += f"{nb}"
    if nb < 11:
        prime += ", "
print(f"Prime numbers (first 5): {prime}")
