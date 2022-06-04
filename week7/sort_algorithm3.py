def swapNumbers(array, ind1, ind2):

    array[ind1], array[ind2] = array[ind2], array[ind1]
    return array


array1 = [31, 72, 10, 32, 18, 95, 25, 50]

index1 = 0
index2 = 0
counter = 1
minus = -1
largest = 0


for check in array1:
    pivot = array1[-1]
    # largest = check
    for number in array1:
        if largest < number:
            largest = number
            if largest > pivot:
                index1 = array1.index(largest)
                index2 = array1.index(pivot)
        # minus = minus - 1         
            #     print(array1)
            
        swapNumbers(array1, index1, index2)

print(minus)    
print(array1)
print(largest)


# for check in array1:
#     print("first loop----starts")
#     print(check)
#     print("first loop----ends")
#     for numbers in array1:
#         print("second loop-----starts")
#         print(numbers)
#         print("second loop----ends")
