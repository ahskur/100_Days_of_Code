from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

print("Welcome to the coffee machine - Let's get you something hot to drink!")

# Set flag to turn machine on/off
is_on = True
# Now let's use our 'blueprints' to make the parts of our project
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like to drink? ({options}) ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        chosen_drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(chosen_drink):
            if money_machine.make_payment(chosen_drink.cost):
                coffee_maker.make_coffee(chosen_drink)
