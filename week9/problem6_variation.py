def main():
    print(f"Your input was: {numbers}")
    print(numEvenOdd(numbers))


def numEvenOdd(numbers):
    counterEven = 0
    counterOdd = 0
    for number in range(1, numbers + 1):
        if number % 2 == 0:
            counterEven += 1
        elif number % 2 != 0:
            counterOdd += 1
    return f"\nThere are {counterEven} even numbers.\nThere are {counterOdd} odd numbers."


# greeting, then ask the user for the input
print("--------Welcome to the odd/even calculator--------")
numbers = int(input("\nPlease input a number to calculate odds and evens: "))

# call the main function
if __name__ == "__main__":
    main()
