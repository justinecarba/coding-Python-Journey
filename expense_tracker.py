


# Expense Tracker
"""
- Add Expense
- View Expense
- Search Expense
- Delete Expense
- Show Expense
- Show Remaining Expense
- Exit
"""

import pandas as pd
import numpy as np
from datetime import datetime

user_budget = 0
df = pd.DataFrame(columns = ["ID", "Expense", "Category", "Amount", "Date"])

def add_budget():
    global user_budget

    try:
        budget = int(input("Enter your budget : "))
    except ValueError:
        print("Budget should be a number!!")
        return
    
    if int(budget) <= 0:
        print("Invalid Budget!!")

    else:
        user_budget += budget

        print("\n========YOUR TOTAL BUDGET=========")
        print(f"Your total budget            : {user_budget}")
        print("==================================")

def add_expense():
    global df
    global user_budget

    print("\n================AVAILABLE EXPENSES==================")
    print(df.to_string())
    print("======================================================")

    add = input("Add Expenses? (Y/n) : ").strip().lower()

    if add == "n":
        print("Decline successfully!")

    elif add == "y":

        while True:

            if user_budget <= 0:
                print("Cannot add expense due to low budget!!")
                break

            adding_expense = input("Enter expenses : ").strip()
            adding_category = input("Enter category : ").strip()

            try:
                adding_amount = float(input("Enter amount: "))
            except ValueError:
                print("Amount should be a number, not words!")
                continue

            date = datetime.now().strftime("%Y-%m-%d")

            if adding_expense == "" or adding_category == "":
                print("You haven't entered yet, make sure to check!!")
                continue

            elif adding_expense.isdigit():
                print("Expense should be a name, not a number!")
                continue

            elif adding_category.isdigit():
                print("Category should be a name of your expense!")
                continue

            remaining_budget = user_budget - df["Amount"].sum()

            if adding_amount <= 0:
                print("Amount must be greater than 0!")
                continue

            elif adding_amount > remaining_budget:
                print(f"Expense is greater than your remaining budget!")
                print(f"Remaining budget: {remaining_budget}")
                continue

            else:
                df.loc[len(df)] = [
                    len(df) + 1,
                    adding_expense,
                    adding_category,
                    adding_amount,
                    date
                ]

                print("Added Successfully!!")
                print("Date : ", date)

                print("\n====== YOUR ADDED EXPENSE ======")
                print(df)
                print("===============================")

                again = input("Add again? (Y/n) : ").strip().lower()

                if again == "n":
                    break

def view_expense():
    global df
    global user_budget
    print("\n********************************************")
    print("                 YOUR EXPENSES              ")
    print("********************************************")
    print(df)
    print("********************************************")

def search_expense():
    global df
    global user_budget
    search = input("Search Expense: ").strip()

    if search in df['Expense'].values:
        product = df[df['Expense'] == search]
        print(product)

    else:
        print("Expense not found!!")

def delete_expense():
    global df

    print("\n********************************************")
    print("                 YOUR EXPENSES              ")
    print("********************************************")
    print(df)
    print("********************************************")

    delete_expense = input("\nEnter an expense to delete: ").strip()

    if delete_expense in df["Expense"].values:

        again = input("You sure to delete this expense? (Y/n): ").strip().upper()

        if again == "Y":

            df = df.loc[df["Expense"] != delete_expense].reset_index(drop=True)

            print("Remove Successfully!!")

            print("\n********************************************")
            print("                  YOUR EXPENSES             ")
            print("********************************************")
            print(df)
            print("********************************************")

        else:
            print("Cancelled Successfully!!")

    else:
        print("Expense not found!!")

        print("\n********************************************")
        print("                  YOUR EXPENSES             ")
        print("********************************************")
        print(df)
        print("********************************************")

def show_total_expense():
    global user_budget
    total = df["Amount"].sum()

    print("\n======== TOTAL EXPENSES ========")
    print(f"Total Expenses : ₱{total:.2f}")
    print("===============================")

def remaining_expense():
    global user_budget
    total = df["Amount"].sum()
    remaining_budget = user_budget - total

    print("\n======== REMAINING BUDGET ========")
    print(f"Budget           : ₱{user_budget:.2f}")
    print(f"Total Expenses   : ₱{total:.2f}")
    print(f"Remaining Budget : ₱{remaining_budget:.2f}")
    print("==================================")

    if remaining_budget < 0:
        print("Warning!! You have exceeded your budget!")

    elif remaining_budget == 0:
        print("Warning!! Your budget is already ₱0!")

    elif remaining_budget < 10:
        print(f"Reminder!! Your remaining budget is only ₱{remaining_budget:.2f}.")

    else:
        print("You still have a remaining budget!")       

def exit():
    while True:
        again = input("Exit? (Y/n) : ").strip() .title()

        if again == "Y":
            print("Exiting the program....")
            break

        elif again == "n":
            continue

        else:
            print("Choose Y/n only!!")
        

running = True

while running:
    print("\n*******************************************")
    print("                EXPENSE TRACKER            ")
    print("*******************************************")
    print("1. Add Budget")
    print("2. Add Expense")
    print("3. View Expense")
    print("4. Search Expense")
    print("5. Delete Expense")
    print("6. Show Total Expense")
    print("7. Show Remaining Expense")
    print("8. Exit")
    print("*******************************************")

    choice = input("\n Enter your choice (1-8) : ")

    if choice == "1":
        add_budget()

    elif choice == "2":
        add_expense()

    elif choice == "3":
        view_expense()

    elif choice == "4":
        search_expense()

    elif choice == "5":
        delete_expense()

    elif choice == "6":
        show_total_expense()

    elif choice == "7":
        remaining_expense()

    elif choice == "8":
        exit()
        running = False

    else:
        print("Invalid Choice!!")