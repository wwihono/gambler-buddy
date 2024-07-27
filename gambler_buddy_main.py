from itertools import combinations
import numpy as np
import func as fn


NO_OF_PLAYERS = 2
TOTAL_CARDS = 52 - 2 * NO_OF_PLAYERS


def generate_possibilities(amount_of_cards, hand_and_flop):
    # Get an array with all cards
    possibilities = []
    pool = []
    for x in range(amount_of_cards):
        pool.append(x)
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


if __name__ == '__main__':

    # List to keep track of taken cards
    taken_cards = []

    # Get the player's cards
    PLAYER_CARDS = fn.get_player(taken_cards)

    # Get the flop cards
    FLOP_CARDS = fn.get_flop(taken_cards)

    # Convert taken cards to prepare for operations
    taken_cards = fn.encode(taken_cards)


    # User Outputs
    print("Flop cards are:", fn.convert_to_original(FLOP_CARDS))
    print("Player's cards are:", fn.convert_to_original(PLAYER_CARDS))
    print("taken cards: " + str(taken_cards))
    print(generate_possibilities(TOTAL_CARDS, taken_cards))