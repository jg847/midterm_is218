from app.operations import addition, subtraction, multiplication, division, modulus, power

def calculator():
    """Basic REPL calculator that performs addition, subtraction, multiplication, division, modulus, and powers."""
    
    # Welcome Message
    print("Welcome to the calculator REPL! Type 'exit' to quit")
    
    while True:    # While the calulator is running...
        # User inputs operation and two numbers
        user_input = input("Enter an operation (add, subtract, multiply, divide, modulus, power) and two numbers, or 'exit' to quit: ")
        if user_input.lower() == "exit": # If user inputs 'exit'...
            print("Exiting calculator...")
            break  # Stops running the loop and exits the calculator function

        try:
            # Splits input into three parts: operation used and two numbers.
            operation, num1, num2 = user_input.split()
            num1, num2 = float(num1), float(num2) # Convert number to floats
        except ValueError:
            # Shows error if user types in incorrect inputs: i.e letters for numbers
            print("Invalid input. Please follow the format: <operation> <num1> <num2>")
            continue  # Try again by going back to the top of the loop.

        # Check what operation user asked for and call the right function
        if operation == "add":
            result = addition(num1, num2)  # We call the addition function to add the two numbers.
        elif operation == "subtract":
            result = subtraction(num1, num2)  # We call the subtraction function to subtract the two numbers.
        elif operation == "multiply":
            result = multiplication(num1, num2)  # We call the multiplication function to multiply the two numbers.
        elif operation == "divide":
            try:
                result = division(num1, num2)  # We call the division function to divide the two numbers.
            except ValueError as e:
                # Handles the case where someone tries to divide by zero
                # Sends error message when diving by zero is attempted
                print(e)  # Show the error message.
                continue 
        elif operation == "modulus":
            try:
                result = modulus(num1, num2) # We call the modulus function to find the remainder of a division function
            except ValueError as e: # Handles case when diving by zero again
                print(e)
                continue
        elif operation == "power": 
            result = power(num1,num2) # Calls the power function to raise num1 to the power of num2

        else:
            # If the user types an unregistered operation, the following message will be shown.
            print(f"Unknown operation '{operation}'. Supported operations: add, subtract, multiply, divide, modulus, power.")
            continue  # Go back to the top of the loop and try again.

        #Print the result of the operation.
        print(f"Result: {result}")
