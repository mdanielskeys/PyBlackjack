class CalculateWinner:
    def __init__(self, game, next_step):
        self.game = game
        self.next_step = next_step

    def game_step(self):
        player_total = self.game.player_hand.get_total()
        dealer_total = self.game.dealer_hand.get_total()
        display = self.game.display

        self.game.display_cards()
        if player_total > 21:
            display.player_busts(self.game.player_hand)
        elif dealer_total > 21:
            display.player_busts(self.game.dealer_hand)
            display.player_wins(self.game.player_hand)
        elif player_total == dealer_total:
            display.push()
        elif player_total < dealer_total:
            display.player_lost(self.game.player_hand)
        else:
            display.player_wins(self.game.player_hand)

        return self.next_step
