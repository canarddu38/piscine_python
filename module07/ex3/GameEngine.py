from ex3 import CardFactory, GameStrategy


class GameEngine:
    """
    A class representing the game engine.

    Attributes:
        factory (CardFactory): The factory used to create cards.
        strategy (GameStrategy): The strategy used for the game.
        turns_simulated (int): The number of turns simulated.
        total_damage (int): The total damage dealt.
        cards_created (int): The number of cards created.
    """
    def __init__(self):
        """
        Initialize the GameEngine.
        """
        self.factory = None
        self.strategy = None
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        """
        Configure the game engine with a factory and strategy.

        Args:
            factory (CardFactory): The card factory to use.
            strategy (GameStrategy): The game strategy to use.
        """
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        """
        Simulate a game turn.

        Returns:
            dict: The result of the turn simulation.
        """
        if not self.factory or not self.strategy:
            raise ValueError("Engine not configured")

        strategy = self.strategy.get_strategy_name()\
            .replace('Strategy', '').lower()
        print(f"Simulating {strategy} turn...")

        hand = []
        hand.append(self.factory.create_creature("Dragon"))
        hand.append(self.factory.create_creature("Goblin"))
        hand.append(self.factory.create_spell("Lightning Bolt"))

        hand_desc = []
        for card in hand:
            hand_desc.append(f"{card.name} ({card.cost})")
        print(f"Hand: [{', '.join(hand_desc)}]")

        self.cards_created += len(hand)

        battlefield = []
        print("\nTurn execution:")
        print(f"Strategy: {self.strategy.get_strategy_name()}")

        turn_result = self.strategy.execute_turn(hand, battlefield)

        print(f"Actions: {turn_result}")

        self.turns_simulated += 1
        self.total_damage += turn_result.get('damage_dealt', 0)
        return turn_result

    def get_engine_status(self) -> dict:
        """
        Get the current status of the game engine.

        Returns:
            dict: A dictionary containing engine status.
        """
        return {
            'turns_simulated': self.turns_simulated,
            'strategy_used': self.strategy.get_strategy_name()
            if self.strategy else None,
            'total_damage': self.total_damage,
            'cards_created': self.cards_created
        }
