import json

filename = 'Lab02.json'
with open(filename) as data_source:
    all_data = json.load(data_source)
    # json.dump(all_data, f, indent=4)

usernames = all_data['username']
passwords = all_data['password']

counter = 0
id = 0

user_input = input("Username: ")
password_input = input("Password: ")
inputs = str(user_input + password_input)

for (username, password) in zip(usernames, passwords):
    full_user = (str(counter) + username + password)
    full_user = usernames[counter] + passwords[counter]
    counter += 1

if user_input in usernames:
    print("Correct username")
    if password_input in passwords:
        print("Correct Password")
        if inputs == full_user:
            print("Authenticated")
        else:
            print("Error Auth")
    else:
        print("Wrong password")
        
else:
    print("Username doesnt exist")

# print(usernames[0])
# print(passwords[0])
