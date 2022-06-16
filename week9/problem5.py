transactions = [123.7, 345.9, 33.4, 89.2, 112.6, 22255.6]
menu = ["See Transactions and total", "Remove Transaction", "Exit"]
run = True

print("-------------------------------")
print("Welcome to your transactions account")
print("-------------------------------")

while run:
    print(" ")
    print("-----Menu-----")
    for index, menu_item in enumerate(menu):
        print(f"{index + 1}. {menu_item}")
    print("--------------")

    user_choice = int(input("\nWhat you want to do? "))

    if user_choice == 1:
        total = 0
        print("\nYour current transactions are: ")
        print(" ")
        for index, transaction in enumerate(transactions):
            print(f"{index + 1}. {transaction}")
            total += transaction

        print("---------------")
        print(f"The total is: ${total: .2f}")

    elif user_choice == 2:
        print(" ")
        for index, transaction in enumerate(transactions):
            print(f"{index + 1}. {transaction}")

        remove_transaction = int(
            input("\nWhat is the transaction you want to delete? "))
        print(" ")
        transactions.pop(remove_transaction - 1)
        print("\nTransaction removed succesfully!")

    elif user_choice == 3:
        print("Thank you, please come back later!")
        run = False

    else:
        print("Please enter a valid number")
