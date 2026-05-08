import random 
from card import Card


class Deck:
    """
    Represents a deck of card 
    """
    def __init__(self):
        self.cards = []
        self.create_deck()
        self.shuffle ()
    def create_deck(self):
        """
        Creates a 52 card deck 
        """
        suits = [
            "spades",
            "hearts",
            "diamonds",
            "clubs"
        ]
        ranks = [
            "A","2","3","4","5",
            "6","7","8","9","10",
            "J","Q","K"
        ]
        for suit in suits:
            for rank in ranks:
                if rank == "A":
                    points = 1
                elif rank in ["J", "Q", "K"]:
                    points = 10
                else:
                    points = int(rank)
                
                card = Card(rank,suit,points)
                self.cards.append(card)
    def shuffle(self):
        """
        Randomly shuffles the cards
        """
        random.shuffle(self.cards)
    
    def draw_card(self):
        """
        Removes and returns the top card
        """
        return self.cards.pop()

