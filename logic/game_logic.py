from assets.game_assets import GameAssets
from logic.blackjack import Blackjack
from logic.player_hand import PlayerHand
from logic.dealer_hand import DealerHand
from logic.calculate_winner import CalculateWinner
from logic.end_hand import EndHand

class Game:
    def __init__(self, display):
        self.game_asset = GameAssets(display)
        self.next_state = self.setup_state_classes()

    def game_step(self):
        self.game_asset.start_new_game()
        return self.next_state

    def setup_state_classes(self):
        # Recipe is as follows
        # deal a new hand and then check if there is a blackjack
        # then proceed to play out the player hand
        # if the player does not bust then proceed to the dealer hand
        # finally calculate the winner of the hand
        end_game = EndHand(self.game_asset, self)
        calc_winner = CalculateWinner(self.game_asset, end_game)
        dealer_hand = DealerHand(self.game_asset, calc_winner)
        player_hand = PlayerHand(self.game_asset, dealer_hand)

        return Blackjack(self.game_asset, player_hand, end_game)