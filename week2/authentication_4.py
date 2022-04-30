# 1. Name:
#      Nefi Melgar
# 2. Assignment Name:
#      Lab 02: Authentication
# 3. Assignment Description:
#      A JSON file with users information has to be opened.
#      It receives 2 inputs (username, password).
#      It will check if both username and password are in the JSON file
#      It will assign the index of the input that matches with the index in the file
#      It will check if both inputs have the same index
#      If both inputs have the same index, the user will be authenticated.
#      Auth will fail If any of the inputs is wrong or indexes don't match
# 4. What was the hardest part? Be as specific as possible.
#      It was a hard assignment to me. My logic wasn't enough to understand how to get
#      both lists to match. I tried many different ways, tried different printing lists
#      techniques, but any of them were enough to get it. I wasn't able to match both
#      index. I researched and learned about lists again. I was able to learn about
#      the index() method which returns the index that matches with a specific value.
#      with this method is was easier to get a relationship between both elements in the lists.
# 5. How long did it take for you to complete the assignment?
#      It took me around 8 hours to complete the assignment.

import json

try:
    # get the json file
    filename = 'Lab02.json'

    # open the file with the variable data_source
    with open(filename) as data_source:
        all_data = json.load(data_source)

    # create the lists
    usernames = all_data['username']
    passwords = all_data['password']

    # receive inputs from the user both, username and password
    user_input = input("Username: ")
    password_input = input("Password: ")

    # this variables will hold the index that will match users' input
    user_index = ""
    password_index = ""

    # verify if user's input is in usernames' list
    if user_input in usernames:
        # assign the index that matches user input
        user_index = usernames.index(user_input)

        # verify if user's input is in passwords' list
        if password_input in passwords:
            # assign the index that matches user input
            password_index = passwords.index(password_input)

            # verify that both inputs have the same index
            if user_index == password_index:
                print("You are authenticated!")
            else:
                print("You are not authorized to use the system")
        else:
            print("You are not authorized to use the system")
    else:
        print("You are not authorized to use the system")

# if file is doesn't exist an error will show
except FileNotFoundError:
    print("Unable to open file Lab02.json.")
