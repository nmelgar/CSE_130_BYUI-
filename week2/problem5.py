# primer numbers

number = int(input("Please enter the number: "))


if (number % 2 == 0) and (number != 2):
    print("Not prime")
elif (number % 2 != 0) and (number / number == 1) and (number / 1 == number):
    print("Prime")
