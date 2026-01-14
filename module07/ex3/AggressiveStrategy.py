from ex3 import GameStrategy
from ex0 import CreatureCard
from ex1 import SpellCard


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        actions = {
            'cards_played': [],
            'mana_used': 0,
            'targets_attacked': [],
            'damage_dealt': 0
        }
        available_mana = 5

        hand.sort(key=lambda x: (0 if isinstance(x, CreatureCard)
                                 else 1, x.cost))

        for card in hand:
            if card.cost <= (available_mana - actions['mana_used']):
                actions['mana_used'] += card.cost
                actions['cards_played'].append(card.name)

                if isinstance(card, CreatureCard):
                    actions['damage_dealt'] += card.attack
                    actions['targets_attacked'].append("Enemy Player")
                elif isinstance(card, SpellCard):
                    actions['damage_dealt'] += card.cost
                    actions['targets_attacked'].append("Enemy Player")
        actions['targets_attacked'] = list(set(actions['targets_attacked']))
        return actions

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return ["Enemy Player"]
