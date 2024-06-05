#Import
import random
#main python loop

# Variables
hearts = "♥"
clubs = "♣"
diamonds = "♦"
spades = "♠"
suits = [hearts, clubs,diamonds, spades]
ranks = ["2","3","4","5","6","7","8","9","10","JACK","QUEEN","KING","ACE"]

face_cards = [
    {"ACE","11"},
    {"KING","10"},
    {"QUEEN","10"},
    {"JACK","10"} 
]

class Card:
    def __init__(self,value,suit):
        self.value = value
        self.suit = suit
    
    def print_card(self):
        print(f"you drew a {self.value} of {self.suit}")

class Deck: 
    def __init__(self): 
        self.card_deck = []     
        for i in range(3):
            self.build_deck()
            i+=1

    def build_deck(self):
        for s in suits:
            for r in ranks:
                self.card_deck.append(Card(r,s))

    def show_card(self):
        for i in self.card_deck:
            i.print_card()

    def get_card(self):
        card = self.card_deck.pop()
        return card 
    
    def shuffle_deck(self):
        random.shuffle(self.card_deck)
    
class Player():
    def __init__(self):
        pass
    
    def deal_card(self, deck):
        self.hand = []
        self.points = 0
        i = 0
        user_card = deck.get_card()
        self.hand.append(user_card)
        self.hand[i].print_card()
        i+=1

            
                

deck = Deck()
deck.shuffle_deck()
deck.show_card()
player = Player()
player.deal_card(deck)
player.deal_card(deck)
