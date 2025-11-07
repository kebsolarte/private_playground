import random 
import os

# simple list of cards in the deck (A as 11; J, Q, K as 10)
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,]

# define functions
def deal_hand(deck, num):
    cards = random.choices(population=deck, k=num)
    return cards

def additional_draw(hand, deck):
    new_card = deal_hand(deck, 1)
    hand.extend(new_card)
    return hand

def sum_cards(cards):
    # sum() function can take an iterable as an input
    return sum(cards)

def blackjack_difference(cards):
    difference = 21 - sum_cards(cards)
    return difference

def over_21(cards):
    if sum_cards(cards) > 21:
        return True
    else: 
        return False
    
def flip_aces(cards):
    while over_21(cards) and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return cards

def determine_winner(dealer_score, player_score):
    if dealer_score < player_score:
        result = "The dealer wins!"
    elif dealer_score == player_score:
        result = "It's a draw!"
    else:
        result = "The player wins!"
    return result




# main program
game_over = False

while not game_over:
    print("Welcome to the simple blackjack game!\n")

    # initialize empty hands
    dealer = []
    player = []

    # initial draw for dealer and player
    dealer = deal_hand(deck, 2)
    player = deal_hand(deck, 2)

    # reveals first card of dealer and player cards
    print(f"The dealer's first card is {dealer[0]}.")
    print(f"Your cards are {player}.\n")
    
    # asks player if player wants another card
    choice = input("Would you like another card? (Y/N): ").lower()

    # used extend since the output of deal_hand function is a list
    if choice == 'y':
        additional_draw(player, deck)

    # draw another card for dealer if total is below 17
    if sum_cards(dealer) < 17:
        additional_draw(dealer, deck)
        print("\nThe dealer asked for another card.\n")

    # flips aces when necessary before checking the overall winner
    flip_aces(dealer)
    flip_aces(player)

    # disqualify dealer or player if sum is over 21
    if over_21(dealer) and not over_21(player):
        print("The dealer's hand is over 21, player wins!")
        game_over = True

    elif over_21(player) and not over_21(dealer):
        print("The player's hand is over 21, dealer wins!")
        game_over = True

    elif over_21(dealer) and over_21(player):
        print("Both hands are over 21, no one wins.")
        game_over = True 

    # valid game after extra draws
    print(f"\nThe dealer's cards are {dealer}")
    print(f"Your cards are {player}\n")
    print(f"The dealer's total is {sum_cards(dealer)}, while the player's total is {sum_cards(player)}.")

    # computes the blackjack differences
    dealer_score = blackjack_difference(dealer)
    player_score = blackjack_difference(player)

    # determine the winner
    result = determine_winner(dealer_score, player_score)
    print(result)

    # ask if player wants to keep playing
    new_game = input("Do you want to keep playing? (Y/N): ").lower()

    if new_game == 'y':
        os.system('cls' if os.name == 'nt' else 'clear')
        game_over = False
    else:
        game_over = True
        
    