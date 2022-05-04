users = {
    "peter23": "holamundo123",
    "john131": "h663",
    "mark345": "hola",
    "luke67": "mundo",
    "hanna256": "world",
    "mary99": "777",
}

run = True


def new_user_info():
    """Create a new user and password and added to the dictionary"""
    print("\nLet's create a new username")
    new_user = input("Enter a new username: ")
    new_password = input("Enter a new password: ")
    users[new_user] = new_password
    print("User created succesfully!")


while run:
    user_has_user = input("\nDo you have an username? (Y/N) ")

    if user_has_user.upper() == "Y":
        user_name = input("Please enter your username: ")
        user_password = input("Please enter your password: ")

        if user_name in users.keys():
            if user_password == users.get(user_name):
                print("You are authorized to use the system!")
                run = False
            else:
                print("Wrong password")
        elif user_name not in users.keys():
            print(f"The user {user_name} doesn't exist.")

    elif user_has_user.upper() == "N":
        new_user_info()
