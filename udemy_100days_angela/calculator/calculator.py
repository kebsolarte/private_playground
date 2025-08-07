import os

# create calculate function
# compressed math opeartions into one function
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    elif operation not in ['+', '-', '*', '/']:
        return "Invalid"

# main program
while True:
    num1 = float(input("What is the first number?: "))
    operation = input("Pick an operation (+, -, *, /): ")
    num2 = float(input("What is the second number?: "))
    result = calculate(num1, num2, operation)
    print(f"{num1} {operation} {num2} = {result}")

    # checks if user wants to continue using the result in downstream calculations
    while True:
        continue_calculation = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start new calculation or quit: ")
        
        if continue_calculation == 'y':
            num1 = result
            operation = input("Pick an operation (+, -, *, /): ")
            num2 = float(input("What is the second number?: "))
            result = calculate(num1, num2, operation)
            print(f"{num1} {operation} {num2} = {result}")
            continue
        elif continue_calculation == 'n': break
        else:
            print("Invalid answer!")
            continue
    
    # clears terminal if user wants to create a new thread or to quit
    os.system('cls' if os.name == 'nt' else 'clear')
    repeat = input("Type 'new' to start new calculation or 'quit' to quit?: ")

    if repeat == 'new': continue
    else: break
        


