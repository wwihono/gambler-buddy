from itertools import combinations


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


def parse_cards(card_input, num_cards, taken):
    card_dict = {}
    i = 0
    curr_value = ""

    while len(card_dict) < num_cards and i < len(card_input):
        input_val = card_input[i].lower()
        if input_val not in "dchs":
            if check_royal(input_val):
                curr_value += add_royal(input_val)
            else:
                curr_value += card_input[i]
            i += 1
        else:
            suit = get_suit(input_val)
            curr_value = str(int(curr_value) - 1)
            curr_value += suit
            if curr_value not in taken:
                value = curr_value[:-1]
                if value in card_dict:
                    card_dict[value].append(suit)
                else:
                    card_dict[value] = [suit]
                taken.append(curr_value)
                curr_value = ""  # Clear curr val
            i += 1

    return card_dict


def get_suit(val):
    if val == 'd':
        return 'a'
    elif val == 'c':
        return 'b'
    elif val == 'h':
        return 'c'
    else:
        return 'd'


def check_royal(val):
    return val.lower() in "jqka"


def add_royal(val):
    if val.lower() == 'j':
        return "11"
    elif val.lower() == 'q':
        return "12"
    elif val.lower() == 'k':
        return "13"
    else:
        return "14"


def get_flop(taken):
    print("\nPlease input cards using this format (value-suit-value-suit-value-suit)" +
          "\n D = diamond, C = clover, H = heart, S = spade\n" +
          "J = jack, Q = queen, K = king, A = Ace\n" +
          "CASE-INSENSITIVE\n" +
          "---\n")
    x = input("Input flop cards (Ex: 'Ad10cKc', '10d9s6c'): ").strip()
    return parse_cards(x, 3, taken)


def get_player(taken):
    print("Please input cards using this format (value-suit-value-suit)" +
          "\n D = diamond, C = clover, H = heart, S = spade\n" +
          "J = jack, Q = queen, K = king, A = Ace\n" +
          "CASE-INSENSITIVE\n" +
          "---\n")
    x = input("Input player cards (Ex: 'AdKc', '10d9s'): ").strip()
    return parse_cards(x, 2, taken)


if __name__ == '__main__':
    INITIAL_CARDS = list(range(1, 53))
    NUM_PLAYERS = 2

    # List to keep track of taken cards
    taken_cards = []

    # Get the player's cards
    PLAYER_CARDS = get_player(taken_cards)

    # Get the flop cards
    FLOP_CARDS = get_flop(taken_cards)
    print("Flop cards are:", FLOP_CARDS)
    print("Player's cards are:", PLAYER_CARDS)
