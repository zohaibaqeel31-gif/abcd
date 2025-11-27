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

def perform_calculation():
    print("Available operations: +, -, *, /")
    
    result = None

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        op = input("Enter the operator (+, -, *, /): ")

        if op == '+':
            result = add(num1, num2)
        elif op == '-':
            result = subtract(num1, num2)
        elif op == '*':
            result = multiply(num1, num2)
        elif op == '/':
            result = divide(num1, num2)
        else:
            print("Error: Invalid operation.")
            return

    except ValueError:
        print("Error: Invalid input. Please enter only numerical values.")
        return
    
    if result is not None:
        print(f"Result is: {result}")

if __name__ == "__main__":
    perform_calculation()