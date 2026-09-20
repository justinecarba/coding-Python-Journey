"""
-  we're gonna recall our knowledge in python
"""

"""
-  calculator 
- temperature 
- number guessing game
- rock, paper, scissor
- grade manager
- book store
- to continue..
"""

# Calculator

"""
- we're gonna make a calculator for recalling
"""

while True:
    print("\n=====CALCULATOR=====")
    operator = input("Enter the operator (* - + /) press q to quit: ")
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))

    if operator == "q":
        break

    elif operator == "*":
        result = first_number * second_number
        print(result)

    elif operator == "-":
        result = first_number - second_number
        print(result)

    elif operator == "+":
        result = first_number + second_number
        print(result)

    elif operator == "/":
        if first_number < second_number:
            print("lower number cannot be divided in greater number!")

        else:
            result = first_number / second_number
            print(result)

    else:
        print("Invalid Operator!!")


# TEMPERATURE
"""
-  F = (°C × 9/5) + 32. - Celscius
- C = ( F − 32) × 5/9 - Farenheit
"""

running = True

while running:
    print("========TEMPERATURE========")
    temp = int(input("Enter the temperature: "))
    is_farenheit = input("Is it farenheit or celscius press F or C (press Q to quit): ").title()

    if is_farenheit == "Q":
        running = False

    elif is_farenheit == "F":
        celscius = (temp - 32) * 5 / 9
        print(celscius)

        if celscius > 36:
            print("Too Hot!")

        else:
            print("Too Cold!!")

    elif is_farenheit == "C":
        farenheit = (temp * 9 / 5) + 32
        print(farenheit)

        if farenheit > 40:
            print("Too Hot!!")

        else:
            print("Too Cold!!")

    else:
        print("Invalid Choice!!")



# NUMBER GUESSING GAME

"""
- we're gonna guess some numbers from 1 to 10 until we get correct answer
"""

import random

lowest_number = 1
highest_number = 10

running = True

while True:
    print("\n=======WELCOME TO NUMBER GUESSING GAME=======")
    print(f"===GUESS SOME NUMBER FROM {lowest_number} to {highest_number}====")

    comp = random.randint(lowest_number, highest_number)

    player  = (input("Enter your guess (q to quit): ")).lower()

    if player == "q":
        break

    elif int(player) < lowest_number and int(player) > highest_number:
        print("That's out of range!!")

    elif int(player) < comp:
        print("Too low!")

    elif int(player) > comp:
        print("Too high!!")

    else:
        print("Correct!!")

        


# BATO BATO PICK

"""
- we're gonna make a game rock, paper, scissor
"""   
import random
running = True

opponent = {1 : "Justine",
            2 : "Jason",
            3 : "Rannel"
            }

choice1 = {
    "Opponent" : "Justine",
    "Category" : "Trashtalker!",
    "Justine" : "Hello, give me your shot!!",
    "Justine" : "Your such a weakness!!"
}

justine1 = {
    "Justine"  : "You're such a dumb as always!",
    "Justine"  : "HAHAHA, loser!!"
}

choice2 = {
    "Opponent"  : "Jason",
    "Category"  : "Kind",

    "Jason"  :  "Hello, can i play with you? :(",
    "Jason"  :  "It will be really fun:)"
}

Jason1 = {
    "Jason"  : "Ahh, good game!",
    "Jason"  : "Come back, next time!"
}

choice3 = {
    "Oponent"   :   "Rannel",
    "Category"  :   "Crazy",

    "Rannel"    :   "Yoww, what's up buang!!",
    "Rannel"    :   "You can't win pakshit!!"
}

Rannel1 = {
    "Rannel"   :    "HAHAHAHA, TALO!!!",
    "Rannel"   :    "Better luck next time!! dude!!"
}

options = ["rock", "paper", "scissor"]

while running:
    print("\n*************************************")
    print("       WELCOME TO BATO BATO PICK       ")
    print("***************************************")
    print("1. Play")
    print("2. Exit")

    choice = input("Enter your choice (1-2): ")

    if choice == "1":
        print("\n===== SELECT OPONENT=====")
        for key, value in opponent.items():
            print(f"{key:10} : {value}")
        print("=========================")

        choose = input("Choose your opponent by entering their number code (1, 2, 3): ")

        if choose == "1":
            for i, j in choice1.items():
                print(f"{i} :         {j}")
            print()

            while True:  

                result = random.choice(options)

                user = input("Enter your choice press rock, paper, or scissor (press q to quit): ").lower()

                print(f"Justine Pick : {result}")
                print(f"Your Pick : {user}")

                if user == "q":
                    break
                
                elif user == result:
                    print("Tie!!")

                elif user == "rock" and result == "scissor":
                    print("You win!!")

                elif user == "scissor" and result == "paper":
                    print("You win!!")

                elif user == "paper" and result == "rock":
                    print("You win!!")

                else:
                    print("You Lose!!")
                    for key, value in justine1.items():
                        print(f"\n{key} :          {value}")
                    print()

        elif choose == "2":
            print("\n====SELECT OPONENT====")
            for key, value in choice2.items():
                print(f"{key}      :   {value}")
            print("========================")

            while True:
                result = random.choice(options)
                
                user = input("Enter your choice press rock, paper, or scissor (press q to quit): ").lower()

                print(f"Jason Pick : {result}")
                print(f"Your Pick  : {user}")

                if user == "q":
                    break
                
                elif user == result:
                    print("Tie!!")

                elif user == "rock" and result == "scissor":
                    print("You win!!")

                elif user == "scissor" and result == "paper":
                    print("You win!!")

                elif user == "paper" and result == "rock":
                    print("You win!!")

                else:
                    print("You Lose!!")
                    for key, value in Jason1.items():
                        print(f"\n{key} :          {value}")
                    print()

        elif choose == "3":
            print("\n====SELECT OPONENT====")
            for key, value in choice3.items():
                print(f"{key}     :        {value}")
            print("========================")

            while True:
                result = random.choice(options)
                                
                user = input("Enter your choice press rock, paper, or scissor (press q to quit): ").lower()

                print(f"Rannel Pick : {result}")
                print(f"Your Pick   : {user}")

                if user == "q":
                    break
                
                elif user == result:
                    print("Tie!!")

                elif user == "rock" and result == "scissor":
                    print("You win!!")

                elif user == "scissor" and result == "paper":
                    print("You win!!")

                elif user == "paper" and result == "rock":
                    print("You win!!")

                else:
                    print("You Lose!!")
                    for key, value in Rannel1.items():
                        print(f"\n{key} :          {value}")
                    print()

        else:
            print("Invalid Choice!!")

    elif choice == "2":
        again = input("Exit? pres y for yes and n for no: ").lower()

        if again == "y" and again != "n":
            print("Thankyouuu for playing!!")
            running = False

    else:
        print("Invalid Choice!!")


# Grade Manager 

"""
- we're gonna make a grade manager for our recall project
- enter student name 
- enter grade for math, english, science, filipino
- calculate average
- display average grade
- display letter grade
- display highest grade
- dislpay lowest grade
"""

grade = ["Math", "English", "Science", "Filipino"]

# Use the bool function in while functions
running = True

while running:
    print("\n=================================")
    print("      MANAGING STUDENT GRADE     ")
    print("=================================")

    name = input("Enter the student name: ")

    print("====ENTER GRADE====")
    for i in grade:
        print(i)
    print()

    choose = input("Choose subject grade: ").title()

    if choose in grade:
        enter_grade = int(input("Enter grade: "))

        if enter_grade <= 0 or enter_grade > 100:
            print("Invalid Grade!")

        else:
            print("Record Successfully!")

    else:
        print("That subject is not available!!")

    print(f"Student Name: {name}")
    print(f"Student Grade: {enter_grade}")

    again = input("Enter again? press Y for yes and N for no: ").upper()

    if again == "N" and again != "Y":
        print("Thankyou for using our program!!")
        running = False

