# Weighted Sum Average

An implementation of a weighted moving average filter for signal processing applications.

## Features

- Implements a weighted moving average filter
- Supports custom weights for the moving window
- Efficient processing of streaming data
- Includes a sine wave generator for testing
- Demonstrates moving average behavior with equal weights

## Usage

```python
from weighted_average import WeightedAverage
import matplotlib.pyplot as plt
import numpy as np

# Initialize with weights
weights = [0.5, 0.3, 0.2]  # Weights for the moving window
wa = WeightedAverage(weights)

# Process a sequence of values
values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
results = []

for value in values:
    result = wa.process(value)
    results.append(result)
    print(f"Input: {value}, Weighted Average: {result:.2f}")

# Plot results
plt.plot(values, label='Original')
plt.plot(results, label='Weighted Average')
plt.legend()
plt.show()
```

## Methods

- `__init__(self, w: List[float])`: Initialize with a list of weights
- `process(self, x: float) -> float`: Process a new value and return the weighted average
- `generate_sine_wave(samples: int, frequency: float = 1.0, amplitude: float = 1.0) -> List[float]`: Static method to generate test signals

## Example: Moving Average Filter

```python
# Create a moving average filter (all weights = 1)
window_size = 5
weights = [1] * window_size
wa = WeightedAverage(weights)

# Process a noisy signal
import random
signal = [random.gauss(0, 0.5) + np.sin(2 * np.pi * i/50) for i in range(200)]
filtered = [wa.process(x) for x in signal]
```


## Dependencies

- Python 3.6+
- numpy (for testing and examples)
- matplotlib (for examples)

## Mathematical Background

The weighted sum average is calculated as:

y[n] = (w[0]*x[0] + w[1]*x[1] + ... + w[N-1]*x[N-1]) / N

Where:
- x[0] is the most recent input
- w[0] is the weight for the most recent input
- N is the window size (number of weights)
