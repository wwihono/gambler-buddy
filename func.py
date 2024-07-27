# Contributors: Justrene Hartono and Winston Wihono
# Getter and Setter functions required for the script to function properly


def parse_cards(card_input, num_cards, taken):
    """
        Parses the input string of cards and creates a dictionary mapping card values to their suits.

        Args:
            card_input (str): A string of card inputs in the format 'key-suit'.
            num_cards (int): The number of cards to parse.
            taken (list): A list of cards that have already been taken.

        Returns:
            dict: A dictionary where keys are card values and values are lists of suits.
    """
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
            suit = input_val
            curr_key = str(int(curr_key) - 2)
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


def check_royal(val):
    """
        Function to check whether a card is a face card or not

        Args:
            val(char): A card value or symbol

        Returns:
            boolean: Returns true if the card is a face card, else false
    """

    return val.lower() in "jqka"


def add_royal(val):
    """
        Converts a face_card to our own enumerating convention

        Args:
            val(char): A card value or symbol

        Returns:
            string: Returns the enumerated value corresponding the card symbol
    """

    if val.lower() == 'j':
        return "11"
    elif val.lower() == 'q':
        return "12"
    elif val.lower() == 'k':
        return "13"
    else:
        return "14"


def get_flop(taken):
    """
        Getter function to set and get flop cards from user input

        Args:
            taken(list): list of unavailable cards

        Returns:
            dict: Returns a dictionary of value:suit pairs converted to our enumerated values
    """

    print("\nPlease input cards using this format (key-suit-key-suit-key-suit)" +
          "\n D = diamond, C = clover, H = heart, S = spade\n" +
          "J = jack, Q = queen, K = king, A = Ace\n" +
          "CASE-INSENSITIVE\n" +
          "---\n")
    x = input("Input flop cards (Ex: 'Ad10cKc', '10d9s6c'): ").strip()
    return parse_cards(x, 3, taken)


def get_player(taken):
    """
        Getter and Setter function to initialize player cards

        Args:
            taken(list): list of unavailable cards

        Returns:
            dict: Returns a dictionary of value:suit pairs converted to our enumerated values
    """

    print("Please input cards using this format (key-suit-key-suit)" +
          "\n D = diamond, C = clover, H = heart, S = spade\n" +
          "J = jack, Q = queen, K = king, A = Ace\n" +
          "CASE-INSENSITIVE\n" +
          "---\n")
    x = input("Input player cards (Ex: 'AdKc', '10d9s'): ").strip()
    return parse_cards(x, 2, taken)


def convert_to_original(dictionary):
    """
        Converts cards back to their real values from our enumerated conventions

        Args:
            dictionary(dict): Dictionary of cards

        Returns:
            result(dict): Returns a dictionary of value:suit with original card values
    """
    result = {}
    for key in dictionary.keys():
        int_key = int(key)
        if int_key > 8:
            if int_key == 9:
                result['J'] = [suit for suit in dictionary[key]]
            elif int_key == 10:
                result['Q'] = [suit for suit in dictionary[key]]
            elif int_key == 11:
                result['K'] = [suit for suit in dictionary[key]]
            elif int_key == 12:
                result['A'] = [suit for suit in dictionary[key]]
        else:
            new_key = str(int_key)
            if new_key in result:
                result[new_key].extend([suit for suit in dictionary[key]])
            else:
                result[new_key] = [suit for suit in dictionary[key]]
    return result
