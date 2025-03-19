import math

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
    return x ** (1/2)

def exp(x, terms=100):
    result = 1.0
    term = 1.0
    for n in range(1, terms):
        term *= x / n
        result += term
    return result

def ln(x, terms=100):
    if x <= 0:
        raise ValueError("Input must be greater than 0.")
    result = 0.0
    y = (x - 1) / (x + 1)
    y_squared = y * y
    for n in range(1, terms):
        result += (1 / (2 * n - 1)) * (y ** (2 * n - 1))
    return 2 * result

def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def sin(x, terms=10):
    sine = 0
    for n in range(terms):
        sign = (-1) ** n
        sine += sign * (x ** (2 * n + 1)) / factorial(2 * n + 1)
    return sine

def sin(x, terms=10):
    sine = 0
    for n in range(terms):
        sign = (-1) ** n  # Alternating sign
        sine += sign * (x ** (2 * n + 1)) / factorial(2 * n + 1)
    return sine

def cos(x, terms=10):
    cosine = 0
    for n in range(terms):
        sign = (-1) ** n
        cosine += sign * (x ** (2 * n)) / factorial(2 * n)
    return cosine

def tan(x, terms=10):
    cosine_value = cos(x, terms)
    if cosine_value == 0:
        raise ValueError("Tangent is undefined for this value of x (cos(x) = 0).")
    return sin(x, terms) / cosine_value

def arcsin(x, terms=10):
    if x < -1 or x > 1:
        raise ValueError("Input must be in the range [-1, 1].")
    arcsine = 0
    for n in range(terms):
        sign = (-1) ** n
        arcsine += sign * (factorial(2 * n) * (x ** (2 * n + 1))) / (4 ** n * (factorial(n) ** 2) * (2 * n + 1))
    return arcsine

def arccos(x, terms=10):
    if x < -1 or x > 1:
        raise ValueError("Input must be in the range [-1, 1].")
    
    return (math.pi / 2) - arcsin(x, terms)

def arctan(x, terms=10):
    arctangent = 0
    for n in range(terms):
        sign = (-1) ** n
        arctangent += sign * (x ** (2 * n + 1)) / (2 * n + 1)
    return arctangent

def sinh(x):
    return (exp(x) - exp(-x)) / 2

def cosh(x):
    return (exp(x) + exp(-x)) / 2

def tanh(x):
    return sinh(x) / cosh(x)

def arcsinh(x):
    return ln(x + (x**2 + 1)**0.5)

def arccosh(x):
    if x < 1:
        raise ValueError("Input must be greater than or equal to 1.")
    return ln(x + (x**2 - 1)**0.5)

def arctanh(x):
    if x <= -1 or x >= 1:
        raise ValueError("Input must be in the range (-1, 1).")
    return 0.5 * ln((1 + x) / (1 - x))

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
