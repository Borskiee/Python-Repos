# Guess the number game
# Try to guess the secretly generated number by picking a number between 1 - 20.
# Max attempts = 5 guesses only

import random
secret = random.randint(1, 20)
max_attempts = 5

# Input section
def get_number():
    while True:
        try:
            x = int(input("\nEnter a number between 1-20: "))
        except ValueError:
            print("\nInvalid input")
            continue
        if 0 < x <= 20:
            return x
        else:
            print("\nPlease select a number between 1-20.")

# Logic and Output
def run_game():
    attempts = 0
    while True:
        attempts += 1
        choice = get_number()
        if choice > secret:
            print("\nGuess too high")
        elif choice < secret:
            print("\nGuess too low")
        else:
            print("\nCongrats! You guessed correctly!")
            break
        if attempts == max_attempts:
            print(f"\nMax attempts reached. Answer is {secret}")
            break
        print(f"\nAttempts: {attempts}/{max_attempts}")

# Run main
run_game()