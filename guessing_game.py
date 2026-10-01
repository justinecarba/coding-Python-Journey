

"""
so today we're gonna make a game which user have to guess the number until she guess it correctly


"""


import random

lowest_number = 1
highest_number = 10

target_number = random.randint(lowest_number, highest_number)

running = True

while running:
    print("\n*************************************************")
    print("           WELCOME TO NUMBER GUESSING GAME       ")
    print("*************************************************")

    user_input = input(f"\nGuess a number between {lowest_number} and {highest_number}: ")

    if not user_input.isdigit():
        print("Please enter a valid number.")
        continue

    user_guess = int(user_input)

    if user_guess < lowest_number or user_guess > highest_number:
        print(f"Please guess a number within the range {lowest_number} to {highest_number}.")
        continue

    if user_guess < target_number:
        print("Too low! Try again.")
    elif user_guess > target_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the correct number!")

        again = input("Do you want to play again? (yes/no): ").strip().lower()
        if again == "yes":
            target_number = random.randint(lowest_number, highest_number)
            print("Great! Let's play again.")
        else:
            print("Exiting the program......")
            running = False