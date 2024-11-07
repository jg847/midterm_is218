import pytest
from app.operations import addition, subtraction, multiplication, division, modulus, power

def test_addition():
    """Test Addition"""
    assert addition(1,1) == 2

def test_subtraction():
    """Test Subtraction"""
    assert subtraction(1,1) == 0

def test_multiplication():
    """Test Multiplication"""
    assert multiplication(1,1) == 1

def test_division_positive():
    """Test Division"""
    assert division(1,1) == 1

def test_division_zero():
    """Test Division by Zero"""
    with pytest.raises(ValueError, match = "Cannot divide by zero."):
        division(1,0)

def test_modulus_positive():
    """Test Modulus"""
    assert modulus(1,1) == 0

def test_modulus_zero():
    """Test Modulus When Divisor is Zero"""
    with pytest.raises(ValueError, match = "Divisor cannot be zero."):
        modulus(1,0)

def test_power():
    """Test Power"""
    assert power(1,1) == 1