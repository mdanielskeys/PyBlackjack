import pygame

import deck
import hand_utils

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
BACKGROUND = (90, 130, 60)
TEXT_COLOR = (40, 40, 40)

GS_BLACKJACK = 0
GS_PLAYER_BLACKJACK = 1
GS_PLAYER = 2
GS_DEALER = 3
GS_GAME_OVER = 4
GS_QUIT = 5
GS_PLAYER_BUST = 6
GS_FINAL_CALC = 7


def initialize_pygame() -> pygame.Surface:
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("100 Days of Python - Blackjack")

    return screen


def draw_participant_cards(screen: pygame.Surface, participant_hand: list[dict[str, str, int, pygame.Surface]],
                           x: int, y: int, hidden=True):
    card_width_and_buffer = participant_hand[0]["image"].get_width() + 10

    for i in range(0, len(participant_hand)):
        if hidden and i == 0:
            card_img = deck.CARD_BACK
        else:
            card_img = participant_hand[i]["image"]
        dx = x + (i * card_width_and_buffer)
        screen.blit(card_img, (dx, y))


def draw_card(screen: pygame.Surface, card_img: pygame.Surface, row, column):
    y = row * (card_img.get_height() + 10)
    x = column * (card_img.get_width() + 5)
    screen.blit(card_img, (x, y))


def deal_hand(card_deck) -> dict[str, list]:
    hand = {"Player": [], "Dealer": []}
    # Get two cards for the dealer and player
    for i in range(0, 2):
        for key in hand:
            hand[key].append(deck.deal_card(card_deck))
    return hand


def create_text(text: str, color: (int, int, int), top_left: (int, int), font: pygame.font):
    _text = font.render(text, True, color, BACKGROUND)
    _text_rect = _text.get_rect()
    _text_rect.top = top_left[1]
    _text_rect.left = top_left[0]

    return _text, _text_rect


def play_blackjack_hand(screen, font, start_drawing, clock, card_deck):
    player_card_drawing, player_rect, player_text = get_text_surface("Player Hand", font, start_drawing, 180)

    hand = deal_hand(card_deck)

    player_total = hand_utils.calculate_hand_total(hand["Player"])
    dealer_total = hand_utils.calculate_hand_total(hand["Dealer"])

    # get initial state
    if dealer_total == 21:
        game_state = GS_BLACKJACK
    elif player_total == 21:
        game_state = GS_PLAYER_BLACKJACK
    else:
        game_state = GS_PLAYER

    done = False
    final_countdown = 200
    msg_text = ""

    while not done:
        # get game actions
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                keys_pressed = pygame.key.get_pressed()
                if keys_pressed[pygame.K_h] and game_state == GS_PLAYER:
                    hand["Player"].append(deck.deal_card(card_deck))
                    player_total = hand_utils.calculate_hand_total(hand["Player"])
                elif keys_pressed[pygame.K_s] and game_state == GS_PLAYER:
                    game_state = GS_DEALER

        # process out the game state
        if game_state == GS_PLAYER:
            msg_text = "Hit 'H' to hit or 'S' to stand"
        if game_state == GS_BLACKJACK:
            game_state = GS_GAME_OVER
            msg_text = "Dealer Blackjack! You Lose!"
        elif game_state == GS_PLAYER_BLACKJACK:
            game_state = GS_GAME_OVER
            msg_text = "Blackjack! You Win!"
        elif player_total > 21:
            game_state = GS_GAME_OVER
            msg_text = "You busted! You Lose!"
        elif game_state == GS_FINAL_CALC:
            game_state = GS_GAME_OVER
            if dealer_total > 21:
                msg_text = "Dealer busts! You win!"
            elif player_total == dealer_total:
                msg_text = "It's a push (tie)"
            elif player_total > dealer_total:
                msg_text = "You win!"
            else:
                msg_text = "The dealer wins"

        if game_state == GS_DEALER:
            if dealer_total < 17 and dealer_total <= player_total:
                hand["Dealer"].append(deck.deal_card(card_deck))
                dealer_total = hand_utils.calculate_hand_total(hand["Dealer"])

            if dealer_total >= 17 or dealer_total > player_total:
                game_state = GS_FINAL_CALC

        # draw out the player surface
        screen.fill(BACKGROUND)
        draw_text("Dealer hand", font, screen, start_drawing[0], start_drawing[1])

        if game_state == GS_PLAYER:
            draw_participant_cards(screen, hand["Dealer"], start_drawing[0], start_drawing[1]+font.get_height()+10)
        else:
            draw_participant_cards(screen, hand["Dealer"], start_drawing[0], start_drawing[1]+font.get_height()+10,
                                   False)
            draw_text(f"Total Dealer Face Value: {dealer_total}", font, screen,
                      start_drawing[0], start_drawing[1]+140)

        draw_text("Player Hand", font, screen, start_drawing[0], start_drawing[1]+180)

        draw_participant_cards(screen, hand["Player"], start_drawing[0], start_drawing[1]+font.get_height()+190, False)

        draw_text(f"Total Player Face Value: {player_total}", font, screen, start_drawing[0], start_drawing[1]+320)
        draw_text(msg_text, font, screen, start_drawing[0], start_drawing[1]+font.get_height()+340)

        if game_state == GS_GAME_OVER:
            final_countdown -= 1
            if final_countdown <= 0:
                return done

        pygame.display.update()
        clock.tick(60)


def main():
    screen = initialize_pygame()
    clock = pygame.time.Clock()

    card_deck = deck.prepare_deck()
    font = pygame.font.Font('freesansbold.ttf', 20)

    start_drawing = [int(SCREEN_WIDTH / 4), 70]

    game_wait_rect, game_wait = inst_drawing_surface("Would you like to play a game of Blackjack ('Y' or 'N')",
                                                     font,
                                                     start_drawing,
                                                     320)
    game_state = GS_GAME_OVER
    done = False
    while game_state != GS_QUIT and not done:
        # get game actions
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                keys_pressed = pygame.key.get_pressed()
                if keys_pressed[pygame.K_y]:
                    if len(card_deck) < 12:
                        card_deck = deck.prepare_deck()
                    done = play_blackjack_hand(screen, font, start_drawing, clock, card_deck)
                elif keys_pressed[pygame.K_n]:
                    game_state = GS_QUIT

        # draw out the player surface
        screen.fill(BACKGROUND)
        screen.blit(game_wait, game_wait_rect)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()


def draw_text(msg: str, font: pygame.font, screen: pygame.Surface, x, y, color=TEXT_COLOR, background=BACKGROUND):
    text_surface = font.render(msg, True, color, background)
    text_rect = text_surface.get_rect()
    text_rect.top = y
    text_rect.left = x
    screen.blit(text_surface, text_rect)


def inst_drawing_surface(object_text, font, start_drawing, offset):
    text_drawing = start_drawing.copy()
    text_drawing[1] += offset
    text, rect = create_text(object_text, TEXT_COLOR, text_drawing, font)

    return rect, text


def get_text_surface(object_text, font, start_drawing, offset=0):
    text_drawing = start_drawing.copy()
    text_drawing[1] += offset

    card_drawing = text_drawing.copy()
    card_drawing[1] += font.get_height() + 10

    text, rect = create_text(object_text, TEXT_COLOR, text_drawing, font)
    return card_drawing, rect, text


if __name__ == "__main__":
    main()
