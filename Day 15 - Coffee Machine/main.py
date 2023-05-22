from menu import MENU, resources
import random
# TODO
#  Make a surprise option which chooses for you

print("Welcome to the coffe machine! - Let's brew some beverages!")


# Set machine to on or off
machine_on = True

money_on_machine = 0


def resource_sufficient(ingredients):
    """Takes the user's choice to check if machine can make beverage
    Returns false if there are no ingredients and true if possible to make drink"""
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}")
        return False
    return True


def take_money():
    """Return total amount of coins inserted"""
    print("Please insert coins.")
    total = int(input("How many Quarters?: ")) * 0.25
    total += int(input("How many Dimes?: ")) * 0.21
    total += int(input("How many Nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_payment_successful(money_received, drink_cost):
    """Check if payment is true or return false if insufficient funds"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"Here is your change: ${change}")
        global money_on_machine
        money_on_machine += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_coffe(drink_name, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here's your {drink_name}!")


while machine_on:
    choice = input("What would you like to drink? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ${money_on_machine}")

    else:
        beverage = MENU[choice]
        if resource_sufficient(beverage["ingredients"]):
            money = take_money()
            if is_payment_successful(money, beverage["cost"]):
                make_coffe(choice, beverage["ingredients"])
