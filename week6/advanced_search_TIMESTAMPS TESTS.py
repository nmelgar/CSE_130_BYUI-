import json


def binarySearch(input_array, left_side, right_side, word_search):
    """Function to perform a binary search, the purpose is to
    check if the searched element is greater or lower than
    the middle element in the array, then it will divide in subarrays
    until finding if the element is in the array. """
    if right_side >= left_side:
        mid = left_side + (right_side - left_side) // 2

        # in the middle
        if input_array[mid] == word_search:
            return mid

        # to be at left side
        elif input_array[mid] > word_search:
            return binarySearch(input_array, left_side, mid-1, word_search)

        # to be at the right side
        else:
            return binarySearch(input_array, mid + 1, right_side, word_search)

    else:
        # not found in the array
        return -1


# get the json file
filename = 'languages.json'

# get file name from user
user_file_input = input("What is the name of the file? ")

if filename == user_file_input:
    # get word to search from user
    word_search = input("What name are we looking for? ")

    # open the json file
    with open(filename) as data_source:
        all_data = json.load(data_source)

    # use for the array
    languages = all_data['array']

    search_result = binarySearch(languages, len(
        languages[:1]), len(languages)-1, word_search)
    if search_result != -1:
        print(f"\nWe found {word_search} at index {search_result}.")
    else:
        print("\nSearch word was not found.")

else:
    print("\nSorry, the file was not found. :)")
