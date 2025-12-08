history = []

def calculate(num1, num2, op):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Invalid operator"

def print_history():
    if not history:
        print("\nNo history available")
    else:
        print("\n----- Calculation History -----")
        for i, entry in enumerate(history, start=1):
            print(f"{i}. {entry}")
        print("-------------------------------")

while True:
    print("\nSimple Calculator")
    print("1. Calculate")
    print("2. Show History")
    print("3. Clear History")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        try:
            num1 = float(input("Enter first number: "))
            op = input("Choose operation (+ - * /): ")
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Try again.")
            continue

        result = calculate(num1, num2, op)
        print(f"Result: {result}")

        history.append(f"{num1} {op} {num2} = {result}")

    elif choice == "2":
        print_history()

    elif choice == "3":
        history.clear()
        print("History cleared!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
