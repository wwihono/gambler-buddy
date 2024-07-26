def generate_possibilities():

    pass

# Main function
# Generate player and flop cards and determine percentage that the player has
# of having the winning hand.
if __name__ == '__main__':
    INITIAL_CARDS = list(range(1,53))
    PLAYER_CARDS = [] # players initial 2 cards
    NUM_PLAYERS = 2
    FLOP_CARDS = [] # take in multiple input for flop cards


def getFlop(FLOP_CARDS):
    print("Please input cards using this format(value-suit-value-suit-value-suit)"+
          "\n D = diamond, C = clover, H = heart, S = spade\n" +
          "J = jack, Q = queen, K = king, A = Ace\n" +
          "CASE-INSENSITIVE\n"
          "---\n")
    for i in range(3):
        # a = diamond, b = clover, c = heart, d = spade
        x = input("Input flop card" + str(i+1) + " (Ex: 'Aa6cAd', '10a9b6c'): ")
        FLOP_CARDS.append(x)

def getPlayer(PLAYER_CARDS):
