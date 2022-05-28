import json

# def binary_search(item_list,item):
# 	first_element = len(item_list[:1])
# 	last_element = len(item_list)-1
# 	found = False
# 	while( first_element<=last_element and not found):
# 		mid_element = (first_element + last_element)//2
# 		if item_list[mid_element] == item :
# 			found = True
# 		else:
# 			if item < item_list[mid_element]:
# 				last_element = mid_element - 1
# 			else:
# 				first_element = mid_element + 1
# 	return found


user_file_input = input("what is the name of the file? ")
user_lang_input = input("What name are we looking for? ")

# get the json file
filename = 'languages.json'


if filename == user_file_input:
    # open the file with the variable data_source
    with open(filename) as data_source:
        all_data = json.load(data_source)

    # create the lists
    languages = all_data['array']
    # i = 0
    # try printing the languages
    # for index, value in enumerate(languages):
    #     print(f"-{index}. {value}")
    first_element = len(languages[:1])
    last_element = len(languages)-1
    found = False
    while(first_element <= last_element and not found):
        mid_element = (first_element + last_element)//2
        if languages[mid_element] == user_lang_input:
            found = True
            print("FOund")
        else:
            if user_lang_input < languages[mid_element]:
                last_element = mid_element - 1
                print("FOund1")
            else:
                first_element = mid_element + 1
                print("FOund2")

else:
    print("Sorry, the file was not found. :)")
