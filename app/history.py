import pandas as pd
import os
from app.config import HISTORY_FILE, MAX_HISTORY_ENTRIES

# Function to manage history
class HistoryManager:
    def __init__(self):
        self.history_file = HISTORY_FILE
        self.max_entries = MAX_HISTORY_ENTRIES
        self.history = pd.DataFrame(columns=["Operation", "Operands", "Result"])
        if os.path.exists(self.history_file):
            self.load_history()
    # Records calculation history 
    def add_record(self, operation, operands, result):
        new_record = {"Operation": operation, "Operands": operands, "Result": result}
    
        if self.history.empty: # If no prior calculations were made...
        # Initialize the DataFrame with the first record
            self.history = pd.DataFrame([new_record])
        else:
        # Append the new record to the existing DataFrame
            self.history = pd.concat([self.history, pd.DataFrame([new_record])], ignore_index=True)

    # Function to save calculation history
    def save_history(self):
        self.history.to_csv(self.history_file, index=False)
        print(f"History saved to {self.history_file}.")

    # Function to load the previously saved calculation history
    def load_history(self):
        if os.path.exists(self.history_file): # If save file exists...
            self.history = pd.read_csv(self.history_file)
            print(f"History loaded from {self.history_file}.")
        else: # If no save file exists...
            print(f"No history file found at {self.history_file}. Starting with an empty history.")

    # Function to clear history
    def clear_history(self):
        self.history = pd.DataFrame(columns=["Operation", "Operands", "Result"])
        if os.path.exists(self.history_file):
            os.remove(self.history_file)
        print("History cleared successfully.")

    # Function to delete history
    def delete_history_file(self):
        if os.path.exists(self.history_file): # If history exists...
            os.remove(self.history_file)
            print("History file deleted successfully.")
        else: # If there is no history...
            print("No history file to delete.")

    # Function to print history
    def show_history(self):
        if self.history.empty: # If there is no history...
            print("No history to display.") 
        else: # If there is history...
            print(self.history.to_string(index=False)) # Print history
