def divide(a, b):
    try:
        result = a / b
        print("Result of division:", result)
    except ZeroDivisionError:
        print("Error: Division by zero!")

# Example usage:
num1 = 10
num2 = 0

divide(num1, num2)
