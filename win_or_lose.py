def win_or_lose(player_cards, opponent_cards):
    player_value = assign_value(player_cards)
    opponent_value = assign_value(opponent_cards)
    # 0 -> player wins, 1 -> player loses, 2 -> draw
    if player_value > opponent_value:
        return 0
    elif player_value < opponent_value:
        return 1
    else:
        return 2


def assign_value(cards):
    return 0


def check_flush(cards):
    # check suite
    suite = cards[0] % 13
    flag = False
    for card in cards:
        if suite is not (card % 13):
            flag = True
            break
    return not flag


def full_house(cards):
    pass

