# SARAO Graduate Training - Technical Challenge

Welcome to my submission for the SARAO Graduate Training Technical Challenge! This repository contains four Python projects, each designed to solve specific programming challenges.

## Project Structure

```
Thavhana_Pfunzo/
├── project_1/           # Word Counter
├── project_2/           # Weighted Average
├── project_3/           # Pangram Checker
├── project_4/           # Number Machine
└── tests/               # Test files for all projects
    ├── project_1/
    ├── project_2/
    ├── project_3/
    └── project_4/
```

## Project Descriptions

### 1. Word Counter (`project_1/`)
A Python class that counts word frequencies in a given text and returns the most common words.

**Key Features:**
- Case-insensitive word counting
- Basic punctuation handling
- Configurable number of top words to return

### 2. Weighted Average (`project_2/`)
A Python class that calculates weighted moving averages with various utility functions.

**Key Features:**
- Weighted average calculation
- Moving average functionality
- Sine wave generation for testing

### 3. Pangram Checker (`project_3/`)
A function to check if a given string is a pangram (contains all letters of the alphabet).

**Key Features:**
- Case-insensitive checking
- Support for custom alphabets
- Handles basic special characters

### 4. Number Machine (`project_4/`)
A utility class for number manipulation with various mathematical operations.

**Key Features:**
- Number reversal
- Digit sum calculation
- Digit incrementing with wrap-around

## Getting Started

### Prerequisites
- Python 3.6+
- pytest (for running tests)
- numpy (for Project 2)

### Installation
1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd Thavhana_Pfunzo
   ```

2. Install the required dependencies:
   ```bash
   pip install pytest numpy
   ```

### Running Tests
To run all tests:
```bash
pytest tests/ -v
```

To run tests for a specific project:
```bash
pytest tests/project_1/ -v  # For Project 1 tests
```

## Current Status
- **Project 1**: Basic functionality implemented, some test cases failing
- **Project 2**: Core functionality working, sine wave generation needs adjustment
- **Project 3**: Basic pangram checking working, some edge cases need handling
- **Project 4**: All tests passing! ✅

## Notes
- Each project has its own detailed README with specific usage examples
- Test coverage is comprehensive but some edge cases are still being addressed
- The code follows PEP 8 style guidelines

## Author
[Your Name]

## License
This project is licensed under the MIT License - see the LICENSE file for details.
