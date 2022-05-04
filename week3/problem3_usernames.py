users = {
    "peter23": "holamundo123",
    "john131": "h663",
    "mark345": "hola",
    "luke67": "mundo",
    "hanna256": "world",
    "mary99": "777",
}


def new_user_info():
    new_user = input("Enter a new username: ")
    new_password = input("Enter a new password: ")
    users[new_user] = new_password


user_has_user = input("Do you have an username? (Y/N) ")

if user_has_user.upper() == "Y":
    user_name = input("Please enter your username: ")
    user_password = input("Please enter your password: ")
    full_info_input = user_name + user_password
    for user, password in users.items():
        full_info = user + password
        if full_info == full_info_input:
            print("You are authenticated")


if user_has_user.upper() == "N":
    new_user_info()
