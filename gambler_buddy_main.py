from itertools import combinations
import numpy as np
import func as fn
import win_or_lose
from win_or_lose import win_or_lose as wl


NO_OF_PLAYERS = 2
TOTAL_CARDS = 52


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

    # User Outputs
    """print("Flop cards are:", fn.convert_to_original(FLOP_CARDS))
    print("Player's cards are:", fn.convert_to_original(PLAYER_CARDS))
    print("taken cards: " + str(taken_cards))
    print(generate_possibilities(TOTAL_CARDS, taken_cards))"""

    # MAIN OPERATION

    #Get user input

    # Get the player's cards
    PLAYER_CARDS = fn.get_player(taken_cards)

    # Get the flop cards
    FLOP_CARDS = fn.get_flop(taken_cards)

    # Convert taken cards to prepare for operations
    taken_cards = fn.encode(taken_cards)

    # Possibilities
    posses = generate_possibilities(TOTAL_CARDS, taken_cards)

    # Statistic
    total_wins = 0
    total = 0
    ties = 0

    # Find probability of winning
    for pos in posses:
        river_turn = pos[0]
        opponent_hand = pos[1]

        result = win_or_lose.win_or_lose(fn.encode_dict(PLAYER_CARDS), opponent_hand,
                                   fn.encode_dict(FLOP_CARDS) + river_turn)
        # Find victor
        if result == 2:
            total_wins += 1
        elif result == 1:
            ties += 1
        total += 1

    # Probabilities
    winning_percentage = total_wins/total *100
    loss_percentage = (total-ties-total_wins)/total *100
    tie_percentage = (ties)/total *100

    # Output values with rounding to 3 decimal places (this does not ensure 3 significant figures)
    print("Winning Percentage:", round(winning_percentage, 1), "%")
    print("Loss Percentage:", round(loss_percentage, 1), "%")
    print("Tie Percentage:", round(tie_percentage, 1), "%")