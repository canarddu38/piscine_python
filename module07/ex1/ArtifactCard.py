from ex0 import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, durability: int,
                 effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        mana = game_state['mana']
        if type(mana) is int and self.is_playable(mana):
            return {
                'card_played': self.name,
                'mana_used': self.cost,
                'effect': f'Permanent: +1 {self.effect} per turn'
            }
        else:
            return {"success": False}

    def activate_ability(self) -> dict:
        if self.durability > 0:
            self.durability -= 1
            status = "active"
        else:
            status = "broken"

        return {
            'card': self.name,
            'ability_stats': {
                'effect': self.effect,
                'durability': self.durability,
                'status': status
            }
        }
