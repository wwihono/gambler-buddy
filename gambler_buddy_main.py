from itertools import combinations


def generate_possibilities(amount_of_cards, hand_and_flop):
    length = len(hand_and_flop)
    # Get an array with all cards
    possibilities = []
    pool = []
    for x in range(52):
        pool.append(x + 1)
    for known in hand_and_flop:
        pool.remove(known)
    # Choose 4 cards from the remaining
    four_cards = set(combinations(pool, 4))
    for four_card in four_cards:
        two_and_twos = set(combinations(four_card, 2))
        for two in two_and_twos:
            total = list(four_card)
            for number in two:
                total.remove(number)
            two = list(two)
            possibilities.append([total, two])
    return possibilities
