from display import pygame_wrapper


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.points = self.get_points()
        self.image = self.load_card()

    def get_text(self):
        return f"{self.rank} of {self.suit}"

    def load_card(self):
        rank_str = self.get_rank_string(self.rank)
        return pygame_wrapper.load_image(f"./images/card-BMPs/{self.suit}{rank_str}.bmp")

    def get_points(self):
        if self.rank == 'A':
            return 11
        elif self.rank in ['J', 'Q', 'K']:
            return 10
        else:
            return self.rank

    @staticmethod
    def get_rank_string(rank: str) -> str:
        if rank == 'A':
            card_num = 1
        elif rank == 'J':
            card_num = 11
        elif rank == 'Q':
            card_num = 12
        elif rank == 'K':
            card_num = 13
        else:
            card_num = int(rank)

        return f"{card_num:02}"
