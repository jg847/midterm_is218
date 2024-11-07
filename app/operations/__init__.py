def addition(a: float, b: float) -> float:
    return a + b

def subtraction(a: float, b: float) -> float:
    return a - b

def multiplication(a: float, b: float) -> float:
    return a * b

def division(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def modulus(a: float, b: float) -> float:
    if b==0:
        raise ValueError("Divisor cannot be zero.")
    return a % b