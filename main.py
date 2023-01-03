from data import MENU
from data import resources

real_resources = {
    "water": resources['water'],
    "milk": resources['milk'],
    "coffee": resources['coffee'],
    "money": 0
}


# TODO: 1. print report
def report(real_resources):
    print(f"""
    Water: {real_resources["water"]}ml
    Milk: {real_resources["milk"]}ml
    Coffee: {real_resources["coffee"]}g
    Money: ${round(real_resources["money"], 2)}
    """)


# TODO: 2. check resource sufficient?
def check_resources(product, real_resources):
    if "water" in MENU[product]["ingredients"]:
        product_water = MENU[product]["ingredients"]["water"]
        if product_water > real_resources["water"]:
            print("There is not enough water..")
            return False

    if "coffee" in MENU[product]["ingredients"]:
        product_coffee = MENU[product]["ingredients"]["coffee"]
        if product_coffee > real_resources["coffee"]:
            print("There is not enough coffee..")
            return False

    if "milk" in MENU[product]["ingredients"]:
        product_milk = MENU[product]["ingredients"]["milk"]
        if product_milk > real_resources["milk"]:
            print("There is not enough milk..")
            return False
    return True


# TODO: 3. process coins
def process_coins():
    print("Please insert coins...")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennis = float(input("How many pennis?: "))
    money = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennis * 0.01
    # print(round(money, 2))
    return money


# TODO: 4. check transaction successful?
def check_transaction(product, money):
    price = MENU[product]["cost"]
    print(f"money: {money}")
    print(f"price: {price}")
    if float(money) < price:
        print("There is not enough money..")
        return False
    return True


# TODO: 5. make coffee
def make_coffee(product, real_resources, money):
    if "water" in MENU[product]["ingredients"]:
        product_water = MENU[product]["ingredients"]["water"]
        real_resources["water"] = real_resources["water"] - product_water

    if "coffee" in MENU[product]["ingredients"]:
        product_coffee = MENU[product]["ingredients"]["coffee"]
        real_resources["coffee"] = real_resources["coffee"] - product_coffee

    if "milk" in MENU[product]["ingredients"]:
        product_milk = MENU[product]["ingredients"]["milk"]
        real_resources["milk"] = real_resources["milk"] - product_milk

    price = MENU[product]["cost"]
    change = round(money - price, 2)
    real_resources["money"] += price
    print(f"Here is ${round(change, 2)} in change")
    print(f"Here is your {product} ☕ Enjoy!")
    return real_resources


def main(real_resources):
    choice = input('What would you like? (espresso/latte/cappuccino):')
    if choice == "off":
        return
    elif choice == "report":
        report(real_resources)
        main(real_resources)
    elif choice in MENU:

        # check resources sufficient?
        resources_checked = check_resources(product=choice, real_resources=real_resources)

        if resources_checked:
            # process coins
            money = process_coins()

            # check transaction successful?
            transaction_checked = check_transaction(product=choice, money=money)
            if transaction_checked:
                # make coffee
                real_resources = make_coffee(product=choice, real_resources=real_resources, money=money)

        main(real_resources)

    else:
        main(real_resources)


main(real_resources)
