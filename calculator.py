# Instructions:
# Define a function named calculator that accepts three parameters: num1, num2, and operation.
# The function should support the following operations:
# Addition (+)
# Subtraction (-)
# Multiplication (*)
# Division (/)
# Use conditional statements to execute the corresponding arithmetic operation based on the input.
# Return the result of the calculation.
# Call the function with different values to test its functionality.
# Example Input & Output:
# print(calculator(10, 5, '+'))  # Output: 15
# print(calculator(8, 2, '/'))   # Output: 4.0

def calculator(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        return "Invalid operation"

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Enter the operation: ")

print(calculator(num1, num2, operation))

# print(calculator(10, 5, '+'))  # Output: 15
# print(calculator(8, 2, '/'))   # Output: 4.0