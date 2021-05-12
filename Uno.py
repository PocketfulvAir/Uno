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
        '''
        Add card to player's hand
        '''
        self.cards.append(card)

    def play(self, card_index):
        return self.cards.pop(card)
    
    def get_card(self, index):
        return self.cards[index]

    def hand_size(self):
        return len(self.cards)

    def wipe_hand(self):
        self.cards.clear()

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
        self.active = {0,1,2,3}

    def reset_deck(self):
        self.deck = Deck()

    def kick_player(self, playernum):
        self.active.remove(playernum)
        self.ranking.append(player)

    def ingame(self, playernum):
        if playernum in self.active:
            return True
        return False

    def num_active_players(self):
        return len(self.active)

    def active_players(self):
        actives = ''
        for playernum in self.active:
            actives += self.players[playernum].name + " "
        return actives.strip()

class Pile:
    def __init__(self):
        self.stack = []

    def add(self, card):
        self.stack.append(card)

    def wipe(self):
        self.stack.clear()

    def scoop(self):
        top = self.stack.pop()
        output = self.stack
        self.stack = top
        return output

    def top_card(self):
        if len(self.stack) < 1:
            print("this is somehow empty")
            return "Nan"
        return self.stack[-1]

class GameState:
    '''
    Overmind. Maintains all objects states and controls actions taken.
    '''
    def __init__(self):
        self.turn = random.randint(0,3)
        players = []
        for i in range(4):
            players.append(Player("Player " + str(i)))
        self.board = Board(players)
        self.pile = Pile()
    
    def end_turn(self):
        self.turn = self.turn + 1 if self.turn < self.board.num_active_players() - 1 else 0

    def draw(self):
        card = self.board.deck.draw_card()
        self.board.players[self.turn].add_card(card)

    def playable(self, card):
        check_card = self.pile.top_card()
        if card.val == check_card.val or card.suit == check_card.suit:
            return True
        return False

    def all_playable(self):
        cards = []
        current_player = self.board.players[self.turn]
        for i in range(current_player.hand_size()):
            if self.playable(current_player.get_card(i)):
                cards.append(i)
        return cards

    def play_card(self, card_index, player):
        pass

    def init_draw(self):
        init_hand_size = 6
        for i in range(self.board.num_active_players()):
            for j in range(init_hand_size):
                card = self.board.deck.draw_card()
                self.board.players[i].add_card(card)
    
    def start_game(self):
        for player in self.board.players:
            player.wipe_hand()
        self.board.reset_deck()
        self.pile.wipe()
        self.init_draw()
        self.pile.add(self.board.deck.draw_card())

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
    state.start_game()
    for player in board.players:
        print(player.name + ": "+ player.show_hand())
    while power:
        no_move = 1
        current_player = board.players[state.turn]
        print(current_player.name + ": "+ current_player.show_hand())
        print(current_player.name + "'s turn")
        print("Current Card: ", state.pile.top_card().value_abr())
        playables = state.all_playable()
        print("Playable Cards: ", playables)
        print("Playable values: ", [current_player.cards[i].value_abr() for i in playables])
        while no_move:
            action = input("Enter action: ")
        
            if action == "e":
                power = 0
            else:
                try:
                    choice = int(action)
                except ValueError:
                    print("Choice not an int")
            no_move = 0              
        state.end_turn()