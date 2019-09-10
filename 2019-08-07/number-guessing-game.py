'''
Task: "Number guessing game"
Difficulty: Intermediate
Description: Write a guessing game where the user has to guess a secret number. After every guess the program tells the user
whether their number was too large or too small. The program should end when the user guesses the correct number or
types "quit" as their guess.
Bonus: Count the number of tries the user has, and tell them at the end
'''
import random

# Generate a (secret) random number between our range
rangemin = 1
rangemax = 10
target = random.randrange(rangemin, rangemax)

# Number of attempts
attempts = 0

print(f"I'm thinking of a number between {rangemin} and {rangemax}")

while True:
    guess = input("What's your guess? (type \"quit\" to exit): ")

    # Case-insensitive check
    if guess.upper() == "QUIT":
        break

    try:
        numberguess = int(guess)

        # Valid attempt, user entered a number        
        attempts += 1

        # Check guess against our target
        # Note we're not telling the user if they are outside our range, but we could do that
        if numberguess == target:
            print("Congratulations! You guessed the right number!")
            break
        elif numberguess < target:
            print("I'm thinking of a bigger number, try again")
        else:
            print("I'm thinking of a smaller number, try again")

    # User didn't enter a valid option
    except ValueError:
        print("Sorry I didn't understand that. Please guess a number, or type \"quit\" to exit")
        continue

print(f"You had {attempts}", "attempt" if attempts == 1 else "attempts")


'''
Comments: We're checking user input. I'm only counting tries if the user enters a number.
'''