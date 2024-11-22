import math

def calculator():
    print("Simple Calculator")
    print("Type 'quit' to exit\n")

    while True:
        num1 = input("Enter the first number: ")
        if num1.lower() == 'quit':
            break
        operator = input("Enter an operator (+, -, *, /, sqrt): ")
        if operator.lower() == 'quit':
            break

        try:
            num1 = float(num1)
        except ValueError:
            print("Invalid number\n")
            continue

        if operator == 'sqrt':
            if num1 < 0:
                print("Cannot take the square root of a negative number\n")
                continue
            result = math.sqrt(num1)
        else:
            num2 = input("Enter the second number: ")
            if num2.lower() == 'quit':
                break
            try:
                num2 = float(num2)
            except ValueError:
                print("Invalid number\n")
                continue

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("Cannot divide by zero\n")
                    continue
                result = num1 / num2
            else:
                print("Invalid operator\n")
                continue

        print(f"Result: {result}\n")

if __name__ == "__main__":
    calculator()