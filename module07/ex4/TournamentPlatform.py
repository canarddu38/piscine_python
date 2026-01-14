from ex4 import TournamentCard


class TournamentPlatform:
    def __init__(self):
        self.cards = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        base_id = card.name.lower().replace(" ", "_")
        existing_count = sum(1 for cid in self.cards
                             if cid.startswith(base_id))
        card_id = f"{base_id}_{existing_count + 1:03d}"

        self.cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        if card1_id not in self.cards or card2_id not in self.cards:
            raise ValueError("One or both card IDs not found")

        c1 = self.cards[card1_id]
        c2 = self.cards[card2_id]

        score1 = c1.attack_power + c1.defense_power + (c1.rating / 10)
        score2 = c2.attack_power + c2.defense_power + (c2.rating / 10)

        winner = c1 if score1 >= score2 else c2
        loser = c2 if score1 >= score2 else c1
        winner_id = card1_id if score1 >= score2 else card2_id
        loser_id = card2_id if score1 >= score2 else card1_id

        # elo formula
        K = 32
        expected_score_winner = 1 / (1 + 10 ** ((loser.rating - winner.rating)
                                                / 400))
        rating_change = int(K * (1 - expected_score_winner))

        winner.rating += rating_change
        loser.rating -= rating_change

        winner.update_wins(1)
        loser.update_losses(1)

        self.matches_played += 1

        return {
            'winner': winner_id,
            'loser': loser_id,
            'winner_rating': winner.rating,
            'loser_rating': loser.rating
        }

    def get_leaderboard(self) -> list:
        sorted_cards = sorted(
            self.cards.items(),
            key=lambda item: item[1].calculate_rating(),
            reverse=True
        )
        return [
            {
                "id": cid,
                "name": card.name,
                "rating": card.calculate_rating(),
                "record": f"{card.wins}-{card.losses}"
            }
            for cid, card in sorted_cards
        ]

    def generate_tournament_report(self) -> dict:
        total_rating = sum(c.calculate_rating() for c in self.cards.values())
        avg_rating = total_rating / len(self.cards) if self.cards else 0

        return {
            'total_cards': len(self.cards),
            'matches_played': self.matches_played,
            'avg_rating': int(avg_rating),
            'platform_status': 'active'
        }
