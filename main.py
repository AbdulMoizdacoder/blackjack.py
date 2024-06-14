# Import
import random

# Variables
hearts = "♥"
clubs = "♣"
diamonds = "♦"
spades = "♠"
suits = [hearts, clubs, diamonds, spades]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "JACK", "QUEEN", "KING", "ACE"]
values = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "JACK": 10, "QUEEN": 10, "KING": 10, "ACE": 11
}

class Card:
    #Class representing a single card in the deck
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def print_card(self):
        #Prints the card in a readable format
        print(f"a {self.value} of {self.suit}")

class Deck:
    #Class representing a deck of cards
    def __init__(self):
        self.card_deck = []
        self.full_deck()
        self.shuffle_deck()

    def build_deck(self):
        #Builds a single deck of 52 cards
        for s in suits:
            for r in ranks:
                self.card_deck.append(Card(r, s))
    
    def full_deck(self):
        #Builds a full deck consisting of 6 standard decks
        for _ in range(6):
            self.build_deck()

    def get_card(self):
        #Draws a card from the deck
        return self.card_deck.pop()
    
    def shuffle_deck(self):
        #Shuffles the deck
        random.shuffle(self.card_deck)

class Player:
    #Class representing a player in the game
    def __init__(self):
        self.hand = []
        self.points = 0

    def draw(self, times, deck):
        #Draws a specified number of cards from the deck
        for _ in range(times):
            user_card = deck.get_card()
            self.hand.append(user_card)
            self.points += values[user_card.value]
            self.adjust_for_ace()

    def adjust_for_ace(self):
        #Adjusts the value of an Ace if the total points exceed 21
        for card in self.hand:
            if self.points > 21 and card.value == "ACE":
                self.points -= 10

    def show_hand(self):
        #Displays the player's hand
        for card in self.hand:
            card.print_card()
        print(f"Total points: {self.points}")

class Game:
    #Class representing the Blackjack game
    def __init__(self):
        self.player = Player()
        self.computer = Player()
        self.deck = Deck()
        self.loop = False

    def start_game(self):
        #Starts the Blackjack game
        print(f"\nWelcome to BlackJack!")
        user_start_input = input(f"\nDo you want to play (y/n)? ")
        if user_start_input == "n":
            print("Goodbye!")
        elif user_start_input == "y":
            self.loop = True
        while self.loop:
            if self.deck.card_deck:
                self.play_round()
            else:
                print("Deck is empty. Game over!")
                self.loop = False

    def play_round(self):
        #Plays a round of Blackjack
        print(f"\nYou drew:")
        self.player.draw(2, self.deck)
        self.player.show_hand()

        print("\nDealer draws one card:")
        self.computer.draw(1, self.deck)
        self.computer.show_hand()

        while self.player.points < 21:
            user_input1 = input("\nWould you like to hit or stand? (hit/stand): ")
            if user_input1 == "hit":
                self.player.draw(1, self.deck)
                self.player.show_hand()
                if self.player.points > 21:
                    print("You busted! Dealer wins.")
                    self.loop = False
                    return
            elif user_input1 == "stand":
                break

        while self.computer.points < 17:
            print("\nDealer draws one card:")
            self.computer.draw(1, self.deck)
            self.computer.show_hand()
            if self.computer.points > 21:
                print("Dealer busted! You win.")
                self.loop = False
                return

        self.determine_winner()

    def determine_winner(self):
        #Determines the winner of the round
        if self.player.points > self.computer.points:
            print("You win!")
        elif self.player.points < self.computer.points:
            print("Dealer wins!")
        else:
            print("It's a tie!")
            self.loop = False
# Main game loop
if __name__ == "__main__":
    game = Game()
    game.start_game()


            
            



