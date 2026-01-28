import pytest
import string
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from project_3.pangram_checker import is_pangram, ispangram

class TestPangramChecker:
    def test_english_pangram(self):
        """Test with a standard English pangram"""
        assert is_pangram("The quick brown fox jumps over the lazy dog") is True
        assert is_pangram("Pack my box with five dozen liquor jugs") is True
        assert is_pangram("How vexingly quick daft zebras jump!") is True
    
    def test_non_pangram(self):
        """Test with strings that are not pangrams"""
        assert is_pangram("This is not a pangram") is False
        assert is_pangram("The quick brown fox jumps over the lazy do") is False  # Missing 'g'
        assert is_pangram("") is False  # Empty string
    
    def test_case_insensitivity(self):
        """Test that the function is case-insensitive"""
        assert is_pangram("The Quick brOwn Fox Jumps Over The Lazy Dog") is True
        assert is_pangram("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG") is True
        assert is_pangram("the quick brown fox jumps over the lazy dog") is True
    
    def test_special_characters(self):
        """Test with strings containing special characters and numbers"""
        assert is_pangram("The quick brown fox jumps over the lazy dog 123!") is True
        assert is_pangram("Pack my box with five dozen liquor jugs! @#$%^&*()") is True
        assert is_pangram("Not a pangram 12345!") is False
    
    def test_unicode_characters(self):
        """Test with Unicode characters"""
        # Pangram with some accented characters
        assert is_pangram("El pingüino Wenceslao hizo kilómetros bajo exhaustiva lluvia y frío, añoraba a su querido cachorro") is False
        
        # Not a pangram (missing some Spanish letters)
        assert is_pangram("El veloz murciélago hindú comía feliz cardillo y kiwi") is False
    
    def test_custom_alphabet(self):
        """Test with a custom alphabet"""
        # Binary alphabet
        assert is_pangram("01", "01") is True
        assert is_pangram("0011", "01") is True
        assert is_pangram("0", "01") is False  # Missing '1'
        
        # DNA alphabet
        assert is_pangram("ACGT", "ACGT") is True
        assert is_pangram("ACGTACGT", "ACGT") is True
        assert is_pangram("ACGT", "ACGTN") is False  # Missing 'N'
    
    def test_empty_alphabet(self):
        """Test with an empty alphabet (should always return True)"""
        assert is_pangram("", "") is True
        assert is_pangram("any string", "") is True
        assert is_pangram("", "") is True
    
    def test_whitespace_handling(self):
        """Test that whitespace is handled correctly"""
        assert is_pangram("The quick brown fox jumps over the lazy dog") is True
        assert is_pangram("Thequickbrownfoxjumpsoverthelazydog") is True  # No spaces
        assert is_pangram("  The quick brown fox jumps over the lazy dog  ") is True  # Extra spaces
    
    def test_backward_compatibility(self):
        """Test that the ispangram alias works the same as is_pangram"""
        assert ispangram is is_pangram  # They should be the same function object
        assert ispangram("The quick brown fox jumps over the lazy dog") is True
        assert ispangram("Not a pangram") is False

class TestEdgeCases:
    def test_non_string_input(self):
        """Test with non-string input (should raise TypeError)"""
        with pytest.raises(TypeError):
            is_pangram(123)  # type: ignore
        
        with pytest.raises(TypeError):
            is_pangram(["a", "b", "c"])  # type: ignore
    
    def test_non_string_alphabet(self):
        """Test with non-string alphabet (should raise TypeError)"""
        with pytest.raises(TypeError):
            is_pangram("test", 123)  # type: ignore
    
    def test_duplicate_letters_in_alphabet(self):
        """Test with duplicate letters in the alphabet"""
        # Should still work, but may be inefficient
        assert is_pangram("abc", "aabbcc") is False  # Missing 'b' and 'c' in input
        assert is_pangram("abcabc", "aabbcc") is True

if __name__ == "__main__":
    pytest.main()
