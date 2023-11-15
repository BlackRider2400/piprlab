""" cheapcalc - a cheap terminal calculator """
import cheapcalc_tools


def main():
    """Runs cheapcalc"""
    print("Welcome to CheapCalc")

    operations = {
        "1": cheapcalc_tools.add,
        "2": cheapcalc_tools.subtract,
        "3": cheapcalc_tools.multiply,
        "4": cheapcalc_tools.divide,
    }

    while True:
        for choice, operation in operations.items():
            print(f"{choice}: {operation.__name__}")
        operation = input("Choose an operation: ")
        if operation not in operations:
            print("Invalid choice")
            continue

        num1, num2 = 0, 0
        while True:
            try:
                num1 = float(input("First operand: "))
                break
            except ValueError:
                print("Invalid Value")
        while True:
            try:
                num2 = float(input("Second operand: "))
                break
            except ValueError:
                print("Invalid Value")
        chosen_operation = operations[operation]
        try:
            print(chosen_operation(num1, num2))
        except ZeroDivisionError:
            print("Error, you can not divide by zero.")


if __name__ == "__main__":
    main()
