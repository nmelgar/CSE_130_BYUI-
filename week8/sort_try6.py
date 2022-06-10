def swapPositions(list, pos1, pos2):

    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


# array1 = [31, 72, 10, 32, 18, 95, 25, 50]
array1 = [19, 13, 29, 76, 19, 77, 99, 12, 5, 25, 19]
# array1 = ["a", "c", "f", "h", "d", "t", "n", "d"]

minus = -1
# i_pivot = array1[minus]
for i in range(len(array1)):
    i_largest = array1[0]
    for i_check in array1[0:len(array1) - i]:
        i_pivot = array1[minus]
        if i_check > i_largest:
            i_largest = i_check
    if i_largest > i_pivot:
        index1 = array1.index(i_largest)
        swapPositions(array1, index1, minus)
        print(array1)
    minus -= 1


# works with both numbers an letters
# for i_check in array1:
#     i_pivot = array1[minus]
#     i_largest = i_check
#     for i_check in array1:
#         if i_check > i_largest:
#             i_largest = i_check
#             if i_largest > i_pivot:
#                 index1 = array1.index(i_largest)
#                 index2 = minus
#                 swapPositions(array1, index1, index2)
#             i_pivot = array1[minus]
#             print(array1)
#     minus = minus + 1
# print(array1)


# functions with both but not with repeated items
# for i_check in array1:
#     i_pivot = array1[minus]
#     i_largest = i_check
#     for i_check in array1:
#         if i_check > i_largest:
#             i_largest = i_check
#             if i_largest > i_pivot:
#                 index1 = array1.index(i_largest)
#                 index2 = array1.index(i_pivot)
#                 swapPositions(array1, index1, index2)
#             i_pivot = array1[minus]
#             print(array1)
#     minus = minus + 1
# print(array1)


# functions with numbers but not with repeated items
# for i_check in range(len(array1)):
#     i_pivot = array1[minus]
#     i_largest = 0
#     for i_check in array1:
#         if i_check > i_largest:
#             i_largest = i_check
#             if i_largest > i_pivot:
#                 index1 = array1.index(i_largest)
#                 index2 = array1.index(i_pivot)
#                 swapPositions(array1, index1, index2)
#             i_pivot = array1[minus]
#             print(array1)
#     minus = minus + 1
