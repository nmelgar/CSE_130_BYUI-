# 1. Name:
#    Nefi Melgar
# 2. Assignment Name:
#    Lab 01: Python Review
# 3. Assignment Description:
#    Create a number guessing game. There will be a random number and the user
#    have to guess it, it will stop when the user guess.
#  4. What was the hardest part? Be as specific as possible.
#    One of the hardests parts was to simplify the code and create it as the comment said.
#    I wrote so many lines at the beginning. I had to start by creating a
#    different file to avoid the comments from the template because they
#    were confusing me. I started writing the code and the first it was completed
#    there were like 60 lines of code. Then I tried by copying and pasting the lines
#    at the template, but I created the program in a different order so I had to
#    change the order of many lines and simplify it as much as possible.
#    From around 32 lines (without blanks and comments, it was reduced to 21)
#    It was great to make it more straightforward and avoiding unnecessary repetitions.
# 5. How long did it take for you to complete the assignment?
#    It took me around 2 hours and 35 minutes

import random

# Game introduction
print('This is the "guess a number" game.')
print("You try to guess a random number in the smallest number of attempts.")
# Prompt the user for how difficult the game will be. Ask for an integer
print("\nGuess a number between 1 and 20.")
# Generate a random number between 1 and the chosen value
value_random = random.randint(1, 20)
# Give the user instructions as to what he or she will be doing
print("Pick a positive integer: ")
# Initialize the sentinal and the array of guesses
guessed = False
number_of_guesses = 0
tried_numbers = []

# Play the guessing game
while guessed == False:
    # Prompt the user for a number
    user_guess = int(input("> "))
    # Store the number in an array so it can be displayed later
    number_of_guesses += 1
    tried_numbers.append(user_guess)
    # Make a decision: was the guess too high, too low, or just right
    if user_guess == value_random:
        guessed = True

    elif user_guess < value_random:
        print("\tToo low!")

    elif user_guess > value_random:
        print("\tToo high!")

# Give the user a report: How many guesses and what the guesses where
print(f"You were able to find the number in {number_of_guesses} guesses.")
print(f"The numbers you guessed were: {tried_numbers}")