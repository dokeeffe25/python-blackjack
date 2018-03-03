from player import Hand


class Dealer:

    def __init__(self):
        self.hello = ""
        self.hand = Hand()

    def show_first_card(self):
        print("")
        print("Dealers' first card:")
        print(self.hand.cards[0])
        print("")

    def draw_remaining_cards(self, deck):
        while self.hand.score < 17:
            self.hand.draw_card(deck)

    def deal_card(self, player, deck):
        player.hand.draw_card(deck)

    def show_hand(self):
        print("")
        print('DEALER has cards:')
        for card in self.hand.cards:
            print(card)
        print("")

    def is_bust(self):
        return self.hand.is_bust()
