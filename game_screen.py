import pygame
from pygame.locals import *
from game_logic import Game

CARD_BACK = pygame.image.load(f"./images/card-BMPs/b1fv.bmp")
LOGO = pygame.image.load(f"./images/blackjack2_generated.jpg")


class GameScreen:

    def __init__(self, caption):
        # Values used to draw the screen
        self.SCREEN_WIDTH = 1000
        self.SCREEN_HEIGHT = 800
        self.BACKGROUND = (22, 43, 10)
        self.TEXT_COLOR = (231, 204, 61)
        self.GAME_BOARD_TOP = 300

        # values used to message the screen from the
        # game logic classes
        self.key_pressed = ""
        self.player_message = []
        self.next_step = None
        self.tick_count = 0
        self.game = Game(self)

        # setup the screen
        pygame.init()
        self.screen = screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), DOUBLEBUF)
        pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()

        self.font = self.set_font('freesansbold.ttf', 16)
        self.logo = pygame.transform.scale_by(LOGO, .25)

        self.left = (self.screen.get_width() / 2) - (self.logo.get_width() / 2)

    # the main function of the game, it will run in a loop
    # until the player quits out of the game
    def game_start(self):
        done = False
        # main game loop
        self.next_step = self.game.game_step()
        self.tick_count = 0
        while not done:
            # get player input
            done = self.get_player_input()

            # perform game logic
            if hasattr(self.next_step, "tick_count"):
                if self.next_step.tick_count < self.tick_count:
                    self.next_step = self.next_step.game_step()
            else:
                self.next_step = self.next_step.game_step()
                if type(self.next_step).__name__ == "Game":
                    self.player_message = []

                if not self.next_step:
                    done = True

            # use tick_count to slow action down
            self.tick_count += 1

            # reset key press
            self.key_pressed = ""

            # draw every thing
            self.begin_drawing()

            # draw the player area
            self.draw_game_board()

            # draw next steps
            self.draw_player_message()

            self.end_drawing()

        GameScreen.quit()

    def set_font(self, font_name, size):
        self.font = pygame.font.Font(font_name, size)
        return self.font

    def draw_text(self, msg: str, x, y):
        text_surface = self.font.render(msg, True, self.TEXT_COLOR, self.BACKGROUND)
        text_rect = text_surface.get_rect()
        text_rect.top = y
        text_rect.left = x
        self.screen.blit(text_surface, text_rect)

    @staticmethod
    def quit():
        pygame.quit()

    @staticmethod
    def load_image(path):
        return pygame.image.load(path)

    @staticmethod
    def display_hand(hand):
        print(f"\nCards for {hand.player_name}")
        first_card = True
        for card in hand.cards:
            if first_card and hand.is_hidden:
                print("[***]", end="")
            else:
                print(f"[{card.suit}{card.rank}]", end="")
            first_card = False
        if hand.is_hidden:
            print("\n")
        else:
            print(f"\n{hand.get_total()} in hand")

    def begin_drawing(self):
        self.screen.fill(self.BACKGROUND)

        self.screen.blit(self.logo, (self.left, -100))

    def end_drawing(self):
        pygame.display.flip()
        self.clock.tick(60)

    def blackjack(self, hand):
        self.player_message.append(f"{hand.player_name} has Blackjack")
        self.game.game_asset.dealer_hand.is_hidden = False
        print(self.player_message[-1])

    def player_lost(self, hand):
        self.player_message.append(f"{hand.player_name} lost.")
        print(self.player_message[-1])

    def player_wins(self, hand):
        self.player_message.append(f"{hand.player_name} wins!")
        print(self.player_message[-1])

    def player_busts(self, hand):
        self.player_message.append(f"{hand.player_name} busted")
        print(self.player_message[-1])

    def push(self):
        self.player_message.append("It's a push.")
        print(self.player_message[-1])

    def get_player_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                keys_pressed = pygame.key.get_pressed()
                if keys_pressed[pygame.K_h]:
                    self.key_pressed = "h"
                elif keys_pressed[pygame.K_s]:
                    self.key_pressed = "s"
                elif keys_pressed[pygame.K_y]:
                    self.key_pressed = "y"
                elif keys_pressed[pygame.K_n]:
                    self.key_pressed = "n"

        return False

    def draw_participant_cards(self, participant_hand, x: int, y: int):
        card_width_and_buffer = participant_hand.cards[0].image.get_width() + 10

        for i in range(0, len(participant_hand.cards)):
            if participant_hand.is_hidden and i == 0:
                card_img = CARD_BACK
            else:
                card_img = participant_hand.cards[i].image
            dx = x + (i * card_width_and_buffer)
            self.screen.blit(card_img, (dx, y))

    def draw_game_board(self):
        game_board_x = int(self.left)
        dealer_y = self.GAME_BOARD_TOP
        self.draw_text("Dealer Hand", game_board_x, dealer_y)
        self.draw_participant_cards(self.game.game_asset.dealer_hand, game_board_x, dealer_y + 25)
        if not self.game.game_asset.dealer_hand.is_hidden:
            self.draw_text(f"Dealer Total: {self.game.game_asset.dealer_hand.get_total()}", game_board_x, dealer_y + 130)

        player_y = dealer_y + 165
        self.draw_text("Player Hand", game_board_x, player_y)
        self.draw_participant_cards(self.game.game_asset.player_hand, game_board_x, player_y + 25)
        self.draw_text(f"Player total: {self.game.game_asset.player_hand.get_total()}", game_board_x, player_y + 130)

        #     for i in range(0, len(participant_hand)):
        #         if hidden and i == 0:
        #             card_img = deck.CARD_BACK
        #         else:
        #             card_img = participant_hand[i]["image"]
        #         dx = x + (i * card_width_and_buffer)
        #         screen.blit(card_img, (dx, y))

    def draw_player_message(self):
        if type(self.next_step).__name__ == "PlayerHand":
            self.draw_text("Press 'H' to hit or 'S' to stand", int(self.left), self.GAME_BOARD_TOP + 340)
        elif type(self.next_step).__name__ == "EndHand":
            self.draw_text("Press 'Y' to play or 'N' to quit", int(self.left), self.GAME_BOARD_TOP + 360)

        if len(self.player_message) > 0:
            display_string = ""
            for s in self.player_message:
                display_string += s
                display_string += " "
            self.draw_text(display_string, int(self.left), self.GAME_BOARD_TOP + 330)
