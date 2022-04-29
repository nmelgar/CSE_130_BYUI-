import json

filename = 'Lab02.json'
with open(filename) as data_source:
    all_data = json.load(data_source)
    # json.dump(all_data, f, indent=4)

usernames = all_data['username']
passwords = all_data['password']

counter = 0
id = 0

for (username, password) in zip(usernames, passwords):
    # full_user = (str(counter) + username + password)
    full_user = usernames[counter] + passwords[counter]
    counter += 1
    print(full_user)

user_input = input("Username: ")
password_input = input("Password: ")
inputs = str(user_input + password_input)

if inputs == full_user:
    print("Authenticated")
else:
    print("Error authenticating")

# print(usernames[0])
# print(passwords[0])
