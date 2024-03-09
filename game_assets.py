from blackjack_hand import BlackjackHand
from deck import DeckOfCards


class GameAssets:
    def __init__(self, display):
        self.deck = DeckOfCards()
        self.player_hand = BlackjackHand("Player", False)
        self.dealer_hand = BlackjackHand("Dealer", True)
        self.display = display

    def start_new_game(self):
        if self.deck.is_deck_count_less_than(12):
            self.deck.prepare_deck()
        self.player_hand.reset()
        self.dealer_hand.reset(True)
        for _ in range(0, 2):
            self.player_hand.add_card(self.deck.deal_card())
            self.dealer_hand.add_card(self.deck.deal_card())

    def display_cards(self):
        self.display.display_hand(self.dealer_hand)
        self.display.display_hand(self.player_hand)

    def get_player_choice(self):
        return self.display.player_choice()

    def display_player_bust(self):
        self.display_cards()
        self.display.player_busts(self.player_hand)