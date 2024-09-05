import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def exponentiate(x, y):
    return x ** y

def modulus(x, y):
    return x % y

def square_root(x):
    if x < 0:
        return "Error! Cannot take the square root of a negative number."
    return math.sqrt(x)

def display_menu():
    print("\nAvailable operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiate")
    print("6. Modulus")
    print("7. Square Root")
    print("8. Exit")

def main():
    history = []

    while True:
        display_menu()
        choice = input("Choose an operation (1-8): ")

        if choice == '8':
            print("Exiting the calculator!")
            break

        if choice in ['1', '2', '3', '4', '5', '6']:
            try:
                n = float(input("Enter the first number: "))
                m = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid input! Please enter numerical values.")
                continue

        if choice == '1':
            result = add(n, m)
            operation = "add"
        elif choice == '2':
            result = subtract(n, m)
            operation = "subtract"
        elif choice == '3':
            result = multiply(n, m)
            operation = "multiply"
        elif choice == '4':
            result = divide(n, m)
            operation = "divide"
        elif choice == '5':
            result = exponentiate(n, m)
            operation = "exponentiate"
        elif choice == '6':
            result = modulus(n, m)
            operation = "modulus"
        elif choice == '7':
            try:
                n = float(input("Enter the number for square root: "))
                result = square_root(n)
                operation = "square root"
                # Store the result in history without needing a second number
                history.append(f"{operation.capitalize()} of {n} is: {result}")
            except ValueError:
                print("Invalid input! Please enter a numerical value.")
                continue
        else:
            print("Invalid choice! Please select a valid operation.")
            continue

        # For operations that require two numbers, store history with both n and m
        if choice in ['1', '2', '3', '4', '5', '6']:
            history.append(f"{operation.capitalize()} of {n} and {m} is: {result}")

        # Display history
        print("\nCalculation History:")
        for entry in history:
            print(entry)

if __name__ == "__main__":
    main()
