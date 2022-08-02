MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def ingredient_check(item):
    if resources["water"] >= MENU[f"{item}"]["ingredients"]["water"]:
        if resources["milk"] >= MENU[f"{item}"]["ingredients"]["milk"]:
            if resources["coffee"] >= MENU[f"{item}"]["ingredients"]["coffee"]:
                return True
    else:
        return False


def prepare_item(item):
    resources["water"] = resources["water"] - MENU[f"{item}"]["ingredients"]["water"]
    resources["milk"] = resources["milk"] - MENU[f"{item}"]["ingredients"]["milk"]
    resources["coffee"] = resources["coffee"] - MENU[f"{item}"]["ingredients"]["coffee"]
    return f"There you go with your {item} ☕, Have a nice day!!"


def return_change(item):
    quarters = int(input("Enter number of quarters : "))
    dime = int(input("Enter number of dimes : "))
    nickels = int(input("Enter number of nickels : "))
    penny = int(input("Enter number of penny : "))
    money = (0.25 * quarters) + (0.1 * dime) + (0.05 * nickels) + (0.01 * penny)
    if money >= MENU[f"{item}"]["cost"]:
        global profit
        profit += MENU[f"{item}"]["cost"]
        change = money - MENU[f"{item}"]["cost"]
        return f"Here is your change ${change}"
    else:
        return "Sorry this amount is not sufficient"


def refill_coffee_machine():
    resources["water"] = 300
    resources["milk"] = 200
    resources["coffee"] = 100


while True:
    choice = input("Which type of coffee do you want, espresso/latte/cappuccino : ").lower()
    if choice == "report":
        print(resources)
    else:
        if choice == "refill":
            refill_coffee_machine()
        else:
            if ingredient_check(choice):
                print(return_change(choice))
                print(prepare_item(choice))
            else:
                print("Sorry not enough ingredients")
