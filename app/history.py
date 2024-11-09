import pandas as pd
import os
from app.config import HISTORY_FILE, MAX_HISTORY_ENTRIES

class HistoryManager:
    def __init__(self):
        self.history_file = HISTORY_FILE
        self.max_entries = MAX_HISTORY_ENTRIES
        self.history = pd.DataFrame(columns=["Operation", "Operands", "Result"])
        if os.path.exists(self.history_file):
            self.load_history()

    def add_record(self, operation, operands, result):
        new_record = {"Operation": operation, "Operands": operands, "Result": result}
    
        if self.history.empty:
        # Initialize the DataFrame with the first record
            self.history = pd.DataFrame([new_record])
        else:
        # Append the new record to the existing DataFrame
            self.history = pd.concat([self.history, pd.DataFrame([new_record])], ignore_index=True)

    def save_history(self):
        self.history.to_csv(self.history_file, index=False)
        print(f"History saved to {self.history_file}.")

    def load_history(self):
        if os.path.exists(self.history_file):
            self.history = pd.read_csv(self.history_file)
            print(f"History loaded from {self.history_file}.")
        else:
            print(f"No history file found at {self.history_file}. Starting with an empty history.")

    def clear_history(self):
        self.history = pd.DataFrame(columns=["Operation", "Operands", "Result"])
        if os.path.exists(self.history_file):
            os.remove(self.history_file)
        print("History cleared successfully.")

    def delete_history_file(self):
        if os.path.exists(self.history_file):
            os.remove(self.history_file)
            print("History file deleted successfully.")
        else:
            print("No history file to delete.")

    def show_history(self):
        if self.history.empty:
            print("No history to display.")
        else:
            print(self.history.to_string(index=False))
