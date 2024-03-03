import random
from typing import List, Any

import pygame

# create a deck of cards (make a real deck since this is a capstone)
suits = ['s', 'd', 'h', 'c']
ranks: list[str] = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

CARD_BACK = pygame.image.load(f"./images/card-BMPs/b1fv.bmp")


def get_rank_string(rank: str) -> str:
    card_num = 0
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


def load_card(suit: str, rank: str) -> pygame.Surface:
    rank_str = get_rank_string(rank)

    return pygame.image.load(f"./images/card-BMPs/{suit}{rank_str}.bmp")


# Create a deck cards with the appropriate face values and suits
def create_deck():
    deck = []
    for suit in suits:
        for rank in ranks:
            card = {"suit": suit, "rank": rank}
            if card["rank"] == 'A':
                card["points"] = str(11)
            elif card["rank"] in ['J', 'Q', 'K']:
                card["points"] = str(10)
            else:
                card["points"] = card['rank']

            card["image"] = load_card(suit, rank)
            deck.append(card)
    return deck


# create a deck prepare a deck for play
def prepare_deck():
    deck = create_deck()
    random.shuffle(deck)
    return deck


# deal a card off the deck
def deal_card(deck):
    return deck.pop()
