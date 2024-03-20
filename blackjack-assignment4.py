import random


# Deals a card. Values range from 1 to 10
def deal_card():
    return random.randint(1, 10)


# Handles the player's turn.  Returns the point value for the player's hand.
def get_score():
    # ACTION: Initial Deal
    player_val = deal_card()    # Get the player's score. [player's 1st draw]
    dealer_val = deal_card()    # Get dealer's score.     [dealer's 1st draw]
    player_val += deal_card()   # Get the player's score. [player's 2nd draw]
    dealer_val += deal_card()   # Get dealer's score.     [dealer's 2nd draw]

    print("The sum of your first two cards is:", player_val)

    user_response = input("HIT or STAY: Do you want to take another card?: (Y/N)")

    ## you should display the sum of the two cards
    ## then, ask users whether they want to get another card
    ## if either the user is busted or the user wants to stop, then you need to stop
    while user_response == "Y" or user_response == "y":

        ## Once you got the player_score, you have to check whether the player got busted, whether player's score
        ## is larger than the dealer's score. According to the result you should diaply different prompt.
        ## You also need to check whether dealer got busted.

        # ACTION: Deal
        player_val += deal_card()  # Get the player's score.
        dealer_val += deal_card()  # Get dealer's score.

        print("Your hand now has a total value of ", player_val)
        if player_val > 21:
            return player_val, dealer_val
        else:
            ## ask user whether they want to get another card
            user_response = input("HIT or STAY: Do you want to take another card?: (Y/N)")


    ## return the player's score
    return player_val, dealer_val

# The main function.  It repeatedly plays games of blackjack until the user decides to stop.
def main():
    # Prime the loop and start the first game.
    user_response = "Y"
    while user_response == "Y" or user_response == "y":
        # Get scores of the player and dealer.
        # Game STARTS
        player, dealer = get_score()

        ## Once you got the player_score and dealer_score, you have to check whether the player got busted, whether player's score
        ## is larger than the dealer's score. you also need to check the dealer's score.
        ## According to the result you should diaply different prompt.

        # Game ENDING
        print("You have stopped taking more cards with a hand value of", player)

        if player > 21:                             # Player busts
            print("You BUSTED with a total value of", player)
            print("** You lose. **")
        elif (dealer > player) and (dealer < 21):   # Dealer busts
            print("The dealer was dealt a hand with a value of", dealer)
            print("** You lose! **")
        elif (dealer > 21) and (player < 21):       # Dealer busts
            print("The dealer was dealt a hand with a value of", dealer)
            print("** You win! **")
        elif (player > dealer) and (player <= 21):  # Player wins
            if player == 21:
                print("You got a BLACKJACK!")
            print("** You win! **")
        elif player == dealer:                      # Ties
            print("TIE or PUSH")
            print("** No winners or losers! **")

        ## ask user whether he/she wants to play another game
        user_response = input("Do you want to play another game?: (Y/N)")


# Call the main function to start the blackjack program.
main()