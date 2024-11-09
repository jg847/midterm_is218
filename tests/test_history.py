import os
from unittest.mock import patch
import pandas as pd
import pytest
from app.history import HistoryManager
from app.config import HISTORY_FILE

@pytest.fixture
def history_manager():
    manager = HistoryManager()
    yield manager
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)

def test_add_record(history_manager):
    history_manager.add_record("add", [1, 2], 3)
    assert len(history_manager.history) == 1
    assert history_manager.history.iloc[0]["Operation"] == "add"

def test_add_record_to_non_empty_history(history_manager):
    """Test adding a record to a non-empty history."""
    # Set up initial history with one record
    history_manager.history = pd.DataFrame(
        [{"Operation": "add", "Operands": [1, 2], "Result": 3}]
    )

    # Add a new record to the existing history
    history_manager.add_record("subtract", [5, 3], 2)

    # Assert that the history now contains two records
    assert len(history_manager.history) == 2

    # Assert that the second record matches the added record
    assert history_manager.history.iloc[1].to_dict() == {
        "Operation": "subtract",
        "Operands": [5, 3],
        "Result": 2,
    }

    # Assert that the first record remains unchanged
    assert history_manager.history.iloc[0].to_dict() == {
        "Operation": "add",
        "Operands": [1, 2],
        "Result": 3,
    }

def test_save_and_load_history(history_manager):
    history_manager.add_record("add", [1, 2], 3)
    history_manager.save_history()
    new_manager = HistoryManager()
    assert len(new_manager.history) == 1
    assert new_manager.history.iloc[0]["Operation"] == "add"

def test_load_history_no_file(history_manager, capsys):
    """Test loading history when no file exists."""
    with patch("os.path.exists", return_value=False):
        history_manager.load_history()
        
        # Capture the output
        captured = capsys.readouterr()
        
        # Assert that the correct message is printed
        assert f"No history file found at {HISTORY_FILE}. Starting with an empty history." in captured.out
        
        # Ensure the history remains empty
        assert history_manager.history.empty

def test_clear_history(history_manager):
    history_manager.add_record("add", [1, 2], 3)
    history_manager.clear_history()
    assert history_manager.history.empty

def test_delete_history_file(history_manager):
    history_manager.save_history()
    history_manager.delete_history_file()
    assert not os.path.exists(HISTORY_FILE)

# Testing when History is Empty
def test_show_history_empty(history_manager, capsys):
    """Test displaying history when it is empty."""
    # Ensure the history is empty
    history_manager.history = pd.DataFrame(columns=["Operation", "Operands", "Result"])
    
    # Call the show_history method
    history_manager.show_history()
    
    # Capture printed output
    captured = capsys.readouterr()
    
    # Assert that the empty message is printed
    assert "No history to display." in captured.out

# Testing Showing History
def test_show_history_non_empty(history_manager, capsys):
    """Test displaying non-empty history."""
    # Populate the history with a sample record
    history_manager.history = pd.DataFrame(
        [{"Operation": "add", "Operands": [1, 2], "Result": 3}]
    )
    
    # Call the show_history method
    history_manager.show_history()
    
    # Capture printed output
    captured = capsys.readouterr()
    
    # Assert that the history is displayed correctly
    assert "add" in captured.out
    assert "[1, 2]" in captured.out
    assert "3" in captured.out