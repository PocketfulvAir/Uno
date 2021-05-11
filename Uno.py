import random

class Card:
    def __init__(self, val, suit):
        self.val = val
        self.suit = suit

    def value(self):
        suit = self.suit + "s"
        val = self.val
        if self.val == 'A':
            val = "Ace"
        elif self.val == 'J':
            val = "Jack"
        elif self.val == 'Q':
            val = "Queen"
        elif self.val == 'K':
            val = "King"
        return val + " of " + suit

class Deck:
    values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    suits = ['diamond','club','heart','spade']
    def __init__(self):
        self.cards = []
        self.fullshuffle()

    def fullshuffle(self):
        for val in self.values:
            for suit in self.suits:
                self.cards.append(Card(val,suit))
        random.shuffle(self.cards)

    def shuffle(self, cards):
        random.shuffle(cards)
        self.cards = cards

    def show(self):
        for card in self.cards:
            print(card.value())

class Player:
    def __init__(self, name):
        self.name = name

class Board:
    ranking = []
    def __init__(self, players):
        self.players = players

    def kick_player(self, player):
        self.players.remove(player)
        self.ranking.append(player)

    def num_active_players(self):
        return len(self.players)

    def active_players(self):
        actives = ''
        for player in self.players:
            actives += player.name + " "
        return actives.strip()

class GameState:
    def __init__(self):
        self.turn = random.random() * 3
        players = []
        for i in range(4):
            players.append(Player("Player " + str(i)))
        self.board = Board(players)
        self.deck = Deck()

    def print_state(self):
        print("Players: ", self.board.active_players())
        print("Deck: ")
        self.deck.show()

if __name__ == '__main__':
    state = GameState()
    state.print_state()