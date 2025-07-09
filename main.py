import sys
import random
import math


def buildDeck(numDecks, cutDecks):
    if numDecks <= cutDecks or numDecks < 1:
        print(
            "Number of decks must be at least 1 and greater than the number of cut decks."
        )
        sys.exit()
    if cutDecks < 0.5:
        print("Must cut at least 0.5 decks.")
        sys.exit()

    deck = []
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    cards = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]

    for suit in suits:
        for card in cards:
            deck.append([suit, card])

    deckSize = len(deck)
    if deckSize < 52:
        print("Decks should be at least 52 cards.")
        sys.exit()

    deck = numDecks * deck
    random.shuffle(deck)
    deck.insert(
        math.floor(random.uniform(-5, 5) + deckSize * (numDecks - cutDecks)),
        ["Cut", "C"],
    )

    return deck


if __name__ == "__main__":
    print(buildDeck(numDecks=1, cutDecks=0.5)[20:30])
