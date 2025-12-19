#!/usr/bin/env python3

def inventory_value(inv):
    """Calculate the value of an inventory"""
    total = 0
    for item in inv.values():
        total += item["qty"] * item["value"]
    return total


def item_count(inv):
    """Count the number of items in inventory"""
    count = 0
    for item in inv.values():
        count += item["qty"]
    return count


def categories(inv):
    """Get the list of categories"""
    cats = {}
    for item in inv.values():
        cat = item["type"]
        if cats.get(cat) is None:
            cats[cat] = 0
        cats[cat] += item["qty"]
    return cats


def print_inventory(name, inv):
    """Display players's inventory"""
    print(f"=== {name}'s Inventory ===")
    for k, v in inv.items():
        total = v["qty"] * v["value"]
        print(f"{k} ({v['type']}, {v['rarity']}): {v['qty']}x @ \
{v['value']} gold each = {total} gold")
    print(f"\nInventory value: {inventory_value(inv)} gold")
    print(f"Item count: {item_count(inv)} items")
    cats = categories(inv)
    out = []
    for k, v in cats.items():
        out.append(f"{k}({v})")
    print("Categories:", ", ".join(out))


def main():
    """Main function"""
    alice = {
        "sword": {"qty": 1,
                  "type": "weapon",
                  "rarity": "rare",
                  "value": 500
                  },
        "potion": {"qty": 5,
                   "type": "consumable",
                   "rarity": "common",
                   "value": 50
                   },
        "shield": {"qty": 1,
                   "type": "armor",
                   "rarity": "uncommon",
                   "value": 200
                   }
    }

    bob = {}

    print("=== Player Inventory System ===\n")
    print_inventory("Alice", alice)

    print("\n=== Transaction: Alice gives Bob 2 potions ===")
    if alice.get("potion") and alice["potion"]["qty"] >= 2:
        alice["potion"]["qty"] -= 2
        if bob.get("potion"):
            bob["potion"]["qty"] += 2
        else:
            bob.update({
                "potion": {
                    "qty": 2,
                    "type": "consumable",
                    "rarity": "common",
                    "value": 50
                }
            })
        print("Transaction successful!")
    else:
        print("Transaction failed!")

    print("\n=== Updated Inventories ===")
    print("Alice potions:", alice["potion"]["qty"])
    print("Bob potions:", bob["potion"]["qty"])

    players = {
        "Alice": alice,
        "Bob": bob
    }

    print("\n=== Inventory Analytics ===")

    richest = None
    most_items = None
    max_value = -1
    max_items = -1

    for name, inv in players.items():
        val = inventory_value(inv)
        cnt = item_count(inv)
        if val > max_value:
            max_value = val
            richest = name
        if cnt > max_items:
            max_items = cnt
            most_items = name

    print(f"Most valuable player: {richest} ({max_value} gold)")
    print(f"Most items: {most_items} ({max_items} items)")

    rarest = []
    for inv in players.values():
        for k, v in inv.items():
            if v["rarity"] == "rare" and k not in rarest:
                rarest.append(k)

    rarest.append("magic_ring")
    print("Rarest items:", ", ".join(rarest))


if __name__ == "__main__":
    main()
