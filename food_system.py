"""
Online food delivery system.

The program allows the user to:
- Display a menu of food items with prices.
- Add food items to a cart.
- Change the quantity of an item in the cart.
- Remove an item from the cart.
- View the current cart.
- Calculate the subtotal.
- Apply a discount code.
- Add a delivery fee.
- Checkout and calculate the final total.
- Accept a payment amount and calculate the change.
- Display an order receipt.
- Exit the program.
"""


class FoodDeliverySystem:
    def __init__(self):
        self.menu = {
            "Burger": 5.99,
            "Pizza": 8.99,
            "Salad": 4.99,
            "Soda": 1.99,
            "Fries": 2.99,
        }
        self.cart = {}
        self.discount_code = None
        self.delivery_fee = 3.00

    def display_menu(self):
        print("\n===============================")
        print("         FOOD MENU             ")
        print("===============================")
        for item, price in self.menu.items():
            print(f"{item:<10} : ${price:.2f}")
        print("===============================")

    def add_to_cart(self, item, quantity):
        item_name = item.strip().title()

        if item_name not in self.menu:
            print("\nThis item is not in the menu.")
            return False

        if quantity <= 0:
            print("\nQuantity must be greater than zero.")
            return False

        self.cart[item_name] = self.cart.get(item_name, 0) + quantity
        print(f"\n{quantity} {item_name}(s) added to the cart successfully!")
        return True

    def change_quantity(self, item, quantity):
        item_name = item.strip().title()

        if item_name not in self.cart:
            print(f"\n{item_name} is not in the cart.")
            return False

        if quantity <= 0:
            self.remove_from_cart(item_name)
            return True

        self.cart[item_name] = quantity
        print(f"\nQuantity of {item_name} changed to {quantity}.")
        return True

    def remove_from_cart(self, item):
        item_name = item.strip().title()

        if item_name not in self.cart:
            print(f"\n{item_name} is not in the cart.")
            return False

        del self.cart[item_name]
        print(f"\n{item_name} removed from the cart.")
        return True

    def view_cart(self):
        if not self.cart:
            print("\nYour cart is empty.")
            return

        print("\n===============================")
        print("         CURRENT CART          ")
        print("===============================")
        for item, quantity in self.cart.items():
            item_total = self.menu[item] * quantity
            print(f"{item:<10} x {quantity:<2} : ${item_total:.2f}")
        print("===============================")

    def calculate_subtotal(self):
        subtotal = sum(self.menu[item] * quantity for item, quantity in self.cart.items())
        return subtotal

    def apply_discount(self, code):
        code = code.strip().upper()

        if code == "DISCOUNT10":
            self.discount_code = code
            print("\nDiscount code applied successfully!")
            return True

        print("\nInvalid discount code.")
        return False

    def calculate_total(self):
        subtotal = self.calculate_subtotal()
        discount = 0.10 * subtotal if self.discount_code == "DISCOUNT10" else 0
        total = subtotal - discount + self.delivery_fee
        return total

    def display_order_receipt(self, payment_amount=None, change=None):
            subtotal = self.calculate_subtotal()
            discount = 0.10 * subtotal if self.discount_code == "DISCOUNT10" else 0
            total = subtotal - discount + self.delivery_fee
    
            print("\n===============================")
            print("         ORDER RECEIPT         ")
            print("===============================")
            for item, quantity in self.cart.items():
                item_total = self.menu[item] * quantity
                print(f"{item:<10} x {quantity:<2} : ${item_total:.2f}")
            print("===============================")
            print(f"Subtotal        : ${subtotal:.2f}")
            if self.discount_code == "DISCOUNT10":
                print(f"Discount        : -${discount:.2f}")
            print(f"Delivery Fee    : ${self.delivery_fee:.2f}")
            print(f"Total           : ${total:.2f}")
    
            if payment_amount is not None:
                print(f"Payment Amount  : ${payment_amount:.2f}")
            if change is not None:
                print(f"Change          : ${change:.2f}")
    
            print("===============================")

    def checkout(self, payment_amount):
        if not self.cart:
            print("\nYour cart is empty. Add items before checkout.")
            return False

        total = self.calculate_total()

        if payment_amount < total:
            print("\nInsufficient payment amount.")
            return False

        change = payment_amount - total
        self.receive_receipt(payment_amount, change)
        self.cart.clear()
        self.discount_code = None
        return True
    
    def receive_receipt(self, payment_amount, change):
        self.display_order_receipt(payment_amount, change)
        print("\nThank you for your order! Your receipt has been generated.")

    def exit_program(self):
        print("\nExiting the program. Thank you for using our food delivery system!")
        raise SystemExit


def main():
    store = FoodDeliverySystem()

    while True:
        print("\n===============================")
        print("   ONLINE FOOD DELIVERY SYSTEM ")
        print("===============================")
        print("1. Display menu")
        print("2. Add item to cart")
        print("3. Change quantity")
        print("4. Remove item")
        print("5. View cart")
        print("6. Apply discount")
        print("7. Checkout")
        print("8. Receive receipt")
        print("9. Exit")
        print("================================")

        choice = input("\nChoose an option (1-9): ").strip()

        if choice == "1":
            store.display_menu()

        elif choice == "2":
            item = input("Enter the item name: ")
            quantity = int(input("Enter the quantity: "))
            store.add_to_cart(item, quantity)

        elif choice == "3":
            item = input("Enter the item name: ")
            quantity = int(input("Enter the new quantity: "))
            store.change_quantity(item, quantity)

        elif choice == "4":
            item = input("Enter the item name to remove: ")
            store.remove_from_cart(item)

        elif choice == "5":
            store.view_cart()

        elif choice == "6":
            code = input("Enter the discount code: ")
            store.apply_discount(code)

        elif choice == "7":
            if not store.cart:
                print("\nYour cart is empty.")
                continue

            print(f"\nSubtotal: ${store.calculate_subtotal():.2f}")
            payment_amount = float(input("Enter payment amount: $"))

            if payment_amount < store.calculate_total():
                print("\nInsufficient payment amount.")
                continue

            elif payment_amount > store.calculate_total():
                change = payment_amount - store.calculate_total()
                print(f"\nChange to be returned: ${change:.2f}")

            else:
                print("\nPayment amount is exact. No change to return.")
                store.checkout(payment_amount)

        elif choice == "8":
            store.receive_receipt(payment_amount, change)
            
        elif choice == "9":
            store.exit_program()
            
        else:
            print("\nInvalid option. Please choose a number from 1 to 9.")


if __name__ == "__main__":
    main()

