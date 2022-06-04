def swapNumbers(array, ind1, ind2):

    array[ind1], array[ind2] = array[ind2], array[ind1]
    return array


array1 = [31, 72, 10, 32, 18, 95, 25, 50]
minus = -1
counter = 1
pivot = array1[minus]
largest = 0

for check in array1:
    if counter < len(array1):
        right_number = array1[counter]
        print(f"{check} vs {right_number}")
        # counter += 1
        if check > right_number:
            largest = check
        #     index1 = array1.index(largest)
        #     index2 = array1.index(pivot)
        #     swapNumbers(array1, index1, index2)
        #     minus -= -1
        # elif check < right_number:
        #     pass

        counter += 1

print(array1)
print(largest)
print(pivot)

#               index1 = array1.index(largest)
#             index2 = array1.index(pivot)
#             swapNumbers(array1, index1, index2)
#             minus -= -1
