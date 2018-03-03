class Hand:

    def __init__(self):
        self.cards = []
        self.score = 0

    def draw_card(self, deck):
        card = deck.next_card()
        self.score += card.rank.value
        self.cards.append(card)

    def return_cards(self, deck):
        deck.return_cards(self.cards)
        self.cards = []
        self.score = 0

    def is_bust(self):
        return self.score > 21
