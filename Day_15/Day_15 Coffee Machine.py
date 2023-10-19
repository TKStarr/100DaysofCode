import menu

def resource_checker(order):
    """Checks to see if there are enough resources to make the drink"""
    for resource in menu.resources:
        if order[resource] > menu.resources[resource]:
            print(f"Sorry, not enough {resource}.")
            return False

    else:
        return True


def money_deposit():
    """calculates total amount of money inserted"""
    print("Please insert money.")
    pennies = int(input("How many pennies?"))
    nickels = int(input("How many nickels?"))
    dimes = int(input("How many dimes?"))
    quarters = int(input("How many quarters?"))
    dollars = int(input("How many dollar bills?"))

    money_inserted = .01 * pennies + .05 * nickels + .1 * dimes + .25 * quarters + dollars

    return money_inserted

def txn_success_checker(money_inserted,cost_of_drink):
    """Checks if enough user has paid enough money for the drink"""
    if money_inserted >= cost_of_drink:
        print(f"Thank you!  Here is your ${round(money_inserted - cost_of_drink,2)} change.")
        return True
    else:
        print(f"That's not enough money.  Try again.")
        return False

def drink_maker(drink_name, ingredients):
    """Makes the drink and subtracts the resources from the total resources."""
    for item in ingredients:
        menu.resources[item] = menu.resources[item] - ingredients[item]
    print(f"Here is your {drink_name}!")


power = 'on'

while power == 'on':
    coffee_order = input("What kind of coffee would you like? (espresso/latte/cappuccino).  Or type \'off\' to turn off the machine.")

    if coffee_order == 'off':
        power = 'off'
    elif coffee_order == 'status':
        print(f"{menu.resources['water']} ml of water")
        print(f"{menu.resources['milk']} ml of milk")
        print(f"{menu.resources['coffee']} ml of coffee")
    else:
        beverage = menu.MENU[coffee_order]
        print(f"The cost of this drink is {beverage['cost']}")
        if resource_checker(beverage['ingredients']) == True:
            payment = money_deposit()
            if txn_success_checker(payment, beverage['cost']):
                drink_maker(coffee_order, beverage['ingredients'])
