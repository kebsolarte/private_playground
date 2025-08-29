from constants import COFFEE_TYPES
import functions as utils


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
        utils.report_resources(resource_bank)
    elif order == 'refill':
        resource_bank = utils.refill_resources()
        utils.report_resources(resource_bank)

    # check availability
    elif not utils.check_availability(order, resource_bank): continue

    # proceeds with order and asks for payment
    else:
        print(f"Nice order! That would be ${COFFEE_TYPES[order]["price"]} only. Kindly insert your coins below:")
        payment = utils.get_payment()

        # checks if payment is enough, and proceeds with making order if it is
        if utils.check_payment(payment, order):
            utils.give_change(payment, order)
            utils.loading_animation(f"Let me make your {order}")
            utils.loading_animation("Creating yummy magic")
            utils.loading_animation("Dispensing")
            print(f"Thank you for waiting! Here's you {order}. Have a nice day!")
            resource_bank = utils.update_resources(resource_bank, order)
        else:
            print("Sorry, you have entered an insufficient amount.")
            print(f"Giving you back your ${payment}. Please try again.")

    if utils.another_transaction():
        continue
    else:
        successful_transaction = True

    