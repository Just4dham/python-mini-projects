def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y


def main():
    print("\n=== CLI Calculator ===")
    print("Available operations: +, -, *, /")

    while True:
        op = input(
            "\nSelect operation (+, -, *, /) or 'q' to quit: "
        ).strip()

        if op.lower() == "q":
            print("Exiting calculator. Goodbye!")
            break

        if op not in ["+", "-", "*", "/"]:
            print("❌ Invalid operation! Please enter +, -, *, or /.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("❌ Invalid input! Please enter numbers only.")
            continue

        if op == "+":
            result = add(num1, num2)
        elif op == "-":
            result = subtract(num1, num2)
        elif op == "*":
            result = multiply(num1, num2)
        elif op == "/":
            result = divide(num1, num2)

        print(f"\nResult: {num1} {op} {num2} = {result}")


if __name__ == "__main__":
    main()