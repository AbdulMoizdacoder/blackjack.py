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

class Card:
    def __init__(self,value,suit):
        self.value = value
        self.suit = suit
    
    def print_card(self):
        print(f"a {self.value} of {self.suit}")

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
        user_card = deck.get_card()
        self.hand.append(user_card)

class Computer():
    def __init__(self):
        pass

class Deal():
    def __init__(self):
            pass
   

class Game():
    def __init__(self):
        pass
    player = Player()
    computer = Player()
    deck = Deck()

    loop = True
    while loop:
        print(f"\nWelcome to BlackJack!")
        user_start_input = input(f"\nDo you want to play (y/n)?")
        if user_start_input == "n":
            print("goodbye!")
        elif user_start_input == "y":   
            #draw cards for player
            deck.shuffle_deck()
            print(f"you drew")
            player.deal_card(deck)
            player.deal_card(deck)
            player.print_card(deck)
            #draw card for computer
            print("\ndealer draws one card")
            computer.deal_card(deck)
            

            
            



