from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    user_order = input(f"What would you like? ({menu.get_items()}): ")
    if user_order == "off":
        is_on = False
    elif user_order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_order)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)





