
"""
Student Management System
ATM Machine
Banking System
Library Management System
Inventory Management System
Expense Tracker
Contact Book
Hangman Game
Tic Tac Toe
Grocery Store POS
Hotel Reservation System
Cinema Booking System
Tkinter GUI Projects
Database (SQLite)
APIs
Flask
Django
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
    print("4. Delete Student")
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

    else:
        print("Invalid Choice!!")



# ATM Machine
"""
- we're gonna make a log in first!!
- we're gonna make a ATM machine
- we're gonna make user check balance
- Deposit
- Withdraw
- See Transaction
- Exit
"""



# but i think let's finish it tommorow because its 2:46 at madaling araw na!!
# Library Management System
"""
- we're gonna make a library which have a set of books that a user can buy
- we're gonna make it an online platform
- user should log in first to make account then store there account
- user can see available books
- user can add to cart
- user can search
- user can delete cart
- user can see the famous book
- user can check out of course
- then user can exit

"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

user_username = []
user_password = []
cart = {
    "Title" : [],
    "Price" : []
}


def log_in():
    while True:
        sign_up = input("Already have an account? (Y/N) : ").strip() .upper()

        if sign_up == "Y":
            username1 = input("Enter your username : ")
            password1 = input("Enter your password : ")

            if username1 == user_username and password1 == user_password:
                print("\nAccount checking......")
                print("Welcome to books store......")
                print("=========YOUR ACCOUNT=========")
                for i in user_username:
                    print(f"Username             :    {i}", end = "")
                print()
                for j in user_password:
                    print(f"Password             :    {j}", end = "")
                print()
                print("==============================")
                break

            else:
                print("Account not found!!")
                break

        elif sign_up == "N":
            
            log_in = input("You sure to want login? (Y/N) : ").strip() .upper()

            if log_in == "Y":
                username = input("Enter your username : ")
                password = input("Enter your password : ")

                if username == "" or password == "":
                    print("Username/Password haven't entered yet!!")

                elif len(username) < 0 and len(username) > 14:
                    print("Username must contain of atleats 5 to 14 characters!!")

                elif len(password) < 0 and len(password) > 14:
                    print("Password must contain of not more than 14 characters!!")

                else:
                    user_username.append(username)
                    user_password.append(password)
                    print("Log in sucessfuly!!")

                    print("\n===============YOUR ACCOUNT===============")
                    for i in user_username:
                        print(f"Username                             : {i}", end = "")
                    print()
                    for j in user_password:
                        print(f"Password                             : {j}", end = "")
                    print()
                    print("============================================")
                    break

            elif log_in == "N":
                break

            else:
                print("Invalid choice!!")
                

        else:
            print("Invalid choice!!")

def view_books():
    if not user_username and user_password:
        print("Login first!!")

    else:
        print("========AVAILABLE BOOKS=======")
        import pandas as pd

        df = pd.read_csv("books.csv")

        print(df.to_string())
        print("==============================")

def add_cart():

    import pandas as pd

    # Load books.csv
    df = pd.read_csv("books.csv")

    # Remove accidental spaces from column names
    df.columns = df.columns.str.strip()

    # Cart
    cart = {
        "Title": [],
        "Price": []
    }

    print("========AVAILABLE BOOKS=======")
    print(df.to_string(index=False))
    print("==============================")

    while True:

        add_to_cart = input(
            "Select item to add to cart (s to stop): "
        ).strip().lower()

        if add_to_cart == "":
            print("You haven't selected yet!!")

        elif add_to_cart == "s":
            break

        else:
            found = False

            # ANIME
            for i in range(len(df)):

                if str(df.loc[i, "Anime"]).strip().lower() == add_to_cart:

                    cart["Title"].append(df.loc[i, "Anime"])
                    cart["Price"].append(df.loc[i, "Price"])

                    found = True
                    break

                # HORROR
                elif str(df.loc[i, "Horror"]).strip().lower() == add_to_cart:

                    cart["Title"].append(df.loc[i, "Horror"])
                    cart["Price"].append(df.loc[i, "Price.1"])

                    found = True
                    break

                # COMEDY
                elif str(df.loc[i, "Comedy"]).strip().lower() == add_to_cart:

                    cart["Title"].append(df.loc[i, "Comedy"])
                    cart["Price"].append(df.loc[i, "Price.2"])

                    found = True
                    break

                # LOVE STORY
                elif str(df.loc[i, "Love Story"]).strip().lower() == add_to_cart:

                    cart["Title"].append(df.loc[i, "Love Story"])
                    cart["Price"].append(df.loc[i, "Price.3"])

                    found = True
                    break

            if found:

                print("\n=================YOUR CART================")

                cart_df = pd.DataFrame(cart)

                print(cart_df.to_string(index=False))

                print("==========================================")
                print("Add to cart successfully!!")

            else:
                print("Book not found!!")

def search_books():

    if not user_username and user_password:
        print("Login first!!")
        return

    else:
        df = pd.read_csv("books.csv")
        df.columns = [col.strip() for col in df.columns]

        print("========AVAILABLE BOOKS=======")
        print(df.to_string(index=False))
        print("==============================")

        while True:
            search = input("Search book (s to stop): ").strip().lower()

            if search == "":
                print("You haven't selected yet!!")

            elif search == "s":
                break

            else:
                found = False
                title_columns = ["Anime", "Horror", "Comedy", "Love Story"]

                for title_col in title_columns:
                    matches = df[df[title_col].astype(str).str.strip().str.lower().str.contains(search, na=False)]

                    if not matches.empty:
                        print("\n=================BOOK FOUND================")
                        print(matches.to_string(index=False))
                        print("========================================")
                        found = True
                        break

                if not found:
                    print("Book not found!!")

def view_famous():
    import matplotlib.pyplot as plt
    import numpy as np

    x = np.array(["Anime", "Horror", "Comedy", "Love Story"])
    y = np.array([98, 80, 80, 90])

    font1 = {"family" : "serif", "color" : "#1f3e53", "size" : "20"}
    font2 = {"family" : "arial", "color" : "#2298e7", "size" : "10"}

    plt.title("FAMOUS BOOKS", loc = "center", fontdict = font1)
    plt.xlabel("BOOKS", fontdict = font2)
    plt.ylabel("RATING", fontdict = font2)
    plt.bar(x, y)
    plt.show()

def buy_books():
    global cart

    if not user_username and user_password:
        print("Login first!!")
        return

    if not cart["Title"]:
        print("Empty cart!!")
        return

    total = sum(cart["Price"])
    print("\n================YOUR CART====================")
    print(pd.DataFrame(cart).to_string(index=False))
    print(f"Total Price: {total}")
    print("==============================================")
    print("Purchase successful!!")

    cart["Title"].clear()
    cart["Price"].clear()

    

def exit():
    while True:
        again = input("Exit? (Y/N) : ").strip() .upper()

        if again == "Y":
            print("Exiting the program......")
            break

        else:
            continue

running = True

while running:
    print("********************************************")
    print("          LIBRARY MANAGEMENT SYSTEM         ")
    print("********************************************")
    print("1. Log in")
    print("2. View Books")
    print("3. Add to cart")
    print("4. Search Books")
    print("5. View Famous Books")
    print("6. Buy Books")
    print("7. Exit")

    choice = input("Enter your choice (1-7) : ")

    if choice == "1":
        log_in()

    elif choice == "2":
        view_books()

    elif choice == "3":
        add_cart()

    elif choice == "4":
        search_books()

    elif choice == "5":
        view_famous()

    elif choice == "6":
        buy_books()

    elif choice == "7":
        exit()
        running = False

    else:
        print("Invalid Choice!!")