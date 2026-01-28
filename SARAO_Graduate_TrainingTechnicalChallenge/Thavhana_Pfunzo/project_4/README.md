# Number Machine

A utility class that performs three different transformations on five-digit numbers:
1. Reverses the number's digits
2. Calculates the sum of its digits
3. Generates a new number by adding one to each digit (with 9 wrapping around to 0)

## Features

- Validates input to ensure five-digit numbers
- Pure Python implementation with no external dependencies
- Clean, well-documented code with type hints
- Includes both class methods and a convenience function
- Comprehensive error handling

## Installation

No installation required. Simply import the class:

```python
from number_machine import NumberMachine
```

## Usage

### Using the Process Method (All Transformations)

```python
# Process a number through all transformations
result = NumberMachine.process_number(12345)

# Access individual results
print(f"Original: {result['original']}")
print(f"Reversed: {result['reversed']}")
print(f"Sum of digits: {result['digit_sum']}")
print(f"Incremented digits: {result['incremented']}")
```

### Using Individual Methods

```python
# Reverse the digits
reversed_num = NumberMachine.reverse_number(12345)  # Returns 54321

# Calculate sum of digits
digit_sum = NumberMachine.sum_digits(12345)  # Returns 15 (1+2+3+4+5)

# Increment each digit (9 wraps to 0)
new_num = NumberMachine.add_one_to_digits(12391)  # Returns 23402
```

## Method Reference

### `reverse_number(number: int) -> int`
Reverses the digits of a five-digit number.

**Parameters:**
- `number`: A five-digit integer (10000-99999)

**Returns:** The number with its digits reversed

**Raises:**
- `ValueError`: If input is not a five-digit number

### `sum_digits(number: int) -> int`
Calculates the sum of the digits of a number.

**Parameters:**
- `number`: Any integer

**Returns:** Sum of the absolute value of the digits

### `add_one_to_digits(number: int) -> int`
Generates a new number by adding one to each digit (9 wraps to 0).

**Parameters:**
- `number`: A five-digit integer (10000-99999)

**Returns:** New five-digit number with each digit incremented by 1

**Raises:**
- `ValueError`: If input is not a five-digit number

### `process_number(number: int) -> dict`
Processes a number through all three transformations.

**Parameters:**
- `number`: A five-digit integer (10000-99999)

**Returns:** Dictionary with keys: 'original', 'reversed', 'digit_sum', 'incremented'

## Examples

```python
# Example from the problem statement
result = NumberMachine.process_number(12391)
# {
#   'original': 12391,
#   'reversed': 19321,
#   'digit_sum': 16,
#   'incremented': 23402
# }

# Edge case: All nines
result = NumberMachine.process_number(99999)
# {
#   'original': 99999,
#   'reversed': 99999,
#   'digit_sum': 45,
#   'incremented': 0
# }
```


## Error Handling

The class includes input validation for five-digit numbers:

```python
try:
    NumberMachine.reverse_number(1234)  # Too few digits
    NumberMachine.reverse_number(100000)  # Too many digits
except ValueError as e:
    print(f"Error: {e}")
```

## Dependencies

- Python 3.6+
- No external dependencies required
