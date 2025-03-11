import math

'''
Add Ons
-------
-Basic Calc
-Calc Calc
-Discrete Math Calc
-Programming Calc

Basic: add, subtract, etc.
Calc: Derivitaves, integrals, limits, etc.
Discrete: propositions, predicates
Programming: convert between types

Why not use AI? If you get an answer but need and explanations, the AI can do that for you maybe?
OpenAi, Deepseek, etc. 
Deepseek does use Python... they are also open source.
Objective: Look in Deepseek

Also have a more detailed list (.txt) in the folder that does teh work
Each calculator type needs to have a file. 
'''

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

def square_root(x):
    if x < 0:
        return "Error! Cannot take the square root of a negative number."
    return math.sqrt(x)

def power(x, y):
    return math.pow(x, y)

def calculator():
    print("Welcome to the Python Calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Power")

    while True:
        choice = input("Enter choice (1/2/3/4/5/6) or 'q' to quit: ")

        if choice == 'q':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5', '6']:
            if choice in ['1', '2', '3', '4', '6']:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            elif choice == '5':
                num = float(input("Enter number: "))
                print(f"Square root of {num} = {square_root(num)}")
            elif choice == '6':
                print(f"{num1} ^ {num2} = {power(num1, num2)}")
        else:
            print("Invalid input. Please enter a valid choice.")

if __name__ == "__main__":
    calculator()
