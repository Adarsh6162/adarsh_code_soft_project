def calculate(num1, num2, operation):
    if operation == '1':
        return num1 + num2
    elif operation == '2':
        return num1 - num2
    elif operation == '3':
        return num1 * num2
    elif operation == '4':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Invalid operation "

# Display the menu
print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Get user input
num1 = float(input("Enter the your first number: "))
num2 = float(input("Enter the your second number: "))
operation = input("Enter your choice (1/2/3/4): ")

# Perform the calculation
result = calculate(num1, num2, operation)
# Display the result
if isinstance(result, str):
    print(result)
else:
    print("Result: ", result)