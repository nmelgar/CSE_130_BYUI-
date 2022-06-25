array1 = [2, 1]
assert len(array1) > 0, "Array cannot be empty"

user_integer = int(input("Which Francois number would you like to see? "))
assert user_integer > 0, "Integer must be greater than 0"

if user_integer == 1:
    print(f"Francois number {user_integer} is {array1[0]}")
elif user_integer == 2:
    print(f"Francois number {user_integer} is {array1[1]}")
else:
    for x in range(user_integer):
        n1 = array1[x]
        n2 = array1[x + 1]

        new_number = n1 + n2
        array1.append(new_number)

        x += 1
    print(f"\nFrancois number {user_integer} is {array1[x-1]}")


# array1 = [2, 1]

# user_integer = int(input("Which Francois number would you like to see? "))
# assert user_integer > 0, "Integer must be greater than 0"

# if user_integer == 1:
#     print(f"Francois number {user_integer} is {array1[0]}")
# elif user_integer == 2:
#     print(f"Francois number {user_integer} is {array1[1]}")
# else:
#     for x in range(user_integer):
#         n1 = array1[x]
#         n2 = array1[x + 1]

#         new_number = n1 + n2
#         array1.append(new_number)
#         # print(f"{x+1}. {array1[x]}")
#         x += 1
#     print(f"\nFrancois number {user_integer} is {array1[x-1]}")


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
