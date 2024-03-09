class BlackjackHand:
    def __init__(self, name, hidden):
        self.cards = []
        self.playing = True
        self.player_name = name
        self.is_hidden = hidden

    def is_playing(self):
        if self.get_total() > 21:
            self.playing = False
        return self.playing

    def add_card(self, card):
        self.cards.append(card)

    def is_blackjack(self):
        if self.get_total() == 21 and len(self.cards) == 2:
            return True

        return False

    def get_total(self):
        ace_place = []
        total = 0
        for card in self.cards:
            if card.rank == "A":
                ace_place.append(1)
            total += int(card.points)

        if total > 21:
            while len(ace_place) > 0:
                total -= 11
                total += ace_place.pop()
                if total < 21:
                    break
        return total

    def reset(self, hidden=False):
        self.cards = []
        self.is_hidden = hidden
