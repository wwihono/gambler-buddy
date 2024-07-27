def parse_cards(card_input, num_cards, taken):
    card_dict = {}
    i = 0
    curr_key = ""

    while len(card_dict) < num_cards and i < len(card_input):
        input_val = card_input[i].lower()
        if input_val not in "dchs":
            if check_royal(input_val):
                curr_key += add_royal(input_val)
            else:
                curr_key += card_input[i]
            i += 1
        else:
            suit = get_suit(input_val)
            curr_key = str(int(curr_key) - 1)
            curr_key += suit
            if curr_key not in taken:
                key = curr_key[:-1]
                if key in card_dict:
                    card_dict[key].append(suit)
                else:
                    card_dict[key] = [suit]
                taken.append(curr_key)
                curr_key = ""  # Clear curr val
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
        return "11"
    elif val.lower() == 'q':
        return "12"
    elif val.lower() == 'k':
        return "13"
    else:
        return "14"


def get_flop(taken):
    print("\nPlease input cards using this format (key-suit-key-suit-key-suit)" +
          "\n D = diamond, C = clover, H = heart, S = spade\n" +
          "J = jack, Q = queen, K = king, A = Ace\n" +
          "CASE-INSENSITIVE\n" +
          "---\n")
    x = input("Input flop cards (Ex: 'Ad10cKc', '10d9s6c'): ").strip()
    return parse_cards(x, 3, taken)


def get_player(taken):
    print("Please input cards using this format (key-suit-key-suit)" +
          "\n D = diamond, C = clover, H = heart, S = spade\n" +
          "J = jack, Q = queen, K = king, A = Ace\n" +
          "CASE-INSENSITIVE\n" +
          "---\n")
    x = input("Input player cards (Ex: 'AdKc', '10d9s'): ").strip()
    return parse_cards(x, 2, taken)


def convert_to_original(dictionary):
    result = {}
    for key in dictionary.keys():
        int_key = int(key)
        if int_key > 9:
            if int_key == 10:
                result['J'] = [get_suit(suit) for suit in dictionary[key]]
            elif int_key == 11:
                result['Q'] = [get_suit(suit) for suit in dictionary[key]]
            elif int_key == 12:
                result['K'] = [get_suit(suit) for suit in dictionary[key]]
            elif int_key == 13:
                result['A'] = [get_suit(suit) for suit in dictionary[key]]
        else:
            new_key = str(int_key + 1)
            if new_key in result:
                result[new_key].extend([get_suit(suit) for suit in dictionary[key]])
            else:
                result[new_key] = [get_suit(suit) for suit in dictionary[key]]
    return result
