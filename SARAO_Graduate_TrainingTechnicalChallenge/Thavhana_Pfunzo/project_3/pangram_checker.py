import string

def is_pangram(input_string: str, alphabet: str = string.ascii_lowercase) -> bool:
    """
    Check if the input string is a pangram (contains every letter of the alphabet at least once).
    
    Args:
        input_string: The string to check
        alphabet: The set of characters to check for (default: English lowercase letters)
        
    Returns:
        bool: True if all characters in alphabet are present in input_string (case-insensitive)
        
    Raises:
        TypeError: If input_string is not a string
    """
    # Input validation
    if not isinstance(input_string, str) or not isinstance(alphabet, str):
        raise TypeError("Input must be a string")
    
    # Handle empty alphabet case
    if not alphabet:
        return True
    
    # Normalize the input to lowercase for case-insensitive comparison
    input_lower = input_string.lower()
    
    # For custom alphabets, check each character exactly as provided
    if alphabet != string.ascii_lowercase:
        # Convert to set to remove duplicates and filter non-letters
        required_chars = {char.lower() for char in alphabet if char.isalpha()}
        # For empty required chars (e.g., alphabet has no letters), return True
        if not required_chars:
            return True
        # Check if all required characters are present in the input
        return all(any(c == char for c in input_lower) for char in required_chars)
    
    # For standard English alphabet, check a-z
    return all(any(c == letter for c in input_lower) for letter in string.ascii_lowercase)

# Alias for backward compatibility
ispangram = is_pangram

def main():
    # Example usage
    test_strings = [
        "The quick brown fox jumps over the lazy dog",  # English pangram
        "Pack my box with five dozen liquor jugs",      # Another English pangram
        "This is not a pangram",                        # Not a pangram
        """
        The five boxing wizards jump quickly.
        This sentence contains all the letters in the English alphabet.
        """,  # Pangram with punctuation and multiple lines
        ""  # Empty string
    ]
    
    for test in test_strings:
        result = is_pangram(test)
        print(f"\nString: {test[:50]}..." if len(test) > 50 else f"\nString: {test}")
        print(f"Is pangram? {'Yes' if result else 'No'}")
    
    # Test with a custom alphabet
    custom_alphabet = "abc"
    print(f"\nTesting with custom alphabet: {custom_alphabet}")
    print(f"'abc' is pangram? {is_pangram('abc', custom_alphabet)}")
    print(f"'ab' is pangram? {is_pangram('ab', custom_alphabet)}")


if __name__ == "__main__":
    main()
