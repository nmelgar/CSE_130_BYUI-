import json

filename = 'Lab02.json'
with open(filename) as data_source:
    all_data = json.load(data_source)
    # json.dump(all_data, f, indent=4)

usernames = all_data['username']
passwords = all_data['password']

user_input = input("Username: ")
password_input = input("Password: ")
inputs = str(user_input + password_input)

counter = 0
counter_psw = 0

for username in usernames:
    id = counter
    username = f"{id}. {usernames[counter]}"
    # print(username)
    counter += 1

for password in passwords:
    id_psw = counter_psw
    password = f"{id_psw}. {passwords[counter_psw]}"
    # print(password)
    counter_psw += 1

user_info = username + password
print(user_info)
# if user_input in usernames:
#     if password_input in passwords:
#         if inputs == 

print(usernames[7])
print(passwords[7])
