# separate file for constants used in the program
# available coffee types and their attributes
COFFEE_TYPES = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18, "milk": 0,},
        "price": 1.50,
    },
    "latte": {
        "ingredients": {"water": 200, "coffee": 24, "milk": 150,},
        "price": 2.50,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "coffee": 24, "milk": 100,},
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