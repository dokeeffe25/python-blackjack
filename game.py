from deck import Deck
from player import Player
from dealer import Dealer


class Game:
    def __init__(self, *players, chips=100):
        self.deck = Deck()
        self.deck.shuffle()
        self.dealer = Dealer()
        self.players = [Player(player, chips) for player in players]

    def betting_round(self):
        for player in self.players:
            player.make_bet()

    def initial_deal(self):
        for player in self.players:
            self.dealer.deal_card(player, self.deck)
            self.dealer.deal_card(player, self.deck)
            player.show_hand()

        self.dealer.deal_card(self.dealer, self.deck)
        self.dealer.show_first_card()

    def hitting_round(self):
        for player in self.players:
            while player.is_hitting():
                self.dealer.deal_card(player, self.deck)
                player.show_hand()
                if player.is_bust():
                    print("{} BUSTS!".format(player.name))
                    break

    def dealer_hitting(self):
        while self.dealer.hand.score < 17:
            print("Dealer Hits!")
            self.dealer.deal_card(self.dealer, self.deck)
        self.dealer.show_hand()

    def bet_result(self, player, did_win):
        if did_win:
            player.chips += player.bet
        else:
            player.chips -= player.bet

    def results(self):
        print('--------------------------------')
        print("Dealer final score:", self.dealer.hand.score)
        for player in self.players:
            print('-----------------------------')
            print("{} final score:".format(player.name), player.hand.score)

            if player.is_bust():
                print("RESULT: BUST!")
                self.bet_result(player, False)
            elif player.hand.score > self.dealer.hand.score and not player.is_bust(
            ):
                print("RESULT: WIN!")
                self.bet_result(player, True)
            elif self.dealer.is_bust():
                print("RESULT: WIN!")
                self.bet_result(player, True)
            else:
                print("RESULT: LOSS!")
                self.bet_result(player, False)

            print("Current Chips: ", player.chips)
            if (player.chips <= 0):
                print("Player Eliminated!")
            print('-----------------------------')

    def reset_game(self):
        self.dealer.hand.return_cards(self.deck)
        new_player_list = []
        for player in self.players:
            player.bet = 0
            player.hand.return_cards(self.deck)
            if player.chips > 0:
                new_player_list.append(player)
        self.players = new_player_list
        self.deck.shuffle()

    def play_again(self):
        if not self.players:
            return False
        else:
            return input("Would you like to play again? (Y/N): ").lower(
            ).startswith('y')

    def play(self):
        playing = True
        while playing:
            self.betting_round()
            self.initial_deal()
            self.hitting_round()
            self.dealer_hitting()
            self.results()
            self.reset_game()
            playing = self.play_again()


def main():
    game = Game("Jim", "Bob")
    game.play()


if __name__ == '__main__':
    main()
