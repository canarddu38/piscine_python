import random
from ex0 import Card, CreatureCard
from ex1 import SpellCard, ArtifactCard


class Deck:
    """
    A class representing a deck of cards.

    Attributes:
        cards (list): A list of cards in the deck.
    """
    def __init__(self):
        """
        Initialize a new Deck instance using list.
        """
        self.cards = []

    def add_card(self, card: Card) -> None:
        """
        Add a card to the deck.

        Args:
            card (Card): The card to add to the deck.
        """
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        """
        Remove a card from the deck by name.

        Args:
            card_name (str): The name of the card to remove.

        Returns:
            bool: True if the card was removed, False otherwise.
        """
        try:
            idx = self.cards.index(card_name)
            self.cards.pop(idx)
            return True
        except ValueError:
            return False

    def shuffle(self) -> None:
        """
        Shuffle the cards in the deck.
        """
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        """
        Draw a card from the top of the deck.

        Returns:
            Card: The drawn card, or None if the deck is empty.
        """
        if len(self.cards) > 0:
            return self.cards.pop(0)
        return None

    def get_deck_stats(self) -> dict:
        """
        Get statistics about the deck.

        Returns:
            dict: Dictionary containing deck statistics with card counts.
        """
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
