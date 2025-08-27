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

RESOURCES_FULL = {
    "water": 300,
    "coffee": 100,
    "milk": 200,
}

COIN_VALUES = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.1,
    "quarter": 0.25,
}

def report_resources():
    print(f"""
          The remaining resources are:
          Water: {RESOURCES_FULL["water"]} mL
          Milk: {RESOURCES_FULL["milk"]} mL
          Coffee: {RESOURCES_FULL["coffee"]} g
          """)
    
def refill_resources():
    return RESOURCES_FULL

def check_resources(resource_bank, coffee_type):
    if all(
        resource_bank["water"] >= COFFEE_TYPES[coffee_type]["ingredients"]["water"],
        resource_bank["coffee"] >= COFFEE_TYPES[coffee_type]["ingredients"]["coffee"],
        resource_bank["milk"] >= COFFEE_TYPES[coffee_type]["ingredients"]["milk"]
        ): 
        return True
    else:
        return False

def sum_payment(penny, nickel, dime, quarter):
    penny = penny * COIN_VALUES["penny"]
    nickel = nickel * COIN_VALUES["nickel"]
    dime = dime * COIN_VALUES["dime"]
    quarter = quarter * COIN_VALUES["quarter"]

    total = penny + nickel + dime + quarter

    return total

def check_payment(payment, coffee_type):
    if payment >= COFFEE_TYPES[coffee_type]["price"]:
        return True
    else:
        return False

def give_change(payment, coffee_type):
    change = payment - COFFEE_TYPES[coffee_type]["price"]
    return change


# TODO: create coin operation function

# TODO: ask for the coins and gives changes

# TODO: check success of transaction



