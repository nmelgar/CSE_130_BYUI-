import random

print('This is the "guess a number" game.')
print("You try to guess a random number in the smallest number of attempts.")
print("\nGuess a number between 1 and 20.")
value_random = random.randint(1, 20)
print("Pick a positive integer: ")

guessed = False
number_of_guesses = 0
tried_numbers = []

while guessed == False:
    
    user_guess = int(input("> "))
    number_of_guesses += 1
    tried_numbers.append(user_guess)
    if user_guess == value_random:
        guessed = True

    elif user_guess < value_random:
        print("\tToo low!")

    elif user_guess > value_random:
        print("\tToo high!")

print(f"You were able to find the number in {number_of_guesses} guesses.")
print(f"The numbers you guessed were: {tried_numbers}")