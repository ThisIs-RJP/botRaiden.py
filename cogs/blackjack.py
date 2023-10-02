#!/usr/bin/env python3
#### IMPORTING

import random

"""
    Made by Smoodeazy, RJ, 2023
    Feel free to edit the code as much as you like
"""

cardSym: list = ["Spades", "Clubs", "Hearts", "Diamonds"]
faceCards: list = ["King", "Queen", "Jack", "Ace"]
invalid: str = "Invalid Input. Please try again"
values: list = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "King", "Queen", "Jack"]

def makeDeck():
    deck = []
    for i in cardSym:
        for j in values:
            deck.append(f"{j} of {i}")
    
    return deck

class Game():

    def __init__(self, deck):

        self.player = 0
        self.playerHand = 2
        self.dealerHand = 2
        self.dealer = 0
        self.deck = deck

    def hit(self, q, amount):

        if q == "dealer":
            self.dealer = self.dealer + amount
        
        else:
            self.player = self.player + amount

    def addCard(self):
        print(self.deck)
        card = random.choice(self.deck)
        self.deck.remove(card)

        return f"{card}"

    def createHand(self):
        hand = []
        for i in range(2):
            card = random.choice(self.deck) # Creating a hand and removing the card being used from the original list
            self.deck.remove(card)
            hand.append(card)
        
        return hand

    def getHandValue(self, hand):
        output = []
        for j in hand: # Go through the hand
            first = j.split()[0] # Split the string, an input such as "King of Spades" will be split into a list ["King", "Of", "Spades"]
            # By getting the first element of the list, we find out the value of the card
            if first in faceCards and first != "Ace":
                output.append(10)
                
            elif first == "Ace":
                output.append("11A") ## Return 11 if its an ace, this will be used later...
                
            else:
                output.append(int(first))

        # print(output)
        return output
