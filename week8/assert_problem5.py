array1 = [1]
search = 2

def binary_search(array, search):
    i_first = 0
    #Assert to evaluate that the array length is greater than 0
    assert len(array) > 0, "Array cannot be empty."
    i_last = len(array) - 1
    while i_first <= i_last:
            i_middle = (i_first + i_last) // 2

            # Found!
            if array[i_middle] == search:
                return True

            # Too high or too low
            elif array[i_middle] < search:
                i_first = i_middle + 1
            else:
                i_last = i_middle - 1

    return False

binary_search(array1, 2)