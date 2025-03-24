# Calculator

**Goal**: Around the time that I started my freshman year in college, I realized just how little I remembered the math from my high school days. Therefore, I had the idea to manually code out the math for a multi-functional calculator that ranges from basic arithmatic to advanced calculus.
Because of my slow decrease in understanding even the most basic math operations, I gave myself a challenge: code a calculator using Python and manually do every single math operation using pure math to fully grasp the concepts. Some were simple enough such as arithmatic. Other like equation solvers were a bit more complex. The most difficult was concepts I never fully undertsood, but simply accepted, such as Trig. identities and hyperbolic function. 

## Overview

This is a simple command-line calculator implemented in Python. It supports basic arithmetic operations, logarithmic functions, trigonometric functions, and hyperbolic functions. The calculator is designed to demonstrate mathematical concepts and provide a user-friendly interface for performing calculations.

## Features

- **Basic Operations**: Addition, subtraction, multiplication, and division.
- **Square Root**: Calculate the square root of a number.
- **Exponential and Logarithmic Functions**: Calculate natural logarithm, base 10 logarithm, and logarithm with any base.
- **Trigonometric Functions**: Calculate sine, cosine, tangent, and their inverse functions (arcsin, arccos, arctan).
- **Hyperbolic Functions**: Calculate hyperbolic sine, cosine, and tangent, along with their inverse functions (arcsinh, arccosh, arctanh).
- **Power Function**: Raise a number to the power of another number.

## Requirements

- Python 3.x

## Installation

1. Clone the repository or download the source code.
2. Navigate to the project directory.
3. Run the calculator script using Python.

```bash
python calculator.py
```

## Usage

1. Run the script to start the calculator.
2. Follow the on-screen prompts to select an operation.
3. Enter the required numbers when prompted.
4. To exit the calculator, enter 'q'.

### Example Operations

- **Addition**: 
  - Input: `1` (for addition), then enter two numbers.
  - Output: Displays the sum of the two numbers.

- **Square Root**: 
  - Input: `5` (for square root), then enter a number.
  - Output: Displays the square root of the number.

- **Logarithm**: 
  - Input: `log` (for logarithm), then enter the number and the base.
  - Output: Displays the logarithm of the number to the specified base.

## Functions

Here are some of the key functions implemented in the calculator:

- `add(x, y)`: Returns the sum of `x` and `y`.
- `subtract(x, y)`: Returns the difference of `x` and `y`.
- `multiply(x, y)`: Returns the product of `x` and `y`.
- `divide(x, y)`: Returns the quotient of `x` and `y`, with error handling for division by zero.
- `square_root(x)`: Returns the square root of `x`, with error handling for negative inputs.
- `exp(x)`: Returns the exponential of `x` using a series expansion.
- `ln(x)`: Returns the natural logarithm of `x` using a series expansion.
- `log10(x)`: Returns the base 10 logarithm of `x`.
- `log(x, base)`: Returns the logarithm of `x` to the specified `base`.
- `sin(x)`, `cos(x)`, `tan(x)`: Returns the sine, cosine, and tangent of `x`, respectively.
- `arcsin(x)`, `arccos(x)`, `arctan(x)`: Returns the inverse sine, cosine, and tangent of `x`, respectively.
- `sinh(x)`, `cosh(x)`, `tanh(x)`: Returns the hyperbolic sine, cosine, and tangent of `x`, respectively.

## Error Handling

The calculator includes error handling for:
- Division by zero.
- Invalid inputs for logarithmic and trigonometric functions.
- Negative inputs for square root calculations.

## Contributing

Contributions are welcome! If you have suggestions for improvements or additional features, feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments

- This calculator is built using basic mathematical principles and Python programming concepts.

---

Feel free to modify any sections to better fit your project or add any additional information that you think would be helpful for users.
