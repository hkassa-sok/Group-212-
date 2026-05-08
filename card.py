# Gavin code 
class Card:
    """
    Represents a single card in the deck.
    """

    def __init__(self, rank, suits, points):
        self.rank = rank
        self.knock = suits
        self.points = points

    def __str__(self):
        return f"{self.rank} of {self.knock}"