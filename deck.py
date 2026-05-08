from typing import Self


class Deck

    def_init_(self): # type: ignore
    Self.cards = []
    self.create_deck()
    self.shuffle()

    def create_deck(self):
        
       pattern = ["hearts", "spades", "diamonds", "clubs"]
       
       ranks = [ 
                "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"
            ] 
       
       for pattern: str in pattern
    for rank in rank:
                
                if rank == "A"
                    points = 1
                    
                elif rank in ["J", "Q", "K"]:
                    points = 10
                    
                else:
                    points = int(rank) 
                    
                card = Card(rank, pattern, points)
                
                self.cards.append(card)
                
            def shuffle(self):
                random.shuffle(self.cards)
                
            def draw_card(self):
                return self.cards.pop()