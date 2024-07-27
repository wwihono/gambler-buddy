from itertools import combinations
from config import NUM_PLAYERS, INITIAL_CARDS
from win_or_lose import win_or_lose as wl
import func as fn


def generate_possibilities(amount_of_cards, hand_and_flop):
    # Get an array with all cards
    possibilities = []
    pool = []
    for x in range(amount_of_cards):
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


if __name__ == '__main__':

    # List to keep track of taken cards
    taken_cards = []

    # Get the player's cards
    PLAYER_CARDS = fn.convert_to_original(fn.get_player(taken_cards))

    # Get the flop cards
    FLOP_CARDS = fn.convert_to_original(fn.get_flop(taken_cards))

    print("Flop cards are:", FLOP_CARDS)
    print("Player's cards are:", PLAYER_CARDS)
