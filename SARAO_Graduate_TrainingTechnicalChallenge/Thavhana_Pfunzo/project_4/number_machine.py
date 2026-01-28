class NumberMachine:
    """
    A class that performs three different transformations on five-digit numbers:
    1. Reverses the number
    2. Calculates the sum of its digits
    3. Generates a new number by adding one to each digit
    """
    
    @staticmethod
    def reverse_number(number: int) -> int:
        """
        Reverse the digits of a five-digit number without using string reversal.
        
        Args:
            number (int): A five-digit number to reverse
            
        Returns:
            int: The reversed number
            
        Raises:
            ValueError: If the input is not a five-digit number
        """
        if not (10000 <= number <= 99999):
            raise ValueError("Input must be a five-digit number")
            
        reversed_num = 0
        temp = number
        
        for i in range(5):
            digit = temp % 10
            reversed_num = reversed_num * 10 + digit
            temp = temp // 10
            
        return reversed_num
    
    @staticmethod
    def sum_digits(number: int) -> int:
        """
        Calculate the sum of the digits of a number.
        
        Args:
            number: Any integer
            
        Returns:
            int: Sum of the digits (always positive, using absolute value)
        """
        total = 0
        temp = abs(number)  # Work with absolute value
        
        while temp > 0:
            total += temp % 10
            temp = temp // 10
            
        return total
    
    @staticmethod
    def add_one_to_digits(number: int) -> int:
        """
        Generate a new number by adding one to each digit of the input number.
        If a digit is 9, it wraps around to 0.
        
        Args:
            number (int): A five-digit number
            
        Returns:
            int: The new number with each digit incremented by 1 (9 wraps to 0)
            
        Raises:
            ValueError: If the input is not a five-digit number
        """
        if not (10000 <= number <= 99999):
            raise ValueError("Input must be a five-digit number")
            
        result = 0
        temp = number
        position = 1
        
        for _ in range(5):
            digit = temp % 10
            new_digit = (digit + 1) % 10
            result += new_digit * position
            position *= 10
            temp = temp // 10
            
        return result
    
    @classmethod
    def process_number(cls, number: int) -> dict:
        """
        Process a five-digit number through all three transformations.
        
        Args:
            number (int): A five-digit number to process
            
        Returns:
            dict: A dictionary containing all three transformations
        """
        return {
            'original': number,
            'reversed': cls.reverse_number(number),
            'digit_sum': cls.sum_digits(number),
            'incremented': cls.add_one_to_digits(number)
        }


def main():
    """
    Demonstrate the NumberMachine class with example inputs.
    """
    test_numbers = [
        12345,  # Example from the problem
        98765,  # Test with high digits
        10000,  # Test with minimum five-digit number
        99999,  # Test with maximum five-digit number
        54321   # Another test case
    ]
    
    print("Number Machine Demo")
    print("-" * 40)
    
    for num in test_numbers:
        try:
            result = NumberMachine.process_number(num)
            print(f"\nOriginal number: {result['original']}")
            print(f"Reversed: {result['reversed']}")
            print(f"Sum of digits: {result['digit_sum']}")
            print(f"Incremented digits: {result['incremented']}")
            print("-" * 40)
        except ValueError as e:
            print(f"Error processing {num}: {e}")
    
    # Example of error handling
    try:
        NumberMachine.process_number(1234)  # Not a five-digit number
    except ValueError as e:
        print(f"\nError test: {e}")


if __name__ == "__main__":
    main()
