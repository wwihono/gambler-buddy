import numpy as np


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
    suites = {}
    for card in cards:
        suite = card % 13
        if suite not in suites:
            suites[suite] = 1
        else:
            suites[suite] += 1
    largest_value = max(suites.values())
    if largest_value >= 5:
        return True
    return False


def check_straight(cards):
    numbers = []
    for card in cards:
        numbers.append(card % 13)
        numbers.append((card % 13) + 13)
    numbers.sort()
    numbers = np.unique(numbers)
    for i in range(10):
        if all(numbers[i] + j == numbers[i + j] for j in range(5)):
            return True
    return False


def check_straight_flush(cards):
    pass


def full_house(cards):
    pass

