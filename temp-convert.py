
# Define a function named convert_temperature that accepts two parameters: value and unit.
# If the unit is 'C', convert the temperature to Fahrenheit using the formula:
# F = (C * 9/5) + 32
# If the unit is 'F', convert the temperature to Celsius using the formula:
# C = (F - 32) * 5/9
# Return the converted temperature rounded to two decimal places.
# Call the function with different values to test its functionality.
# Example Input & Output:
# print(convert_temperature(100, 'C'))  # Output: 212.0
# print(convert_temperature(32, 'F'))   # Output: 0.0

def convert_temperature(value, unit):
    if unit == 'C':
        return (value * 9/5) + 32
    elif unit == 'F':
        return (value - 32) * 5/9
    else:
        return "Invalid unit"

value = int(input("Enter a number: "))
unit = input("Enter the unit: ")    

print(convert_temperature(value, unit))

# print(convert_temperature(100, 'C'))  # Output: 212.0
# print(convert_temperature(32, 'F'))   # Output: 0.0

