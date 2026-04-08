print("           Welcome to the expense Tracker!")
print("-----------------------------------------------------")

while True:
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
        pass
    elif option == 2:
        pass
    elif option == 3:
        pass
    elif option == 4:
        print("Ok, Goodbye!")
        break
