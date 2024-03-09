
class DealerHand:
    def __init__(self, game, calc_winner):
        self.game = game
        self.calc_winner = calc_winner
        self.tick_count = 40

    def game_step(self):
        self.game.dealer_hand.is_hidden = False
        # self.game.display_cards()
        if self.game.player_hand.get_total() > 21:
            return self.calc_winner

        if self.game.dealer_hand.get_total() < 17:
            self.game.dealer_hand.add_card(self.game.deck.deal_card())
            self.game.display.tick_count = 0
        else:
            return self.calc_winner

        return self
