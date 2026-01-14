from ex0 import Card, CreatureCard


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        mana = game_state['mana']
        if type(mana) is int and self.is_playable(mana):
            return {
                'card_played': self.name,
                'mana_used': self.cost,
                'effect': f'Deal {self.cost} {self.effect_type} to target'
            }
        else:
            return {"success": False}

    def resolve_effect(self, targets: list) -> dict:
        affected_creatures = []
        for target in targets:
            if isinstance(target, CreatureCard):
                affected_creatures.append(target.name)
        return {
            'action': 'resolve_effect',
            'affected_targets': affected_creatures,
            'status': 'resolved'
        }
