MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
        },
        "cost": 15,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 25,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 30,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0
use = True
def exchange(coins,ch):
    if coins < MENU[ch]["cost"]:
        print("Insufficient money")
    else:
        count = 0
        for i in resources:
            if resources[i]> MENU[ch]["ingredients"][i]:
                count +=1
        if count == 3:
            for i in resources:
                resources[i] -= MENU[ch]["ingredients"][i]
                change = coins - MENU[ch]["cost"]
                global money
                money += MENU[ch]["cost"]
                print(f"Here's your change: {change}")
                print(f"Enjoy your {ch}")
        else:
            print(f"Sorry there isn't enough resources to make {ch} :(")
while use == True:
    ch = input("What would you like? (espresso/latte/cappuccino), 'report' for info OR 'off' to close")
    if ch == "report":
        for i in resources:
            print(i, resources[i])
        print("Money ", money)
    elif ch == "espresso" or ch == "latte" or ch == "cappuccino":
        coins = int(input("Please insert coins"))
        exchange(coins, ch)
    else:
        use = False
