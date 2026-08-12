
# My Second Practice

#Input:
#5
#8
#2
#10
#7

#Output:
#Largest number is 10

#x = 5
#y = 8
#z = 2
#r = 10
#j =7

#result = max(x, y, z, r, j)

#print(result)

# 2. Count Even and Odd Numbers

#Ask the user for 10 numbers and count how many are even and how many are odd.

#Example Output:

#Even: 6
#Odd: 4

#even_count = 0
#odd_count = 0

#for i in range(10):
#    num = int(input("Enter a number: "))
#    if num % 2 == 0:
#        even_count += 1
#    else:
#        odd_count += 1

#print(f"Even: {even_count}")
#print(f"Odd: {odd_count}")

# 3. Sum of Digits

#Ask the user for a number and calculate the sum of its digits.

#Example:

#Input: 1234
#Output: 10



# 4. Number Guessing Game (Improved)

#Generate a random number from 1–100 and give the user only 7 attempts to guess it.

#Extra Challenge:

#Show remaining attempts.
#Tell if the guess is too high or too low.

#import random


#secret_number = random.randint(1, 100)
#attemps = 0

#print("---Welcome to the Number Guessing Game---")
#print("---Guess some Numbers from 1 to 100---")

#while True:
 #   guess = int(input("Guess some numbers from (1 to 100): "))
 #   if guess > secret_number:
 #       print("Too High!")
 #       attemps += 1
 #   elif guess < secret_number:
 #       print("Too Low!!")
 #       attemps += 1
 #   else:
 #       print("Correct!!")
#        break



# 5. Password Strength Checker

#ask the user for a password.

#Rules:

#At least 8 characters
#Contains a number
#Contains a capital letter

#password = input("Enter your password: ")

#has_number = True
#has_capital = True

#for char in password:
#    if password.isdigit:
#        has_number = True
#    elif password.capitalize:
#        has_capital = True
#    break

#if len(password) <= 8 and has_number and has_capital:
#    print("Valid Password!")
#else:
#    print("Invalid Password!")

# 6. Find the Second Largest Number

#Ask the user for 5 numbers and find the second largest.

#Example:

#Input:
#10
#25
#15
#40
#30

#Output:
#Second largest is 30

#numbers = []

#for i in range(5):
#    num = int(input(f"Enter number {i+1}: "))
#    numbers.append(num)

#numbers.sort()

#print("Second largest is", numbers[-2])

# 7. Count Words in a Sentence

#Ask the user for a sentence and count how many words it contains.

#Example:

#Input:
#I love Python programming

#Output:
#4 words

#Hint: Use .split().

#ask = input("Enter some sentence to counts how many words it contains: ")
#word_count = 0

# Conssesion Stand Program

# dictionary {key:value}

#menu = {"pop corn":  7,
#        "burger"  :  5,
 #       "pizza"   :  110.00,
 #       "fries"   :  3.50,
 #       "lemonade":  7.70}

#cart = []
#total = 0

#print("----------MENU--------------")
#for key, value in menu.items():
#    print(f"{key:10} : ${value:.2f}")
#print("-----------------------------")

#while True:
 #   food = input("Select an item (q to quit): ")
 #   if food == "q":
 #       break
 #   elif menu.get(food) is not None:
 #       cart.append(food)

#print("--------YOUR ORDER-------")
#for food in cart:
#    total += menu.get(food)
#    print(food, end=" ")

#print()
#print(f"Total is: ${total}")


#import random

#low = 1
#high = 100
#option = ("paper", "rock", "scissor")
#cards = ["2", "3", "4", "5", "6", "K", "Q", "J", "A"]

#result = random.randint(low, high)
#result = random.random()
#option = random.choice(option)
#random.shuffle(cards)
#print(cards)

# Number Guessing Game

#import random

#lowest_num = 1
#highest_num = 20

#answer = random.randint(lowest_num, highest_num)

#guesses = 0
#is_running = True

#print("-------WELCOME TO NUMBER GUESSING GAME-------")
#print(f"-------GUESS SOME NUMBERS FROM {lowest_num} TO {highest_num}-------")

#while is_running:
#    guess = input("Enter your guess: ")

#    if guess.isdigit():
#        guess = int(guess)
#        guess += 1

#        if guess < lowest_num or guess > highest_num:
#            print("That guess is out of range!")
#            print(f"Please select from {lowest_num} to {highest_num}: ")

#        elif guess < answer:
#            print("Too Low!")
#        elif guess > answer:
#            print("Too High!!")
#            break
#        elif guess == answer:
#            print("Correct!!")
#            print(f"You guessed the number in {guesses} attempts!")
#            is_running = False
#            break
            
#        else:
#            print("Invalid Guess")
#            print(f"Please select from {lowest_num} to {highest_num}: ")

#    else:
#        print("Invalid Guess")
#        print(f"Please select from {lowest_num} to {highest_num}: ")

# Will be Fixed it tommorow!!......

#import random

#lowest_num = 1
# = 20

#answer = random.randint(lowest_num, highest_num)

#guesses = 0
#is_running = True

#print("-------WELCOME TO NUMBER GUESSING GAME-------")
#print(F"-------GUESS SOME NUMBER FROM {lowest_num} to {highest_num}")

#while True:
#    guess = int(input(f"Enter your guess: "))

#    if guess < lowest_num or guess > highest_num:
#        print("That number is out of range!")
#        print(f"Please select from {lowest_num} to {highest_num}!")
#    elif guess < answer:
#        print("Low, Try Again!")
#    elif guess > answer:
#        print("Too High, Try Again!")
#    else:
#        print("Correct!")
#        break
# 2nd Project
# Bato Bato Pick Game

#import random

#options = ("paper", "rock", "scissor")
#running = True

#while running:
#
#    player = None
#
#    computer = random.choice(options)
#
#    while player not in options:
#        player = input("Please select an choice (paper, rock, scissor): ")
#
#        print(f"Player: {player}")
#        print(f"Computer: {computer}")
#
#        if player == computer:
#            print("It's a tie!")
#        elif player == "paper" and computer == "rock":
#            print("You win!")
#        elif player == "rock" and computer == "scissor":
#            print("You win!")
#        elif player == "scissor" and computer == "paper":
#            print("You win!")
#        else:
#            print("You lose!")
#
#        if not input("Play again? (y/n): ").lower()== "y":
#            running = False
#print("Thankss for Playing!!")


# Rehearsing
# Number Guessing Game

import random


lowest_num = 1
highest_num = 10

answer = random.randint(lowest_num, highest_num)

guesses = []
is_running = True

print("------WELCOME TO NUMBER GUESSING GAME-------")
print(f"------GUESS THE NUMBER IN {lowest_num} to {highest_num}")

while True:
    guess = int(input("Enter your choice: "))

    if guess < lowest_num or guess > highest_num:
        print("That's out of range!!")
        print(f"Pleasee select from {lowest_num} to {highest_num}!")
    elif guess < answer:
        print("Too Low!!")
    elif guess > answer:
        print("Too High!!")
    else:
        print("Correct!!")
        break
print("Thankyouu for Playing!!")

# Bato Bato Pick

import random

options = ("rock", "paper", "scissors")

running = True

while running:

    player = None

    computer = random.choice(options)

    while player not in options:
        player = input("Pleasee select a choice (rock, paper scissors): ")

        print(f"Player: {player}")
        print(f"Computer: {computer}")

        if player == computer:
            print("It's a tie!")
        elif player == "rock" and computer == "scissors":
            print("You win!!")
        elif player == "paper" and computer == "rock":
            print("You win!!")
        elif player == "scissors" and computer == "paper":
            print("You win!!")
        else:
            print("You lose!!")
        
        if not input("Play again? (y/n): ").lower() == "y":
            running = False
print("Thankyou for Playing!!")

# Password Validator

operator = input("Enter the operator (* / + -): ")

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

if operator == "*":
    result = num1 * num2
    print(f"The result is {result}")
elif operator == "/":
    result = num1 / num2
    print(f"The result is {result}")
elif operator == "+":
    result = num1 + num2
    print(f"The result is {result}")
elif operator == "-":
    result = num1 - num2
    print(f"The result is {result}")
else:
    print(f"{operator} is invalid!")

# Activity Game

while True:
    print("---------WELCOME TO ACTIVITY PLANNING--------")
    print("1. Activity")
    print("2. Travel")
    print("3. Meal")
    print("4. Done")
    print("---------------------------------------------")

    game = input("Enter your choice (1, 2, 3, or 4): ")

    if game == "1":
        print("--------ACTIVITY CHOICES--------")
        print("1. Exercise")
        print("2. Swimming")
        print("3. Cooking")
        print("4. Done")
        print("--------------------------------")

        activity = input("Pleasee select what kind of activity (1, 2, 3, 4): ")

        if activity == "1":
            print("Exercise is a good for health❤️")
        elif activity == "2":
            print("swimming is a good for endurance🏊‍♀️")
        elif activity == "3":
            print("cooking is a good for creativity🍳")
        elif activity == "4":
            print("Thank you for using the Activity Planning Game!")
            break
    elif game == "2":
        print("-------PLACE CHOICES--------")
        print("1. Baguio")
        print("2. Boracay")
        print("3. BGC")
        print("4. Done")
        print("----------------------------")

        places = input("Select an options (1, 2, 3, or 4): ")

        if places == "1":
            print("Oh, Bagui is a nice place!")
            print("It sure be cooldy there!")
        elif places == "2":
            print("Oh nice choice!!")
            print("Welcome to boracay the famous foreign spot for beach🏊‍♀️")
        elif places == "3":
            print("Oh! You sure some big time huh!")
            print("BGC is for richiest people come and visit then!!")
        elif places == "4":
            print("Thankyou for choosing!!")
            break
    elif game == "3":
        menu = {"burger" : 10.55,
                "Steak" : 18.50,
                "Shawarma" : 20.90,
                "Pizza" : 19.90,
                "Pie" : 10.50}
        
        cart = []
        total = 0

        print("--------FOOD MENU-------")
        for key, value in menu.items():
            print(f"{key:10} : {value:.2f}")
        print("------------------------")

        while True:
            food = input("Select an item (q to quit): ")

            if food == "q":
                break
            elif menu.get(food) is not None:
                cart.append(food)

        print("-----YOUR ORDER-----")
        for food in cart:
            total += menu.get(food)
            print(food, end=" ")
        
        print()
        print(f"The total is ${total}")
    
    elif game == "4":
        print("Thankyouuu for Playing our Activity Game!")
        print("Great Job!!")
        break
                
# To be continued........

# log in form

while True:
    form = input("Login your email account: ")

    if "@" not in form:
        print("Your email must have (@) to login!")
    elif "." not in form:
        print("Your email must contain (.) to login!")
    elif len(form) > 24:
        print("To login it cannot be more than 24 characters!")
    elif form == " ":
        print("email cannot be have spaces!")
    elif form.isdigit():
        print("email must contain numbers!")
    else:
        print("Login Successful!")
        break

# Password Validator

password = input("Enter your password: ")

has_numbers = True
has_upper = True
has_lower = True

for char in password:
    if char.upper:
        has_upper = True
    elif char.lower:
        has_lower = True
    elif char.isdigit:
        has_numbers = True
    
if len(password ) <= 12 and has_upper and has_lower:
    print("Password Successful!")
else:
    print("Invalid Password!")

# Next Project

student = input("Enter student name: ")

score1 = int(input("Enter the 1st score: "))
score2 = int(input("Enter the 2nd score: "))
score3 = int(input("Enter the 3rd score: "))

average = (score1 + score2 + score3) / 3

if average > 90:
    grade = "A"
elif average > 80:
    grade = "B"
elif average > 70:
    grade = "C"
elif average > 60:
    grade = "D"
else:
    grade = "F"

print(f"Student: {student}")
print(f"Average: {round(average, 2)}")
print(f"Grade: {grade}")

# Next Project


"""
Let's make a diamond pattern
"""

for i in range(1,6):
    print(" " * (5-i) + "*" * (2 * i -1))

for i in range(4, 0, -1):
    print(" " * (5-i) + "*" * (2*i -1))



# . Password Generator

#Features:

#User chooses password length
#Generate random password
#Include numbers and symbols

#Skills:

#random
#Strings
#Loops

import random

user = ("pssppw.123", "owsma90", "#hadty10", "yoyoka.125", "jud.123")

computer = random.choice(user)

while True: 
    password = input("Enter your password: ")

    if password not in user:
        print(f"Strong password Suggestions: {computer}")
    elif len(password) > 12:
        print("Password cannot be more than 12 characters!!")
    elif password == " ":
        print("You haven't entered your password yet!!")
    else:
        print("Password Successful!")
        break




# Trying on my own

# Quiz Game

questions = ((" Who is the currently president of the phillipines? "),
             (" What is the national language in the phillipines? "),
             (" What is the national animal in the phillipines? "))

options = (("a. Duterte ", "b. Marcos sr. ", "c. Marcos jr.", "d. Corazon Aquino"),
           ("a. English", "b. Spanish", "c. Filipino ", "d. Japanese"),
           ("a. Karabaw", "b. Parrot ", "c. Eagle ","d. Dog" ))

answers = ("c", "c", "a")

guesses = []

scores = 0

question_num = 0

for question in questions:
    print("--------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter your guess (a b c d): ").lower()
    guesses.append(guess)

    if guess == answers[question_num]:
        scores += 1
        print("Correct!")
    else:
        print("Incorrect!")
    print(f"The correct answer is {answers[question_num]}!")
    question_num += 1


print("---------------------")
print("       RESULT        ")
print("---------------------")

print("Answers: ", end = "")

for answer in answers:
    print(answer, end = " ")
print()

print("Guesses: ", end = "")

for guess in guesses:
    print(guess, end = " ")
print()

scores = int(scores / len(questions) * 100)
print(f"Your total score is: {scores}%")

if scores > 90:
    grade = "A"
    print(f"Grade: {grade}")
elif scores > 80:
    grade = "B"
    print(f"Grade: {grade}")
elif scores > 70:
    grade = "C"
    print(f"Grade: {grade}")
elif scores > 60:
    grade = "D"
    print(f"Grade: {grade}")
else:
    grade = "F"
    print(f"Grade: {grade}!")


# Project Player vs Computer Quiz Game

#import random

#questions = (("1. What is the national fruit in the philippines? "))
#options = ("a. Manggo", "b. Apple", "c. Banana", "d. Grapes")

#answers = ("a. Manggo")
#guesses = []

#score = 0

#question_num = 0

#print("----------WELCOME TO QUIZ GAME------------")
#print("1. What is the national fruits of the philippines? ")
#print("a. Manggo  b. Apple  c. Banana  d. Grapes")
#options = ("a", "b", "c", "d")

#running = True

#while running:
  #  player = input("Enter your choice: ")
  #  computer = random.choice(options)

  #  while player not in options:
  #      print("That choice is not in options!")
  #      player = input("Pleasee select from (a b c d): ")

  #      print(f"Player choice: {player}")
  #      print(f"Computer choice: {computer}")

  #      if player == "a" and computer == "a":
  #          print("It's a tie!")
  #      elif player == "a" and computer == "b":
   #         print("You win!")
 #       elif player == "a" and computer == "c":
 #           print("You win!")
 #       elif player == "a" and computer == "d":
 #           print("You win!")
 #       elif player == "b" and computer == "a":
  #          print("You lose!")
 #       elif player == "c" and computer == "a":
 #           print("You lose!")
 #       elif player == "d" and computer == "a":
 #          print("You lose!!")
 #       else:
 #          print("You both lose!")
#           print(f"The correct answer is {answers}")
           
 #          if not input("Play again? (y/n): ").lower() == "y":
#               running = False
#               break
           
#print("Thankyouu for playing!!")

# next project
# To Do list app:

# Trying it on my own...

#tasks = []

#while True:
 #   print("====TO DO LIST======")
 #   print("1. View Task")
 #   print("2. Add Task")
 #   print("3. Delete Task")
 #   print("4. Exit")

 #   choice = input("Enter your option (1-4): ")

 #   if choice == "1":
  #      if len(tasks) == 0:
  #          print("No task available!")
  #      else:
  #          print("\nYour Task")
  #          for i, task in enumerate(tasks, start=1):
   #             print(f"{i}.{task}")

   # elif choice == "2":
   #     task = input("Enter a new task: ")
   #     tasks.append(task)
    #    print("Task added successfully!")

   # elif choice == "3":
   #     if len(tasks) == 0:
   #         print("No task to delete!")
   #     else:
   #         print("\nYou Task")
   #         for i, task in enumerate(tasks, start=1):
   #             print(f"{i}.{task}")
            
   #         try:
   #             task_num = int(input("Enter the tasks number to delete: "))
   #             if 1 <= task_num <= len(task):
   #                 remove_task = tasks.pop(task_num - 1)
   #                 print(f"{remove_task} has been deleted!")
   #             else:
   #                 print("Invalid task number!")
   #         except ValueError:
   #             print("Please enter a valid number!")
            
  #  elif choice == "4":
  #      print("Goodbye!")
  #      break
  #  else:
  #      print("Invalid choice. Try again!")


    
# revise
# Number Guessing Game
import random

lowest_num = 1
highest_num = 20

answers = random.randint(lowest_num, highest_num)

guesses = []
is_running = True
print("======WELCOME TO NUMBER GUESSING GAME====")
print(f"------GUESS NUMBER FROM {lowest_num} to {highest_num}-------")

while True:
    guess = int(input("Enter your guess: "))

    if guess < lowest_num and guess > highest_num:
        print("That's out of range!")
        print(f"Please select from {lowest_num} to {highest_num}!")
    elif guess < answers:
        print("Too low!")
    elif guess > answers:
        print("Too high!!")
    else:
        print("Correct!")
        break
print("Thankyou for playing")

# Bato Bato Pick

import random

options = ("rock", "paper", "scissor")

running = True

while running:
    player = None

    computer = random.choice(options)

    while player not in options:
        player = input("Please select from (rock, paper, scissor): ")

        print(f"Player select: {player}")
        print(f"Computer select: {computer}")

        if player == computer:
            print("It's a tie!")
        elif player == "rock" and computer == "scissor":
            print("You win!")
        elif player == "paper" and computer == "rock":
            print("You win!")
        elif player == "scissor" and computer == "paper":
            print("You win!")
        else:
            print("You lose!!")

        if not input("Play again? (y/n): ").lower() == "y":
            running = False
print("Thankyou for playing!")

# Python Calculator

operator = input("Enter the operator (* + / -): ")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if operator == "*":
    result = num1 * num2
    print(result)
elif operator == "+":
    result = num1 + num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
else:
    print(f"{operator} is not valid!")

# Bank System

balanced = 0

while True:
    print("======Banking System=====")
    print("1. Deposit")
    print("2. Withdrawal")
    print("3. Check Balanced")
    print("4. Exit")
    print("=========================")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        amount = float(input("Enter the amount: "))

        if amount >= 0:
            balanced += amount
            print("Deposit Successful!")
        else:
            print("Invalid Amount!")

    elif choice == "2":
        amount = float(input("Enter your withdrawal amount: "))

        if amount > balanced:
            print("Insufficient Balanced!")
        elif amount <= 0:
            print("Invalid Amount!")
        else:
            print("Withdrawal Successful!!")

    elif choice == "3":
        print(f"Your balanced: {balanced}")

    elif choice == "4":
        print("Thankyou for using my banking system!!")
        break


# Quiz Game

import random

questions = (("1. What is the largest volcano in phillipines? "),
             ("2. What is the best university in phillipines? "),
             ("3. Who is the most genius man in history? "))

options = (("a. Taal Volcano", "b. Mayon Volcano", "c. Lake Volcano", "d. Everis Volcano"),
           ("a. UNC", "b. LASSALE", "c. MAPUA", "d. ATENEO"),
           ("a. Albert Einstein", "b. Jose Rizal", "c. Galilieo Galili", "d. BBM"))

answers = ("b", "d", "a")

guesses = []

scores = 0

question_num = 0

for question in questions:
    print("=======================")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter your guess (a b c d): ").lower()
    guesses.append(guess)

    if guess == answers[question_num]:
        scores += 1
        print("Correct!")
    else:
        print("Inccorect!")
        print(f"The correct answer is {answers[question_num]}!")
    
    question_num += 1

print("=====================")
print("       RESULT        ")
print("=====================")

print("Answers:", end = "")

for answer in answers:
    print(answer, end=" ")
print()

print("Guesses:", end="")

for guess in guesses:
    print(guess, end = " ")
print()

scores = int(scores / len(questions) * 100)
print(f"Your total score is: {scores}%")

if scores > 90:
    grade = "A"
    print(f"Grade: {grade}")
elif scores > 80:
    grade = "B"
    print(f"Grade: {grade}")
elif scores > 70:
    grade = "C"
    print(f"grade: {grade}")
elif scores > 60:
    grade = "D"
    print(f"Grade: {grade}")
else:
    grade = "F"
    print(f"Grade: {grade}")

# TO DO LIST APP

tasks = []

while True:
    print("======To Do List=======")
    print("1. View Task")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice task (1-4): ")

    if choice == "1":
        if len(tasks) == 0:
            print("No Task Available!")
        else:
            print("\n Your Task")
            for i, key in enumerate(tasks, start=1):
                print(f"{i}.{key}")

    elif choice == "2":
        task = input("Enter your new task: ")
        tasks.append(task)
        print("Task Added Successfully!")

    elif choice == "3":
        if len(tasks) == 0:
            print("No task available!")
        else:
            print("Your Task")
            for i, key in enumerate(tasks, start=1):
                print(f"{i}.{key}")
        
        try:
            task_num = int(input("Enter the tasks number to delete: "))
            if 1 <= task_num <= len(tasks):
                remove_task = tasks.pop(task_num - 1)
                print(f"{remove_task} has been deleted!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter valid number!")
    
    elif choice == "4":
        print("Thankyouu and Goodbye!")
        break
    else:
        print("Invalid Choice! Try again.")

# Student Grade Manager

#Features:

#Add student names
#Add grades
#Calculate averages
#Find highest grade

#Skills:

#Dictionaries
#Functions
#File handling

student = input("Enter students name: ")
score1 = int(input("Enter the first grade: "))
score2 = int(input("Enter the second grade: "))
score3 = int(input("Enter the third grade: "))

average = int(score1 + score2 + score3) / 3


if average > 90:
    grade = "A"
elif average > 80:
    grade = "B"
elif average > 70:
    grade = "C"
elif average > 60:
    grade = "D"
else:
    grade = "F"


result = max(score1, score2, score3)
print(f"{student} highest average is: {result}")

print("=====RESULT======")
print(f"Student name: {student}")
print(f"Average: {round(average, 2)}")
print(f"Grade: {grade}")

# . Number Statistics Program

#User enters numbers and the program finds:

#Largest number
#Smallest number
#Average
#Second largest number

#Skills:

#Lists
#Sorting
#Math operations

#import math
#num1 = int(input(f"Enter the first number: "))
#num2 = int(input("Enter the second number: "))
#num3 = int(input("Enter the third number: "))

#average = int(num1 + num2 + num3) / 3                # This is wrong

#result1 = max(num1, num2, num3)
#print(f"The Largest number is : {result1}")

#result2 = min(num1, num2, num3)
#print(f"The smallest number is: {result2}")

#print(math.ceil,2(num1, num2, num3))

#print(f"The average is: {average}")


# trying on my own

numbers = []

print("====Enter 5 Number====")

for i in range(5):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)

largest = max(numbers)
smallest = min(numbers)
average = sum(numbers) / len(numbers)

sorted_numbers = sorted(numbers)
second_largest = sorted_numbers[-2]

print("====STATISTICS=====")
print(f"Numbers: {numbers}")
print(f"Largest: {largest}")
print(f"Smallest: {smallest}")
print(f"Average: {average}")
print(f"Second Largest: {second_largest}")

# Next Project......

"""
I better be improved my skill in this course,
I want someday i gonna be a programmer,
and become a software engineer.

"""
# The real battle will start now and i promise to my self that i will never give up until i win!!!

"""
To be continued........
"""


# List
"""
- Access list items
- Change list items
- Add list items
- Remove list items
- Loop list
- list comprehensions
- sort list
- copy list
- join list
- list methods
- list exercises
"""


# Access list items- more on indexing

list = ["apple", "banana", "cherry"]
print(list[0])  # Output: apple
print(list[1])  # Output: banana
print(list[2])  # Output: cherry

# Change list items - to change the value of a specific item, you can access it by its index and assign a new value to it.
list[0] = "orange"
print(list)  # Output: ['orange', 'banana', 'cherry']

# Add list items - adding items to a list can be done using the append() method, which adds an item to the end of the list, or the insert()
# method, which allows you to specify the index where the new item should be added.

"""

"""
list.append("grape")
print(list)  # Output: ['orange', 'banana', 'cherry', 'grape']

# Remove list items - to remove an item from a list, you can use the remove() method.
"""

"""
list.remove("banana")
print(list)  # Output: ['orange', 'cherry', 'grape']


