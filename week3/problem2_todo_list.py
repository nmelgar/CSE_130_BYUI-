todo_list = []
menu = ["See list", "Add item", "Remove item", "Exit"]
run = True

print("Welcome to the to-do list")
print("--------------------------")

while run:
    print(" ")
    for index, menu_item in enumerate(menu):
        print(f"{index + 1}. {menu_item}")

    user_choice = int(input("What you want to do? "))

    if user_choice == 1:
        if not todo_list:
            print(" ")
            print("--------------------------")
            print("List is empty")
            print("Please add an element")

            print("--------------------------")
        else:
            print(" ")
            print("--------------------------")
            print("Tasks to complete:")
            for index, task in enumerate(todo_list):
                print(f"{index + 1}. {task}")

            print("--------------------------")

    elif user_choice == 2:
        (print(" "))
        add_item = input("Type the task you want to add: ")
        todo_list.append(add_item)
        print("Task added succesfully")

    elif user_choice == 3:
        print("")
        for index, task in enumerate(todo_list):
            print(f"{index + 1}. {task}")
        remove_item = int(input("Type the task you want to remove (number): "))
        todo_list.pop(remove_item - 1)
        print("\nTask removed succesfully!")

    elif user_choice == 4:
        print("\nThank you, please come back later!")
        run = False

    else:
        print("\nPlease choose a valid number and try again")
