import random
from assets.card import Card

# create a deck of cards (make a real deck since this is a capstone)
suits = ['s', 'd', 'h', 'c']
ranks: list[str] = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


class DeckOfCards:
    def __init__(self):
        self.deck: list[Card] = []
        self.prepare_deck()

    # Create a deck cards with the appropriate face values and suits
    def create_deck(self):
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank, suit))

    # create a deck prepare a deck for play
    def prepare_deck(self):
        self.deck = []          # empty an existing deck
        self.create_deck()
        random.shuffle(self.deck)

    # deal a card off the deck
    def deal_card(self):
        return self.deck.pop()

    def is_deck_count_less_than(self, count):
        return len(self.deck) < count
