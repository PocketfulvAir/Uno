import random

class Card:
    def __init__(self, val, suit):
        self.val = val
        self.suit = suit

    def value(self):
        suit = self.suit.lower()
        valid = {'d','c','h','s'}
        if suit in valid:
            suit_name = "diamonds" if suit == 'd' else "clubs" if suit == 'c' else "hearts" if suit == 'h' else "spade"      
        else:
            raise Exception("not a valid card")
        val = self.val
        if self.val == 'A':
            val = "Ace"
        elif self.val == 'J':
            val = "Jack"
        elif self.val == 'Q':
            val = "Queen"
        elif self.val == 'K':
            val = "King"
        return val + " of " + suit_name

    def value_abr(self):
        '''
        value abbreviated
        '''
        return self.val + self.suit

class Deck:
    values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    suits = ['D','C','H','S']
    def __init__(self):
        self.cards = []
        self.fullshuffle()

    def decksize(self):
        return len(self.cards)

    def fullshuffle(self):
        '''
        Shuffle the entire deck of cards
        '''
        for val in self.values:
            for suit in self.suits:
                self.cards.append(Card(val,suit))
        random.shuffle(self.cards)

    def shuffle(self, cards):
        '''
        Randomly shuffle the cards not in visible play
        '''
        random.shuffle(cards)
        self.cards = cards

    def draw_card(self):
        '''
        Draw a card from the top of the deck
        '''
        return self.cards.pop(0)

    def show(self):
        ''' 
        Display the value of the cards inside the deck in order
        '''
        output = ''
        for card in self.cards:
            output += card.value

class Player:

    def __init__(self, name):
        self.name = name
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def play(self, card):
        self.cards.remove(card)

    def show_hand(self):
        hand = ''
        for card in self.cards:
            hand += "[" + card.value_abr() + "]"
        return hand

class Board:

    def __init__(self, players):
        self.players = players
        self.deck = Deck()
        self.ranking = []

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
        self.turn = random.randint(0,3)
        players = []
        for i in range(4):
            players.append(Player("Player " + str(i)))
        self.board = Board(players)
    
    def end_turn(self):
        self.turn = self.turn + 1 if self.turn < self.board.num_active_players() - 1 else 0

    def draw(self):
        card = self.board.deck.draw_card()
        self.board.players[self.turn].add_card(card)

    def init_draw(self):
        init_hand_size = 6
        for i in range(self.board.num_active_players()):
            for j in range(init_hand_size):
                card = self.board.deck.draw_card()
                self.board.players[i].add_card(card)

    def print_state(self):
        print("Players: ", self.board.active_players())
        print("Deck: ")
        self.deck.show()

if __name__ == '__main__':
    state = GameState()
    board = state.board
    #state.print_state()
    print(state.turn)
    state.init_draw()
    print(board.deck.decksize())
    power = 1
    while power:
        for player in board.players:
            print(player.name + ": "+ player.show_hand())
        print(board.players[state.turn].name + "'s turn")
        
        action = input("Enter action: ")
        state.end_turn()
        if action == "e":
            power = 0