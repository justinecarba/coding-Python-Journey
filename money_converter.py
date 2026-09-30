

"""
So, today we're gonna make a python program that can convert a money in dollar or in php
- supposed to be the exchange rate in php is 57.58
"""

# Money Converter

exchange_rate = 57.58

def php_to_usd():
    php_amount = float(input("Enter php amount : "))
    
    convert = php_amount / exchange_rate

    print(f"PHP AMOUNT      : $ {php_amount:.2f}")
    print(f"CONVERT TO USD  : $ {convert:.2f}")


def usd_to_php():
    
    usd_amount = float(input("Enter usd amount : $ "))

    convert_to_php = usd_amount * exchange_rate

    print(f"USD AMOUNT      : $ {usd_amount:.2f}")
    print(f"CONVERT TO PHP  : $ {convert_to_php:.2f}")


def exit_prog():
    again = input("Exit? Y/n : ").lower() .strip()
    
    if again == "Y" and again != "n":
        print("Exiting the program.....")
        running = False
        

running = True

while running:
    print("\nChoose converter : ")
    print("1. PHP to USD")
    print("2. USD to PHP")
    print("3. Exit")

    choice = input("\nEnter your choice (1-3) : ")

    if choice == "1":
        php_to_usd()

    elif choice == "2":
        usd_to_php()

    elif choice == "3":
        exit_prog()
        running = False

    else:
        print("Invalid Choice!!")





