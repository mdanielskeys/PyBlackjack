class PlayerHand:
    def __init__(self, game, dealer_hand):
        self.game = game
        self.dealer_hand = dealer_hand

    def game_step(self):
        self.game.display_cards()
        choice = self.game.display.key_pressed
        if choice == 'h':
            self.game.player_hand.add_card(self.game.deck.deal_card())
        elif choice == 's':
            self.game.display.tick_count = 0
            return self.dealer_hand

        # if you go over then proceed to the next step
        if self.game.player_hand.get_total() > 21:
            return self.dealer_hand

        return self
