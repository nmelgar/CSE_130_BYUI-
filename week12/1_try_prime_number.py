range_1 = range(1, 101)
numbers = list(range_1)

# print(numbers)

for number in numbers:
    num_string = repr(number)
    last_digit_str = num_string[-1]
    last_digit = int(last_digit_str)

    range_2 = range(1, 10, 2)
    range_2 = list(range_2)

    for x in range_2:
        if last_digit == x:
            print(num_string)
