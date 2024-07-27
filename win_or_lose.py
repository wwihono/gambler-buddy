import numpy as np


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


def check_full_house(cards):
    numbers = {}
    for card in cards:
        card = card % 13
        if card not in numbers:
            numbers[card] = 1
        else:
            numbers[card] += 1
    if 2 in numbers.values() and 3 in numbers.values():
        return True
    return False


def check_trey(cards):
    numbers = {}
    for card in cards:
        card = card % 13
        if card not in numbers:
            numbers[card] = 1
        else:
            numbers[card] += 1
    if max(numbers.values()) >= 3:
        return True
    return False


def check_deuce(cards):
    numbers = {}
    for card in cards:
        card = card % 13
        if card not in numbers:
            numbers[card] = 1
        else:
            numbers[card] += 1
    if max(numbers.values()) >= 2:
        return True
    return False


def check_double_deuce(cards):
    numbers = {}
    doubles = 0
    for card in cards:
        card = card % 13
        if card not in numbers:
            numbers[card] = 1
        else:
            numbers[card] += 1
    if max(numbers.values()) >= 2:
        doubles += 1
    if doubles >= 2:
        return True
    return False


def assign_value(cards):
    if check_straight_flush(cards):
        return 8
    elif check_four_of_a_kind(cards):
        return 7
    elif check_full_house(cards):
        return 6
    elif check_flush(cards):
        return 5
    elif check_straight(cards):
        return 4
    elif check_trey(cards):
        return 3
    elif check_double_deuce(cards):
        return 2
    elif check_deuce(cards):
        return 1
    return 0
