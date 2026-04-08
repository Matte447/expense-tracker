print("           Welcome to the expense Tracker!")
print("-----------------------------------------------------")
balance = 0


# Add income to the balance
def income(balance):
    print("              Add income to your balance")
    print("-----------------------------------------------------")
    print("")
    print("How much money do you want to add?")
    gained_money = int(input("> "))
    balance += gained_money
    return balance


while True:
    print(f"Your current balance is {balance}")
    print("What do you want to do?")
    print("1. Track your income")
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
        pass
    elif option == 3:
        pass
    elif option == 4:
        print("Ok, Goodbye!")
        break
