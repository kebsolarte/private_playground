import os

print("Welcome to the secret auction program.")

# initializes the dictionary and iterator
bids = {}
auction_end = False

# main program
while not auction_end:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: "))

    # populates the dictionary with user input
    bids[name] = bid

    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")

    if other_bidders == 'yes':
        os.system('cls' if os.name == 'nt' else 'clear')
        continue
    else:
        os.system('cls' if os.name == 'nt' else 'clear')

        # initializes the highest bidder and bid values
        highest_bid = 0
        highest_bidder = None
        
        # loops throught the dictionary and check for the highest bidder and bid
        for name, bid in bids.items():
            if bid > highest_bid:
                highest_bidder = name
                highest_bid = bid
            
        print(f"The winner is {highest_bidder} with a bid of ${highest_bid}!")

        # breaks the while loop
        auction_end = True




