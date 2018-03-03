from hand import Hand


class Player:
    def __init__(self, name, chips=100):
        self.chips = chips
        self.hand = Hand()
        self.name = name
        self.bet = 0

    def make_bet(self):
        while True:
            bet = int(input("{}, Enter your bet: ".format(self.name)))
            if bet > self.chips or bet <= 0:
                print("Invalid bet, try again")
            else:
                self.bet = bet
                print("{} bets ".format(self.name), self.bet)
                break

    def is_hitting(self):
        return input("{}, Would you like to hit or stand? (H/S): ".format(
            self.name)).lower().startswith('h')

    def show_hand(self):
        print("")
        print("Player", self.name, "has cards:")
        for card in self.hand.cards:
            print(card)
        print("Total Value: ", self.hand.score)
        print("")

    def is_bust(self):
        return self.hand.is_bust()
