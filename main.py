# MY OWN PROJECT
# 9. Banking System
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






    




















