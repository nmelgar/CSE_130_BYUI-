import json

# get the json file
filename = 'Lab02.json'
with open(filename) as data_source:
    all_data = json.load(data_source)
    # json.dump(all_data, f, indent=4)

# create the lists
usernames = all_data['username']
passwords = all_data['password']

user_input = "King Arthur"
password_input = "None shall pass"
counter = 0

print(type(usernames))

# for (index, information) in enumerate(zip(usernames, passwords)):
#     password_index = passwords[index]
#     user_index = usernames[index]
#     print(password_index)

# if user_input in usernames:
#     print("Correct username")
#     if password_input in passwords:
#         print("Correct password")
        
#     else:
#         print("Wrong password")
# else:
#     print("Wrong username")


