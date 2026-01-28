# Pangram Checker

A Python function to check if a given string is a pangram (contains every letter of the alphabet at least once).

## Features

- Checks if a string contains all letters of the alphabet
- Case-insensitive comparison
- Handles punctuation and numbers gracefully
- Supports custom alphabets
- Simple and efficient implementation

## Installation

No installation required. Simply import the function:

```python
from pangram_checker import is_pangram
```

## Usage

### Basic Usage

```python
text = "The quick brown fox jumps over the lazy dog"
result = is_pangram(text)  # Returns True
print(f"Is pangram? {result}")
```

### With Custom Alphabet

```python
# Check if a string contains all letters of a custom alphabet
custom_alphabet = "abc"
result = is_pangram("abcabc", custom_alphabet)  # Returns True
print(f"Contains all letters? {result}")
```

### Checking for Specific Character Sets

```python
# Check for digits
import string
digits = string.digits  # '0123456789'
result = is_pangram("The year 2023 has 365 days", digits)  # Returns False
```

## Function Signature

```python
def is_pangram(input_string: str, alphabet: str = string.ascii_lowercase) -> bool:
    """
    Check if the input string is a pangram.
    
    Args:
        input_string: The string to check
        alphabet: The set of characters to check for (default: English lowercase letters)
        
    Returns:
        bool: True if all characters in alphabet are present in input_string (case-insensitive)
    """
```

## Examples

```python
# English pangram (all letters used at least once)
is_pangram("Pack my box with five dozen liquor jugs")  # True

# Not a pangram (missing letters)
is_pangram("This is not a pangram")  # False

# With punctuation and mixed case
is_pangram("The five boxing wizards jump quickly!!!")  # True
```



## Dependencies

- Python 3.6+
- No external dependencies required (uses Python's standard `string` module)

## Performance

The function has a time complexity of O(n + m) where:
- n is the length of the input string
- m is the size of the alphabet

Memory usage is O(m) where m is the size of the alphabet.
