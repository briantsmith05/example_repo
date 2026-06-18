
operation = input("Enter an operation (+, -, *, /): ")
if operation not in ["+", "-", "*", "/"]:
    print("Error: Invalid operation. Please enter one of +, -, *, or /.")
    exit()
num1 = float(input("Enter the first number: "))

num2 = float(input("Enter the second number: "))





def calculate(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation ==  "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operation."
    
result = calculate(operation, num1, num2)

#file not found error handling
try:
    with open("equation.txt", "a") as file:
        result = calculate(operation, num1, num2)
        file.write(f"{num1} {operation} {num2} = {result}\n")
        print(f"The result of {num1} {operation} {num2} is: {result}")
except FileNotFoundError:
        print("Error: The file was not found.")
        

    

try:
    with open("equation.txt", "r") as file:
        for i in file:
            print(i)
except FileNotFoundError:
        print("Error: The file was not found.")
