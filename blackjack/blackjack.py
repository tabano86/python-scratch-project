import enum
import queue
import random
from functools import reduce


class Suit(enum.Enum):
    clubs = "Clubs"
    spades = "Spades"
    diamonds = "Diamonds"
    hearts = "Hearts"


class Card:
    name: str
    value: int
    suit: Suit

    def __init__(self, name: str, value: int, suit: Suit):
        self.name = name
        self.value = value
        self.suit = suit


class BlackjackGame:
    class Card:
        name: str
        value: int
        suit: Suit

        def __init__(self, name: str, value: int, suit: Suit):
            self.name = name
            self.value = value
            self.suit = suit

    card_deck: queue = []
    player_cards: list[Card] = list()

    def __init__(self):
        self.cards = []
        self.player_cards = list()
        self.generate_cards()
        self.shuffle_cards()
        print("You were dealt the following cards:")
        self.deal()

    def generate_cards(self):
        for _suit in Suit:
            for i in range(1, 15):
                if i <= 10:
                    self.card_deck.append(self.Card(str(i), i, _suit))
                elif i == 11:
                    self.card_deck.append(self.Card("Jack", i, _suit))
                elif i == 12:
                    self.card_deck.append(self.Card("Queen", i, _suit))
                elif i == 13:
                    self.card_deck.append(self.Card("King", i, _suit))
                elif i == 14:
                    self.card_deck.append(self.Card("Ace", i, _suit))

    def shuffle_cards(self):
        random.shuffle(self.card_deck)

    def deal(self):
        card: Card = self.card_deck.pop()
        self.player_cards.append(card)
        print(card.name + " of " + card.suit.value + "(" + str(card.value) + ")")

    def tally_cards(self) -> bool:
        return reduce(lambda a, b: a + b, map(lambda c: c.value, self.player_cards))


# Start game here (This part could be placed in a separate file)
game = BlackjackGame()
while (True):
    print("Would you like another card? [Y / N]")
    res = str(input())
    if res.lower() == "y":
        game.deal()
        if game.tally_cards() > 21:
            print("Game over")
            break
    elif res.lower() == "n":
        break
print("Game ended with a score of " + str(game.tally_cards()))
