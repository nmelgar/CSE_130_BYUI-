import json

# get the json file
filename = 'Lab02.json'
with open(filename) as data_source:
    all_data = json.load(data_source)
    # json.dump(all_data, f, indent=4)

# create the lists
usernames = all_data['username']
passwords = all_data['password']

# receive inputs from the user both, username and password
user_input = input("Username: ")
password_input = input("Password: ")

user_index = ""
password_index = ""

if user_input in usernames:
    print("Correct username")
    user_index = usernames.index(user_input)
    if password_input in passwords:
        password_index = passwords.index(password_input)
        if user_index == password_index:
            print("You are authenticated!")
        else:
            print("You are not authorized to use the system")
    else:
        print("You are not authorized to use the system")
else:
    print("You are not authorized to use the system")
