from game_screen import GameScreen

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
BACKGROUND = (90, 130, 60)
TEXT_COLOR = (40, 40, 40)


def main():

    display = GameScreen("100 Days of Python - Blackjack")
    display.game_start()

    quit()


if __name__ == "__main__":
    main()





