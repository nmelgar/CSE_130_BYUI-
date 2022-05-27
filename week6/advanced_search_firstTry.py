import json

user_file_input = input("what is the name of the file? ")
# user_name_input = input("What name are we looking for? ")

# get the json file
filename = 'languages.json'


if filename == user_file_input:
    # open the file with the variable data_source
    with open(filename) as data_source:
        all_data = json.load(data_source)

    # create the lists
    languages = all_data['array']

    # try printing the languages
    for language in languages:
        print("- " + language)

    # print("here is the file" + filename)
else:
    print("Sorry, the file was not found. :)")
