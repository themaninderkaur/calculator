import math
import statistics

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def power(base, exponent):
    return base ** exponent

def sqrt(x):
    return math.sqrt(x)

def sin(angle):
    return math.sin(angle)

def cos(angle):
    return math.cos(angle)

def tan(angle):
    return math.tan(angle)

def ln(x):
    return math.log(x)

def log10(x):
    return math.log10(x)

def mean(data):
    return statistics.mean(data)

# Add more functions as needed...
