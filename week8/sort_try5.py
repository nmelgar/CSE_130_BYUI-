def swapPositions(list, pos1, pos2):

    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


array1 = [31, 72, 10, 32, 18, 95, 25, 50]

minus = -1
for a in range(len(array1)):
    i_largest = 0

    for i_check in array1[0:len(array1) - a:-1]:
        i_pivot = array1[minus]
        if i_check > i_largest:
            i_largest = i_check
            if i_largest > i_pivot:
                index1 = array1.index(i_largest)
                index2 = array1.index(i_pivot)
                swapPositions(array1, index1, index2)
                # minus = minus - 1
    print(array1)
# print(array1)
