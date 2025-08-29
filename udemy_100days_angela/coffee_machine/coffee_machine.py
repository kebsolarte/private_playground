# available coffee types and their attributes
COFFEE_TYPES = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "price": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150,
        },
        "price": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100,
        },
        "price": 3.00,
    },
}


# resources bank at full capacity
RESOURCES_FULL = {
    "water": 300,
    "coffee": 100,
    "milk": 200,
}

# coin values in cents
COIN_VALUES = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.1,
    "quarter": 0.25,
}


def report_resources(resource_bank):
    """Reports current level of resources."""
    print(f"""
          The remaining resources are:
          Water: {resource_bank["water"]} mL
          Milk: {resource_bank["milk"]} mL
          Coffee: {resource_bank["coffee"]} g
          """)
    
def update_resources(resource_bank, coffee_type):
    """Updates resource bank after every successful order."""
    water = resource_bank["water"] - COFFEE_TYPES[coffee_type]["ingredients"]["water"]
    coffee = resource_bank["coffee"] - COFFEE_TYPES[coffee_type]["ingredients"]["coffee"]
    milk =resource_bank["milk"] - COFFEE_TYPES[coffee_type]["ingredients"]["milk"]

    return {"water": water, "coffee": coffee, "milk": milk}

def refill_resources():
    """Resets the level of resources."""
    return RESOURCES_FULL


def check_resources(resource_bank, coffee_type):
    """Checks if resources are enough for the desired coffee type."""
    if all(
        resource_bank["water"] >= COFFEE_TYPES[coffee_type]["ingredients"]["water"],
        resource_bank["coffee"] >= COFFEE_TYPES[coffee_type]["ingredients"]["coffee"],
        resource_bank["milk"] >= COFFEE_TYPES[coffee_type]["ingredients"]["milk"]
        ): 
        return True
    else:
        return False
    
def check_availability(order, resource_bank):
    """Checks if order is available."""
    if order not in [coffee for coffee in COFFEE_TYPES.keys]:
        print(f"Sorry {order} is not available. Please try again.")
        return False
    elif not check_resources(resource_bank, order):
        print(f"Sorry {order} is not available. We need to refill our stocks for that. Apologies. Please select another option.")
        return False
    else:
        return True
        

def get_payment():
    """Computes for the total value of coins inserted."""
    # asks for coin counts
    penny = int(input("Pennies: "))
    nickel = int(input("Nickels: "))
    dime = int(input("Dimes: "))
    quarter = int(input("Quarters: "))

    # computes for the total payment value
    penny = penny * COIN_VALUES["penny"]
    nickel = nickel * COIN_VALUES["nickel"]
    dime = dime * COIN_VALUES["dime"]
    quarter = quarter * COIN_VALUES["quarter"]

    total = penny + nickel + dime + quarter

    return total

def check_payment(payment, coffee_type):
    """Checks if payment is enough for the order."""
    if payment >= COFFEE_TYPES[coffee_type]["price"]:
        return True
    else:
        return False

def give_change(payment, coffee_type):
    """Computes and returns the change to the customer, if any."""
    change = payment - COFFEE_TYPES[coffee_type]["price"]
    
    if change == 0:
        print("Thank you for giving the exact amount!")
    else:
        print(f"Thank you. Here's your change of ${change}.")

def another_transaction():
    """Asks if user wants another transaction."""
    repeat = input("Would you like another transaction (y/n)?: ").lower()

    if repeat == 'y':
        return True
    else: 
        return False


# main program
successful_transaction = False

resource_bank = {
    "water": 300,
    "coffee": 100,
    "milk": 200,
}

while not successful_transaction:
    print("Welcome to Kevin's coffee machine!")

    # take order
    order = input("What do you want today? I can make you an espresso, latte, or cappuccino!: ").lower()

    # secret maintenance functions for operators
    if order == 'report':
        report_resources(resource_bank)
    elif order == 'refill':
        resource_bank = refill_resources()

    # check availability
    elif not check_availability(order, resource_bank): continue

    # proceeds with order and asks for payment
    else:
        print(f"Nice order! That would be ${COFFEE_TYPES[order]["price"]} only. Kindly insert your coins below:")
        payment = get_payment()

        # checks if payment is enough, and proceeds with making order if it is
        if check_payment(payment, order):
            give_change(payment, order)
            print(f"Let me make your {order}.")
            print("Creating yummy magic ...")
            print("Dispensing ...")
            print(f"Thank you for waiting! Here's you {order}. Have a nice day!")
            resource_bank = update_resources(resource_bank, order)
        else:
            print("Sorry, you have entered an insufficient amount.")
            print(f"Giving you back your ${payment}. Please try again.")

    if another_transaction():
        continue
    else:
        successful_transaction = True

    