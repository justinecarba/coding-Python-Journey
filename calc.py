
class Calculator:
    def add(self, first_num, second_num):
        return first_num + second_num

    def multiply(self, first_num, second_num):
        return first_num * second_num

    def division(self, first_num, second_num):
        if second_num == 0:
            raise ValueError("Cannot divide by zero.")
        return first_num / second_num

    def subtraction(self, first_num, second_num):
        return first_num - second_num


def main():
    print("\n=========== WELCOME TO JUSTINE CALCULATOR ===========")
    first_num = float(input("Enter the first number: "))
    second_num = float(input("Enter the second number: "))
    operation = input("Choose an operation (+, -, *, /): ").strip()

    calculator = Calculator()
    operations = {
        "+": calculator.add,
        "-": calculator.subtraction,
        "*": calculator.multiply,
        "/": calculator.division,
    }

    if operation not in operations:
        print("Invalid operation.")
        return

    try:
        print(f"Result: {operations[operation](first_num, second_num)}")
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()