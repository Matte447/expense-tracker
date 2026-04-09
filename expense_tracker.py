import json
import datetime

print("           Welcome to the expense Tracker!")
print("-----------------------------------------------------")


def get_balance():
    with open("tracker.json", "r") as f:
        json_file = json.loads(f.read())

    balance = json_file["balance"]
    return balance


def update_json(location, value, title):
    with open("tracker.json", "r") as f:
        json_file = json.loads(f.read())

    json_entry = {
        "description": title,
        "amount": value,
        "timestamp": str(datetime.datetime.now()),
    }

    json_file[location].append(json_entry)
    if location == "incomes":
        json_file["balance"] += value
    elif location == "expenses":
        json_file["balance"] -= value

    with open("tracker.json", "w") as f:
        f.write(json.dumps(json_file, indent=4))


# Add income to the balance
def income(balance):
    print("             Add income to your balance")
    print("-----------------------------------------------------")
    print("")
    print("How much money do you want to add?")
    try:
        gained_money = int(input("> "))
    except ValueError:
        print("Please input a number")
        return balance
    print("Please enter a description for your income.")
    income_title = input("> ")

    update_json("incomes", gained_money, income_title)
    balance += gained_money
    return balance


def expense(balance):
    print("                  Track your expense")
    print("-----------------------------------------------------")
    print("")
    print("How much did you spent?")
    try:
        money_expense = int(input("> "))
    except ValueError:
        print("Please input a number")
        return balance

    print("Please enter a description for your expense.")
    expense_title = input("> ")
    update_json("expenses", money_expense, expense_title)
    balance -= money_expense
    return balance


def generate_overview():
    with open("tracker.json", "r") as f:
        json_file = json.loads(f.read())
    print(json_file)


while True:
    balance = get_balance()
    print(f"Your current balance is {balance}€")
    print("What do you want to do?")
    print("1. Add income to your balance")
    print("2. Track your expense")
    print("3. Generate an Overview of your financial situation")
    print("4. Quit")
    print("-----------------------------------------------------")
    option = input("> ")

    try:
        option = int(option)
    except ValueError:
        print("Please input a number between 1 and 4")

    if option == 1:
        balance = income(balance)
    elif option == 2:
        balance = expense(balance)
    elif option == 3:
        generate_overview()
    elif option == 4:
        print("Ok, Goodbye!")
        break
