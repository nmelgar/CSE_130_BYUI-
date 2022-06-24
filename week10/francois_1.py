
# n1 = 2
# n2 = 1
array1 = [2, 1]

for x in range(100 - 2):
    n1 = array1[x]
    n2 = array1[x + 1]
    
    new_number = n1 + n2
    array1.append(new_number)
    # new_number = array1[x - 1] + array1[x + 1]
    # array1[x - 1] = array1[x+1]
    # array1[x+1] = new_number
    # 
    # print(f"{x+1}. {new_number}")
    # print(x)
    x += 1

print(array1)
# print(f"New number: {new_number}. N1{n1}. N2 {n2}")


####FIRST VERSION####

# n1 = 2
# n2 = 1
# array1 = [2, 1]

# for x in range(100 - 2):
#     new_number = n1 + n2
#     n1 = n2
#     n2 = new_number

#     print(f"{x+1}. {new_number}")
#     x += 1


# print(f"New number: {new_number}. N1{n1}. N2 {n2}")
