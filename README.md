# IS218 Midterm

## Background
This is a simple calculator application that does not include design patterns.
The application executes the following operations: Add, Subtract, Multiply, Divide, Modulus, and Power. 

## Logging
The application logs operations used from user input. In this application, three levels of logging was used: INFO, WARNING, ERROR.
You can check how I used logging under the calculation function in my Calculator function [here](app/calculator/__init__.py)
You can also check my logging configurations [here](app/logging_config.py)
### INFO 
* used to log information from user input
* example: Logs when user opens calculator
### WARNING
* used to log warning messages from invalid user input
* example: Using invalid commands for operations
### ERROR
* used to log error messages 
* example: dividing by zero

## History
The application imports the package "Pandas" to manage user's history. 
* The application can view, save, load, clear, and delete callculation history.

## Environmental Variable
I used environmental variables to save logs into a folder, my history into a seperate folder, and log levels, format, and maximum amount of saved history entries. You can view how I used environmental variables [here](app/config.py)

## LBYL (Look Before You Leap)
This applications demonstrated LBYL by assuring inputs are checked before an action is performed. For example: If divisor is a 0, an error message is sent.
Check LBYL usage [here](app/operations/__init__.py)

## EAFP (Easier to Ask for Forgiveness than Permission)
This approach is demonstrated by using try/except handling to avoid errors, ex: dividing by zero.
Check EAFP usage [here](app/calculator/__init__.py))