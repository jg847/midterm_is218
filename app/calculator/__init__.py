from app.operations import addition, subtraction, multiplication, division, modulus, power
import logging
from app.history import HistoryManager

logger = logging.getLogger(__name__)
history_manager = HistoryManager()

def calculator():
    """Basic REPL calculator that performs addition, subtraction, multiplication, division, modulus, and powers."""
    
    # Welcome Message
    logger.info(f"Welcome to the calculator REPL! Type 'exit' to quit")
    
    while True:    # While calulator is running
        # Asks user for input
        user_input = input(
                "Enter an operation (add, subtract, multiply, divide, modulus, power) and two numbers,"
                " or 'history' to manage history, or 'exit' to quit: ")
       
       # Exiting calculator
        if user_input.lower() == "exit":
            logger.info("Exiting calculator...")
            break  # Stops running the loop and exits the calculator function
        
        # History management commands
        if user_input.lower() == "history":
            manage_history()
            continue

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
            result = addition(num1, num2) 
            logger.info(f"Performed addition: {num1} + {num2} = {result}")
            history_manager.show_history()
        elif operation == "subtract":
            result = subtraction(num1, num2) 
            logger.info(f"Performed subtraction: {num1} - {num2} = {result}")
            history_manager.show_history()
        elif operation == "multiply":
            result = multiplication(num1, num2) 
            logger.info(f"Performed multiplication: {num1} x {num2} = {result}")
            history_manager.show_history()
        elif operation == "divide":
            try:
                result = division(num1, num2) 
                logger.info(f"Performed division: {num1} / {num2} = {result}")
                history_manager.show_history()
            # Handling error when user attempts to divide by zero
            except ValueError as e:
                logger.error(e)
                continue 
        elif operation == "modulus":
            try:
                result = modulus(num1, num2) 
                logger.info(f"Performed modulo: {num1} % {num2} = {result}")
                history_manager.show_history()
            except ValueError as e: # Handles case when diving by zero again
                logger.error(e)
                continue
        elif operation == "power": 
            result = power(num1,num2) # Calls the power function to raise num1 to the power of num2
            logger.info(f"Performed power: {num1} ^ {num2} = {result}")
            history_manager.show_history()

        else:
            # If the user types an unregistered operation, the following message will be shown.
            logger.warning(f"Unknown operation '{operation}'.")
            logger.info("Supported operations: add, subtract, multiply, divide, modulus, power.")
            continue  # Go back to the top of the loop and try again.
        
        # Save the result to history
        history_manager.add_record(operation, [num1,num2], result)
        print(f"Result: {result}")

# Manage calculation history
def manage_history():
    while True: # while history command is running
        # Prints commands available to be used for the user.
        # Asks user to input a number 1-6, each number is tied to a function
        print("\nHistory Management Options:")
        print("1. View history")
        print("2. Save history")
        print("3. Load history")
        print("4. Clear history")
        print("5. Delete history file")
        print("6. Back to calculator")
        choice = input("Choose an option (1-6): ")

        # History function called upon user input
        if choice == "1":
            history_manager.show_history()
        elif choice == "2":
            history_manager.save_history()
        elif choice == "3":
            history_manager.load_history()
        elif choice == "4":
            history_manager.clear_history()
        elif choice == "5":
            history_manager.delete_history_file()
        elif choice == "6":
            break
        # If user used an invalid option, an error line is printed
        else:
            print("Invalid choice. Please try again.")