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

mydeck = Deck()

len(mydeck.all_cards)