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

profit = 0.0

def report():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: ${profit}")

def resources_availability(choice):
    for item in choice:
        if choice[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return 0
    return 1

def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def pay(total, cost):
    global profit
    remaining = round(total - cost, 2)
    if remaining < 0:
        print("Sorry that's not enough money. Money refunded.")
        return 0
    elif remaining > 0:
        print(f"Here is ${remaining} in change.")
    profit += cost
    return 1

def make_coffee(choice, coffee_name):
    for item in choice:
        resources[item] -= choice[item]
    print(f"Here is your {coffee_name} ☕️. Enjoy!")

def make_order(choice):
    coffee_name = choice
    cost = MENU[choice]["cost"]
    choice = MENU[choice]['ingredients']
    
    available = resources_availability(choice)
    if available:
        total = process_coins()
        is_paid = pay(total, cost)
        if is_paid:
            make_coffee(choice, coffee_name)


def coffee_machine():
    is_on = 'on'
    while is_on == 'on':
        choice = input("​What would you like? (espresso/latte/cappuccino): ")
        if choice == 'report':
            report()
        elif choice == 'off':
            break
        elif choice in MENU:
            make_order(choice)
        else:
            print("Wrong input!")

coffee_machine()
