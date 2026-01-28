# Frequently Used Words

A Python class that tracks and returns the n most frequently used words from a given text.

## Features

- Tracks word frequencies in a case-insensitive manner
- Removes punctuation from words
- Returns top N most frequent words (configurable)
- Processes both full text and individual words
- Handles edge cases (empty strings, punctuation, etc.)

## Usage

```python
from word_counter import WordCounter

# Initialize with default top 10 words
counter = WordCounter()

# Process text
counter.process_text("Hello world! Hello Python. Python is awesome.")

# Get top words
top_words = counter.get_top_words()
for word, count in top_words:
    print(f"{word}: {count}")

# Process individual words
counter.process_word("Python")
counter.process_word("programming")

# Get updated top words
top_words = counter.get_top_words(3)  # Get top 3 words
```

## Methods

- `__init__(self, n=10)`: Initialize with the number of top words to track
- `process_word(self, word)`: Process a single word
- `process_text(self, text)`: Process a full text string
- `get_top_words(self, n=None)`: Get the top n words (defaults to the n set in __init__)

## Example Output

```
Top words:
hello: 3
python: 2
world: 1
is: 1
awesome: 1
```



## Dependencies

- Python 3.6+
- No external dependencies required
