

list_1 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

counter = 2
even_number = 0

for x in list_1:
    while even_number <= len(list_1):
        even_number = x * counter
        counter += 1
        print(even_number)

# x = 0
# while x < len(list_1):
#     print(list_1[x])
#     x += 1

