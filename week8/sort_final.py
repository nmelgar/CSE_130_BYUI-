import json


def main():
    print("The values in languages.json are:\n")
    sorted = sortFunction(languages)
    for sort_element in sorted:
        print(sort_element)


def swapPositions(list, pos1, pos2):
    """This function will swap the position of two elements in
    a list.
    Takes in 3 parameters:
    -list: array that contains the elements
    -pos1: position of the first elemement to be changed
    -pos2: positions of the second element to be changed
    Returns: the list with the elements in their new position.
    """
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


def sortFunction(list):
    """This function will go through a list of elements
    and will sort it by comparing the largest element in
    list with the last element, it will send the largest element
    to the end of the list and will repeat the process until
    the list is sorted from less to more.
    Takes in 1 parameter:
    -list: the list that will hold the elements
    """
    minus = -1

    # This will check that minus starts at -1, so it can decrease
    assert minus == -1, "minus variable should start at -1"

    for i in range(len(list)):


        i_largest = list[0]
        for i_check in list[0:len(list) - i]:
            i_pivot = list[minus]
            if i_check > i_largest:
                i_largest = i_check
        if i_largest > i_pivot:
            index1 = list.index(i_largest)
            swapPositions(list, index1, minus)
        minus -= 1
    return list


try:
    # get the json file
    # filename = 'languages.json'
    
    #empty list
    # filename = 'Lab08.empty.json'
    
    #list with one element
    # filename = 'Lab08.trivial.json'

    #small list
    # filename = 'Lab08.languages.json'
    
    #medium list
    # filename = 'Lab08.states.json'
    
    #large list
    filename = 'Lab08.cities.json'

    # open the file with the variable data_source
    with open(filename) as data_source:
        all_data = json.load(data_source)

     # use for the array
    languages = all_data['array']
    
    # this will check that the length of the list is > than 0
    assert len(languages) > 0, "List length should be greater than 0"

    # call the main function
    if __name__ == "__main__":
        main()

# if file is doesn't exist an error will show
except FileNotFoundError:
    print("Unable to open file languages.json.")
