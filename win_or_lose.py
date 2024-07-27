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
        suite = card // 13
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
    length = len(numbers) - 4
    for i in range(length):
        if all(numbers[i] + j == numbers[i + j] for j in range(5)):
            return True
    return False


def check_four_of_a_kind(cards):
    numbers = {}
    for card in cards:
        card = card % 13
        if card not in numbers:
            numbers[card] = 1
        else:
            numbers[card] += 1
    if max(numbers.values()) >= 4:
        return True
    return False


def check_straight_flush(cards):
    # check suite
    suites = {}
    for card in cards:
        suite = card // 13
        if suite not in suites:
            suites[suite] = 1
        else:
            suites[suite] += 1
    largest_value = max(suites.values())
    if largest_value >= 5:
        biggest = 0
        for key in suites:
            if suites[key] == largest_value:
                biggest = key
                break
        lowest = biggest * 13
        highest = (biggest + 1) * 13
        for card in cards:
            if card < lowest or card >= highest:
                cards.remove(card)
        return check_straight(cards)
    return False


def full_house(cards):
    pass


print(check_straight_flush([1, 2, 3, 4, 7, 6, 13]))

