class WordCounter:
    """
    A class to track and retrieve the n most frequently used words from a given text.
    
    Attributes:
        word_counts (dict): A dictionary to store word counts
        n (int): Number of top frequent words to track
    """
    
    def __init__(self, n=10):
        """
        Initialize the WordCounter with a default of top 10 words.
        
        Args:
            n (int): Number of top frequent words to track (default: 10)
        """
        self.word_counts = {}
        self.n = n
    
    def process_word(self, word: str) -> None:
        """
        Process a single word, updating its count in the tracker.
        
        Args:
            word (str): The word to process
        """
        if not word:
            return
            
        # Convert to lowercase to make the count case-insensitive
        word = word.lower()
        self.word_counts[word] = self.word_counts.get(word, 0) + 1
    
    def get_top_words(self, n: int = None) -> list:
        """
        Get the top n most frequently used words.
        
        Args:
            n (int, optional): Number of top words to return. Defaults to the n set in __init__.
            
        Returns:
            list: List of tuples containing (word, count) sorted by frequency (descending)
        """
        # Sort words by count in descending order, then alphabetically
        sorted_words = sorted(
            self.word_counts.items(),
            key=lambda x: (-x[1], x[0])
        )
        # Return top n words, but handle empty input case
        top_n = n if n is not None else self.n
        return sorted_words[:min(top_n, len(sorted_words))] if top_n > 0 else []
    
    def process_text(self, text: str) -> None:
        """
        Process a string of text, splitting it into words and updating counts.
        
        Args:
            text (str): The text to process
        """
        import re
        # Split on word boundaries, keeping apostrophes within words
        words = re.findall(r"\b[\w']+\b", text.lower())
        for word in words:
            # Remove any remaining non-alphabetic characters except apostrophes
            clean_word = re.sub(r"[^a-z']", '', word)
            if clean_word and any(c.isalpha() for c in clean_word):
                self.word_counts[clean_word] = self.word_counts.get(clean_word, 0) + 1


def main():
    # Example usage
    text = """
    This is a test. This is only a test. Testing the word counter.
    This should show that 'this' and 'test' are the most common words.
    """
    
    # Create a WordCounter instance (default top 10 words)
    counter = WordCounter()
    
    # Process the text
    counter.process_text(text)
    
    # Get and display the top words
    top_words = counter.get_top_words()
    print("Top words:")
    for word, count in top_words:
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
