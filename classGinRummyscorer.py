class Card:
    """
    Represents a single card in the deck.
    """

    def __init__(self, gin, knock, points):
        self.rank = gin
        self.knock = knock
        self.points = points

    def __str__(self):
        return f"{self.rank} of {self.knock}"