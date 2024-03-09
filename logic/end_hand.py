class EndHand:
    def __init__(self, game, start_hand):
        self.game = game
        self.next_step = start_hand

    def game_step(self):
        choice = self.game.display.key_pressed
        if choice == 'y':
            return self.next_step
        elif choice == 'n':
            return None

        return self
