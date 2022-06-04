def swapPositions(list, pos1, pos2):

    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


array1 = [31, 72, 10, 32, 18, 95, 25, 50]

counter = 1
largest = 0
minus = -1
pivot = array1[minus]


for check in array1:
    if check > largest:
        largest = check
for number in array1:
    if largest > pivot:
        index1 = array1.index(largest)
        index2 = array1.index(pivot)
        minus = minus - 1
    swapPositions(array1, index1, index2)
    


print(array1)
print(largest)
