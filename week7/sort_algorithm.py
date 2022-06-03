numbers = [31, 72, 10, 32, 18, 95, 25, 50]
i_pivot = numbers[-1]
i_check = numbers[0]
i_largest = 0

# if i_check > i_largest

# i is for the values in the array
# for i in numbers:
# j is for the indexes
# for j in range(len(numbers)):
#     print(i, j)

# for i, j in enumerate(numbers):
#     if i <= len(numbers):
#         # if numbers[i] > numbers[i + 1]:
#         #     numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
#         print(i)
#         i += 1
# print(numbers)

# for i in range(len(numbers)):
#     for j in range(len(numbers)):


def swapNumbers(array, ind1, ind2):

    array[ind1], array[ind2] = array[ind2], array[ind1]
    return array


index1 = 0
index2 = 0
largest = 0
counter = 1
for check in numbers:
    if counter < len(numbers):
        next_number = numbers[counter]
        if check > next_number:
            largest = check
            index1 = numbers.index(largest)
            index2 = numbers.index(i_pivot)
        swapNumbers(numbers, index1, index2)
        counter = counter + 1

print(numbers)
