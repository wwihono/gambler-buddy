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

def parse_cards(card_input, num_cards, taken_cards):
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
            curr_value += get_suit(input_val)
            if curr_value not in taken_cards:
                card_dict[curr_value] = curr_value
                taken_cards.append(curr_value)
                curr_value = ""  # Clear curr val
            i += 1

    return card_dict


def get_suit(val):
    if val == 'd':
        return 'd'
    elif val == 'c':
        return 'c'
    elif val == 'h':
        return 'h'
    else:
        return 's'


def check_royal(val):
    return val.lower() in "jqka"


def add_royal(val):
    if val.lower() == 'j':
        return "J"
    elif val.lower() == 'q':
        return "Q"
    elif val.lower() == 'k':
        return "K"
    else:
        return "A"


def get_flop(taken_cards):
    print("Please input cards using this format (value-suit-value-suit-value-suit)" +
          "\n D = diamond, C = clover, H = heart, S = spade\n" +
          "J = jack, Q = queen, K = king, A = Ace\n" +
          "CASE-INSENSITIVE\n" +
          "---\n")
    x = input("Input flop cards (Ex: 'Ad10cKc', '10d9s6c'): ").strip()
    return parse_cards(x, 3, taken_cards)


def get_player(taken_cards):
    print("Please input cards using this format (value-suit-value-suit)" +
          "\n D = diamond, C = clover, H = heart, S = spade\n" +
          "J = jack, Q = queen, K = king, A = Ace\n" +
          "CASE-INSENSITIVE\n" +
          "---\n")
    x = input("Input player cards (Ex: 'AdKc', '10d9s'): ").strip()
    return parse_cards(x, 2, taken_cards)


if __name__ == '__main__':
    INITIAL_CARDS = list(range(1, 53))
    NUM_PLAYERS = 2

    # List to keep track of taken cards
    taken_cards = []

    # Get the player's cards
    PLAYER_CARDS = get_player(taken_cards)
    print("Player's cards are:", PLAYER_CARDS)

    # Get the flop cards
    FLOP_CARDS = get_flop(taken_cards)
    print("Flop cards are:", FLOP_CARDS)

