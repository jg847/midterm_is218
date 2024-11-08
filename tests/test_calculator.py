import sys
from io import StringIO
from app.calculator import calculator


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
        output = run_calculator_with_input(monkeypatch, inputs)
    assert "INFO" in [record.levelname for record in caplog.records]
    assert "Performed addition: 2.0 + 3.0 = 5.0" in caplog.text


def test_subtraction(monkeypatch, caplog):
    """Test subtraction operation in REPL."""
    inputs = ["subtract 5 2", "exit"]
    with caplog.at_level("INFO"):
        output = run_calculator_with_input(monkeypatch, inputs)
    assert "INFO" in [record.levelname for record in caplog.records]
    assert "Performed subtraction: 5.0 - 2.0 = 3.0" in caplog.text


def test_multiplication(monkeypatch, caplog):
    """Test multiplication operation in REPL."""
    inputs = ["multiply 4 5", "exit"]
    with caplog.at_level("INFO"):
        output = run_calculator_with_input(monkeypatch, inputs)
    assert "INFO" in [record.levelname for record in caplog.records]
    assert "Performed multiplication: 4.0 x 5.0 = 20.0" in caplog.text


def test_division(monkeypatch, caplog):
    """Test division operation in REPL."""
    inputs = ["divide 10 2", "exit"]
    with caplog.at_level("INFO"):
        output = run_calculator_with_input(monkeypatch, inputs)
    assert "INFO" in [record.levelname for record in caplog.records]
    assert "Performed division: 10.0 / 2.0 = 5.0" in caplog.text

def test_modulus(monkeypatch, caplog):
    """Test modulus operation in REPL."""
    inputs = ["modulus 10 5", "exit"]
    with caplog.at_level("INFO"):
        output = run_calculator_with_input(monkeypatch, inputs)
    assert "INFO" in [record.levelname for record in caplog.records]
    assert "Performed modulo: 10.0 % 5.0 = 0.0" in caplog.text


def test_power(monkeypatch, caplog):
    """Test power operation in REPL."""
    inputs = ["power 4 2", "exit"]
    with caplog.at_level("INFO"):
        output = run_calculator_with_input(monkeypatch, inputs)
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