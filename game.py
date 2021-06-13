'''
This is a recreation of the card game war in python
'''

#We'll use this later
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks= ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank 
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:

    def __init__(self):
        # Note this only happpens onoce upon creation of a new Deck
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                #This assumes the Card class has already been defined
                self.all_cards.append(Card(suit,rank))
    def shuffle(self):
        #This will not return anything
        random.shuffle(self.all_cards)
    
    def deal_one(self):
        #Note we remove one card from the list of all_cards
        return self.all_cards.pop()

class Player:
         
    def __init__(self, name):
        self.name = name
        #A new player has no cards
        self.all_cards = []

    def remove_one(self):
        # Note we remove one card from the list of all_cards
        # We state 0 to remove from the "top" of the deck
        # We'll imagine index -1 as the bottom of the deck
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
                self.all_cards.append(new_cards)

        def __str__(self):
            return f'Player {self.name} has {len{self.all_cards)} cards.'

player_one = Player("One")

player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

import pdb

game_on = True

round_num = 0
while game_on:

    round_num += 1
    print(f"Round {round_num}")

    #Check to see if a player is out of cards:
    if len(player_one.all_cards) == 0:
        print("Player One is out of cards! Game Over")
        print("Player Two Wins!")
        game_on = False
