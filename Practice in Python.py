
# BOOK STORE 
"""
- using def functions
"""
books = []

book = {
    "Drama" : 100.00,
    "Horror" : 110.00,
    "Comedy" : 120.00,
    "Romance" : 130.00
}
select = ""
total = 0

def view_book():
    print("**********************")
    print("       BOOK STORE     ")
    print("**********************")
    for key, value in book.items():
        print(f"{key.title():12} : {value:.2f}")
    print("***********************")

view_book()

def select_book():
    while True:

        select = input("Select a book (q to quit): ").strip() .title()

        if select == "q".title():
            break

        elif select not in book:
            print(f"{select} are not available!!")

        else:
            books.append(select)
            print("Thankyou for purchasing!!")    

select_book()

def buy_book():
    global total
    total = 0

    print("\n***********************************")
    print("             YOUR CART             ")
    print("***********************************")
    for item in books:
        print(f"{item.title():12}  : ${book[item]:.2f}")
        total += book[item]
    print("************************************")

    print(f"Total Payment:                ${total:.2f}")

    purchase = input("Do you want to purchase? (y/n): ").strip().lower()

    if purchase == "y":
        print("Thank you for purchasing!!")

    else:
        books.clear()
        total = 0
        print("Thank you for your interest!!")
           
buy_book()

def view_receipt():
    if not books:
        print("No Transactions!!")

    else:
        global total
        total = 0

        print("\n****************************")
        print("         YOUR RECEIPT       ")
        print("****************************")
        for item in books:
            print(f"{item.title():12}  : ${book[item]:.2f}")
            total += book[item]
        print("****************************")

        print(f"Total Payment:            :  ${total:.2f}")

view_receipt()

def exit():
    again = input('Exit? (y/n): ').strip().lower()

    if again == "y":
        books.clear()
        total = 0
        print("Thank you for choosing our book store!!")
        return True

    else:
        return False

exit()

"""
- I'll be finish this later!!
- Yupp Done!!
"""