

from main import *
print(__name__)


#pi = 3.14159 # This can use by importing modules using import function

# MY OWN PROJECT

import datetime

a = datetime.datetime.now()
a = a.strftime("%Y-%m-%d %H:%M:%S")
print(a)


# 1. Banking System
"""
Features:

Deposit
Withdraw
Check balance
Save account data

Skills:

Functions
File handling
Dictionaries
"""
withdraw = 0
while True:
    print("====BANKING SYSTEM====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Save account data")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        amount = int(input("Enter your deposit amount: "))

        total = 0
        balance = 0

        if amount <= 0:
            print("Invalid amount!")
        else:
            total += amount
            balance += amount
            print("Deposit Successfully!")

    elif choice == "2":
        withdraw = int(input("Enter your withdrawal amount: "))
        

        if withdraw <= 0:
            print("Insufficient amount!")
        elif withdraw > balance:
            print("Invalid amount!")
        else:
            print("Withdrawal successful!!")

    elif choice == "3":
        print(f"Your previous balanced: ${balance}")
        result = balance - withdraw
        print(f"Your new balance ${result} ")

    elif choice == "4":
        print("Save acount data!")
        print("Thankyou for using my bank system!")
        break
    else:
        print("Invalid choice!")
        

# Bato Bato Pick Game
# MY PROJECT

import random

scores = 0
score = 0

options = ["rock", "paper", "scissor"]

running = True

while running:
    print("===WELCOME TO BATO BATO PICK GAME====")
   
    player = None
    
    computer = random.choice(options)
    player = input("Enter your choice: ")

    print(f"Player select: {player}")
    print(f"Computer select: {computer}")

    while player not in options:
        print("That's out for options!!")
        print("Try Again!!")
        break
    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissor":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissor" and computer == "paper":
        print("You win!!")
        break
    else:
        print("You lose!!")
        
        
    
    if not input("Play again? (y/n): ").lower() == "y":
        running = False

print("Thankou for playing!!")

# next project
# NUMBER GUESSING GAME

import random

lowest_num = 1
highest_num = 10

answer = random.randint(lowest_num, highest_num)
running = True

while True:
    print("===WELCOME TO NUMBER GUESSING GAME===")
    print(f"GUESS SOME NUMBER FROM {lowest_num} to {highest_num}")

    player = int(input("Enter your choice from (1-10): "))
    
    if player < lowest_num and player > highest_num:
        print("That's out of range!!")
        print(f"Please select from {lowest_num} to {highest_num}!!")
    elif player > answer:
        print("Too high!!")
    elif player < answer:
        print("Too low!!")
    else:
        print("Correct!!")
        break

print("Thankyou for playing!!")

# Restaurant Food - MY WORK

"""
- Online
- Menu
- Order
- Total
- Done
"""


menu = {
    "chicken joy" : 99.00,
    "steak" : 119.00,
    "shawarma" : 110.00,
    "pansit bato" : 89.50,
    "sphagetti" : 50.00,
    "burger" : 59.50,
    "milk tea" : 79.00
}


cart = []
running = True

while running:
    print("======WELCOME TO JUSTINE ONLINE FOOD=======")
    print("1. View Menu")
    print("2. Select Order")
    print("3. Total Payment")
    print("4. Done/Exit")

    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":

        print("=====MENU AVAILABLE=====")
        for key, value in menu.items():
            print(f"{key.title():12} : ${value:.2f}")
        print("========================")

    elif choice == "2":

        while True:
            choose = input("Enter you want to bought (q to quit): ").lower()
            
            if choose == "q":
                break

            elif choose in menu:
                cart.append(choose)
                
                total = 0

                print("===YOUR CART===")
                for item in cart:
                    print(item.title())
                    total += menu[item]

                print(f"Your total: ${total:.2f}")


            else:
                print("Menu not found!!")

    elif choice == "3":
        if not cart:
            print("Your cart is totally empty!!")

        else:
            total = 0

            print("==========RECEIPT==========")
            for item in cart:
                print(f"{item.title():12} : ${menu[item]:.2f}")
                total += menu[item]
        
            print("--------------------------------")
            print(f"Your total payment: {total:.2f}")

            cart.clear()
            print("Thankyou for purchase!!")

    elif choice == "4":
        print("Goodbye!!")
        running = False

    else:
        print("Invalid Choice!!")


# to be continued......

#7. Expense Tracker

#Concept:

#Add expenses
#View expenses
#Calculate total spending
#Categorize expenses

#Skills:

#Dictionaries
#Functions
#File handling

expenses = []

running = True

while running:
    print("====EXPENSE TRACKER====")
    print("1. Add expenses")
    print("2. View expenses")
    print("3. Calculate total expenses")
    print("4. Categorize expenses")

    choice = input("Enter your choice from (1-4): ")


    if choice == "1":
        amount = float(input("Enter the amount: "))
        category = input("Enter the category: ")

        expense = {
            "amount" : amount,
            "category" : category
        }

        expenses.append(expense)
        print("Added successfully!!")
    
    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses recorded!!")
        else:
            print("====EXPENSES====")
            for i, expense in enumerate(expenses, start=1):
                print(
                    f"{i}.{expense["category"]} - ${expense["amount"]:.2f}"
                    )

    elif choice == "3":
        total = 0

        for expense in expenses:
            total += expense["amount"]

            print(f"Total expenses: ${total:.2f}")

    elif choice == "4":
        print("Thankyou and goodbye!!")
        break
    else:
        print("Invalid Choice!!")

# to be continued.....

# QUIZ GAME - Yupp my own project
"""
- have questions
- have options
- have answers
- have guesses
- have scores
- have grade
"""
# But before that i'm gonna put player/student name to specify who are playing

questions = ()
options = ()
answers = ()
guesses = []
scores = 0
question_num = 0

running = True

while running:
    print("===========WELCOME TO QUIZ GAME==========")
    print("1. View Questions")
    print("2. View Options")
    print("3. View Provided Answers")
    print("4. Enter Guesses")
    print("5. View Grades")
    print("6. Done")

   

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        
        print("==============QUESTIONS================")
        questions = (("1. What is the name of devil fruit by luffy?: "),
                     ("2. What style of swordsman zoro is?: "),
                     ("3. Who accquire the devil fruit of ace?: "))
        
        for question in questions:
            print(question)
        print()
        
        question_num += 1

    elif choice == "2":
        print("=================OPTIONS======================")
        options = (
            ("a. Hito Hito No Mi", "b. Flame Flame Fruit", "c. Gum Gum Fruit", "d. Gas Gas Fruit"),
            ("a. 1 swordsman", "b. 2 swords style", "c. 3 swordsman style", "d. None of the above"),
            ("a. Luffy", "b. Sabo", "c. Douflamingo", "d. Law")
            )
        
        for option in options:
            print(option)

        question_num += 1

    elif choice == "3":

        print("=====PROVIDED ANSWERS======")
        answers = ("c", "c", "b")

        for answer in answers:
            print(answer)

        question_num += 1
    
    
    elif choice == "4":

        for question_num in range(len(questions)):
            print("\n=====================")
            print(questions[question_num])

            for option in options[question_num]:
                print(option)

            guess = input("Enter your guess (a, b, c, d): ").lower()
            guesses.append(guess)

            if guess == answers[question_num]:
                scores += 1
                print("Correct!")
            else:
                print("Incorrect!")
                print(f"Correct answer: {answers[question_num]}")

        question_num += 1

               
    elif choice == "5":
        print("=============")
        print("    RESULT   ")
        print("=============")

        print("Answer:", end="")

        for answer in answers:
            print(answer, end = " ")
        print()

        print("Guesses: ", end="")

        for guess in guesses:
            print(guess, end = " ")
        print()

        scores = int(scores / len(questions) * 100)
        print(f"Your total score is {scores}%")

        if scores > 90:
            grade = "A"
            print(f"Grade: {grade}")
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
            print(f"Grade: {grade}")

    elif choice == "6":
        print("Thankyou for playing. Goodbye!")
        running = False
        break
    else:
        print("Invalid choice!!")
                
# to be continued.....

# To do list app
"""
- View Task
- Add Task
- Delete Task
- Exit
"""
               
tasks = []

while True:
    print("====TO DO LIST APP====")
    print("1. View Task")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        if len(tasks) == 0:
            print("No Task Recorded!")
        else:
            print("====YOUR TASK====")
            for i, key in enumerate(tasks, start=1):
                print(f"{i}.{key}")

    elif choice == "2":
        task = input("Enter e new task: ")
        tasks.append(task)
        print("Task Added Successfully!!")

    elif choice == "3":
        if len(tasks) == 0:
            print("No Task Recorded!!")
        else:
            print("====YOUR TASK====")
            for i, key in enumerate(tasks, start=1):
                print(f"{i}.{key}")
        
        try:
            task_num = int(input("Enter a new task number to delete: "))
            if 1 <= task_num <= len(tasks):
                remove_task = tasks.pop(task_num - 1)
                print(f"{remove_task} has been deleted!!")
            else:
                print("Invalid Task Number!!")
        except ValueError:
            print("Please enter a valid number!!")

    elif choice == "4":
        print("Thankyou and Goodbye!!")
        break
    else:
        print("Invalid Choice!!")


# Book Store - My own project
"""
- View Books
- Select Books
- Buy Books
- Exit
"""
book = { 
    "romance" : 99.99,
    "comedy" : 110.00,
    "love story" : 119.50,
    "horror" : 99.50,
    "action" : 100.00,
    "drama" : 99.99,
    "motivational" : 150.00,
    "anime book" : 110.50
}


buy = ""
cart = []

running = True

while running:
    print("====BOOK STORE=====")
    print("1. View Books")
    print("2. Select Books")
    print("3. Buy Books")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":

        print("====AVAILABLE BOOKS====")
        for key, value in book.items():
            print(f"{key.title():12} : {value:.2f}")
        print("========================")

    elif choice == "2":
        
        while True:
            choose = input("Select a book your interested! (q to quit): ").lower()

            if choose == "q":
                break

            elif choose in book:
                cart.append(choose)

                total = 0

                print("====YOUR CART====")
                for item in cart:
                    print(f"{item.title()}")
                    total += book[item]

                print(f"The total is: {total:.2f}")

            else:
                print("Book not found!!")

    elif choice == "3":

        if not cart:
            print("Your cart is empty!!")

        else:
            
            total = 0

            print("=====RECEIPT====")
            for item in cart:
                print(f"{item.title():12}  ${book[item]:.2f}")
                total += book[item]

            print("-------------------")
            print(f"The total is: ${total:.2f}")

            cart.clear()
            print("Thankyouuu for purchasing!!")

    elif choice == "4":
        print("Thankyouuu and Goodbyee!!")
        running = False

    else:
        print("Invalid Choice!!")

# to be continued.....

# Temperature
"""
- Search a place
- View Temperature
- View Weather Condition
- Exit
"""

"""
- fahrenheit = (celsius * 9/5) + 32
- celsius = (fahrenheit - 32) * 5/9
"""
place = [
    "naga",
    "cebu",
    "rizal",
    "masbate", 
    "tagaytay"
    ]

search_place = ""
running = True

while running:
    print("=======WELCOME TO WEATHER FORECASTING=======")
    print("1. Search a place")
    print("2. Enter Temperature")
    print("3. View Weather Condition")
    print("4. Exit")
    print("-------------------------------")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        search_place = input("Search a place: ").lower()

        if search_place not in place:
            print("That's out of range!!")
        else:

            print(f"Place: {search_place}")

    elif choice == "2":
        
        if search_place == "":
            print("Select a place first!!")
        
        elif search_place in place:
            temperature = int(input("Enter the temperature: "))
            unit = input("Enter if it is celcius or fahrenheit (C/F): ")

            if unit == "C":
                f = int(temperature * 9/5) + 32
                print(f"The temperature in fahrenheit is: {f:.2f}°F")

            elif unit == "F":
                c = int(temperature - 32) * 5/9
                print(f"The temperature in celsius is: {c:.2f}°C")

        else:
            print("That's not available!!")

    elif choice == "3":

        if search_place == "":
            print("Select a place first!!")

        elif unit == "C":
            print(f"Temperature: {temperature}°C")

            if temperature >= 36:
                print("Hot Day")
            else:
                print("Cold Day")

        elif unit == "F":
            print(f"Temperature: {temperature}°F")

            if temperature >= 96.8:
                print("Hot Day")
            else:
                print("Cold Day")

        else:
            print("That's out of options!!")

    elif choice == "4":
        again = input("See Again? (y/n): ")
        
        if again != "y":
            print("Thankyouu and Goodbye!!")
            running = False

    else:
        print("Invalid Choice!!")

# to be continued.....

# my own project
# Dice Game
"""
- View Prizes
- Play Dice
- See Result
- Exit
"""

jackpot_num = 19
num_of_dice = ""
running = True

while running:
    print("====WELCOME TO DICE GAME====")
    print("1. View Prizes")
    print("2. Play Dice")
    print("3. See Result")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":

        def info(**kwargs):
            print("====AVAILABLE PRIZES====")
            for key, value in kwargs.items():
                print(f"{key:10} : {value}")
            print()

         
        info(luxuries = "car",
            vehicle = "motor bike",
            living = "House and lot")
        
    elif choice == "2":

        import time
        import random

        #print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
        #● ┌ ─ ┐ │ └ ┘

        "┌─────────┐"
        "│         │"
        "│         │"
        "│         │"
        "└─────────┘"

        dice_art = {
            1 : ( "┌─────────┐",
                  "│         │",
                  "│    ●    │",
                  "│         │",
                  "└─────────┘"),
            2 : ( "┌─────────┐",
                  "│ ●       │",
                  "│         │",
                  "│       ● │",
                  "└─────────┘"),
            3 : ( "┌─────────┐",
                  "│ ●       │",
                  "│    ●    │",
                  "│       ● │",
                  "└─────────┘"),
            4 : ( "┌─────────┐",
                  "│ ●     ● │",
                  "│         │",
                  "│ ●     ● │",
                  "└─────────┘"),
            5 : ( "┌─────────┐",
                  "│ ●     ● │",
                  "│    ●    │",
                  "│ ●     ● │",
                  "└─────────┘"),
            6 : ( "┌─────────┐",
                  "│ ●     ● │",
                  "│ ●     ● │",
                  "│ ●     ● │",
                  "└─────────┘"),
        }

        dice = []
        total = 0
        num_of_dice = int(input("Enter how many number of dice?: "))
        
        print("Dice Game will start in...")
        def count(start, end):
            for x in range(start, end+1):
                print(x)
                time.sleep(1)
            print("Dice Game will start!!")
        count(0, 3)

        for die in range(num_of_dice):
            dice.append(random.randint(1, 6))
        print(f"Result: {dice}")

        for line in range(0, 5):
            for die in dice:
                print(dice_art.get(die)[line], end=" ")
            print()
      
    elif choice == "3":
        if num_of_dice == "":
            print("Please play a dice first!!")

        else:
            print("====TOTAL FOR REWARD====")
            for die in dice:
                total += die
            print(f"Total: {total}")

            if total != jackpot_num:
                print("Ahh better luck next time!!")
            else:
                import random
                reward = ("Car", "Motor Bike", "House and Lot")

                comp = random.choice(reward)

                print(f"Your Reward!!: {comp}")

    elif choice == "4":
        again = input("Play again? (y/n): ").lower()

        if again != "y":
            print("Thankyouu for playing!!")
            print("Goodbye!!")
            running = False
    
    else:
        print("Invalid Choice!!")

# to be continued.....

# Currency Converter

USD_TO_PHP = 58.50
PHP_TO_USD = 1 / USD_TO_PHP

EUR_TO_PHP = 67.00
PHP_TO_EUR = 1 / EUR_TO_PHP

running = True

while running:
    print("\n=====WELCOME TO CURRENCY CONVERTER=====")
    print("1. USD to PHP")
    print("2. PHP to USD")
    print("3. EUR to PHP")
    print("4. PHP to EUR")
    print("5. Exit")
    print("-------------------------")

    choice = input("Enter your choice: ")

    if choice == "1":

        while True:
            amount = float(input("Enter the amount $: "))
            
            if amount <= 0:
                print("Amount must be more than zero!!")
                amount = float(input("Enter the amount $: "))
            else:
                print("====USD TO PHP=====")
                converted = amount * USD_TO_PHP
                print(f"\n {amount:.2f} USD = {converted:.2f} PHP")
                break

    elif choice == "2":

        while True:
            amount = float(input("Enter the amount: "))

            if amount <= 0:
                print("Amount must be more than zero!!")
                amount = float(input("Enter the amount $: "))
            else:
                print("=====PHP TO USD=====")
                converted = amount * PHP_TO_USD
                print(f"\n{amount:.2f} PHP = {converted:.2f} USD")
                break

    elif choice == "3":

        while True:
            amount = float(input("Enter the amount $: "))

            if amount <= 0:
                print("Amount must be more than 0!!")
                amount = float(input("Enter the amount $: "))
            else:
                print("====EUR TO PHP====")
                converted = amount * EUR_TO_PHP
                print(f"\n{amount:.2f} EUR = {converted:.2f} PHP")
                break

    elif choice == "4":

        while True:
            amount = float(input("Enter the amount $: "))

            if amount <= 0:
                print("Amount must be more than 0!!")
                amount = float(input("Enter the amount $: "))
            else:
                print("\n====PHP TO EUR====")
                converted = amount * PHP_TO_EUR
                print(f"\n{amount:.2f} PHP = {converted:.2f} EUR")
                break

    elif choice == "5":
        again = input("Convert again? (y/n): ").lower()

        if again != "y":
            print("Thankyou and Goodbye!!")
            running = False
    
    else:
        print("Invalid Choice!!!")

# Slot Machine

import random

def spin_row():
    symbols = ['🍒', '🍌', '🥭', '🔔', '⭐']

    results = []

    for symbol in range(3):
        results.append(random.choice(symbols))
    return results

def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍌':
            return bet * 4
        elif row[0] == '🥭':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    return 0


def main():
    balance = 1000

    print("****************************")
    print("===WELCOME TO SLOT GAMES====")
    print("Symbol:    🍒 🍌 🥭 🔔 ⭐")
    print("****************************")

    while balance > 0:
        print(f"Current Balance: ${balance}")

        bet = input("Enter your bet amount $: ")

        if not bet.isdigit():
            print("Please enter a valid number!!")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient Amount!!")
            continue

        if bet <= 0:
            print("Bet must be more than 0!!")
            continue

        balance -= bet

        row  = spin_row()
        print("Spinning......\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("Sorry you lose this round!")

        balance += payout



        again  = input("Bet again? (y/n): ").lower()

        if again != "y":
            print("**********************************************")
            print(f"Game over!! Your final balanced is ${balance}")
            print("**********************************************")
            break

if __name__ == '__main__':
    main()
    

# Cinema Ticket Booking

"""
Features:

Choose Movie
Choose Seat
Calculate Total
Print Receipt
"""

movie = {
    "Comedy"      :105.00,
    "Horror"      :199.00,
    "Action"      :119.00,
    "Drama"       :119.00,
    "Love Story"  :299.00
}

rows = ["ROW1", "ROW2", "ROW3"]

seat_price = 100.00

selected_movie = ""
selected_row = ""
seat_count = 0

movie_total = 0
row_total = 0
grand_total = 0

running = True

while running:
    print("\n===CINEMA TICKET BOOKING===")
    print("1. Choose Movie")
    print("2. Choose Seat")
    print("3. Calculate Total")
    print("4. Receipt")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print("\n===AVAILABLE MOVIES===")
        for key, value in movie.items():
            print(f"{key:10}  : ${value:.2f}")
        print()

        while True:
            select = input("Choose movie(q to quit): ").strip() .title()

            if select.lower() == "q":
                break

            elif select in movie:
                selected_movie = select
                print(f"{selected_movie} will start soon!!")
    
            else:
                print("That movie is not in options!!")
                
                
    elif choice == "2":
        if selected_movie == "":
            print("Select movie first before the seat!!")
        else:
            print("\n===AVAILABLE ROWS====")
            for i in rows:
                print(i)

            while True:
                selected_row = input("Choose row: ").strip()

                if selected_row not in rows:
                   print("Invalid Row!!")

                else:
                    break

            while True:
                try:
                    seat_count = int(input("Enter how many seats(1-10): "))

                    if 1 <= seat_count <= 10:
                        print("Seats reserved successfully!!")
                        break

                    else:
                        print("Only 1-10 seats allowed!!")

                except ValueError:
                    print("Invalid Input: Enter numbers only!!")

    elif choice == "3":
        if selected_movie == "":
            print("Select a movie first!!")

        elif seat_count == 0:
            print("Reserved a seat first!!")

        else:

            movie_total = movie[selected_movie] * seat_count
            seat_total = seat_price * seat_count
            grand_total = movie_total + seat_total

            print("\n===TOTAL====")
            print(f"Movie Total  :${movie_total:.2f}")
            print(F"Seat Fee     :${seat_total:.2f}")
            print(f"Grand Total  :${grand_total:.2f}")

    elif choice == "4":
        if selected_movie == "" and seat_count == 0:
            print("No booking found!!")

        else:

            print("\n********RECEIPT********")
            print(f"Movie       :{selected_movie}")
            print(f"Movie Price :${movie[selected_movie]:.2f}")
            print(f"Row         :{selected_row}")
            print(f"Tickets     :{seat_count}")
            print(f"Seat Fee    :${seat_price:.2f}each")
            print("--------------------------")
            print(f"Movie Total :${movie_total:.2f}")
            print(f"Seat total  :${seat_total:.2f}")
            print(f"Grand Total :${grand_total:.2f}")
            print("*************************")

    elif choice == "5":
        again = input("Book Again? (y/n): ").lower()

        if again == "y":

            selected_movie = ""
            selected_row = ""
            seat_count = 0
            movie_total = 0
            seat_total = 0
            grand_total = 0

            print("Booking has been reset.")

        else:
            print("Thankyouu for booking!!")
            running = False

# to be continued tomorrow.......
#print(f"Char  :{chars}")
#print(f"Key   :{key}")

history = []
history1 = []

running = True

while running:
    print("\n*****WELCOME TO ENCRYPTED TEXT****")
    print("1. Encrypt Text")
    print("2. Decrypt Text")
    print("3. View History")
    print("4. Exit")
    print("************************************")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        import random
        import string

        chars = " " + string.whitespace + string.punctuation + string.digits + string.ascii_letters
        chars = list(chars)
        key = chars.copy()

        random.shuffle(chars)

        # ENCRYPT

        plain_text = input("Enter a message to encrypt: ")
        cipher_text = ""

        for letter in plain_text:
            index = chars.index(letter)
            cipher_text += key[index]
            history.append({
                "Original": plain_text,
                "Encrypted": cipher_text
                    })

        print(f"original text      :{plain_text}")
        print(f"Encrypted message  :{cipher_text}")


    elif choice == "2":
        import random
        import string

        chars = " " + string.whitespace + string.punctuation + string.digits + string.ascii_letters
        chars = list(chars)
        key = chars.copy()

        random.shuffle(chars)

        # DECRYPT

        cipher_text = input("Enter a message to decrypt: ")
        plain_text = ""

        for letter in cipher_text:
            index = key.index(letter)
            plain_text += chars[index]
            history1.append({
                    "Encrypted": cipher_text,
                    "Original": plain_text
                        })

        print(f"original text      :{cipher_text}")
        print(f"Encrypted message  :{plain_text}")


    elif choice == "3":
        if len(history) == 0 and len(history1) == 0:
            print("No transaction history!!")

        else:
            print("******HISTORY*******")
            for i in history:
                print(f"Original Text : {i['Original']}")
                print(f"Encrypted Text: {i['Encrypted']}")
                print("--------------------")
            for i in history1:
                print(f"Encrypted Text: {i['Encrypted']}")
                print(f"Original Text : {i['Original']}")
                print("--------------------")

    elif choice == "4":
        again = input("Text Again? (y/n): ").lower()

        if again != "y":
            print("Thankyouu for using my text game!!")
            running = False

    else:
        print("Invalid Choice!!")



# Practice

# hangman in python
import random

words = ("apple", "banana", "cherry", "date", "elderberry","grape", "honeydew")

#dictionary of key:()
hangman_art = { 0:("   ",
                   "   ",
                   "   "),
                1:(" o ",
                   "   ",
                   "   "),
                2:(" o ",
                   " | ",
                   "   "),
                3:(" o ",
                   "/|  ",
                   "   "),
                4:(" o ",
                   "/|\\",
                   "   "),
                5:(" o ",
                   "/|\\",
                   "/  "),
                6:(" o ",
                   "/|\\",
                   "/ \\")}

def display_man(wrong_guesses):
   print("***************")
   for line in hangman_art[wrong_guesses]:
      print(line)
   print("***************")

def display_hint(hint):
   print(" ".join(hint))

def display_answer(answer):
   print(" ".join(answer))

def main():
   answer = random.choice(words)
   hint = ["_"] * len(answer)
   wrong_guesses = 0
   guessed_letters = set()
   #answer = []
   running = True

   while running:
      display_man(wrong_guesses)
      display_hint(hint)
      guess = input("Enter a letter: ").lower()

      if len(guess) != 1 or not guess.isalpha():
         print('Invalid Input!!')
         continue

      if guess in guessed_letters:
         print(f"{guess} is already guessed!!")
         continue

      guessed_letters.add(guess)

      if guess in answer:
         for i in range(len(answer)):
            if answer[i] == guess:
               hint[i] = guess

      else:
         wrong_guesses += 1

      if "_" not in hint:
         display_man(wrong_guesses)
         display_answer(answer)
         print("**************")
         print("YOU WON!!")
         print("**************")

         again = input("Play again? (y/n): ").lower()

         if again != "y":
            print("Thanks for playing!!")
            running = False

      elif wrong_guesses >= len(hangman_art) - 1:
         display_man(wrong_guesses)
         display_answer(answer)
         print("**************")
         print("YOU LOST!!")
         print("**************")

         again = input("Play again? (y/n): ").lower()
         
         if again != "y":
            print("Thanks for playing!!")
            running = False

if __name__ == "__main__":
    main()


# to be continued...........


""" 
import random
import numpy as np

list = ["*", "/", "|"]

comp = random.choice(list)

comp = comp * 5 

for i in comp:
    for j in i:
        for word in j:
            print(j + i, end=" ")   
            print(word)  

            """

# Calculator
"""
- Calculate
- Exit
"""
import os
import time

first_number = ""
operator = ""
second_number = ""
screen = ""
pattern = {
    1 : ["┌───┐", "│ * │", "└───┘"],
    2 : ["┌───┐", "│ / │", "└───┘"],
    3 : ["┌───┐", "│ + │", "└───┘"],
    4 : ["┌───┐", "│ - │", "└───┘"]
}

number = ["  1 "," 2 "," 3  ","4"]
number1= ["  5  ", "6", "  7  ", "8"]
number2 =[ "  9  ", "0", "  =  ", "E"]
#pattern = ([[["|", ]]])

symbols = []
running = True

print("Calculator will start in.............")
def timer(start, end):
    for x in range(start, end + 1):
        print(x)
        time.sleep(1)

    timer(0, 3)


while running:

        os.system("cls")

        print()
        print("********************")
        print("     CALCULATOR     ")        
        print("********************")
        print("┌──────────────────┐")
        print(f"│{screen:<18}│")
        print("└──────────────────┘")
        print()

        for i in range(3):
            for value in pattern.values():
                print(value[i], end="")
            print()

        for i in number:
            print(i, end = "  ")
        print()      

        for i in number1:
            print(i, end="  ")
        print()

        for i in number2:
            print(i, end="  ")
        print()

        choice = input("\nPress a button: ").upper()

        if choice.isdigit():
            screen += choice

            if operator == "":
                first_number += choice
            else:
                second_number += choice

        elif choice in ["*", "/", "+", "-"]:
            if first_number == "":
                print("Enter first number!!")

            elif operator != "":
                print("Operator already selected!!")

            else:
                operator = choice
                screen += choice

        elif choice == "=":
            if first_number == "" or operator == "" or second_number == "":
                print("ERROR!!")
            else:
                first_number = int(first_number)
                second_number = int(second_number)

                if operator == "*":
                    result = first_number * second_number
                elif operator == "/":
                    if second_number == 0:
                        print("ERROR: Division by zero is not allowed!!")
                        result = "Undefined"
                    else:
                        result = first_number / second_number
                elif operator == "+":
                    result = first_number + second_number
                elif operator == "-":
                    result = first_number - second_number

                screen = str(result)
                print(f"Result: {result}")
                first_number = str(result)
                operator = ""
                second_number = ""

        elif choice == "X":
            screen = ""
            first_number = ""
            operator = ""
            second_number = ""

        elif choice == "E":
            running = False

        else:
            print("ERROR!!")


"""
Student Management System

"""

# Student Management System

"""
- log in as a student or teacher
- add student
- enter grade
- find average
- category
- extra find low and high score
"""

import pandas as pd

student_list = {
    "Student" : ["name"],
    "Math" : [99],
    "English" : [98],
    "Science" : [96],
    "Grades" : [98.50],
    "Category" : ["Passed"],
    "Highest" : [99],
    "Lowest"  : [96]
}



def log_in():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    position = input("Student or Teacher: ")

    if username == "" or password == "":
        print("Invalid Username/Password!!")

    elif len(username) > 14 and len(password) > 14:
        print("Username/Password must not be more than 14 characters!!")

    elif position != "Teacher" and position == "Student":
        print("This program is for teacher only!!")

    else:
        print("\n==================YOUR ACCOUNT======================")
        print(f"Welcome to Student Management System : {username}!!")
        print(f"Your password : {password}")
        print(f"Position : {position}")
        print("====================================================")



def add_student():
    result = pd.DataFrame(student_list)
    print("\n=================YOUR MANAGEMENT LIST=====================")
    print("Guide List : ")
    print(result)
    print("============================================================\n")
        
    while True:
        add_student = input("Enter student name (press s to stop): ").strip()

        if add_student.isdigit():
            print("Name must be letters!!")

        elif add_student == "s":
            break

        else:
            print("Student added sucessfully!!")
            while True:
                try:
                    math_grade = input("Enter math grade : ")

                    if not math_grade.isdigit():
                        print("Grade should be numbers!!")
                        continue

                    elif math_grade == "":
                        print("You haven't entered yet!!")
                        continue

                    elif int(math_grade) < 0 or int(math_grade) > 100:
                        print("Grade should be between 0 and 100!!")
                        continue

                    else:
                        print("Math grade added sucessfully!!")
                        break

                except ValueError:
                    print("Invalid input. Please enter a valid number for the math grade.")

            while True:
                try:
                    english_grade = input("Enter english grade : ")

                    if not english_grade.isdigit():
                        print("Grade should be numbers!!")
                        continue

                    elif english_grade == "":
                        print("You haven't entered yet!!")
                        continue

                    elif int(english_grade) < 0 or int(english_grade) > 100:
                        print("Grade should be between 0 and 100!!")
                        continue

                    else:
                        print("English grade added sucessfully!!")
                        break
                except ValueError:
                    print("Invalid input. Please enter a valid number for the english grade.")

            

                    print("Added sucessfuly!!")

            while True: 
                try:
                    
                    science_grade = input("Enter science grade : ")

                    if not science_grade.isdigit():
                        print("Grade should be numbers!!")
                        continue

                    elif science_grade == "":
                        print("You haven't entered yet!!")
                        continue

                    elif int(science_grade) < 0 or int(science_grade) > 100:
                        print("Grade should be between 0 and 100!!")
                        continue

                    else:
                        print("Science grade added sucessfully!!")
                        break
                except ValueError:
                    print("Invalid input. Please enter a valid number for the science grade.")

            # Average

            print("Math Grade : ", math_grade)
            print("English Grade : ", english_grade)
            print("Science Grade : ", science_grade)

            average = (
                int(math_grade) +
                int(english_grade) +
                int(science_grade)
            ) / 3

            print(f"Average : {average:.2f}")

            # Category
            if average >= 95:
                category = "Excellent"
                print(f"Category : {category}")
                print("Student Passed!!")

            elif average >= 90:
                category = "Very Good"
                print(f"Category : {category}")
                print("Student Passed!")

            elif average >= 80:
                category = "Good"
                print(f"Category : {category}")
                print("Student Passed!!")

            elif average >= 75:
                category = "Fair"
                print(f"Category : {category}")
                print("Student Passed!!")

            else:
                category = "Poor"
                print(f"Category : {category}")
                print("Student Failed!!")

            # High and Low Grades
            high = max(math_grade, english_grade, science_grade)
            low = min(math_grade, english_grade, science_grade)

            print(f"High : {high}")
            print(f"Low : {low}")

            # Add Student to List
            student_list["Student"].append(add_student)
            student_list["Math"].append(int(math_grade))
            student_list["English"].append(int(english_grade))
            student_list["Science"].append(int(science_grade))
            student_list["Grades"].append(average)
            student_list["Category"].append(category)
            student_list["Highest"].append(high)
            student_list["Lowest"].append(low)

            print("Student Added Sucessfully!!")

def search_student():
    result = pd.DataFrame(student_list)
    print("\n=================YOUR MANAGEMENT LIST=====================")
    print("Guide List : ")
    print(result)
    print("============================================================\n")

    while True:
        search_student = input("Enter student name to search (press s to stop): ").strip()

        if search_student.isdigit():
            print("Name must be letters!!")

        elif search_student == "s":
            break

        elif search_student not in student_list["Student"]:
            print("Student not found!!")

        else:
            index = student_list["Student"].index(search_student)
            math_grade = student_list["Math"][index]
            english_grade = student_list["English"][index]
            science_grade = student_list["Science"][index]
            average_grade = (math_grade + english_grade + science_grade) / 3
            print(f"Student: {search_student}")
            print(f"Math Grade: {math_grade}")
            print(f"English Grade: {english_grade}")
            print(f"Science Grade: {science_grade}")
            print(f"Average Grade: {average_grade}")
            print(f"Category: {student_list['Category'][index]}")

def delete_student():
    result = pd.DataFrame(student_list)
    print("\n=================YOUR MANAGEMENT LIST=====================")
    print("Guide List : ")
    print(result)
    print("============================================================\n")

    while True:
        delete_student = input("Enter student name to delete (press s to stop): ").strip()

        if delete_student.isdigit():
            print("Name must be letters!!")

        elif delete_student == "s":
            break

        elif delete_student not in student_list["Student"]:
            print("Student not found!!")

        else:
            index = student_list["Student"].index(delete_student)
    
            for key in student_list.keys():
                student_list[key].pop(index)
            print(f"Student {delete_student} list deleted successfully!!")

def view_list():
    print("\n=====================YOUR MANAGEMENT SYSTEM PROGRAM======================")
    result = pd.DataFrame(student_list)
    print(result)
    print("==========================================================================")

def exit():
    while True:
        again = input("Are you sure you want to exit? (y/n): ").lower()
        if again == "y":
            print("Exiting the program...")
            global running
            running = False
            break

        elif again == "n":
            continue


running  = True

while running:
    print("\n=================STUDENT MANAGEMENT SYSTEM=====================")
    print("1. Log in")
    print("2. Add Student")
    print("3. Search Student")
    print("4. delete Student")
    print("5. View Management List")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        log_in()

    elif choice == "2":
        add_student()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        view_list()

    elif choice == "6":
        exit()






    
