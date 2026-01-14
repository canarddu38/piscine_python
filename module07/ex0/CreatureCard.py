from ex0 import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int):
        super().__init__(name, cost, rarity)
        self.health = 0
        self.attack = 0
        if health > 0:
            self.health = health
        else:
            print("Invalid CreatureCard health (<=0)")
        if attack > 0:
            self.attack = attack
        else:
            print("Invalid CreatureCard attack (<=0)")

    def play(self, game_state: dict) -> dict:
        mana = game_state['mana']
        if type(mana) is int and self.is_playable(mana):
            return {
                'card_played': self.name,
                'mana_used': self.cost,
                'effect': 'Creature summoned to battlefield'
            }
        else:
            return {"success": False}

    def get_card_info(self) -> dict:
        return {
            'name': self.name,
            'cost': self.cost,
            'rarity': self.rarity,
            'type': CreatureCard.__name__.replace("Card", ""),
            'attack': self.attack,
            'health': self.health
        }

    def attack_target(self, target) -> dict:
        if type(target) is CreatureCard:
            print(f"{self.name} attacks {target.name}:")
            target.health -= self.attack
            return {
                'attacker': self.name,
                'target': target.name,
                'damage_dealt': self.attack,
                'combat_resolved': (target.health <= 0)
            }
        else:
            return {"success": False}
