# Simple mathematicals operations are declared
# Addition function
def addition(a: float, b: float) -> float:
    return a + b

# Subtraction function
def subtraction(a: float, b: float) -> float:
    return a - b

# Multiplication function
def multiplication(a: float, b: float) -> float:
    return a * b

# Division function. Raises error when attempting to divide by zero.
def division(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
# Finding remainder of a division operation. Raises error when dividing by zero.
def modulus(a: float, b: float) -> float:
    if b==0:
        raise ValueError("Divisor cannot be zero.")
    return a % b
# Finding power of a number
def power(a: float, b: float) -> float:
    return a**b