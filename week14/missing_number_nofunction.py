
array_1 = [1, 3, 2, 5]

# the sum of the numbers as if any number where missing
sum_numbers = 0
for number_1 in range(1, len(array_1) + 2):
    sum_numbers += number_1

pre_result = 0
for number_2 in array_1:
    pre_result += number_2

# subtract the the partial_result(sum) to the expected sum_numbers
missing_number = sum_numbers - pre_result
print(f"The missing number is {missing_number}")
