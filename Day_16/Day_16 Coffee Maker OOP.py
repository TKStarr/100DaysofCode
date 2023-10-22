from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

power = True

while power == True:
    options = menu.get_items()
    coffee_order = input(f"What kind of coffee would you like? {options}")
    if coffee_order == "off":
        power = False
    elif coffee_order == "status":
        coffee_maker.report()
        money_machine.report()
    else:

        coffee_order = menu.find_drink(coffee_order)
        if coffee_maker.is_resource_sufficient(coffee_order) and money_machine.make_payment(coffee_order.cost):
               coffee_maker.make_coffee(coffee_order)



