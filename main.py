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
        self.shuffle_deck()

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
        
    def draw(self,times,deck): 
        self.hand = []
        for i in range(times):
            user_card = deck.get_card()
            self.hand.append(user_card)
            self.hand[-1].print_card()
            i +=1

class Game():
    def __init__(self):
        pass
    player = Player()
    computer = Player()
    deck = Deck()

    loop = False
    print(f"\nWelcome to BlackJack!")
    user_start_input = input(f"\nDo you want to play (y/n)?")
    if user_start_input == "n":
        print("goodbye!")
    elif user_start_input == "y":   
        loop=True
    while loop:
            print(f"you drew")
            player.draw(2,deck)
            #draw card for computer
            print("\ndealer draws one card")
            computer.draw(1,deck)
            

            
            



