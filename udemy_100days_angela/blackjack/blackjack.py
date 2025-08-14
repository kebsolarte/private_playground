import random 

# simple list of cards in the deck (A as 11; J, Q, K as 10)
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,]

# define functions
def deal_hand(deck, num):
    cards = random.choices(population=deck, k=num)
    return cards

def sum_cards(cards):
    total = 0
    for card in cards:
        total += card
    return total

def blackjack_difference(cards):
    difference = 21 - sum_cards(cards)
    return difference

def over_21(cards):
    if sum_cards(cards) > 21:
        return True
    else: 
        return False


# main program
game_over = False
dealer = []
player = []

print("Welcome to the simple blackjack game!\n")

while not game_over:
    # initial draw for dealer and player
    dealer = deal_hand(deck, 2)
    player = deal_hand(deck, 2)

    # reveals first card of dealer and player cards
    print(f"The dealer's first card is {dealer[0]}.")
    print(f"Your cards are {player}.\n")
    
    # asks player if player wants another card
    choice = input("Would you like another card? (Y/N): ").lower()

    if choice == 'y':
        additional_draw = deal_hand(deck, 1)
        player.extend(additional_draw)
        print(f"Your cards are {player}.\n")

    # draw another card for dealer if total is below 17
    if sum_cards(dealer) < 17:
        additional_draw = deal_hand(deck, 1)
        dealer.extend(additional_draw)
        print("\nThe dealer also asked for another card.\n")

    # disqualify dealer or player if sum is over 21
    if over_21(dealer) and not over_21(player):
        print("The dealer's hand is over 21, player wins!")
        break

    elif over_21(player) and not over_21(dealer):
        print("The player's hand is over 21, dealer wins!")
        break

    elif over_21(dealer) and over_21(player):
        print("Both hands are over 21, no one wins.")
        break 

    # valid game after extra draws
    print(f"\nThe dealer's cards are {dealer}")
    print(f"Your cards are {player}\n")
    print(f"The dealer's total is {sum_cards(dealer)}, while the player's total is {sum_cards(player)}.")

    # computes the blackjack differences
    dealer_hand = blackjack_difference(dealer)
    player_hand = blackjack_difference(player)

    # determine the winner
    if dealer_hand < player_hand:
        print("The dealer wins!")
    elif dealer_hand == player_hand:
        print("It's a draw!")
    else:
        print("The player wins!")

    game_over = True
        
    