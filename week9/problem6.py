import json

def main():
    print(numEvenOdd(numbers))


def numEvenOdd(numbers):
    counterEven = 0
    counterOdd = 0
    for number in numbers:
        if number % 2 == 0:
            counterEven += 1
        elif number % 2 != 0:
            counterOdd += 1
    return f"There are {counterEven} even numbers.\nThere are {counterOdd} odd numbers."


try:
    # get the file
    filename = 'numbers.json'

    # open the file with the variable data_source
    with open(filename) as data_source:
        all_numbers = json.load(data_source)

    # use for the array 'numbers' in the json file
    numbers = all_numbers['numbers']

    # call the main function
    if __name__ == "__main__":
        main()

# if file is doesn't exist an error will show
except FileNotFoundError:
    print(f"Unable to open {filename}.")
