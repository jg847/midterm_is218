from app.operations import addition, subtraction, multiplication, division, modulus, power
import logging

logger = logging.getLogger(__name__)

def calculator():
    """Basic REPL calculator that performs addition, subtraction, multiplication, division, modulus, and powers."""
    
    # Welcome Message
    logger.info(f"Welcome to the calculator REPL! Type 'exit' to quit")
    
    while True:    # While the calulator is running...
        # User inputs operation and two numbers
        user_input = input("Enter an operation (add, subtract, multiply, divide, modulus, power) and two numbers, or 'exit' to quit: ")
        if user_input.lower() == "exit": # If user inputs 'exit'...
            logger.info("Exiting calculator...")
            break  # Stops running the loop and exits the calculator function

        try:
            # Splits input into three parts: operation used and two numbers.
            operation, num1, num2 = user_input.split()
            num1, num2 = float(num1), float(num2) # Convert number to floats
        except ValueError:
            # Shows error if user types in incorrect inputs: i.e letters for numbers
            logger.warning("Invalid input. Please follow the format: <operation> <num1> <num2>")
            continue  # Try again by going back to the top of the loop.

        # Check what operation user asked for and call the right function
        if operation == "add":
            result = addition(num1, num2)  # We call the addition function to add the two numbers.
            logger.info(f"Performed addition: {num1} + {num2} = {result}")
        elif operation == "subtract":
            result = subtraction(num1, num2)  # We call the subtraction function to subtract the two numbers.
            logger.info(f"Performed subtraction: {num1} - {num2} = {result}")
        elif operation == "multiply":
            result = multiplication(num1, num2)  # We call the multiplication function to multiply the two numbers.
            logger.info(f"Performed multiplication: {num1} x {num2} = {result}")
        elif operation == "divide":
            try:
                result = division(num1, num2)  # We call the division function to divide the two numbers.
                logger.info(f"Performed division: {num1} / {num2} = {result}")
            except ValueError as e:
                # Handles the case where someone tries to divide by zero
                # Sends error message when diving by zero is attempted
                logger.error(e)
                continue 
        elif operation == "modulus":
            try:
                result = modulus(num1, num2) # We call the modulus function to find the remainder of a division function
                logger.info(f"Performed modulo: {num1} % {num2} = {result}")
            except ValueError as e: # Handles case when diving by zero again
                logger.error(e)
                continue
        elif operation == "power": 
            result = power(num1,num2) # Calls the power function to raise num1 to the power of num2
            logger.info(f"Performed power: {num1} ^ {num2} = {result}")

        else:
            # If the user types an unregistered operation, the following message will be shown.
            logger.warning(f"Unknown operation '{operation}'.")
            logger.info("Supported operations: add, subtract, multiply, divide, modulus, power.")
            continue  # Go back to the top of the loop and try again.
