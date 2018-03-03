from card import Card
from suit import Suit
from rank import Rank
import random


class Deck:

    def __init__(self):
        self.cards = [
            Card(rank, suit) for rank in Rank for suit in Suit
        ]

    def shuffle(self):
        random.shuffle(self.cards)

    def next_card(self):
        return self.cards.pop()

    def return_cards(self, cards):
        self.cards += cards
