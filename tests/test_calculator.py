import sys
from io import StringIO
from unittest.mock import patch
from app.calculator import calculator, history_manager


# Helper function to capture print statements
def run_calculator_with_input(monkeypatch, inputs):
    """
    Simulates user input and captures output from the calculator REPL.
    
    :param monkeypatch: pytest fixture to simulate user input
    :param inputs: list of inputs to simulate
    :return: captured output as a string
    """
    input_iterator = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iterator))

    # Capture the output of the calculator
    captured_output = StringIO()
    sys.stdout = captured_output
    calculator()
    sys.stdout = sys.__stdout__  # Reset stdout
    return captured_output.getvalue()

# Positive Tests
def test_addition(monkeypatch, caplog):
    """Test addition operation in REPL."""
    inputs = ["add 2 3", "exit"]
    with caplog.at_level("INFO"):
        with patch.object(history_manager, "add_record") as mock_add_record, \
             patch.object(history_manager, "show_history") as mock_show_history:
            output = run_calculator_with_input(monkeypatch, inputs)
            # Verify addition was performed and recorded in history
            mock_add_record.assert_called_once_with("add", [2.0, 3.0], 5.0)
            # Verify history display was called
            mock_show_history.assert_called_once()
    assert "INFO" in [record.levelname for record in caplog.records]
    assert "Performed addition: 2.0 + 3.0 = 5.0" in caplog.text


def test_subtraction(monkeypatch, caplog):
    """Test subtraction operation in REPL."""
    inputs = ["subtract 5 2", "exit"]
    with caplog.at_level("INFO"):
        with patch.object(history_manager, "add_record") as mock_add_record, \
             patch.object(history_manager, "show_history") as mock_show_history:
            output = run_calculator_with_input(monkeypatch, inputs)
            mock_add_record.assert_called_once_with("subtract", [5.0, 2.0], 3.0)
            # Verify history display was called
            mock_show_history.assert_called_once()
    assert "INFO" in [record.levelname for record in caplog.records]
    assert "Performed subtraction: 5.0 - 2.0 = 3.0" in caplog.text


def test_multiplication(monkeypatch, caplog):
    """Test multiplication operation in REPL."""
    inputs = ["multiply 4 5", "exit"]
    with caplog.at_level("INFO"):
        with patch.object(history_manager, "add_record") as mock_add_record, \
             patch.object(history_manager, "show_history") as mock_show_history:
            output = run_calculator_with_input(monkeypatch, inputs)
            mock_add_record.assert_called_once_with("multiply", [4.0, 5.0], 20.0)
            # Verify history display was called
            mock_show_history.assert_called_once()
    assert "INFO" in [record.levelname for record in caplog.records]
    assert "Performed multiplication: 4.0 x 5.0 = 20.0" in caplog.text


def test_division(monkeypatch, caplog):
    """Test division operation in REPL."""
    inputs = ["divide 10 2", "exit"]
    with caplog.at_level("INFO"):
        with patch.object(history_manager, "add_record") as mock_add_record, \
             patch.object(history_manager, "show_history") as mock_show_history:
            output = run_calculator_with_input(monkeypatch, inputs)
            mock_add_record.assert_called_once_with("divide", [10.0, 2.0], 5.0)
            # Verify history display was called
            mock_show_history.assert_called_once()
    assert "INFO" in [record.levelname for record in caplog.records]
    assert "Performed division: 10.0 / 2.0 = 5.0" in caplog.text

def test_modulus(monkeypatch, caplog):
    """Test modulus operation in REPL."""
    inputs = ["modulus 10 5", "exit"]
    with caplog.at_level("INFO"):
        with patch.object(history_manager, "add_record") as mock_add_record, \
             patch.object(history_manager, "show_history") as mock_show_history:
            output = run_calculator_with_input(monkeypatch, inputs)
            mock_add_record.assert_called_once_with("modulus", [10.0, 5.0], 0.0)
            # Verify history display was called
            mock_show_history.assert_called_once()
    assert "INFO" in [record.levelname for record in caplog.records]
    assert "Performed modulo: 10.0 % 5.0 = 0.0" in caplog.text


def test_power(monkeypatch, caplog):
    """Test power operation in REPL."""
    inputs = ["power 4 2", "exit"]
    with caplog.at_level("INFO"):
        with patch.object(history_manager, "add_record") as mock_add_record, \
             patch.object(history_manager, "show_history") as mock_show_history:
            output = run_calculator_with_input(monkeypatch, inputs)
            mock_add_record.assert_called_once_with("power", [4.0, 2.0], 16.0)
            # Verify history display was called
            mock_show_history.assert_called_once()
    assert "INFO" in [record.levelname for record in caplog.records]
    assert "Performed power: 4.0 ^ 2.0 = 16.0" in caplog.text



# Negative Tests
def test_invalid_operation(monkeypatch, caplog):
    """Test invalid operation in REPL."""
    inputs = ["sigma 5 3", "exit"]
    with caplog.at_level("WARNING"):
        output = run_calculator_with_input(monkeypatch, inputs)
    assert "WARNING" in [record.levelname for record in caplog.records]
    assert "Unknown operation 'sigma'." in caplog.text



def test_invalid_input_format(monkeypatch, caplog):
    """Test invalid input format in REPL."""
    inputs = ["add two three", "exit"]
    with caplog.at_level("WARNING"):
        output = run_calculator_with_input(monkeypatch, inputs)
    assert "WARNING" in [record.levelname for record in caplog.records]
    assert "Invalid input. Please follow the format: <operation> <num1> <num2>" in caplog.text

def test_division_by_zero(monkeypatch, caplog):
    """Test division by zero in REPL."""
    inputs = ["divide 5 0", "exit"]
    with caplog.at_level("ERROR"):
        output = run_calculator_with_input(monkeypatch, inputs)
    assert "ERROR" in [record.levelname for record in caplog.records]
    assert "Cannot divide by zero." in caplog.text

def test_modulus_by_zero(monkeypatch, caplog):
    """Test modulus by zero in REPL."""
    inputs = ["modulus 5 0", "exit"]
    with caplog.at_level("ERROR"):
        output = run_calculator_with_input(monkeypatch, inputs)
    assert "ERROR" in [record.levelname for record in caplog.records]
    assert "Divisor cannot be zero." in caplog.text

# History Testing
def test_save_history(monkeypatch):
    """Test saving history in REPL."""
    inputs = ["history", "2", "6", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "History saved to history.csv." in output


def test_load_history(monkeypatch):
    """Test loading history in REPL."""
    inputs = ["history", "3", "6", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "History loaded from history.csv." in output


def test_clear_history(monkeypatch):
    """Test clearing history in REPL."""
    inputs = ["history", "4", "6", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "History cleared successfully." in output


def test_delete_history_file(monkeypatch):
    """Test deleting history file in REPL."""
    inputs = ["history", "5", "6", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "No history file to delete." in output


def test_manage_history_options(monkeypatch):
    """Test managing history options."""
    inputs = ["history", "1", "2", "3", "4", "5", "6", "exit"]
    with patch.object(history_manager, "show_history") as mock_show_history, \
         patch.object(history_manager, "save_history") as mock_save_history, \
         patch.object(history_manager, "load_history") as mock_load_history, \
         patch.object(history_manager, "clear_history") as mock_clear_history, \
         patch.object(history_manager, "delete_history_file") as mock_delete_history_file:
        output = run_calculator_with_input(monkeypatch, inputs)

        # Verify all history management methods were called
        mock_show_history.assert_called_once()
        mock_save_history.assert_called_once()
        mock_load_history.assert_called_once()
        mock_clear_history.assert_called_once()
        mock_delete_history_file.assert_called_once()

    assert "History Management Options:" in output

def test_invalid_history_choice(monkeypatch):
    inputs = ["history", "invalid", "6", "exit"]  # 'invalid' simulates an invalid choice
    output = run_calculator_with_input(monkeypatch, inputs)
    # Check that the invalid choice message was printed
    assert "Invalid choice. Please try again." in output