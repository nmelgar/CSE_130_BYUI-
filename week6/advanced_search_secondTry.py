# 1. Name:
#      Nefi Melgar
# 2. Assignment Name:
#      Lab 06: Advanced Search
# 3. Assignment Description:
#      Create a program that find an element in a collection by using a search method
#      where the algorithm will divide the array in subarrays depending on the side that
#      the element can be found.
# 4. Algorithmic Efficiency
#      Since we are trying to determine the scenarios to determine what will be
#      the best and the worst, the efficiency is O(log n). Since it works with a
#      a sorted collection, it allow us to easily compare searched values vs the elements
#      in the array. So, the space would be the same for any number of elements.
#      It will work even better for larger amount of inputs, which is a great advantage.
# 5. What was the hardest part? Be as specific as possible. At it
#      The hardest part was to convert the pseudocode to code. I tried to made it as the
#      pseudocode from last week, but many things needed to be changed since
#      the pseudocode didnt provide the expected results. The idea is the same
#      but the way the code was written have variations so that it can work
#      in the practice and not just in the concept.
# 6. How long did it take for you to complete the assignment?
#      It took me around 7 hours. I spent many hours reading to better understand the topic
#      but I don't feel really proficient on it.
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
# filename = 'languages.json'

# get file name from user
user_file_input = input("What is the name of the file? ")

try:
    if user_file_input:
        # get word to search from user
        word_search = input("What name are we looking for? ")

        # open the json file
        with open(user_file_input) as data_source:
            all_data = json.load(data_source)

        # use for the array
        languages = all_data['array']

        search_result = binarySearch(languages, len(
            languages[:1]), len(languages)-1, word_search)
        if search_result != -1:
            print(f"\nWe found {word_search} at index {search_result}.")
        else:
            print("\nSearch word was not found.")

except FileNotFoundError:
    print("\nSorry, the file was not found. :)")
