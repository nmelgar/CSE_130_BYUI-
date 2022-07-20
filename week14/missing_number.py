def main():
    array_1 = [1, 3, 2, 9, 8, 7, 4, 10, 5]

    # the sum of the numbers as if any number where missing
    sum_numbers = 0
    for number in range(1, len(array_1) + 2):
        sum_numbers += number
    partial_result = sub_total(array_1)

    # subtract the the partial_result(sum) to the expected sum_numbers
    missing_number = sum_numbers - partial_result
    print(f"The missing number is {missing_number}")


def sub_total(array_1):
    pre_result = 0
    for number in array_1:
        pre_result += number
    # returns the sum of the actual numbers in the array
    return pre_result


if __name__ == "__main__":
    main()
