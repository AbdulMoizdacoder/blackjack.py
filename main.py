#main python loop

# Variables
hearts = "♥"
clubs = "♣"
diamonds = "♦"
spades = "♠"
suits = [hearts, clubs,diamonds, spades]
ranks = ["2","3","4","5","6","7","8","9","10","JACK","QUEEN","KING","ACE"]
card_deck = []
face_cards = [
    {"KING","10"},
    {"QUEEN","10"},
    {"JACK","10"},
    {"ACE","11"}
]

class Card:
    def __init__(self,value,suit):
        self.value = value
        self.suit = suit
    
    def print_card(self):
        print(f"you drew a {self.value} of {self.suit}")

class Deck:
    def __init__(self):
        self.cards = []
        self.create()

    def create(self):
        for s in suits:
            for r in ranks:
                self.cards.append(Card(r,s))
    
    def show(self):
        for c in self.cards:
            c.print_card()


deck = Deck()
deck.show()


