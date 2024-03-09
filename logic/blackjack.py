
class Blackjack:
    def __init__(self, game, player_hand, end_game):
        self.game = game
        self.player_hand = player_hand
        self.end_game = end_game

    def game_step(self):
        if self.game.dealer_hand.is_blackjack():
            self.game.display_cards()
            self.game.display.blackjack(self.game.dealer_hand)
            return self.end_game

        if self.game.player_hand.is_blackjack():
            self.game.display_cards()
            self.game.display.blackjack(self.game.player_hand)
            return self.end_game

        return self.player_hand
