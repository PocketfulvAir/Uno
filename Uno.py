import random

class Card:
    def __init__(self, val, suit):
        self.val = val
        self.suit = suit

class Deck:
    def __init__(self, cards):
        self.cards = cards

    def shuffle(self, cards):
        random.shuffle(cards)
        self.cards = cards

class Player:
    def __init__(self, name):
        self.name = name

class Board:
    def __init__(self, players):
        self.players = players



if __name__ == '__main__':
    print("hi")