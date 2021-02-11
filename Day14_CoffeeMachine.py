from art import logo
import time

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "water": 1000,
    "milk": 1000,
    "coffee": 1000,
    "money":0,
}


def print_report():
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${'{:.2f}'.format(resources['money'])}")


def print_menu():
    print("######MENU#######")
    print(f"Espresso: ${'{:.2f}'.format(MENU['espresso']['cost'])}\nLatte: ${'{:.2f}'.format(MENU['latte']['cost'])}\nCappuccino: ${'{:.2f}'.format(MENU['cappuccino']['cost'])}")
    print("#################\n")


def insert_coins(choice):
    print(f"The {choice} is ${'{:.2f}'.format(MENU[choice]['cost'])}. Please insert coins.")
    q = input("How many quarters?")
    d = input("How many dimes?")
    n = input("How many nickles?")
    p = input("How many pennies?")

    if q == '':
        q = 0

    if d == '':
        d = 0

    if n == '':
        n = 0

    if p == '':
        p = 0

    total = float((int(q) * .25) + (int(d) * .10) + (int(n) * .05) + (int(p) * .01))
    if total >= MENU[choice]['cost']:
        change = "{:.2f}".format(total - float(MENU[choice]['cost']))
        print(f"Your change is ${change}! Enjoy your {choice}!")
        return True
    else:
        print("You didn't insert enough coins. Refunding money")
        return False


def check_resources(choice):
    # if resources['milk'] >= MENU[choice]['ingredients']['milk'] \
    #     and resources['water'] >= MENU[choice]['ingredients']['water'] \
    #     and resources['coffee'] >= MENU[choice]['ingredients']['coffee']:
    if resources['milk'] >= MENU[choice]['ingredients']['milk']:
        if resources['water'] >= MENU[choice]['ingredients']['water']:
            if resources['coffee'] >= MENU[choice]['ingredients']['coffee']:
                return True
            else:
                print("Sorry, not enough Coffee")
                return False
        else:
            print("Sorry, not enough water")
            return False
    else:
        print("Sorry, not enough milk")
        return False


def adjust_resources(choice):
    resources['milk'] = resources['milk'] - MENU[choice]['ingredients']['milk']
    resources['coffee'] = resources['coffee'] - MENU[choice]['ingredients']['coffee']
    resources['water'] = resources['water'] - MENU[choice]['ingredients']['water']
    resources['money'] += MENU[choice]['cost']

quit = True
while(quit):
    print(logo)
    print_menu()
    choice = input("What would you like?").lower()

    if choice == "report":
        print_report()
        time.sleep(3)
        print('\n' * 40)
    elif choice == "off":
        print("Shutting Down Coffee Maker!")
        quit = False
    elif check_resources(choice):
        if insert_coins(choice):
            adjust_resources(choice)
            time.sleep(3)
            print('\n' * 40)
            quit = True
        else:
            time.sleep(3)
            print('\n' * 40)
            quit = True
    else:
        time.sleep(3)
        print('\n' * 40)
        uit = True
