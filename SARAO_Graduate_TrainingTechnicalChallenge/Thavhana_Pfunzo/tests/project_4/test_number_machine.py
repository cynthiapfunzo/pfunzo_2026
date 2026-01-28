import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from project_4.number_machine import NumberMachine

class TestReverseNumber:
    def test_standard_case(self):
        """Test reversing standard five-digit numbers"""
        assert NumberMachine.reverse_number(12345) == 54321
        assert NumberMachine.reverse_number(10000) == 1  # 00001 is 1
        assert NumberMachine.reverse_number(99999) == 99999
        assert NumberMachine.reverse_number(12034) == 43021
    
    def test_palindromes(self):
        """Test with palindromic numbers"""
        assert NumberMachine.reverse_number(12321) == 12321
        assert NumberMachine.reverse_number(10101) == 10101
        assert NumberMachine.reverse_number(11011) == 11011
    
    def test_edge_cases(self):
        """Test with edge case numbers"""
        assert NumberMachine.reverse_number(10000) == 1  # Smallest 5-digit number
        assert NumberMachine.reverse_number(99999) == 99999  # Largest 5-digit number
        assert NumberMachine.reverse_number(10001) == 10001  # Palindrome with zeros
    
    def test_invalid_input(self):
        """Test with invalid input (not a five-digit number)"""
        with pytest.raises(ValueError, match="Input must be a five-digit number"):
            NumberMachine.reverse_number(1234)  # 4 digits
        
        with pytest.raises(ValueError, match="Input must be a five-digit number"):
            NumberMachine.reverse_number(100000)  # 6 digits
        
        with pytest.raises(ValueError, match="Input must be a five-digit number"):
            NumberMachine.reverse_number(-12345)  # Negative number
        
        with pytest.raises(ValueError, match="Input must be a five-digit number"):
            NumberMachine.reverse_number(1234.5)  # Not an integer

class TestSumDigits:
    def test_standard_case(self):
        """Test summing digits of various numbers"""
        assert NumberMachine.sum_digits(12345) == 15  # 1+2+3+4+5
        assert NumberMachine.sum_digits(10000) == 1   # 1+0+0+0+0
        assert NumberMachine.sum_digits(99999) == 45  # 9*5
        assert NumberMachine.sum_digits(54321) == 15  # 5+4+3+2+1
    
    def test_single_digit(self):
        """Test with single-digit numbers"""
        for i in range(10):
            assert NumberMachine.sum_digits(i) == i
    
    def test_negative_numbers(self):
        """Test with negative numbers (should use absolute value)"""
        assert NumberMachine.sum_digits(-12345) == 15
        assert NumberMachine.sum_digits(-10000) == 1
        assert NumberMachine.sum_digits(-99999) == 45
    
    def test_zero(self):
        """Test with zero"""
        assert NumberMachine.sum_digits(0) == 0

class TestAddOneToDigits:
    def test_standard_case(self):
        """Test adding one to each digit"""
        assert NumberMachine.add_one_to_digits(12345) == 23456
        assert NumberMachine.add_one_to_digits(99999) == 0     # All digits wrap around
        assert NumberMachine.add_one_to_digits(10000) == 21111  # Leading zero becomes 1
        assert NumberMachine.add_one_to_digits(12391) == 23402  # 9 wraps to 0
    
    def test_with_nines(self):
        """Test cases where digits wrap around from 9 to 0"""
        assert NumberMachine.add_one_to_digits(99999) == 0
        assert NumberMachine.add_one_to_digits(19999) == 20000
        assert NumberMachine.add_one_to_digits(99990) == 1  # 00001
    
    def test_invalid_input(self):
        """Test with invalid input (not a five-digit number)"""
        with pytest.raises(ValueError, match="Input must be a five-digit number"):
            NumberMachine.add_one_to_digits(1234)  # 4 digits
        
        with pytest.raises(ValueError, match="Input must be a five-digit number"):
            NumberMachine.add_one_to_digits(100000)  # 6 digits

class TestProcessNumber:
    def test_standard_case(self):
        """Test the process_number method with various inputs"""
        # Example from problem statement
        result = NumberMachine.process_number(12391)
        assert result == {
            'original': 12391,
            'reversed': 19321,
            'digit_sum': 16,  # 1+2+3+9+1
            'incremented': 23402
        }
        
        # Test with minimum 5-digit number
        result = NumberMachine.process_number(10000)
        assert result == {
            'original': 10000,
            'reversed': 1,
            'digit_sum': 1,
            'incremented': 21111
        }
        
        # Test with maximum 5-digit number
        result = NumberMachine.process_number(99999)
        assert result == {
            'original': 99999,
            'reversed': 99999,
            'digit_sum': 45,
            'incremented': 0
        }
    
    def test_invalid_input(self):
        """Test process_number with invalid input"""
        with pytest.raises(ValueError, match="Input must be a five-digit number"):
            NumberMachine.process_number(1234)  # 4 digits
        
        with pytest.raises(ValueError, match="Input must be a five-digit number"):
            NumberMachine.process_number(100000)  # 6 digits

class TestEdgeCases:
    def test_non_integer_input(self):
        """Test with non-integer input (should raise TypeError)"""
        with pytest.raises(TypeError):
            NumberMachine.reverse_number("12345")  # type: ignore
        
        with pytest.raises(TypeError):
            NumberMachine.sum_digits("12345")  # type: ignore
        
        with pytest.raises(TypeError):
            NumberMachine.add_one_to_digits("12345")  # type: ignore
        
        with pytest.raises(TypeError):
            NumberMachine.process_number("12345")  # type: ignore

if __name__ == "__main__":
    pytest.main()
