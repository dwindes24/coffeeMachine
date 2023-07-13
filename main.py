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
            "milk": 100,
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
    "coffee": 100
}

import os



def printResources():
    for resource in resources:
        print(f"{resource}: {resources[resource]}")
    print(f"Money: ${money}")


def checkResources(drink):
    if drink == "espresso":
        if resources['water'] >= MENU['espresso']['ingredients']['water']:
            if resources['coffee'] >= MENU['espresso']['ingredients']['coffee']:
                return True
            else:
                print("Sorry not enough coffee.")
                return False
        else:
            print("Sorry not enough water.")
            return False
    elif drink == "latte":
        if resources['water'] >= MENU['latte']['ingredients']['water']:
            if resources['coffee'] >= MENU['latte']['ingredients']['coffee']:
                if resources['milk'] >= MENU['latte']['ingredients']['milk']:
                    return True
                else:
                    print("Sorry not enough milk")
                    return False
            else:
                print("Sorry not enough coffee.")
                return False
        else:
            print("Sorry not enough water.")
            return False
    else:
        if resources['water'] >= MENU['cappuccino']['ingredients']['water']:
            if resources['coffee'] >= MENU['cappuccino']['ingredients']['coffee']:
                if resources['milk'] >= MENU['cappuccino']['ingredients']['milk']:
                    return True
                else:
                    print("Sorry not enough milk")
                    return False
            else:
                print("Sorry not enough coffee.")
                return False
        else:
            print("Sorry not enough water.")
            return False


def gatherMoney(drink):
    print("Please insert coins")
    q = int(input("How many quarters?"))
    d = int(input("How many dimes?"))
    n = int(input("How many nickles?"))
    p = int(input("How many pennies?"))
    moneyIn = q * .25 + d * .1 + n * .05 + p * .01
    if MENU[drink]['cost'] > moneyIn:
        print("Sorry thats not enough money. Money refunded.")
        return False
    else:
        print(f"Here is ${round(moneyIn - MENU[drink]['cost'], 2)} in change")
        print(f"Here is your {drink}, enjoy!")
        return True


def updateInv(drink):
    for resource in MENU[drink]['ingredients']:
        resources[resource] -= MENU[drink]['ingredients'][resource]


money = 0
coffeLoop = True

while coffeLoop:
    inStock = False
    paid = False

    drink = input("What would you like? (espresso/latte/cappucino):").lower()
    if drink == 'report':
        printResources()
    elif drink in ["espresso", "latte", "cappucino"]:
        inStock = checkResources(drink)
    else:
        print("Invalid input. Please Try again")
        os.system('clear')
        continue
    if inStock:
        paid = gatherMoney(drink)
        if paid:
            updateInv(drink)
            money += MENU[drink]['cost']

printResources()
