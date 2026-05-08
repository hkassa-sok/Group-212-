class Player:
    """
    Represents a player in Gin Rummy
    # Heyaw Kassa's contribution
    """
    def __init__(self,name):
        self.name = name 
        self.hand = []
        self.score = 0
    def add_card(self, card):
        # Heyaw Kassa's contribution
        """
        This adds card to the players hand
        """
        self.hand.append(card)
    
    def show_hand(self):
        #Heyaw Kassa's contribution
        """
        Displays all cards in the player's hand
        """
        print(f"\n{self.name}'s Hand: ")

        for i, card in enumerate (self.hand):
            print(f"{i}: {card}")
    
    def remove_card(self, number):
        # Heyaw Kassa's contribution
        """
        This is to remove a card from the player's hand
        """
        return self.hand.pop(number)
    
    def find_sets(self):
        #Heyaw Kassa's contribution
        """
        Finds all the common sets that a player has in their hand in order to
        highlight how many points they possibly have
        """
        group_sets = {}

        # Groups cards by rank 
        for card in self.hand:
            rank = card.rank 

            if rank not in group_sets:
                group_sets[rank] = []
            group_sets[rank].append(card)
            
        # Finds the valid sets
        sets = []

        for rank in group_sets:
            if len(group_sets[rank])>= 3:
                sets.append(group_sets[rank])
        
        return sets
    
    def calculate_deadwood(self):
        # Heyaw Kassa's code 
        """
        Calculates deadwood points by ignoring cards that 
        are part ofsets
        """
        sets_found = self.find_sets()
        cards_in_sets = []
        # Stores all the card used in sets 
        for group in sets_found:
            for card in group:
                cards_in_sets.append(card)
        total = 0
        #Only counts the cards not in sets 
        for card in self.hand:
            if card not in cards_in_sets:
                total += card.points
        return total 

    def can_knock(self):
        """
        Checks if the player can knock by adding up
        the deadwood points in their hand.
    Returns True if deadwood is 10 or less.
    """
        return self.calculate_deadwood() <= 10
    
            