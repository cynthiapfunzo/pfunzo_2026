import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from project_1.word_counter import WordCounter

class TestWordCounter:
    def test_initialization(self):
        """Test WordCounter initialization with default and custom n values"""
        # Test default n=10
        counter1 = WordCounter()
        assert counter1.get_top_words() == []
        
        # Test custom n value
        counter2 = WordCounter(n=5)
        assert len(counter2.get_top_words(5)) == 0
    
    def test_process_word(self):
        """Test processing individual words"""
        counter = WordCounter()
        
        # Test case insensitivity
        counter.process_word("Hello")
        counter.process_word("hello")
        counter.process_word("WORLD")
        
        top_words = counter.get_top_words()
        assert len(top_words) == 2
        assert top_words[0] == ("hello", 2)
        assert top_words[1] == ("world", 1)
    
    def test_process_text(self):
        """Test processing a block of text"""
        counter = WordCounter()
        text = """
        This is a test. This is only a test.
        Testing the word counter with some text.
        """
        counter.process_text(text)
        
        top_words = counter.get_top_words(3)
        assert len(top_words) == 3
        assert top_words[0][0] == "test"
        assert top_words[0][1] == 2
        assert top_words[1][0] == "this"
        assert top_words[1][1] == 2
    
    def test_punctuation_handling(self):
        """Test that punctuation is properly handled"""
        counter = WordCounter()
        text = "Hello, world! How's it going? It's a beautiful day, isn't it?"
        counter.process_text(text)
        
        # Check that punctuation is removed
        words = [word for word, _ in counter.get_top_words()]
        assert "hello" in words
        assert "world" in words
        assert "its" in words  # 'it's' becomes 'its' after removing punctuation
    
    def test_get_top_words_limit(self):
        """Test limiting the number of top words returned"""
        counter = WordCounter()
        words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
        
        for word in words:
            counter.process_word(word)
        
        # Test getting top 2 words
        top_2 = counter.get_top_words(2)
        assert len(top_2) == 2
        assert top_2[0] == ("apple", 3)
        assert top_2[1] == ("banana", 2)
        
        # Test getting more words than exist
        all_words = counter.get_top_words(10)
        assert len(all_words) == 3  # Only 3 unique words exist
    
    def test_empty_input(self):
        """Test behavior with empty input"""
        counter = WordCounter()
        
        # Test empty string
        counter.process_text("")
        assert counter.get_top_words() == []
        
        # Test string with only whitespace and punctuation
        counter.process_text("  ,  . !? ")
        assert counter.get_top_words() == []
    
    def test_word_boundaries(self):
        """Test that words are properly split on non-alphanumeric characters"""
        counter = WordCounter()
        text = "user@example.com is an email, right?"
        counter.process_text(text)
        
        words = [word for word, _ in counter.get_top_words()]
        assert "user" in words
        assert "example" in words
        assert "com" in words
        assert "email" in words
        assert "right" in words
        assert "user@example.com" not in words  # Should be split

if __name__ == "__main__":
    pytest.main()
