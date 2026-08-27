import time
import sys
from constants import COFFEE_TYPES, RESOURCES_FULL, COIN_VALUES

def loading_animation(text, duration=3):
    """Creates a loading animation and a little pause for printing texts"""
    end_time = time.time() + duration
    while time.time() < end_time:
        # creates the dots animation
        for dot in range(4):
            sys.stdout.write(f"\r{text}{'.' * dot} ")   # \r overwrites the current line
            sys.stdout.flush()  # this forces immediate printing without waiting for the loop
            time.sleep(0.5)
    print()

def report_resources(resource_bank):
    """Reports current level of resources."""
    loading_animation("Checking resource levels")
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
    loading_animation("Refilling resources")
    return RESOURCES_FULL


def check_resources(resource_bank, coffee_type):
    """Checks if resources are enough for the desired coffee type."""
    # all() only takes one iterable as an argument, either tuple or list
    return all([
        resource_bank["water"] >= COFFEE_TYPES[coffee_type]["ingredients"]["water"],
        resource_bank["coffee"] >= COFFEE_TYPES[coffee_type]["ingredients"]["coffee"],
        resource_bank["milk"] >= COFFEE_TYPES[coffee_type]["ingredients"]["milk"]
        ])
    
def check_availability(order, resource_bank):
    """Checks if order is available."""
    if order not in [coffee for coffee in COFFEE_TYPES.keys()]:
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

    return round(total, 2)

def check_payment(payment, coffee_type):
    """Checks if payment is enough for the order."""
    return payment >= COFFEE_TYPES[coffee_type]["price"]

def give_change(payment, coffee_type):
    """Computes and returns the change to the customer, if any."""
    change = payment - COFFEE_TYPES[coffee_type]["price"]
    
    if change == 0:
        print("Thank you for giving the exact amount!")
    else:
        print(f"Thank you. Here's your change of ${change:.2f}.")

def another_transaction():
    """Asks if user wants another transaction."""
    repeat = input("Would you like another transaction (y/n)?: ").lower()

    return repeat == 'y'