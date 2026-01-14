import random
from ex0 import Card, CreatureCard
from ex1 import SpellCard, ArtifactCard


class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        try:
            idx = self.cards.index(card_name)
            self.cards.pop(idx)
            return True
        except ValueError:
            return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if len(self.cards) > 0:
            return self.cards.pop(0)
        return None

    def get_deck_stats(self) -> dict:
        s = len(self.cards)
        if s == 0:
            avg = 0
        else:
            avg = sum([c.cost / s for c in self.cards])
        return {
            'total_cards': s,
            'creatures': len([card for card in self.cards
                              if type(card) is CreatureCard]),
            'spells': len([card for card in self.cards
                           if type(card) is SpellCard]),
            'artifacts': len([card for card in self.cards
                              if type(card) is ArtifactCard]),
            'avg_cost': avg
        }
