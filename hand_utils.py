# calculate the total for the hand
# take into account the ace and shift it to 1 when necessary
def calculate_hand_total(hand):
    ace_place = []
    total = 0
    for card in hand:
        if card["rank"] == "A":
            ace_place.append(1)
        total += int(card["points"])

    if total > 21:
        while len(ace_place) > 0:
            total -= 11
            total += ace_place.pop()
            if total < 21:
                break
    return total