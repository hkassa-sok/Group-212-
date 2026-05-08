from player import Player 
from deck import Deck 

class GinRummy: 
    """
    Controls the Gin Rummy game 
    """
    def __init__(self):
        self.deck = Deck()
        player1_name = input("Player 1, enter your name: ")
        player2_name = input("Player 2, enter your name: ")

        self.player1 = Player(player1_name)

        self.player2 = Player(player2_name)
        self.discard_pile = []
    def deal_cards (self):
        """
        Deals 10 cards to each player
        """
        for _ in range(10):
            self.player1.add_card(
                self.deck.draw_card()
            )
            self.player2.add_card(
                self.deck.draw_card()
            )
    def tutorial(self):
        """
        Explains how to play the game
        """
        print("\n" + "=" *40)
        print("  HOW TO PLAY GIN RUMMY")
        print("=" * 40)

        print(
            "\nGoal:"
            "\nCreate sets or runs while "
            "lowering your deadwood points."
        )

        print(
            "\nA SET is 3 or more cards "
            "with the same rank:"

        )
        print(
            "\nExample:"
            "\n7 of hearts"
            "\n7 of clubs"
            "\n7 of spades"
        )

        print(
             "\nExample:"
            "\n7 of hearts"
            "\n7 of clubs"
            "\n7 of spades"
        )
        
        print(
            "\nA RUN is cards in order "
            "with the same suit:"
        )
        
        print(
            "\nExample:"
            "\n4 of hearts"
            "\n5 of hearts"
            "\n6 of hearts"
        )
        
        print(
            "\nEach turn:"
            "\n1. Draw a card"
            "\n2. Discard a card"
            "\n3. Try to improve your hand"
        )
        
        print(
            "\nDeadwood points are cards "
            "not part of a set or run."
        )

        print(
            "\nYou win by knocking with "
            "low deadwood points." 
        )
        input("\nPress Enter to continue...")





    def start_game(self):
        """
        Runs the Gin Rummy game
        """
        print("Welcome to Gin Rummy!")
        print("\n1. Start Game")
        print("2. View Tutorial")

        choice = input("\nChoose an option: ")

        if choice == "2":

            self.tutorial()
        self.deal_cards()
        
        game_over = False 
        
        current_player = self.player1
        while not game_over:
            print("\n" + "=" *40)
            print(
            f"\n----- {current_player.name}'s Turn -----"
        )
                

            #Shows the player's hand 
            current_player.show_hand()
            print(
            f"\nCurrent Deadwood: "
            f"{current_player.calculate_deadwood()}"
        )
           
            # Show deck size
            print(
                f"\nCards left in deck: "
                f"{len(self.deck.cards)}"
            )
            if self.discard_pile:
                print(
                    f"Top Discard Card: "
                f"{self.discard_pile[-1]}"
                )

            # Draw Card
            input("\n Press Enter to draw a card...")
            draw_a_card = self.deck.draw_card()
            current_player.add_card(draw_a_card)
            print(f"\n You drew: {draw_a_card}")

           
            # Shows the updated hand
            current_player.show_hand()


            # Discard the card 

            discard = int(
                input(
                    "\nChoose the card index to discard: "
                )
            )
            discarded_card = current_player.remove_card(
                discard
            )

            self.discard_pile.append(
                discarded_card
            )
            print(
                f"\nYou discarded: "
                f"{discarded_card}"
            )
            sets_found = (current_player.find_sets())
            
            # Checks for the sets that are there 
            if sets_found: 
                print("\nSets Found:")
                for group in sets_found:
                    for card in group:
                        print(card)
                    print ()
                
                #Calculate the deadwood
                deadwood = (current_player.calculate_deadwood())
                print (
                    f"\nDeadwood Points: "
                f"{deadwood}"
            )
                #Empty deck check
                if len(self.deck.cards) == 0:
                    print("\nDeck is empty.")
                    game_over = True
                
                # Switch Players 
            if current_player == self.player1:
                    current_player = self.player2
            else:
                    current_player = self.player1
                
        








