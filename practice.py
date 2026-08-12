
# Book Store
"""
- were gonna make a book store using while loops
- okay let's go!!
"""

books = []
total = 0
select = ""

book = {
    "Drama" : 100.00,
    "Comedy" : 110.00, 
    "Horror" : 120.00,
    "Romance" : 200.00
}

running = True

while running:
    print('**********************')
    print("      BOOK STORE      ")
    print("**********************")
    print("1. View Books")
    print("2. Select Books")
    print("3. Buy Books")
    print("4. View Receipts")
    print("5. Exit")
    print("**********************")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":

        print("*****************************")
        print("     JUSTINE BOOK STORE      ")
        print("*****************************")
        for key, value in book.items():
            print(f"{key.title():10} : ${value:.2f}")
        print("*****************************")

    elif choice == "2":

        while True:
            print("*****************************")
            print("     JUSTINE BOOK STORE      ")
            print("*****************************")
            for key, value in book.items():
                print(f"{key.title():10} : ${value:.2f}")
            print("*****************************")

            select = input("Select a book (q to quit): ").strip() .title()

            if select == "q".title():
                break

            elif select not in book:
                print(f"{select} are not available!!")

            else:
                books.append(select)
                print("Thankyou for selecting!")
                print("Buy your cart now!!")

    elif choice == "3":
        if select == "":
            print("No transactions!!")

        else:
            print("*******************")
            print("      YOUR CART    ")
            print("*******************")
            for item in books:
                print(f"{item.title():10} : ${book[item]:.2f}")
                total += book[item]

            print(f"Total Payment:  ${total:.2f}")
            print("*******************")

            buy = input("Checkout? (y/n): ").lower()

            if buy == "y":
                print("thankyou for purchasing!!")

            else:
                books.clear() and total - total
                print("Thankyou for your interest!!")
                running = False

    elif choice == "4":
        if select == "":
            print("No transaction History!!")

        else:
            print("***********************************")
            print("            YOUR RECIEPT           ")
            print("***********************************")
            for item in books:
                print(f"{item.title():15}   : ${book[item]:.2f}")
            print("***********************************")
            print(f"Total Payment                : ${total:.2f}")

    elif choice == "5":
        again = input('Exit? (y/n): ')

        if again == "y":
            books.clear() and total = 0
            print("Thankyouu for choosing our book store!!")
            running = False

        elif again != "y" and again == "n":
            books.clear()
            total - total

        else:
            print("press (y) for yes and (n) for no only!!")

    else:
        print("Invalid Choice!!")


